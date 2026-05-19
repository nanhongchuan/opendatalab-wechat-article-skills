# opendatalab-wechat-article-skills

English | [中文](README_zh-CN.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article-skills)

`opendatalab-wechat-article-skills` provides an installable agent skill and a searchable corpus of OpenDataLab WeChat articles.

## Installation

In agent environments that support GitHub skill installation, request installation with:

> Install github.com/nanhongchuan/opendatalab-wechat-article-skills as a skill.

For manual installation, choose one method according to the target environment.

| Environment | Plugin Marketplace Support | Recommended Method |
|-------------|----------------------------|--------------------|
| Codex | Does not use the Claude Code plugin marketplace | Use the Codex skill installation mechanism, or run `npx skills add` in a terminal |
| Claude Code | Supports the `/plugin` marketplace commands | Run `/plugin marketplace add` and `/plugin install` inside Claude Code |
| OpenClaw | Supports marketplace installation | Run `openclaw plugins install --marketplace` in a terminal |

### Codex / General Skill Installation

Run in a terminal:

```bash
npx skills add nanhongchuan/opendatalab-wechat-article-skills
```

### Claude Code Plugin Marketplace Installation

Run the following commands inside Claude Code:

```text
/plugin marketplace add nanhongchuan/opendatalab-wechat-article-skills
/plugin install opendatalab-wechat-article-skills@opendatalab-wechat-article-skills
```

`/plugin marketplace add` registers the marketplace. `/plugin install` installs the plugin from that marketplace.

### OpenClaw Marketplace Installation

Run in a terminal:

```bash
openclaw plugins install opendatalab-wechat-article-skills --marketplace nanhongchuan/opendatalab-wechat-article-skills
```

Requirements: `git`, `python3`. `openpyxl` is optional and is used only when rebuilding metadata from `微信公众号文章.xlsx`.

## Components

| Path | Description |
|------|-------------|
| `.claude-plugin/marketplace.json` | Plugin registration metadata for `opendatalab-wechat-article-skills` |
| `skills/opendatalab-wechat-articles/` | Installable skill used by agents |
| `knowledge/manifest.jsonl` | Search index for article metadata |
| `knowledge/topics.json` | Topic classification rules |
| `knowledge/scripts/` | Local indexing and search scripts |
| `articles/` | WeChat article Markdown corpus |
| `微信公众号文章.xlsx` | Source spreadsheet for article metadata |

## Agent Workflow

```text
User request
  -> Agent activates opendatalab-wechat-articles
  -> Skill runs scripts/search_remote_repo.py
  -> Repository cache is created or updated under the configured local article archive
  -> knowledge/manifest.jsonl is searched first
  -> Relevant Markdown files in articles/ are opened only when needed
  -> Agent responds with titles, filenames, and source URLs
```

Article bodies are stored as Markdown files, not embedded in `SKILL.md`. The skill uses the index for retrieval and reads full articles only when required.

## Local Search

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

```bash
python3 knowledge/scripts/search_articles.py "数据集" --topic Dataset --top-k 10 --pretty
```

```bash
python3 skills/opendatalab-wechat-articles/scripts/search_remote_repo.py "MinerU MCP Server" --top-k 5 --pretty
```

## Index Maintenance

After adding or updating files in `articles/`, rebuild the index:

```bash
python3 knowledge/scripts/build_manifest.py
```

The builder reads `articles/*.md`, `微信公众号文章.xlsx`, and `knowledge/topics.json`, then writes `knowledge/manifest.jsonl`.
