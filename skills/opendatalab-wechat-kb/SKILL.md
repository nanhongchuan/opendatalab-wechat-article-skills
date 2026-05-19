---
name: opendatalab-wechat-kb
description: Use this when the user asks to search, summarize, classify, cite, or reuse OpenDataLab WeChat articles from nanhongchuan/opendatalab-wechat-article, especially for MinerU, RAG, AI datasets, document parsing, OpenDataLab events, tutorials, academic papers, autonomous driving, medical AI, robotics, and large model content planning.
---

# OpenDataLab WeChat Knowledge Base

## Source of Truth

The canonical article repository is:

`https://github.com/nanhongchuan/opendatalab-wechat-article`

Do not assume the article corpus is bundled in this skill. The skill should clone or update the GitHub repo into a local cache, then search that cache.

## Workflow

1. Run `scripts/search_remote_repo.py` with the user's query.
2. Review the JSON results: title, source file, URL, date, topics, summary, and snippet.
3. Open the most relevant Markdown files from the cached repo when deeper reading is needed.
4. Answer with article titles and source filenames. Include original WeChat URLs when present.
5. For broad planning tasks, group results by topic, audience, date, and reuse scenario.

## Commands

Search the remote-backed cache:

```bash
python3 scripts/search_remote_repo.py "MinerU RAG 知识库" --top-k 10 --pretty
```

Filter by topic:

```bash
python3 scripts/search_remote_repo.py "数据集" --topic Dataset --top-k 10 --pretty
```

The script uses this cache by default:

`~/.cache/opendatalab-wechat-article`

If the cache does not exist, the script clones the GitHub repo. If it exists, the script pulls the latest changes before searching.

## Output Expectations

When answering, prefer this source format:

- `文章标题` - `文件名` - `原文链接`

For content reuse tasks, cite only the local article title and filename unless the user asks for full citations.
