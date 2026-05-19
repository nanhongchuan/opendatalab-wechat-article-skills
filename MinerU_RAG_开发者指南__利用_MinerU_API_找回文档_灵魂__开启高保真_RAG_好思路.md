     MinerU-RAG 开发者指南——利用 MinerU API 找回文档“灵魂”，开启高保真 RAG 好思路 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU-RAG 开发者指南——利用 MinerU API 找回文档“灵魂”，开启高保真 RAG 好思路
======================================================

原创 爱学习的 OpenDataLab 2026-02-14 15:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/x3bnsN0fjd4cmUOqNIZTaQ](https://mp.weixin.qq.com/s/x3bnsN0fjd4cmUOqNIZTaQ)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

  

构建 RAG（检索增强生成）系统时，大家往往把精力花在挑选最强的大模型或最快的向量数据库上。但实际跑起来才发现，系统表现不佳往往是因为“第一公里”就走歪了——如果 PDF 解析出的内容是乱码、公式碎成了渣、或者表格逻辑全错，那后端的 LLM 再聪明也只能“一本正经地胡说八道”。

  

这就是为什么我们不仅要关注 RAG，更要关注**文档解析能力。一个好的 RAG 系统应该像人类一样，“看见”并“理解”文档。MinerU 开源项目中 API 存在的意义之一，就是可以帮助大家把那些复杂的 PDF、图片或扫描件，转化成真正对大模型友好的结构化 Markdown 语料。**

**无论是论文里那些复杂的 LaTeX 公式，还是财报中让人头大的跨页表格，经过 MinerU 处理后都能以清晰、有序的格式进入向量库。说白了，当你给模型喂的是这种“精装修”过的高质量语料，而不是乱码碎片的“毛坯房”，RAG 的幻觉问题自然就能从源头上得到显著改善。**

  

为了让大家在使用 MinerU 开源项目 API 搭建 RAG 系统时少走弯路，我们正式发布了一个 **RA****G 实战 Demo——MinerU-RAG。该**Demo 的核心逻辑很简单：它展示了如何利 **MinerU** 开源项目的 **API** 提供超强文档提取能力，把那些原本会让大模型没办法直接理解“读懂” 的 PDF，变成清晰、精准的知识库。

  

如果你正准备动手搭建自己的知识问答系统，这份基于 Demo 的使用指南建议收藏。该 Demo 项目通过自动化地对解析后的内容进行语义切片与向量化存储，配合大模型的生成能力，构建起一套完整的私有知识问答链路。

  

这里需要指出的是：MinerU-RAG项目并不是一个可完全用于生产环境的项目，我们的出发点也不是想定义 RAG 的标准模板，而是希望为广大开发者提供一个**清晰的开发思路，期待大家开发出一个更为强大的 RAG 体系。**

（MinerU RAG演示视频）

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)  

项目核心优势

  

**1\. 高保真数据源**

**解决 RAG 的“幻觉”根源**在 RAG 系统中，回答质量高度依赖于底层解析的准确性。MinerU 能精准识别 PDF 中的多栏布局、复杂表格以及数学公式。相比传统工具产生的“乱码”或“断裂文本”，MinerU 提供的是高保真的结构化 Markdown，从源头上确保了 AI 获取信息的准确性，大幅降低了模型因理解错误而产生的幻觉。

  

**2.一站式全栈集成**

**极简的开发工作流** MinerU-RAG 将“解析、切分、向量化存储、检索、生成”五大环节封装为统一的接口。开发者无需在多个工具链之间反复调试兼容性，仅需几行核心代码即可完成从原始 PDF 到智能问答系统的搭建。这种一体化设计极大地降低了 RAG 系统的开发门槛与维护成本。

  

3. **灵活的部署架构**  

系统在设计上支持高度的扩展性，用户既可以使用 vLLM 等后端进行本地私有化部署。这种架构确保了企业在处理敏感数据时能够完全掌握数据流向，同时支持自定义 Embedding 模型以适配特定的行业领域知识。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)  

快速开始：三大核心组件详解与操作流程

####   

MinerU-RAG 由三个核心组件构成：**MinerUClient**（文档处理）、**RAGBuilder**（知识库构建）以及 **LLMClient**（智能对话）。你只需依次使用它们，即可完成从文档到智能问答的全流程。下面跟着小编从零开始，完成 MinerU RAG 的安装、配置、文档处理、知识库构建及智能问答。

  

**📦第一步：环境准备**
--------------

1\. 安装 MinerU-RAG 核心包并验证

    pip install mineru-rag[rag]

2\. 配置您的大模型API密钥（支持所有OpenAI兼容接口）  

● 以**Windows PowerShell 操作为例（其他系统同理，只需把指令做对应转化即可）**；

● 复制下面的代码块，把引号里的内容换成你真实的大模型API，粘贴进去按回车，就配置成功了！

    # LLM API配置（RAG功能需要）

接下来，从MinerU解析 → 建库  → 召回 → 问答，跟着教程一步一步完成吧

  

  

**📑第二步：使用 MinerUClient 解析文档**
------------------------------

### **本地启用 MinerU-RAG 端口并处理文件**

● 先在终端输入这两行代码

    export MINERU_MODEL_SOURCE=modelscope

通过 http://127.0.0.1:8000/docs 访问web界面，如果能访问，代表MinerU本地服务已经启用成功了

  

● 输入指令进行文件处理

    from mineru_rag import MinerUClient

#### **● 核心字段说明**

**process\_file(input\_path, output\_path, ...)** 用于处理单个文件，不仅支持 PDF，还支持 PNG、JPG 等图片格式。

    \- input\_path：输入文件路径（PDF, PNG, JPG等）

    \- output\_path：输出目录

    \- is\_ocr：遇到扫描件时自动开启文字识别（默认True）

    \- enable\_formula：智能识别复杂的数学公式和表格结构（默认开启）

    \- enable\_table：是否启用表格识别（默认True）

    \- language：文档语言（默认"en"）

    \- layout\_model：布局模型（默认"doclayout\_yolo"）

  

process\_files\_batch(file\_paths, output\_dir, ...)当您有一整文件夹的资料需要处理时，使用批量处理方法会更加高效。

    \- file\_paths：文件路径列表

    \- output\_dir：输出目录

    \- 其他参数同process\_file

**🧱第三步：RAGBuilder：亲手打造你的“知识宝库”** 
----------------------------------

解析完文档后，需要把解析好的信息“切片”存入“向量数据库”里，方便大模型随时检索。

💡小编技巧：建议先把 Embedding 模型下载到本地，这样运行起来飞快！

    #可以将这部分保存为.py文件，运行下载本地embedding模型

然后保存下面代码为 build\_rag.py 文件，运行

    from mineru_rag import RAGBuilder

您可以自定义知识库的存放位置，或是更换更强大的嵌入模型。

    rag = RAGBuilder(

#### **● 核心字段说明**

build\_from\_files(file\_paths, library\_id, metadata)将 Markdown 文件列表转化为向量索引，建议为不同的项目设置不同的 library\_id

    - file\_paths: Markdown文件路径列表

    - library\_id: 知识库ID（默认"default"）

    - metadata: 可选的元数据字典

  

load\_vector\_store(library\_id)加载已存在的向量数据库

    - library\_id: 知识库ID

  

query(question, k, file\_id) 查询知识库

    - question: 查询问题

    - k: 检索文档数量（默认4）

    - file\_id: 可选，限制在特定文件

#### 

**🔍第四步：LLMClient：连接大模型的桥梁**
----------------------------

**1\. 在知识库里“寻找” (仅检索)**
-----------------------

有时候我们只想找找哪句话出现在哪，不需要 AI 生成长篇大论，这时候用查询功能最合适。

    from mineru_rag import RAGBuilder

**2\. 召唤** **AI** **智能对话**

让大模型根据你的知识库来回答问题，再也不怕它“胡编乱造”了。

    from mineru_rag import RAGBuilder, LLMClient

#### **● 核心字段说明**

query(question, context)直接查询LLM

    - question: 问题

    - context: 上下文内容

query\_with\_rag(rag\_result)使用RAG结果查询LLM

    - rag\_result: RAGBuilder.query()的返回结果

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)  

完整工作流（从文档处理到智能问答）

  

小编为你准备了一个从处理 PDF 到智能问答的完整脚本，复制保存为 run\_all.py 就能跑！

    from mineru_rag import MinerUClient, RAGBuilder, LLMClient

**💡 使用提示**
-----------

**1\. 首次使用**：建议先处理一个简单的PDF文件测试

**2\. 环境变量**：推荐使用环境变量配置，避免在代码中硬编码敏感信息

**3\. 本地模式**：使用本地vLLM后端需要先启动MinerU服务

**4\. RAG功能**：需要安装 \`mineru-rag\[rag\]\` 才能使用RAG相关功能

**5\. 向量数据库**：构建一次后可以重复使用，无需每次都重新构建

**6\. 批量处理**：大量文件建议分批处理，避免超时

7\. 如果遇到问题：

    - 检查环境变量是否正确设置

    - 确认已安装所需依赖

    - 查看错误信息中的详细提示

    - 在GitHub Issues中搜索类似问题

    - 提交新的Issue并附上错误信息

  

更多使用方式：

● 命令行工具：无需编写代码，可使用 mineru-rag 命令直接进行文档处理、建库和查询，适用于自动化脚本与快速验证。

● 详细API参考：关于批量处理、高级参数配置及完整API说明，请参阅 MinerU-RAG 官方文档：

https://pypi.org/project/mineru-rag/

  

至此，从解析到问答，你已经掌握了 MinerU-RAG 的全部核心能力。通过以上极简流程，你能够立即聚焦于业务价值验证，快速构建出准确、可信的企业级知识智能应用，欢迎使用。

  

* * *

  

2026 MinerU数据智能与前沿语料挑战赛

🔥火热开赛，等你来战！

↓

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAatpeJfjoTYPGc6X80DXLx0E7Ax3JIqibGFFrC8G8pf2fia812ibklwkaVo2FqVibG2lfWZzEgqyICHOgzwogwoGW4pDshbVicezhmg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

[总激励200万！2026 MinerU数据智能与前沿语料挑战赛正式启幕，筑基 AGI4S 高质量语料新高地！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

  

END  

  

**相关阅读：  
**

  

  

[告别手动录入！MinerU KIE功能上线，三步搞定票据关键信息提取](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551475&idx=1&sn=8c3a2af0052f060b03954e75b20f905e&scene=21#wechat_redirect)

2026-02-02

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW2OYb01iaFw0SIZNVWP5vYIyY18VPVN9VHF2na8lwXzxphLrqIEIHX2DYq1mic2mXok3ichb7LsuZfw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551475&idx=1&sn=8c3a2af0052f060b03954e75b20f905e&scene=21#wechat_redirect)

[如何科学地“设计”微调数据？一次关于后训练数据价值评测平台（ODA）的完整验证](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551483&idx=1&sn=c48e3effbf638e1da18662d7f7f69652&scene=21#wechat_redirect)

2026-02-03

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVjrL9P0GcVnPInOFfib5Q5Oag4Eosr3eWLWtUtyH04iamTT5D3musGQL2KgJBZ2Pe7Is0yclGuPNvw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551483&idx=1&sn=c48e3effbf638e1da18662d7f7f69652&scene=21#wechat_redirect)

[MinerU再次更新，网页解析功能上线！URL一键变Markdown，文档处理再无边界](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551428&idx=1&sn=1f5c63f9755ad714925fd0f9cbb87c61&scene=21#wechat_redirect)

2026-01-21

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVetPrwHQ2AaqicYicsIpeRruauBOGxvNMJVicq1g29v7FdVJuicqcQAeXBEdJZcibsiaYnxRtpUvrIJGSw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551428&idx=1&sn=1f5c63f9755ad714925fd0f9cbb87c61&scene=21#wechat_redirect)

[强强联手！MinerU携手沐曦完成适配，曦云C500推理性能加速60%](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551297&idx=1&sn=3b6a50dd0cb7570f8d26a093d8bb4e8b&scene=21#wechat_redirect)

2025-12-24

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUErF25RmMkX9p2nREV80RribvGPYw6MmAX2ibXhlcibtYRwN5PXZRib6cNCnNBRiaH16eSxgWxYsZnx0g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551297&idx=1&sn=3b6a50dd0cb7570f8d26a093d8bb4e8b&scene=21#wechat_redirect)

[打破桎梏！MinerU-HTML重构网页提取范式，开源超大规模高质量多语言语料AICC](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551242&idx=1&sn=ec6d3a0ef6b0cacbd6c020cd5bf96cc0&scene=21#wechat_redirect)

2025-11-26

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTqlCzSUPj4rBjYG74G5mX45ZMEGeERNI97ibMGOmvvKkWGMvEKtEkPhMdA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551242&idx=1&sn=ec6d3a0ef6b0cacbd6c020cd5bf96cc0&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言