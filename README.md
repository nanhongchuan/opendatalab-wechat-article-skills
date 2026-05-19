# OpenDataLab WeChat Knowledge Base

English | [中文](README_zh-CN.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article)

An OpenDataLab WeChat Official Account article knowledge base for Claude Code, Codex, and other agents. After installation, an agent can search, read, summarize, and cite OpenDataLab WeChat articles from this repository.

This repository is both an article corpus and an installable agent skill.

## Requirements

- `git`
- `python3`
- Node.js / npm if installing with `npx skills add`

The search scripts use only the Python standard library. When rebuilding the index, `openpyxl` is optional and enables structured metadata extraction from `微信公众号文章.xlsx`.

## Installation

### Quick Install (Recommended)

```bash
npx skills add nanhongchuan/opendatalab-wechat-article
```

### Register Plugin Marketplace

In an agent environment that supports plugin marketplaces, run:

```bash
/plugin marketplace add nanhongchuan/opendatalab-wechat-article
```

### Install The Skill

**Option 1: Browse UI**

1. Select **Browse and install plugins**
2. Select **opendatalab-wechat-article**
3. Select the **opendatalab-wechat-article** plugin
4. Select **Install now**

**Option 2: Direct install**

```bash
/plugin install opendatalab-wechat-article@opendatalab-wechat-article
```

**Option 3: Ask the agent**

Tell the agent:

> Please install the skill from github.com/nanhongchuan/opendatalab-wechat-article.

## Updating

If installed through the plugin marketplace, update it in the agent:

1. Run `/plugin`
2. Switch to **Marketplaces**
3. Select **opendatalab-wechat-article**
4. Select **Update marketplace**

You can also enable auto-update so the agent fetches the latest version on startup.

## Available Plugin

The marketplace exposes one plugin to avoid duplicate skill registration.

| Plugin | Description | Contents |
|--------|-------------|----------|
| **opendatalab-wechat-article** | Search and summarize OpenDataLab WeChat articles | The `opendatalab-wechat-kb` skill and the GitHub-backed article knowledge base |

## Available Skill

### opendatalab-wechat-kb

OpenDataLab WeChat article knowledge-base search skill. Use it for:

- Searching historical OpenDataLab WeChat articles
- Finding content about MinerU, RAG, datasets, document parsing, LLMs, events, and tutorials
- Summarizing article viewpoints and preparing citations
- Supporting content planning, knowledge-base Q&A, and RAG workflows

Examples:

```text
Use opendatalab-wechat-kb to find articles about MinerU RAG.
```

```text
Find several OpenDataLab WeChat articles about datasets and group them by topic.
```

```text
Summarize recent MinerU product and ecosystem updates from OpenDataLab WeChat articles.
```

In Codex, you can also invoke it explicitly:

```text
Use $opendatalab-wechat-kb to search MinerU MCP Server articles.
```

## Agent Workflow

The skill does not load every article body into context. It works through a retrieval-first flow:

```text
User asks a question
  ↓
Agent triggers opendatalab-wechat-kb
  ↓
Agent reads skills/opendatalab-wechat-kb/SKILL.md
  ↓
Agent runs scripts/search_remote_repo.py
  ↓
Script clones or updates this GitHub repo into a local cache
  ↓
Script reads knowledge/manifest.jsonl
  ↓
Script searches relevant articles
  ↓
Agent opens matching Markdown files under articles/ only when needed
  ↓
Agent answers, summarizes, or cites from the article content
```

Default cache directory:

```text
~/.cache/opendatalab-wechat-article
```

## Repository Layout

```text
.claude-plugin/
  marketplace.json
skills/
  opendatalab-wechat-kb/
    SKILL.md
    agents/
      openai.yaml
    scripts/
      search_remote_repo.py
      search_articles.py
      build_manifest.py
knowledge/
  manifest.jsonl
  topics.json
  scripts/
    search_articles.py
    build_manifest.py
articles/
  *.md
微信公众号文章.xlsx
```

### Directory Roles

| Path | Purpose |
|------|---------|
| `.claude-plugin/marketplace.json` | Machine-readable plugin registration entry for agents and plugin systems |
| `skills/opendatalab-wechat-kb/` | The installable skill that agents actually use |
| `skills/opendatalab-wechat-kb/SKILL.md` | Agent-facing instructions: when to trigger, how to search, and how to cite |
| `skills/opendatalab-wechat-kb/scripts/` | Skill-bundled scripts for remote clone/update and search |
| `knowledge/manifest.jsonl` | Lightweight searchable index, one JSON record per article |
| `knowledge/topics.json` | Topic classification rules |
| `knowledge/scripts/` | Local index-building and search scripts |
| `articles/` | WeChat article Markdown bodies |
| `微信公众号文章.xlsx` | Spreadsheet metadata source: account, article ID, URL, author, publish time, cover, summary, and related fields |

## Local Search

Search the local repository:

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

Filter by topic:

```bash
python3 knowledge/scripts/search_articles.py "数据集" --topic Dataset --top-k 10 --pretty
```

Search through the skill's remote-backed cache:

```bash
python3 skills/opendatalab-wechat-kb/scripts/search_remote_repo.py "MinerU MCP Server" --top-k 5 --pretty
```

## Maintaining The Index

After adding or updating Markdown articles under `articles/`, rebuild the index:

```bash
python3 knowledge/scripts/build_manifest.py
```

The builder reads:

- `articles/*.md`
- `微信公众号文章.xlsx`
- `knowledge/topics.json`

Then it writes:

```text
knowledge/manifest.jsonl
```

`manifest.jsonl` stores titles, file paths, source URLs, accounts, authors, publish times, summaries, topic labels, and keywords so agents can search quickly before opening full article bodies.

## Data Notes

- The repository currently contains 343 OpenDataLab WeChat articles.
- Article bodies are stored under `articles/`.
- Markdown filenames preserve the exported title format for traceability.
- `微信公众号文章.xlsx` is the structured metadata source.
- The skill keeps article bodies out of `SKILL.md`; it uses the index and scripts to read content only when needed.

