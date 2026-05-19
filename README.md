# OpenDataLab WeChat Articles

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article)

This repository collects exported OpenDataLab WeChat Official Account articles for local search, knowledge-base indexing, and downstream content organization.

## Contents

- 343 Markdown articles exported from the OpenDataLab WeChat Official Account.
- `微信公众号文章.xlsx`, a spreadsheet index for the exported articles.
- `knowledge/`, a lightweight JSONL index and search scripts.
- `skills/opendatalab-wechat-kb/`, an agent skill that searches this GitHub-backed knowledge base.
- `.claude-plugin/marketplace.json`, plugin marketplace metadata following the `skills/<skill-name>` bundle layout.

## Suggested Uses

- Build a local knowledge base for Codex or other AI assistants.
- Search historical OpenDataLab articles by topic, project, dataset, or event.
- Prepare structured metadata and retrieval indexes for RAG workflows.
- Install or reference the bundled skill from agent environments.

## Repository Layout

```text
.claude-plugin/
  marketplace.json
knowledge/
  manifest.jsonl
  topics.json
  scripts/
skills/
  opendatalab-wechat-kb/
    SKILL.md
    agents/
    scripts/
*.md
微信公众号文章.xlsx
```

## Search

Search the local repository:

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

Search through the skill's GitHub-backed cache:

```bash
python3 skills/opendatalab-wechat-kb/scripts/search_remote_repo.py "MinerU RAG 知识库" --top-k 5 --pretty
```

The remote-backed script clones or updates this repository into:

```text
~/.cache/opendatalab-wechat-article
```

## Skill

The bundled skill lives at:

```text
skills/opendatalab-wechat-kb
```

It follows the common skill-bundle structure used by repositories such as `jimliu/baoyu-skills`: keep each installable skill under `skills/<skill-name>/`, register it in `.claude-plugin/marketplace.json`, and keep heavy source data outside `SKILL.md`.

## Notes

The article filenames are preserved from the export source so they remain traceable to the original titles.
