# OpenDataLab 微信公众号文章

[English](README.md) | [中文](README_zh-CN.md)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article)

本仓库收集了 OpenDataLab 微信公众号文章导出内容，方便本地检索、知识库索引，以及后续内容整理与再利用。

## 内容

- `articles/`，343 篇从 OpenDataLab 微信公众号导出的 Markdown 文章。
- `微信公众号文章.xlsx`，文章索引表，包含账号、文章 ID、原文链接、作者、发布时间、封面、摘要和合集等元数据。
- `knowledge/`，轻量级 JSONL 索引与检索脚本。
- `skills/opendatalab-wechat-kb/`，用于检索这个 GitHub 知识库的智能体技能。
- `.claude-plugin/marketplace.json`，遵循 `skills/<skill-name>` 目录结构的插件市场元数据。

## 适用场景

- 为 Codex 或其他 AI 助手构建本地知识库。
- 按主题、项目、数据集或活动检索 OpenDataLab 历史文章。
- 为 RAG 工作流准备结构化元数据和检索索引。
- 在智能体环境中安装或引用仓库内置技能。

## 仓库结构

```text
.claude-plugin/
  marketplace.json
knowledge/
  manifest.jsonl
  topics.json
  scripts/
articles/
  *.md
skills/
  opendatalab-wechat-kb/
    SKILL.md
    agents/
    scripts/
微信公众号文章.xlsx
```

## 检索

检索本地仓库：

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

添加或更新文章后，重新构建 manifest：

```bash
python3 knowledge/scripts/build_manifest.py
```

通过技能的 GitHub 缓存检索：

```bash
python3 skills/opendatalab-wechat-kb/scripts/search_remote_repo.py "MinerU RAG 知识库" --top-k 5 --pretty
```

远程检索脚本会将本仓库克隆或更新到：

```text
~/.cache/opendatalab-wechat-article
```

## 技能

内置技能位于：

```text
skills/opendatalab-wechat-kb
```

它采用与 `jimliu/baoyu-skills` 等仓库类似的技能包结构：每个可安装技能都放在 `skills/<skill-name>/` 下，在 `.claude-plugin/marketplace.json` 中注册，并将体量较大的源数据保留在 `SKILL.md` 之外。

该技能不会把文章正文嵌入 `SKILL.md`。它会克隆或更新这个 GitHub 仓库，读取 `knowledge/manifest.jsonl`，并且只在需要深入阅读时打开匹配的 Markdown 文件。这样既能保持技能轻量，也能让智能体访问完整的微信公众号文章语料和从表格整理出的账号元数据。

## 说明

`articles/` 下保留了原始文章标题对应的文件名，方便追溯每篇文章。
