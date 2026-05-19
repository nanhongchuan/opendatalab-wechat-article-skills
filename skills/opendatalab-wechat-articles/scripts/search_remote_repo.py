#!/usr/bin/env python3
"""Clone/update the OpenDataLab WeChat article skills repo and search it."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


REPO_URL = "https://github.com/nanhongchuan/opendatalab-wechat-article-skills.git"
DEFAULT_CACHE = Path("/Users/weiliqun/Desktop/OpenDataLab 公众号")
SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent


def run(command: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def ensure_git() -> None:
    if not shutil.which("git"):
        raise SystemExit("git is required to clone or update the knowledge repo.")


def ensure_cache(cache_dir: Path, repo_url: str, update: bool = True) -> Path:
    ensure_git()
    if not cache_dir.exists():
        cache_dir.parent.mkdir(parents=True, exist_ok=True)
        run(["git", "clone", repo_url, str(cache_dir)])
        return cache_dir

    if not (cache_dir / ".git").exists():
        raise SystemExit(f"Cache path exists but is not a git repo: {cache_dir}")

    if update:
        run(["git", "-C", str(cache_dir), "pull", "--ff-only"])
    return cache_dir


def ensure_manifest(repo_dir: Path) -> None:
    manifest = repo_dir / "knowledge" / "manifest.jsonl"
    if manifest.exists():
        return
    manifest.parent.mkdir(parents=True, exist_ok=True)
    builder = repo_dir / "knowledge" / "scripts" / "build_manifest.py"
    topics = repo_dir / "knowledge" / "topics.json"
    if not builder.exists():
        builder = SCRIPT_DIR / "build_manifest.py"
    if not topics.exists():
        topics = SKILL_DIR / "topics.json"
    if not builder.exists():
        raise SystemExit(f"Manifest builder is missing in repo and skill: {repo_dir}")
    run(
        [
            sys.executable,
            str(builder),
            "--root",
            str(repo_dir),
            "--topics",
            str(topics),
            "--output",
            str(manifest),
        ],
        cwd=repo_dir,
    )


def search_repo(
    repo_dir: Path,
    query: str,
    top_k: int,
    topic: str | None,
    include_body: bool,
    pretty: bool,
) -> str:
    search_script = repo_dir / "knowledge" / "scripts" / "search_articles.py"
    if not search_script.exists():
        search_script = SCRIPT_DIR / "search_articles.py"
    if not search_script.exists():
        raise SystemExit(f"Search script not found in repo or skill: {repo_dir}")

    command = [
        sys.executable,
        str(search_script),
        query,
        "--root",
        str(repo_dir),
        "--manifest",
        str(repo_dir / "knowledge" / "manifest.jsonl"),
        "--top-k",
        str(top_k),
    ]
    if topic:
        command.extend(["--topic", topic])
    if include_body:
        command.append("--include-body")
    if pretty:
        command.append("--pretty")

    result = run(command, cwd=repo_dir)
    return result.stdout


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the remote OpenDataLab WeChat article knowledge repo.")
    parser.add_argument("query", help="Search query, for example: 'MinerU RAG 知识库'.")
    parser.add_argument("--repo-url", default=REPO_URL, help="GitHub repo URL.")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE, help="Local cache directory.")
    parser.add_argument("--top-k", type=int, default=10, help="Maximum number of results.")
    parser.add_argument("--topic", help="Optional topic filter, for example: MinerU, Dataset, Event.")
    parser.add_argument("--include-body", action="store_true", help="Include full Markdown body in JSON output.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    parser.add_argument("--no-update", action="store_true", help="Use existing cache without git pull.")
    args = parser.parse_args()

    try:
        repo_dir = ensure_cache(args.cache_dir.expanduser(), args.repo_url, update=not args.no_update)
        ensure_manifest(repo_dir)
        sys.stdout.write(
            search_repo(
                repo_dir=repo_dir,
                query=args.query,
                top_k=args.top_k,
                topic=args.topic,
                include_body=args.include_body,
                pretty=args.pretty,
            )
        )
    except subprocess.CalledProcessError as exc:
        error = {
            "error": "command_failed",
            "command": exc.cmd,
            "stdout": exc.stdout,
            "stderr": exc.stderr,
        }
        print(json.dumps(error, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(exc.returncode)


if __name__ == "__main__":
    main()
