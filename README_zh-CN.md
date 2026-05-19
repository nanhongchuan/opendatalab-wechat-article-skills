# OpenDataLab 微信文章知识库

[English](README.md) | 中文

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article)

一个可安装的 Agent skill 和微信文章语料库，用于检索、阅读、总结和引用 OpenDataLab 微信文章。

## 安装

推荐：直接用自然语言告诉 Agent：

> 请安装 github.com/nanhongchuan/opendatalab-wechat-article 这个 skill。

聪明的 Agent 会根据当前环境选择合适的安装方式。它可能直接安装 skill：

```bash
npx skills add nanhongchuan/opendatalab-wechat-article
```

也可能在支持插件的 Agent 里先添加 marketplace，再安装插件：

```text
/plugin marketplace add nanhongchuan/opendatalab-wechat-article
/plugin install opendatalab-wechat-article@opendatalab-wechat-article
```

前置要求：`git` 和 `python3`。如果本机有 `openpyxl`，重建索引时可以读取 `微信公众号文章.xlsx` 里的结构化元数据。

## 安装后有什么

| 项目 | 作用 |
|------|------|
| `opendatalab-wechat-article` | `.claude-plugin/marketplace.json` 注册的插件 |
| `opendatalab-wechat-kb` | Agent 用来检索这个文章知识库的 skill |

使用示例：

```text
使用 opendatalab-wechat-kb 查一下 MinerU RAG 相关的文章。
```

```text
从 OpenDataLab 微信文章里找几篇关于数据集的文章，并按主题分类。
```

## 工作逻辑

```text
用户提出问题
  ↓
Agent 触发 opendatalab-wechat-kb
  ↓
skill 运行 scripts/search_remote_repo.py
  ↓
脚本把这个仓库克隆或更新到 ~/.cache/opendatalab-wechat-article
  ↓
脚本检索 knowledge/manifest.jsonl
  ↓
Agent 只在需要时打开 articles/ 里的相关文章
  ↓
Agent 根据文章标题、文件名和原文链接回答
```

这个 skill 不会把所有文章正文塞进 `SKILL.md`，而是先查索引，再按需读取完整 Markdown。

## 仓库结构

```text
.claude-plugin/marketplace.json      # 给 Agent 看的插件注册入口
skills/opendatalab-wechat-kb/        # 可安装的 skill
knowledge/manifest.jsonl             # 文章检索索引
knowledge/topics.json                # 主题规则
knowledge/scripts/                   # 本地索引和检索脚本
articles/                            # 343 篇微信文章 Markdown
微信公众号文章.xlsx                    # 文章元数据表
```

## 本地检索

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

按主题过滤：

```bash
python3 knowledge/scripts/search_articles.py "数据集" --topic Dataset --top-k 10 --pretty
```

通过 skill 缓存检索：

```bash
python3 skills/opendatalab-wechat-kb/scripts/search_remote_repo.py "MinerU MCP Server" --top-k 5 --pretty
```

## 更新索引

新增或更新 `articles/` 后，重新构建索引：

```bash
python3 knowledge/scripts/build_manifest.py
```

构建脚本会读取 `articles/*.md`、`微信公众号文章.xlsx` 和 `knowledge/topics.json`，然后生成 `knowledge/manifest.jsonl`。

