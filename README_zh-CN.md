# opendatalab-wechat-article-skills

[English](README.md) | 中文

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article-skills)

`opendatalab-wechat-article-skills` 提供可安装的 Agent skill，以及可检索的 OpenDataLab 微信文章语料。

## 安装

在支持 GitHub skill 安装的 Agent 环境中，可通过自然语言发起安装：

> 请将 github.com/nanhongchuan/opendatalab-wechat-article-skills 安装为 skill。

手动安装时，请根据运行环境选择一种方式。

| 环境 | 插件市场支持 | 推荐方式 |
|------|--------------|----------|
| Codex | 不使用 Claude Code 插件市场 | 使用 Codex 的 skill 安装机制，或在终端执行 `npx skills add` |
| Claude Code | 支持 `/plugin` 插件市场 | 在 Claude Code 会话中执行 `/plugin marketplace add` 和 `/plugin install` |
| OpenClaw | 支持 marketplace 安装 | 在终端执行 `openclaw plugins install --marketplace` |

### Codex / 通用 Skill 安装

在终端执行：

```bash
npx skills add nanhongchuan/opendatalab-wechat-article-skills
```

### Claude Code 插件市场安装

在 Claude Code 会话中依次执行：

```text
/plugin marketplace add nanhongchuan/opendatalab-wechat-article-skills
/plugin install opendatalab-wechat-article-skills@opendatalab-wechat-article-skills
```

`/plugin marketplace add` 用于添加 marketplace，`/plugin install` 用于安装该 marketplace 中的插件。

### OpenClaw 插件市场安装

在终端执行：

```bash
openclaw plugins install opendatalab-wechat-article-skills --marketplace nanhongchuan/opendatalab-wechat-article-skills
```

前置要求：`git`、`python3`。`openpyxl` 为可选依赖，仅在通过 `微信公众号文章.xlsx` 重建元数据时使用。

## 组成

| 路径 | 说明 |
|------|------|
| `.claude-plugin/marketplace.json` | `opendatalab-wechat-article-skills` 的插件注册元数据 |
| `skills/opendatalab-wechat-kb/` | Agent 使用的可安装 skill |
| `knowledge/manifest.jsonl` | 文章元数据检索索引 |
| `knowledge/topics.json` | 主题分类规则 |
| `knowledge/scripts/` | 本地索引与检索脚本 |
| `articles/` | 微信文章 Markdown 语料 |
| `微信公众号文章.xlsx` | 文章元数据来源表 |

## Agent 工作流程

```text
用户提出请求
  -> Agent 启用 opendatalab-wechat-kb
  -> skill 运行 scripts/search_remote_repo.py
  -> 仓库缓存创建或更新到 ~/.cache/opendatalab-wechat-article-skills
  -> 优先检索 knowledge/manifest.jsonl
  -> 仅在需要时读取 articles/ 中的 Markdown 原文
  -> Agent 基于标题、文件名和原文链接生成回答
```

文章正文以 Markdown 文件形式存放，不写入 `SKILL.md`。skill 先检索索引，再按需读取完整文章。

## 本地检索

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

```bash
python3 knowledge/scripts/search_articles.py "数据集" --topic Dataset --top-k 10 --pretty
```

```bash
python3 skills/opendatalab-wechat-kb/scripts/search_remote_repo.py "MinerU MCP Server" --top-k 5 --pretty
```

## 索引维护

新增或更新 `articles/` 后，重新构建索引：

```bash
python3 knowledge/scripts/build_manifest.py
```

构建脚本读取 `articles/*.md`、`微信公众号文章.xlsx` 和 `knowledge/topics.json`，并生成 `knowledge/manifest.jsonl`。
