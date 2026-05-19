# OpenDataLab 微信文章知识库

[English](README.md) | 中文

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/nanhongchuan/opendatalab-wechat-article)

OpenDataLab 微信公众号文章知识库，面向 Claude Code、Codex 等 Agent 使用。安装后，Agent 可以检索、阅读、总结和引用本仓库中的 OpenDataLab 微信文章。

这个仓库既是文章语料库，也是一个可安装的 Agent skill。

## 前置要求

- 已安装 `git`
- 已安装 `python3`
- 如使用 `npx skills add` 安装，需要 Node.js / npm 环境

检索脚本只依赖 Python 标准库；重建索引时如果本机有 `openpyxl`，会自动读取 `微信公众号文章.xlsx` 中的结构化元数据。

## 安装

### 快速安装（推荐）

```bash
npx skills add nanhongchuan/opendatalab-wechat-article
```

### 注册插件市场

在支持插件市场的 Agent 中运行：

```bash
/plugin marketplace add nanhongchuan/opendatalab-wechat-article
```

### 安装技能

**方式一：通过浏览界面**

1. 选择 **Browse and install plugins**
2. 选择 **opendatalab-wechat-article**
3. 选择 **opendatalab-wechat-article** 插件
4. 选择 **Install now**

**方式二：直接安装**

```bash
/plugin install opendatalab-wechat-article@opendatalab-wechat-article
```

**方式三：告诉 Agent**

直接告诉 Agent：

> 请帮我安装 github.com/nanhongchuan/opendatalab-wechat-article 这个 skill

## 更新技能

如果通过插件市场安装，可以在 Agent 中更新：

1. 运行 `/plugin`
2. 切换到 **Marketplaces**
3. 选择 **opendatalab-wechat-article**
4. 选择 **Update marketplace**

也可以启用自动更新，让 Agent 每次启动时获取最新版本。

## 可用插件

当前 marketplace 只暴露一个插件，避免同一个 skill 被重复注册。

| 插件 | 说明 | 包含内容 |
|------|------|----------|
| **opendatalab-wechat-article** | 检索和总结 OpenDataLab 微信文章 | `opendatalab-wechat-kb` skill，以及 GitHub 文章知识库 |

## 可用技能

### opendatalab-wechat-kb

OpenDataLab 微信文章知识库检索技能。适合用于：

- 检索 OpenDataLab 历史微信文章
- 查找 MinerU、RAG、数据集、文档解析、大模型、活动、课程等主题内容
- 总结文章观点、整理选题、生成引用材料
- 为内容策划、知识库问答和 RAG 工作流提供语料

示例：

```text
使用 opendatalab-wechat-kb 查一下 MinerU RAG 相关的文章
```

```text
帮我从 OpenDataLab 微信文章里找几篇关于数据集的文章，并按主题分类
```

```text
基于 OpenDataLab 微信文章，总结 MinerU 近期产品和生态进展
```

在 Codex 中也可以明确指定：

```text
Use $opendatalab-wechat-kb to search MinerU MCP Server articles.
```

## Agent 工作流程

Agent 使用这个 skill 时，不会一次性加载所有文章正文。它会按下面的流程工作：

```text
用户提出问题
  ↓
Agent 触发 opendatalab-wechat-kb
  ↓
读取 skills/opendatalab-wechat-kb/SKILL.md
  ↓
运行 scripts/search_remote_repo.py
  ↓
克隆或更新 GitHub 仓库到本地缓存
  ↓
读取 knowledge/manifest.jsonl
  ↓
检索相关文章
  ↓
按需打开 articles/ 中的 Markdown 原文
  ↓
基于文章内容回答、总结或引用
```

默认缓存目录：

```text
~/.cache/opendatalab-wechat-article
```

## 仓库结构

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

### 各目录作用

| 路径 | 用途 |
|------|------|
| `.claude-plugin/marketplace.json` | 给 Agent / 插件系统读取的注册入口，声明本仓库暴露哪些 skill |
| `skills/opendatalab-wechat-kb/` | Agent 真正安装和调用的 skill |
| `skills/opendatalab-wechat-kb/SKILL.md` | 给 Agent 看的使用说明，描述何时触发、如何检索、如何引用 |
| `skills/opendatalab-wechat-kb/scripts/` | skill 内置脚本，负责远程 clone/update 和检索 |
| `knowledge/manifest.jsonl` | 轻量索引，每篇文章一条记录 |
| `knowledge/topics.json` | 主题分类规则 |
| `knowledge/scripts/` | 本地索引构建和检索脚本 |
| `articles/` | 微信文章 Markdown 正文 |
| `微信公众号文章.xlsx` | 文章元数据总表，包含账号、文章 ID、链接、作者、发布时间、封面、摘要等字段 |

## 本地检索

检索本地仓库：

```bash
python3 knowledge/scripts/search_articles.py "MinerU RAG 知识库" --top-k 5 --pretty
```

按主题过滤：

```bash
python3 knowledge/scripts/search_articles.py "数据集" --topic Dataset --top-k 10 --pretty
```

通过 skill 的远程缓存检索：

```bash
python3 skills/opendatalab-wechat-kb/scripts/search_remote_repo.py "MinerU MCP Server" --top-k 5 --pretty
```

## 维护索引

新增或更新 `articles/` 下的 Markdown 文章后，重新构建索引：

```bash
python3 knowledge/scripts/build_manifest.py
```

构建过程会读取：

- `articles/*.md`
- `微信公众号文章.xlsx`
- `knowledge/topics.json`

然后生成：

```text
knowledge/manifest.jsonl
```

`manifest.jsonl` 中会保存标题、文件路径、原文链接、公众号、作者、发布时间、摘要、主题标签和关键词，供 Agent 快速检索。

## 数据说明

- 当前包含 343 篇 OpenDataLab 微信文章。
- 文章正文集中保存在 `articles/`。
- Markdown 文件名保留导出时的标题形式，方便追溯。
- `微信公众号文章.xlsx` 是结构化元数据来源。
- skill 不把正文写进 `SKILL.md`，而是通过索引和脚本按需读取，避免上下文过大。
