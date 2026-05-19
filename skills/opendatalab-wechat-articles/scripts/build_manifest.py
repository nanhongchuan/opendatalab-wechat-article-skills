#!/usr/bin/env python3
"""Build a lightweight JSONL manifest for the OpenDataLab WeChat article repo."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TOPICS = ROOT / "knowledge" / "topics.json"
DEFAULT_OUTPUT = ROOT / "knowledge" / "manifest.jsonl"
DEFAULT_SPREADSHEET_NAME = "微信公众号文章.xlsx"
DEFAULT_ARTICLES_DIR_NAME = "articles"

STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "OpenDataLab",
    "上海",
    "人工智能",
    "实验室",
    "数据",
    "模型",
    "开源",
    "发布",
    "分享",
}


def load_topics(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_spreadsheet_index(path: Path) -> dict[str, dict[str, object]]:
    """Load optional WeChat export metadata from the spreadsheet index."""
    if not path.exists():
        return {}
    try:
        import openpyxl  # type: ignore[import-not-found]
    except ImportError:
        return {}

    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    sheet = workbook.active
    rows = sheet.iter_rows(values_only=True)
    headers = next(rows, None)
    if not headers:
        return {}
    header_map = {str(header): idx for idx, header in enumerate(headers) if header}

    def value(row: tuple[object, ...], key: str) -> object | None:
        idx = header_map.get(key)
        if idx is None or idx >= len(row):
            return None
        cell = row[idx]
        if hasattr(cell, "isoformat"):
            return cell.isoformat(sep=" ")
        return cell

    by_title: dict[str, dict[str, object]] = {}
    by_url: dict[str, dict[str, object]] = {}
    for row in rows:
        title = value(row, "标题")
        url = value(row, "链接")
        if not title and not url:
            continue
        record = {
            "account": value(row, "公众号"),
            "wechat_id": value(row, "ID"),
            "source_url": url,
            "cover_url": value(row, "封面"),
            "spreadsheet_summary": value(row, "摘要"),
            "created_at": value(row, "创建时间"),
            "published_at": value(row, "发布时间"),
            "author": value(row, "作者"),
            "is_original": value(row, "是否原创"),
            "article_type": value(row, "文章类型"),
            "collection": value(row, "所属合集"),
        }
        if title:
            by_title[str(title).strip()] = record
        if url:
            by_url[str(url).strip()] = record
    return {**{f"title:{key}": value for key, value in by_title.items()}, **{f"url:{key}": value for key, value in by_url.items()}}


def clean_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[#>*_`~|{}\[\]()+\\=-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def strip_export_noise(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("![") or stripped.startswith("![]("):
            continue
        if stripped.startswith("<") and stripped.endswith(">"):
            continue
        if any(token in stripped for token in ("font-family", "__page_content__", "wx_fmt=", "padding:", "margin:")):
            if len(stripped) > 300:
                continue
        cleaned.append(stripped)
    return cleaned


def title_from_markdown(path: Path, lines: list[str]) -> str:
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
        if idx + 1 < len(lines) and re.fullmatch(r"=+", lines[idx + 1].strip()):
            candidate = clean_text(stripped)
            if candidate:
                return candidate
    return path.stem.replace("_", " ").strip()


def extract_source_url(text: str) -> str | None:
    match = re.search(r"原文地址:\s*\[?((?:https?://)[^\]\s)]+)", text)
    if match:
        return match.group(1).replace("\\_", "_")
    match = re.search(r"https://mp\.weixin\.qq\.com/[^\]\s)]+", text)
    return match.group(0).replace("\\_", "_") if match else None


def extract_published_at(text: str) -> str | None:
    match = re.search(r"(20\d{2}-\d{2}-\d{2})(?:\s+(\d{1,2}:\d{2}))?", text)
    if not match:
        return None
    return f"{match.group(1)} {match.group(2)}" if match.group(2) else match.group(1)


def summarize(lines: list[str], title: str, max_chars: int = 220) -> str:
    paragraphs: list[str] = []
    for line in lines:
        if title and title in line:
            continue
        if line.startswith("> 原文地址"):
            continue
        if any(token in line for token in ("原创", "OpenDataLab")) and re.search(r"20\d{2}-\d{2}-\d{2}", line):
            continue
        if re.fullmatch(r"[-=]{2,}", line):
            continue
        cleaned = clean_text(line)
        if len(cleaned) < 20:
            continue
        paragraphs.append(cleaned)
        if sum(len(item) for item in paragraphs) >= max_chars:
            break
    summary = " ".join(paragraphs)
    return summary[:max_chars].strip()


def infer_topics(title: str, body: str, topic_rules: dict[str, list[str]]) -> list[str]:
    haystack = f"{title}\n{body}".lower()
    matched: list[str] = []
    for topic, keywords in topic_rules.items():
        if any(keyword.lower() in haystack for keyword in keywords):
            matched.append(topic)
    return matched


def extract_keywords(title: str, body: str, topic_rules: dict[str, list[str]], limit: int = 12) -> list[str]:
    candidates: list[str] = []
    haystack = f"{title}\n{body}".lower()
    for keywords in topic_rules.values():
        for keyword in keywords:
            if keyword.lower() in haystack and keyword not in candidates:
                candidates.append(keyword)

    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_.+-]{1,}|[\u4e00-\u9fff]{2,}", f"{title}\n{body}")
    counts = Counter(token for token in tokens if token not in STOPWORDS and len(token) <= 32)
    for token, _ in counts.most_common(limit * 2):
        if token not in candidates:
            candidates.append(token)
        if len(candidates) >= limit:
            break
    return candidates[:limit]


def spreadsheet_metadata(title: str, source_url: str | None, index: dict[str, dict[str, object]]) -> dict[str, object]:
    if source_url:
        match = index.get(f"url:{source_url}")
        if match:
            return match
    return index.get(f"title:{title}", {})


def build_record(
    path: Path,
    root: Path,
    topic_rules: dict[str, list[str]],
    sheet_index: dict[str, dict[str, object]],
) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    raw_lines = text.splitlines()
    content_lines = strip_export_noise(raw_lines)
    title = title_from_markdown(path, content_lines)
    source_url = extract_source_url(text)
    sheet_meta = spreadsheet_metadata(title, source_url, sheet_index)
    compact_body = clean_text("\n".join(content_lines))
    return {
        "account": sheet_meta.get("account") or "OpenDataLab",
        "wechat_id": sheet_meta.get("wechat_id"),
        "title": title,
        "file": str(path.resolve().relative_to(root.resolve())),
        "source_url": sheet_meta.get("source_url") or source_url,
        "cover_url": sheet_meta.get("cover_url"),
        "created_at": sheet_meta.get("created_at"),
        "published_at": sheet_meta.get("published_at") or extract_published_at(text),
        "author": sheet_meta.get("author"),
        "is_original": sheet_meta.get("is_original"),
        "article_type": sheet_meta.get("article_type"),
        "collection": sheet_meta.get("collection"),
        "topics": infer_topics(title, compact_body, topic_rules),
        "keywords": extract_keywords(title, compact_body, topic_rules),
        "summary": sheet_meta.get("spreadsheet_summary") or summarize(content_lines, title),
        "char_count": len(text),
    }


def iter_article_files(root: Path, articles_dir: Path) -> list[Path]:
    if not articles_dir.is_absolute():
        articles_dir = root / articles_dir
    source_dir = articles_dir if articles_dir.exists() else root
    return sorted(
        path
        for path in source_dir.glob("*.md")
        if path.name != "README.md" and not path.name.startswith(".")
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build knowledge/manifest.jsonl for article search.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root.")
    parser.add_argument("--topics", type=Path, default=DEFAULT_TOPICS, help="Topic rules JSON file.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output JSONL path.")
    parser.add_argument("--spreadsheet", type=Path, help="Optional WeChat export spreadsheet. Defaults to <root>/微信公众号文章.xlsx.")
    parser.add_argument("--articles-dir", type=Path, help="Directory containing article Markdown files. Defaults to <root>/articles.")
    args = parser.parse_args()

    topic_rules = load_topics(args.topics)
    spreadsheet = args.spreadsheet or args.root / DEFAULT_SPREADSHEET_NAME
    sheet_index = load_spreadsheet_index(spreadsheet)
    articles_dir = args.articles_dir or args.root / DEFAULT_ARTICLES_DIR_NAME
    records = [build_record(path, args.root, topic_rules, sheet_index) for path in iter_article_files(args.root, articles_dir)]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    metadata = {
        "article_count": len(records),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "output": str(args.output),
        "spreadsheet_records_loaded": len(sheet_index),
    }
    print(json.dumps(metadata, ensure_ascii=False))


if __name__ == "__main__":
    main()
