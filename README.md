# OpenDataLab WeChat Knowledge Base

English | [中文](README_zh-CN.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article)

An installable agent skill and article corpus for searching, reading, summarizing, and citing OpenDataLab WeChat articles.

## Install

Recommended: tell your agent in natural language:

> Please install github.com/nanhongchuan/opendatalab-wechat-article as a skill.

A capable agent can choose the right install path for its environment. It may use direct skill install:

```bash
npx skills add nanhongchuan/opendatalab-wechat-article
```

Or, in a plugin-enabled agent, it may register the marketplace and install the plugin:

```text
/plugin marketplace add nanhongchuan/opendatalab-wechat-article
/plugin install opendatalab-wechat-article@opendatalab-wechat-article
```

Requirements: `git` and `python3`. The optional `openpyxl` package lets the index builder read spreadsheet metadata from `微信公众号文章.xlsx`.

## What Gets Installed

| Item | Purpose |
|------|---------|
| `opendatalab-wechat-article` | Plugin registered by `.claude-plugin/marketplace.json` |
| `opendatalab-wechat-kb` | Skill used by agents to search this article knowledge base |

Use examples:

```text
Use opendatalab-wechat-kb to find articles about MinerU RAG.
```

```text
Find OpenDataLab WeChat articles about datasets and group them by topic.
```

## How It Works

```text
User asks a question
  ↓
Agent triggers opendatalab-wechat-kb
  ↓
Skill runs scripts/search_remote_repo.py
  ↓
Script clones or updates this repo into ~/.cache/opendatalab-wechat-article
  ↓
Script searches knowledge/manifest.jsonl
  ↓
Agent opens matching files under articles/ only when needed
  ↓
Agent answers with article titles, filenames, and source URLs
```

The skill does not put all article bodies into `SKILL.md`; it searches the index first and reads full Markdown files only when needed.

## Repository Layout

```text
.claude-plugin/marketplace.json      # plugin registration for agents
skills/opendatalab-wechat-kb/        # installable skill
knowledge/manifest.jsonl             # searchable article index
knowledge/topics.json                # topic rules
knowledge/scripts/                   # local index/search scripts
articles/                            # 343 WeChat article Markdown files
微信公众号文章.xlsx                    # spreadsheet metadata
```

## Local Search

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

Filter by topic:

```bash
python3 knowledge/scripts/search_articles.py "数据集" --topic Dataset --top-k 10 --pretty
```

Search through the skill cache:

```bash
python3 skills/opendatalab-wechat-kb/scripts/search_remote_repo.py "MinerU MCP Server" --top-k 5 --pretty
```

## Update The Index

After adding or updating files in `articles/`, rebuild:

```bash
python3 knowledge/scripts/build_manifest.py
```

The builder reads `articles/*.md`, `微信公众号文章.xlsx`, and `knowledge/topics.json`, then writes `knowledge/manifest.jsonl`.

