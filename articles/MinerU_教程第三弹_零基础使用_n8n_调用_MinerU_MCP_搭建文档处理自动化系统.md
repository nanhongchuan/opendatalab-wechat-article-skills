     MinerU 教程第三弹：零基础使用 n8n 调用 MinerU MCP 搭建文档处理自动化系统 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU 教程第三弹：零基础使用 n8n 调用 MinerU MCP 搭建文档处理自动化系统
================================================

原创 热爱实践的 OpenDataLab 2025-06-12 18:51 上海

> 原文地址: [https://mp.weixin.qq.com/s/98OxvwaZEOD9MkJ\_YTZ-lg](https://mp.weixin.qq.com/s/98OxvwaZEOD9MkJ_YTZ-lg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**前言**
======

本教程旨在帮助用户在 n8n 平台中，搭建一个基于 MinerU API 服务 & MCP 服务的文档处理工作流，通过大模型对话实现自动化的文档转 Markdown 功能。无需复杂的编程知识，跟随本教程一步步操作，即可快速搭建属于自己的文档处理流程。

（\* 如果你想快速获取 MinerU 工作流，可以在 OpenDataLab 公众号后台发送“n8n”关键词，获取配置及对话演示json文件）

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUEa5DcURq3yyicWNrhWafc73ZALaxRbJ2mzvcZ8q2icNYWFJrthnkUiaxTQOsicD0ZayB6WCTZKmzT1A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1)什么是 MinerU ？  
**
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MinerU 是一个强大的文档处理工具，能够将 PDF、Word、PPT 等文档自动转换为 Markdown 格式，支持 OCR 识别、公式识别、表格识别等功能，大大提高文档处理效率。

MinerU官网：https://mineru.net/

  

**![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nVAzbhvhL0ns3vtMz0JSfweHyn0beOHuibCUrBbq97EygibKLDUOWGDqw/640?wx_fmt=jpeg)什么是 n8n ？**
-------------------------------------------------------------------------------------------------------------------------------------------------------------

n8n 是一个国外火爆的开源工作流自动化工具，通过可视化界面可以轻松创建各种自动化工作流程，无需编写复杂代码。

n8n官网：https://n8n.io/

  

接下来，跟着小编一步一步进行操作吧。

**一**

**环境准备  
**

**在开始前，请确保你的系统已安装以下依赖：**

****● Python 3.10+**：用于运行 MCP 和 MinerU 服务**

****● Node.js 14+**：用于运行 n8n**

****● npm 或 yarn**：用于安装 n8n**

**如果没有，请根据不同系统完成依赖安装：**

  

 1**.安装**及验证**基础依赖**

### **在Windows上：**

● 下载并安装 Python（确保勾选 `Add Python to PATH` 选项）

● 下载并安装 Node.js（包含 `npm` ）

● 打开**命令提示符**或 PowerShell 验证安装：

    python --version

**在 MacOS 上:**

**使用 Homebrew 安装：**

    # 安装 Homebrew（如果尚未安装）

**在Linux上：**

    # Ubuntu / Debian

  

 **2**.安装uv工具（可选、推荐）****

uv 是一个 Python 包管理工具，比 pip 更快更稳定。你可以选择使用 pip 或 uv 来安装和管理Python 包。

    # 使用 pip 安装 uv

**二**

**n8n及 MinerU MCP Server**

**安装和配置  
**

  

 **1.安装和启动n8n**

1.1使用 npm 或 yarn 全局安装 n8n：

    # 使用 npm

1.2安装完成后，启动 n8n 服务：

    n8n start

n8n 将在 http://localhost:5678 启动，在浏览器中打开该地址访问 n8n 控制台。

  

  

 2**.安装和启动MinerU-MCP服务**

这里需要本地配置和启动 MinerU MCP 服务器，具体操作详见：[MinerU MCP Server源码发布！打通大模型与MinerU，让 PDF 文档处理更 easy](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550656&idx=1&sn=1518731f0787105ceb410731c135d071&scene=21&token=394692334&lang=zh_CN#wechat_redirect)  

  

**三**

****在n8n中**创建**

 **MinerU 的 MCP 集成工作流**

本节将指导你如何在 n8n 中通过调用 MinerU API 来集成一个工作流， 作为 MCP Server 提供服务，最终实现通过大模型对话，完成PDF文档自动处理。

  

  

 1**.配置LLM凭证**

首先，我们需要配置大模型的凭证，这里我们以 OpenAI 为例：

  

1.1打开n8n控制台，进入工作流 页面：

http://localhost:5678/home/workflows

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7noZfp7g4mVZkmlc0IW194PSrBCR1P4LSBMmOlsg36dt2nLl8sGM2jNw/640?wx_fmt=jpeg&from=appmsg)

  

1.2点击 Create Credential 按钮

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nHdNOPjgSyACDm8CDjXtibgicUHJaQbxwHNhl5fsfsowtJmMbpdsS4jibQ/640?wx_fmt=jpeg&from=appmsg)

  

1.3 选择 OpenAI 后点击 Continue

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nXZHLYKLFNrBnOeibeqy7BvRfwrzde8rVPe123bRPnP4ia6shofGqJqZg/640?wx_fmt=jpeg&from=appmsg)

  

1.4 填写模型 API 密钥（API-KEY）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nJuNWzSWafHvQ2GQcCScLjFqB0AMwreD1bHz9RicOhHyJ3ibuSLcr7ia5g/640?wx_fmt=jpeg&from=appmsg)

  

1.5 填写模型 API 基础 URL（Base URL）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nIr4gWmnR3ibXFPAnARMDH4XPSC8MTAN13vzGt2iaz9OL4pLlic0hzI2Gw/640?wx_fmt=jpeg)

  

1.6 点击 Save 保存凭证

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nc9zpnej1kWxsvZR5jAbNSNKck5nPASIlAEk4RFZeqWrYdklZjXgzTw/640?wx_fmt=jpeg&from=appmsg)

  

1.7 点击 Overview 返回概览页面

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nLDQV7fxGh0H7HiarNwcwAGKb2Pw0FUu48liayIsDrxnmGxnISeT7sqvQ/640?wx_fmt=jpeg&from=appmsg)

  

  

 2**.导入并配置工作流**

接下来，我们需要导入 MinerU 文档处理工作流并进行配置：

  

2.1 点击导入我们预先配置好的 MinerU 工作流配置文件（支持2种导入方式：在线url导入、本地file导入；配置文件获取方式见文末）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7n5WhEKdjwHdqay0MGGmku5ML8qlEokojBAP1HQjnMg9CozNZCLC7tUw/640?wx_fmt=jpeg)

  

2.2配置文件保存节点：点击 Write Files from Disk 节点：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nFX9GpCWicPPKOUW0n01zAajl2fsb8NFGAvqEZ10qwFJfS6ichsticBnPg/640?wx_fmt=jpeg&from=appmsg)

  

2.3编辑 文件保存路径 为你本地要保存的路径

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nFPF0ws6JEV1x7jy0zJjSxB1X9fnw5K7ycvQg4UiacQQf2KlfwH73gTA/640?wx_fmt=jpeg&from=appmsg)

  

2.4点击 Back to canvas 返回工作流画布

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7n7ZwawERkmhfHwibicstc4ep26Q41QRKnTRlLuqh7mYZb8mgjwz2Cd1gg/640?wx_fmt=png&from=appmsg)

  

2.5配置 n8n中的 MCP Client：点击 MCP Client 节点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nVCAhk2icIxnOS4kdNWztz5FAcojPOUcNVaItExw0oYxmYnXySaBYNoA/640?wx_fmt=png&from=appmsg)

  

2.6输入你的 MinerU MCP 服务器地址+`/sse`

`(`例如 http://localhost:8000/sse）  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7n7w1gMNCO1aBrFZKr1g5DwEE5Wh6JW1xkHCjgiaaCNsPEbDSXpwoVRnQ/640?wx_fmt=png&from=appmsg)

  

2.7点击 Back to canvas 返回工作流画布

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nD8TAtrB2UADAhAmibdlwWeXjmR2Brp5vbkdwbA7YguXU4VOGiaTmfa9w/640?wx_fmt=png&from=appmsg)

  

  

 3**.测试工作流**

现在，让我们测试这个工作流：

  

3.1点击 Open Chat 按钮进入对话框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7ncucJf4D9bPecbk8knISWkvIZYJggQeNaawjIH9JQh4JTYicj5jkRb0g/640?wx_fmt=png&from=appmsg)

  

3.2点击对话框右侧 上传文件 的按钮，选择一个文件并上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nsG5rlI8jVmvJrAJtH2SF2Kibiaorcfjn2IiaRJNmDae9B2fHLz3Fpcdzg/640?wx_fmt=png&from=appmsg)

  

3.3输入 对话内容 并点击 发送

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nrUtTt6BgF3BOVtMwjpHkzZbIQic1uk4oTSNsEUwlQWupmYXKwVcKgWA/640?wx_fmt=png&from=appmsg)

  

运行结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7n9n3InnmcJAKwLLPHIqxl2lYyMunAia2icWqpyibl5rLTdJWicJibhmwibjGQ/640?wx_fmt=png&from=appmsg)

  

大模型正确解析上传的 PDF 文件，并返回对应的Markdown格式内容，说明工作流搭建成功。

**四**

**常见问题与解决方案  
**

#### **1.n8n 无法连接到 MCP 服务**

#### **● 问题**：n8n 工作流中的 HTTP Request 节点无法连接到 MCP 服务。

#### ● 解决方案：

*   确保 MCP 服务正在运行
    
*   检查 URL 地址是否正确
    
*   检查防火墙设置是否阻止了连接
    
      
    

#### **2.文件路径问题**

#### **● 问题**：使用parse\_documents工具时报找不到文件错误。

#### **● 解决方案**：

*   使用绝对路径而不是相对路径
    
*   检查文件路径中的特殊字符，特别是在 Windows 系统中的路径分隔符
    
*   确保文件有读取权限
    
      
    

#### 3.调用 MCP 服务超时

#### ● 问题：调用 MCP 服务时发生超时。

#### ● 解决方案：

*   在启动 n8n 之前，需要在环境变量中设置 MCP 的超时时间
    

    export NODES_MCP_TIMEOUT=<超时时间>

（左右滑动查看）

  

**五**

**结语  
**

![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Party.png)恭喜你！现在你已经成功搭建了基于 n8n、MCP 和 MinerU 的文档处理系统。通过这个系统，你可以轻松地将各种文档转换为 Markdown格式，极大地提高文档处理效率。

如果在使用过程中遇到任何问题，请参考本教程的"常见问题与解决方案"部分，或者到 MinerU官网 寻求支持：
------------------------------------------------------

https://mineru.net/

**\* 工作流配置文件已上传n8n官网，点击即可复制、粘贴进 n8n 在线工作流中使用（url方式导入）：**

_https://n8n.io/workflows/4808-convert-documents-to-markdown-with-mineru-api-and-gpt-4o-mini/_

_\* 另外，您可在 OpenDataLab 后台发送关键词 “n8n”获取__配置文件，进行file方式导入。_

随着使用经验的积累，你可以根据自己的需求对工作流进行更多定制，实现更加复杂的自动化处理流程。除了大模型对话方式外，n8n中还Webhook 等更多与 MinerU MCP 服务组合的进阶玩法等你探索，快去试试吧~
----------------------------------------------------------------------------------------------------------

_祝您使用愉快！_

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/hkUN8E95VAXoJ0W0JezMA8IuicDhTpfxQScyWyBSvWva6gTdoIdJjhuU70DvSFT6u4ft5R4EbsGzfwlTZeuaKhw/640?wx_fmt=gif&from=appmsg)

END

  

**相关阅读：**

[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

2025-05-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2DfiaWj7tD6u36J9MUptoIn8mjrdEE46UKxxIePWjHAujAAXkRVZR4rA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[MinerU教程第二弹丨MinerU 本地部署保姆级“喂饭”教程](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

2025-05-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUUOH1ib8viafCJ0mFGr96SWphia1CXYlB7PYcd0mOyDymiaPiboxic4YrUJMsYFiaqZ4mJWtY8VxpqumSuQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

[MinerU MCP Server源码发布！打通大模型与MinerU，让 PDF 文档处理更 easy](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550656&idx=1&sn=1518731f0787105ceb410731c135d071&scene=21#wechat_redirect)

2025-06-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVoV2dV45dqibd511A1mD5oo5Whn6YSIfpPw34zOpWycdw4eDD3nZFWtaoJxNia3sFNiagrKlfaLMQHw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550656&idx=1&sn=1518731f0787105ceb410731c135d071&scene=21#wechat_redirect)

[CVPR 2025｜公式识别评测新指标CDM：视觉元素buff加成，让大模型公式识别评价更准确、更客观](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550674&idx=1&sn=a270d72ea7b75fefd90c07eece467e16&scene=21#wechat_redirect)

2025-06-11

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXZ51dpXQ09VWmgID7PImUzeAbMLfx9qNTbhD4MGkm377dlWVXibZ0CTYuxtLtTjO8mZ7t8ttkwHEw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550674&idx=1&sn=a270d72ea7b75fefd90c07eece467e16&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言