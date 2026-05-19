#!/usr/bin/env python3
"""Search OpenDataLab WeChat article manifest and Markdown bodies."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "knowledge" / "manifest.jsonl"


def load_manifest(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"Manifest not found: {path}. Run knowledge/scripts/build_manifest.py first.")
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def terms_from_query(query: str) -> list[str]:
    terms = re.findall(r"[A-Za-z0-9_.+-]+|[\u4e00-\u9fff]{2,}", query.lower())
    return [term for term in terms if term.strip()]


def read_article(root: Path, file_name: str) -> str:
    path = root / file_name
    if not path.exists() and Path(file_name).parent == Path("."):
        path = root / "articles" / file_name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def clean_article_text(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("![") or stripped.startswith("![]("):
            continue
        if any(token in stripped for token in ("font-family", "__page_content__", "wx_fmt=", "padding:", "margin:")):
            if len(stripped) > 300:
                continue
        stripped = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", stripped)
        stripped = re.sub(r"<[^>]+>", " ", stripped)
        stripped = re.sub(r"\s+", " ", stripped)
        if stripped:
            lines.append(stripped)
    return "\n".join(lines)


def make_snippet(text: str, terms: list[str], max_chars: int = 220) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return ""
    lower = compact.lower()
    positions = [lower.find(term.lower()) for term in terms if lower.find(term.lower()) >= 0]
    if positions:
        start = max(0, min(positions) - 70)
        end = min(len(compact), start + max_chars)
        return compact[start:end].strip()
    return compact[:max_chars].strip()


def score_record(record: dict[str, Any], body: str, terms: list[str]) -> tuple[int, int]:
    title = str(record.get("title", "")).lower()
    file_name = str(record.get("file", "")).lower()
    summary = str(record.get("summary", "")).lower()
    keywords = " ".join(record.get("keywords", [])).lower()
    topics = " ".join(record.get("topics", [])).lower()
    body_lower = body.lower()

    score = 0
    body_hits = 0
    for term in terms:
        term = term.lower()
        if term in title:
            score += 20
        if term in file_name:
            score += 10
        if term in keywords:
            score += 8
        if term in topics:
            score += 6
        if term in summary:
            score += 5
        count = body_lower.count(term)
        if count:
            body_hits += count
            score += min(count, 10)
    return score, body_hits


def search(
    root: Path,
    manifest: Path,
    query: str,
    top_k: int,
    topic: str | None = None,
    include_body: bool = False,
) -> list[dict[str, Any]]:
    records = load_manifest(manifest)
    terms = terms_from_query(query)
    if not terms:
        raise SystemExit("Query must contain at least one searchable term.")

    results: list[dict[str, Any]] = []
    for record in records:
        record_topics = record.get("topics", [])
        if topic and topic not in record_topics:
            continue
        body = read_article(root, str(record.get("file", "")))
        clean_body = clean_article_text(body)
        score, body_hits = score_record(record, clean_body, terms)
        if score <= 0:
            continue
        item = {
            "score": score,
            "body_hits": body_hits,
            "account": record.get("account"),
            "wechat_id": record.get("wechat_id"),
            "title": record.get("title"),
            "file": record.get("file"),
            "source_url": record.get("source_url"),
            "cover_url": record.get("cover_url"),
            "created_at": record.get("created_at"),
            "published_at": record.get("published_at"),
            "author": record.get("author"),
            "is_original": record.get("is_original"),
            "article_type": record.get("article_type"),
            "collection": record.get("collection"),
            "topics": record.get("topics", []),
            "keywords": record.get("keywords", []),
            "summary": record.get("summary"),
            "snippet": make_snippet(clean_body or str(record.get("summary", "")), terms),
        }
        if include_body:
            item["body"] = body
        results.append(item)

    results.sort(key=lambda item: (item["score"], item["body_hits"], item.get("published_at") or ""), reverse=True)
    return results[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser(description="Search OpenDataLab WeChat article knowledge base.")
    parser.add_argument("query", help="Search query, for example: 'MinerU RAG 知识库'.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Manifest JSONL path.")
    parser.add_argument("--top-k", type=int, default=10, help="Maximum number of results.")
    parser.add_argument("--topic", help="Optional topic filter, for example: MinerU, Dataset, Event.")
    parser.add_argument("--include-body", action="store_true", help="Include full Markdown body in JSON output.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    results = search(
        root=args.root,
        manifest=args.manifest,
        query=args.query,
        top_k=args.top_k,
        topic=args.topic,
        include_body=args.include_body,
    )
    print(json.dumps(results, ensure_ascii=False, indent=2 if args.pretty else None))


if __name__ == "__main__":
    main()
