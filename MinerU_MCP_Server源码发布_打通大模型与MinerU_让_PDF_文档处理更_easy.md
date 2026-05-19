     MinerU MCP Server源码发布！打通大模型与MinerU，让 PDF 文档处理更 easy \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU MCP Server源码发布！打通大模型与MinerU，让 PDF 文档处理更 easy
===================================================

原创 MinerU OpenDataLab 2025-06-09 20:05 上海

> 原文地址: [https://mp.weixin.qq.com/s/pgzNsbReuZ5fRzkRM7JKoA](https://mp.weixin.qq.com/s/pgzNsbReuZ5fRzkRM7JKoA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**你是否厌倦了手动处理PDF文档？** 

交给大模型试试！![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_06.png)

MinerU MCP Server 源码正式发布

打通大模型与 MinerU

让你拥有“真正懂你的文档助手”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVoV2dV45dqibd511A1mD5oojB1HmXpqCmCD3nTqnfRUp3PX625pWqcibEG8L3aUKBsMIZBqoXE4qkQ/640?wx_fmt=png&from=appmsg)

**MinerU MCP Server 源码获取地址：****https://github.com/opendatalab/MinerU/tree/dev/projects/mcp**

**（![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Party.png)彩蛋预告：目前发布的是本地开源版本，在线 MinerU MCP Server 即将上线，欢迎点赞催更！![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_02.png)）**

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

****什么是 MCP？****

先来明确一下三个概念：

● MCP（Model Context Protocol）是一个开放的模型上下文协议，用于大语言模型与外部数据源和工具之间的标准化连接；

● MinerU API 是负责执行核心文档转换任务（例如，PDF 到 Markdown）的后端服务；

● MinerU MCP Server 则充当一个中间层或桥梁，它将 MinerU API 的功能封装成符合 MCP 规范的接口。

  

简而言之，MinerU MCP Server 接收来自支持 MCP 协议的客户端（如 Claude、Cursor、Cherry Studio）的指令，然后调用 MinerU API 完成实际的转换工作，并将结果返回给客户端。这种架构使得任何支持 MCP 协议的AI 工具都能方便地集成和使用 MinerU 的文档处理能力。

  

所以，要想在大模型、Agent里用 MinerU 工具处理 PDF 文档，则需要依次配置 MinerU API、MinerU-MCP，快来看看怎么做吧~

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****使用 MinerU 官方 API 服务****

如果你想使用MinerU官方 API 服务而不是本地服务，需要进行以下配置：

#### **1\. 获取 MinerU** **API** **密钥**

● 访问 MinerU官网

● 注册并登录账号

● 在用户中心找到 API 密钥申请入口

● 按照指引完成 API 密钥申请

#### 

#### **2\. 配置环境变量**

在源码模式下，编辑 `.env` 文件：

    # 使用远程API

在包管理模式下，设置环境变量：

**Windows：**

    set USE_LOCAL_API=false

**macOS/Linux：**

    export USE_LOCAL_API=false

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****MinerU MCP 服务****配置********

MinerU MCP 服务有两种安装和配置方式：源码模式和包管理模式。下面我们分别介绍这两种方式。

#### 

  

 **方式一：本地源码模式（适合开发和自定义需求）**

#### **1\. 配置本地 MinerU 服务**

首先，我们需要启动本地的 MinerU 服务：

    # 进入 web_api 目录

上述命令将在 http://localhost:8888 启动 MinerU API 服务。

  

#### **2\. 配置 MinerU MCP 服务**

接下来，配置和启动 MinerU MCP 服务：

    # 进入 MinerU-MCP 目录

  

#### **3\. 配置环境变量**

在 MinerU MCP 目录中创建 `.env` 文件（可以复制 `.env.example` 并重命名）：

    # 复制示例配置文件

然后编辑 `.env` 文件，设置以下内容：

    # 使用本地 API

#### **4\. 启动 MCP 服务**

配置完成后，启动 MCP 服务：

    # 确保在 activate 的虚拟环境中

服务将在 http://localhost:8001 启动，使用SSE协议与客户端通信。

#### 

  

**方式二：包管理模式（适合生产环境和简单使用）**

#### **1\. 安装MinerU MCP包**

使用pip或uv直接安装mineru-mcp包：

    pip install mineru-mcp

#### **2\. 配置环境变量**

在这种模式下，我们通过系统环境变量进行配置。

**Windows 上设置环境变量：**

    # CMD命令行

**macOS/Linux上设置环境变量：**

    export MINERU_API_BASE="https://mineru.net"

**注意**：如果使用MinerU 官方 API 服务，需要从 MinerU官网(https://mineru.net) 申请 API 密钥，填入 MINERU\_API\_KEY 字段。

  

#### **3\. 启动 MCP 服务**

设置好环境变量后，启动 MCP 服务：

    mineru-mcp --transport sse

服务将在 http://localhost:8001 启动，使用SSE协议与客户端通信。（\* Stdio协议不需要启动，所以下方Cherry Studio的调用案例就不需要启动）  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

********MCP常见调用工具与Cherry Studio调用案例********

目前，常见的 MCP 接入与调用工具包括：**Cursor、Cline（VSCode 插件）、Windsurf、Claude App、Cherry Studio** 等。以上工具是我们推荐的接入方式，适用于不同的开发与使用场景，便于用户更高效地集成和体验MinerU  MCP 能力。这里我们以**Cherry Studio 为例，配置其中的 MinerU-MCP。**

### **1\. 进入 Cherry Studio 设置**

a. 打开 Cherry Studio 应用程序

b. 点击左下角的"设置"按钮，进入设置页面

c. 在左侧菜单中，选择"MCP 服务器"

  

在右侧的 MCP 服务器配置界面中，您可以看到已有的 MCP 服务器列表。点击右上角的"添加服务器"按钮来创建新的 MCP 服务，或者点击现有服务来编辑配置。

  

### **2\. 添加 MinerU-MCP 配置**

点击"添加服务器"后，您将看到一个配置表单。请按以下步骤填写：

**a. 名称**：输入"MinerU-MCP"或您喜欢的其他名称

**b. 描述**：可选，如"文档转换为Markdown工具"

**c. 类型**：选择"标准输入/输出（stdio）"

**d. 命令**：输入 uvx

**e. 参数**：输入 mineru-mcp

**f. 环境变量**：添加以下环境变量

    MINERU_API_BASE=https://mineru.net

使用 `uvx` 命令可以自动处理 mineru-mcp 的安装和运行，**无需预先手动安装 mineru-mcp 包**。这是最简单的配置方式。

  

### **3\. 保存配置**

确认无误后，点击界面右上角的"保存"按钮完成配置。保存后，MCP 服务器列表中会显示您刚刚添加的 MinerU-MCP 服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVoV2dV45dqibd511A1mD5ooXIdqrNPLe4hy4YB1xXeRuNIVAlHgdmGiccXXI1eDsd0KjbVp1HHTiceA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVoV2dV45dqibd511A1mD5oorDndqKTQ5AUH2DmHApgQ3DRia5SsaNLXNq6neyvBmqmACV1Rj5Wadicw/640?wx_fmt=png&from=appmsg)

### **4\. 使用 Cherry Studio 中的 MinerU MCP**

一旦配置完成，您可以在 Cherry Studio 中的对话中使用 MinerU MCP 工具。在 Cherry Studio 中，您可以使用如下提示让模型调用 MinerU MCP 工具。模型会自动识别任务并调用相应的工具。

###   

### 示例 1: 使用 URL 转换文档

**用户输入:**

    请使用 MinerU MCP 将以下 URL 的 PDF 文档转换为 Markdown 格式：https://example.com/sample.pdf

**模型将执行的步骤：**  

模型识别这是文档转换任务，并调用 `parse_documents` 工具，参数为:

    {"file_sources": "https://example.com/sample.pdf"}

工具处理完成后，模型会告知您转换结果。

    （输出示意1）

### 示例 2: 转换本地文档

**用户输入:**

    请使用 MinerU-MCP 将本地的 D://sample.pdf 文件转换为 Markdown 格式

**模型将执行的步骤：**  

模型识别这是本地文档转换任务，调用 `parse_documents` 工具，参数为:

    {"file_sources": "D://sample.pdf"}

    （输出示意2）

### 示例 3: 启用 OCR 处理扫描文档

**用户输入:**

    请使用 MinerU-MCP 将以下 URL 的扫描版 PDF 文档转换为 Markdown 格式，并启用 OCR 功能：

**模型将执行的步骤：** 

模型识别这是需要 OCR 处理的文档转换任务，调用 `parse_documents` 工具，并启用 OCR 参数:

    {"file_sources": "https://example.com/scanned.pdf","enable_ocr": true}

    （输出示意3）

### 示例 4: 完整对话流程

以下是一个完整的对话流程示例：

**用户:**

    我有一份学术论文的 PDF，网址是 https://arxiv.org/pdf/2303.08774.pdf，能帮我转换成 Markdown 格式吗？

**模型:**

    我可以帮您将这份学术论文转换为 Markdown 格式。我将使用 MinerU-MCP 工具来处理这个任务。

    （输出示意4）

### **5\. 工具参数详解**

在使用过程中，模型会根据您的指令自动选择合适的工具和参数。以下是主要工具的参数说明：

### ● parse\_documents 工具参数

### 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWswugPM93Xibd0cNtXwbPayPatg32dGOD6CJ8KxZsJxhK69sGsqq06se9ickyOfk72qNiaQSwDyuuKg/640?wx_fmt=png&from=appmsg)

    （点击查看大图）

### ● get\_ocr\_languages 工具参数

无需参数，用于获取OCR支持的语言列表。

  

### 6\. 高级用法

### 6.1 指定语言和页码范围

**用户输入:**

    请使用 MinerU MCP 将以下 URL 的文档转换为 Markdown 格式，只处理第 5-10 页，并指定语言为中文：

模型会使用 `parse_documents` 工具，并设置 `language` 参数为 "ch"，`page_ranges` 参数为 "5-10"。

###   

### 6.2 批量处理多个文档

**用户输入:**

    请使用 MinerU-MCP 将以下多个 URL 的文档转换为 Markdown 格式：

模型会调用 `parse_documents` 工具，并将多个 URL 以逗号分隔传入 `file_sources` 参数。

###   

### 7\. 注意事项

● 当设置 `USE_LOCAL_API=true` 时，使用本地配置的API进行解析

● 当设置 `USE_LOCAL_API=false` 时，会使用 MinerU 官网的API进行解析

● 处理大型文档可能需要较长时间，请耐心等待

● 如果遇到超时问题，请考虑分批处理文档或使用本地API模式

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

******常见问题与解决方案******

### **1\. 无法启动 MCP 服务**

**问题**：运行 `uv run -m mineru.cli` 时报错。

**解决方案**：

● 确保已激活虚拟环境

● 检查是否已安装所有依赖

● 尝试使用 `python -m mineru.cli` 命令替代

### 

### **2\. 文件转换失败**

**问题**：文件上传成功但转换失败。

**解决方案**：

● 检查文件格式是否受支持

● 确认API密钥是否正确

● 查看MCP服务日志获取详细错误信息

###   

### 3\. 文件路径问题

**问题**：使用 `parse_documents` 工具处理本地文件时报找不到文件错误。

**解决方案**：请确保使用绝对路径，或者相对于服务器运行目录的正确相对路径。

  

### **4\. MCP 服务调用超时问题**

**问题**：调用 `parse_documents` 工具时出现 `Error calling tool 'parse_documents': MCP error -32001: Request timed out` 错误。

**解决方案**：这个问题常见于处理大型文档或网络不稳定的情况。在某些 MCP 客户端（如 Cursor）中，超时后可能导致无法再次调用 MCP 服务，需要重启客户端。最新版本的 Cursor 中可能会显示正在调用 MCP，但实际上没有真正调用成功。建议：

**● 等待官方修复**：这是Cursor客户端的已知问题，建议等待Cursor官方修复

**● 处理小文件**：尽量只处理少量小文件，避免处理大型文档导致超时

**● 分批处理**：将多个文件分成多次请求处理，每次只处理一两个文件

● 增加超时时间设置（如果客户端支持）

● 对于超时后无法再次调用的问题，需要重启 MCP 客户端

● 如果反复出现超时，请检查网络连接或考虑使用本地 API 模式

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END

  

**相关阅读：**

  

  

[国家数据局点赞！OpenDataLab小语种数据标注方案入选《数据标注优秀案例集》](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550623&idx=1&sn=d0f4750a373ddf37f5976d7c95ad0348&scene=21#wechat_redirect)

2025-05-28

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAX2AvnTTSP4A4f7tXyhh41AibalsauxWPRm71ouL56Viaj1WpneibuyVQzfJn9dTDrGor3Izac7PJ7SA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550623&idx=1&sn=d0f4750a373ddf37f5976d7c95ad0348&scene=21#wechat_redirect)

[MinerU教程第二弹丨MinerU 本地部署保姆级“喂饭”教程](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

2025-05-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUUOH1ib8viafCJ0mFGr96SWphia1CXYlB7PYcd0mOyDymiaPiboxic4YrUJMsYFiaqZ4mJWtY8VxpqumSuQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

2025-05-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2DfiaWj7tD6u36J9MUptoIn8mjrdEE46UKxxIePWjHAujAAXkRVZR4rA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[教程 | 给大模型插上小语种“翅膀”，附ms-swift韩语继续预训练与指令微调教程](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550464&idx=1&sn=5ffb4ac21c32faac9da45e5a56ae6953&scene=21#wechat_redirect)

2025-04-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXvuwoX1MnPTK5CU4AUjky3iaSsp4ld6seW2JdZzzIYUg0icNFWuahoKibIJuMG8bicbeerx09aWucLaw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550464&idx=1&sn=5ffb4ac21c32faac9da45e5a56ae6953&scene=21#wechat_redirect)

[【MinerU × LazyLLM】PDF无损拆包，让RAG更懂你的文章！附PDF解析组件选型与RAG案例分享](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550423&idx=1&sn=aae4f098fd607829e3df9fef37814fe8&scene=21#wechat_redirect)

2025-04-08

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUk7Csn0E5A7R5kcqCt7p1btpsj2Oqmus7IGicuxnkZSWEddwcDeMrFO8eicLszAj8RqIBF1icL29Sqg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550423&idx=1&sn=aae4f098fd607829e3df9fef37814fe8&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言