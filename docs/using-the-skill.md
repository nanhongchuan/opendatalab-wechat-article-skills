# Using opendatalab-wechat-article-skills

This repository follows the common skill-bundle layout:

```text
.claude-plugin/
  marketplace.json
skills/
  opendatalab-wechat-articles/
    SKILL.md
    agents/openai.yaml
    scripts/
knowledge/
  manifest.jsonl
  topics.json
  scripts/
```

The article corpus remains in the GitHub repository. The skill does not bundle article copies; it clones or updates the repository into a local cache before searching.

## Local Search

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

## Remote-Backed Search

```bash
python3 skills/opendatalab-wechat-articles/scripts/search_remote_repo.py "MinerU RAG 知识库" --top-k 5 --pretty
```

By default, the remote-backed script uses:

```text
/Users/weiliqun/Desktop/OpenDataLab 公众号
```

## Install as a Codex Skill

Copy or install the skill directory:

```text
skills/opendatalab-wechat-articles
```

to:

```text
~/.codex/skills/opendatalab-wechat-articles
```

Then ask the agent to use `opendatalab-wechat-articles` for OpenDataLab article search, summarization, topic planning, and citation tasks.
