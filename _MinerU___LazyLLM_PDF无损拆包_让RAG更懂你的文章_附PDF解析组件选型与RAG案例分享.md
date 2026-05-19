     【MinerU × LazyLLM】PDF无损拆包，让RAG更懂你的文章！附PDF解析组件选型与RAG案例分享 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

【MinerU × LazyLLM】PDF无损拆包，让RAG更懂你的文章！附PDF解析组件选型与RAG案例分享
=======================================================

原创 LazyLLM OpenDataLab 2025-04-08 18:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/5NfGGY3Joxe4bHjnugTtXQ](https://mp.weixin.qq.com/s/5NfGGY3Joxe4bHjnugTtXQ)

在大模型与RAG技术蓬勃发展的今天，**PDF文档解析**已成为构建知识库的**核心痛点**。由于 PDF 在跨平台兼容性和格式固定性方面的优势，企业通常选择 PDF 作为知识资产的主要存储形式。然而，这些文档中的复杂排版（如多栏布局、嵌套表格、公式与图表混排）往往让传统解析工具难以应对。尤其在金融、法律、科研等专业领域，**解****析失误可能导****致语义断层、数据错位**，进而引发RAG系统**"幻觉式"回答**。

  

针对PDF格式文档版式多样、解析难度大等难题，上海人工智能实验室推出了一款究极武器——**MinerU**，各位开发者在以往的开发过程中可能听说过这个名字，但这玩意儿究竟是个啥呢？本文将带你一同探索它的奇妙之处，并带大家使用LazyLLM，结合MinerU打造**PDF解析与RAG应用的无缝链路。**

**![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUk7Csn0E5A7R5kcqCt7p1buWRkIAicAy69DGv4iaic5rhOBHlgZVb0ia2RhvOib0IgsygM3iczIqHdxlOg/640?wx_fmt=jpeg)**

当RAG遇上PDF

一场AI的“阅读理解噩梦”

“这PDF怎么像俄罗斯套娃？”  

每个RAG开发者在深夜都会发出的灵魂拷问...

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUk7Csn0E5A7R5kcqCt7p1b0tfhtp1FdNCmTj3VlBjjKxle4kiagkicQnHmuBtpHhB0JWrKPicJxIHUA/640?wx_fmt=jpeg&from=appmsg)

  

你永远不知道一份专业PDF里藏着多少"反AI陷阱"：

🔹 金融报告里嵌套的九层表格  
🔹 法律文书里突然出现的竖排注释  
🔹 科研论文里公式和图表的花式排列组合  
🔹 更别提那些扫描件里堪比抽象画的OCR结果

......

在MagicPDF诞生之前，市面上已经有了很多PDF解析工具，比如**pypdf、llama-parse**，然而都存在一些能力缺陷。我们调研了市面上n种PDF解析工具后得出一个结论——某些工具处理复杂文档时，像极了用汤勺拆快递的憨憨！(小编真的笑得很大声哈哈哈哈哈哈哈~)

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nbVAtbFwhCln449hGnoXMqxQatWvy0siaPEyLwYTJaeLTM5JE8ibibh4pg/640?wx_fmt=png&from=appmsg)

  

有人会说了：“解析组件只要基本够用就行，至于这么折腾不？”，你以为解析不准顶多让AI犯傻？太天真了！PDF拆包失误轻则社会性死亡，重则引发行业地震！  

**🩸血泪案例剧场**

1️⃣ 律所惊魂夜：某合同第37页脚注里的"除外条款"被解析器吃掉，导致AI法务助手给出错误建议，差点引发亿元级纠纷。

2️⃣ 投行黑色三分钟：财报中的嵌套表格被解析成乱码，AI分析师把负债率算成收益率，交易员当场表演川剧变脸。  
3️⃣ 科研社死现场：论文里的关键公式被识别成二维码，学术GPT当场编造出"量子佛学"新理论...

这些啼笑皆非的案例背后

暴露出

RAG对于传统PDF解析技术面对复杂文档的困境

接下来为大家介绍**破局利器**

**👇**

MinerU + LazyLLM

技术CP出道

  

 MinerU——PDF解析界的扫地僧

  

**MinerU**是由上海人工智能实验室（上海AI实验室）大模型数据基座OpenDataLab团队开源的全新的**智能数据提取工具**。MinerU 能够快速识别PDF版面元素，将文档转化为清晰、通顺、易读的Markdown格式。

  

其**核心能力**在于：

● 保留原文档的结构和格式，包括标题、段落、列表等；  

● 自动删除页眉、页脚、脚注、页码等元素；

● 准确提取图片、表格和公式等多模态内容；

● 符合人类阅读顺序的排版格式。

  

MinerU代码公开之后，凭借精准、快速的**SOTA效果**，媲美甚至超过商业软件的性能，获国内外多个技术大V点赞，**GitHub Star突破30K+**，登顶**GitHub Python Trending**（2024年7月28日-29日），成为AI数据清洗中一个亮眼的开源工具。

  

_官网：https://mineru.net/_

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nfeMWkumBbPVznrrllwWjMAr2Qr3Gpkw2Oe0NX8Ck4pkrUOofiaB9mYw/640?wx_fmt=png&from=appmsg)

  

**业界反馈确实不错**

👇

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nU6OmeTFGr8C0RLWaCqaGhXSbBwWEs4gW2VCib0RbibgSicEE9wnzIIu0Q/640?wx_fmt=png&from=appmsg)

  

精准解析只是开始，如何把解析能力融入到RAG框架，提升知识提取与问答能力，协同解决复杂文件数据抽取与智能问答的瓶颈？

  

解决方案来了👇👇👇

  

  

 LazyLLM——RAG框架里的乐高大师

**LazyLLM**是一个开源大模型应用开发框架，可以让我们像搭建积木一样，快速构建出具有生产力的**AI大模型应用**。LazyLLM旨在以最简单的方法和最少的代码，快速构建复杂、强大的多Agent AI应用原型，即使没有大模型应用开发背景也能轻松上手。

  

_官网：https://github.com/LazyAGI/LazyLLM_

  

**LazyLLM架构图**

👇

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1n2VKaNCule0Mk4bqicGSz8gpRdHWWcMTzKRTJFZwVS0nSy52dLV7qgDw/640?wx_fmt=png&from=appmsg)

  

● 以数据流为核心的应用开发范式，集成丰富的标准组件，像搭积木一样开发大模型应用，低至10行代码搭建多路召回的RAG；

● 为同一模块的不同技术选型提供一致的使用体验，用户可以零成本切换基模型、数据库、训推理框架等组件；

● 复杂应用一键部署：利用轻量网关实现分布式应用一键部署，助力用户产品落地；

多Agent编排：封装FunctionCall、React、ReWOO、Plan-and-Solve等多种业界主流的Agent；

● 跨平台：兼容多个操作系统（如Windows、MacOS或Linux）和多种IaaS平台（如裸金属、k8s、slurm、公有云）。

  

让RAG变为阅读理解大师

实测案例

  

如果说**PDF解析是RAG的“眼睛”**，**知识编排则是它的“大脑”**。本节将深入解析两大开源利器如何从技术架构协同、应用场景适配、部署流程贯通三个维度，打造“能读会想”的RAG系统。**通过实测案例，展示从复杂PDF文档到精准问答的完整技术链路**。

  

  

**1**

  

**快速部署方案****——**

**从安装、模型下载配置到无缝接入LazyLLM**

**1.1** **安装配置**

**1.LazyLLM安装**

可参考LazyLLM官方项目进行安装，或直接在命令行中运行以下命令：

    pip install lazyllm

**2.MinerU安装配置及模型选择**

参考MinerU官方项目进行安装配置

  

a.magic-pdf安装

    pip install -U "magic-pdf[full]" --extra-index-url https://wheels.myhloli.com -i https://mirrors.aliyun.com/pypi/simple

  

b.模型和配置文件下载

可参考官方文档通过脚本一键下载

    pip install modelscope

  

至此，环境已就绪，所需模型也已下载完毕。接下来，我们将结合 MinerU 与 LazyLLM 搭建完整的 RAG 流程，实现高效精准的知识检索与生成。

  

**1.2 通过自定义reader接入LazyLLM代码示例**

  

LazyLLM 提供了一套默认的文档解析器，开箱即用，同时也支持用户自定义解析器，用户只需将封装好的可调用对象注册为 Document 类型解析器，即可实现个性化解析方案。

  

基于此，我们首先利用MinerU构建PDF解析器，处理其输出的解析结果为LazyLLM的标准节点DocNode。

    class MagicPDFReader:

_（喜欢动手的朋友们可以在文档后面找到详细的代码~）_

接下来用 LazyLLM 搭建 RAG 流程的 Demo

仅需**不到 20 行代码**！  
**重点！第 6 行 ！**

**只要把刚刚定义的MagicPDFReader**

**注册为pdf文档的解析器**

就能轻松搞定！

    import lazyllm

  

以下为rag框架的流程图，接收到用户query后，通过多路召回（retriever）得到节点，然后通过rerank重排序到输入大模型得到最终回答。每个retriever可以绑定多个document，自定义的解析器仅需通过documents.add\_reader("\*\*/\*.pdf", MagicPDFReader)注册到流程中。

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nBVDOeHqdtoFkE38pyh4nicqJ5hN97f39fHicbC4IUByE4G11l9sJqR5A/640?wx_fmt=png&from=appmsg)

**⚒️实验室暴击现场⚒️**

当MinerU遇上PyPDF，降维打击太残忍了！

  

有了以上启动代码，我们直接运行并测试一下，看看MagicPDF到底给我们的RAG应用带来了什么改变。对比效果如下：

  

**MinerU解析结果:**

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nMXkgicuQwmmJdicDo0etluVA5vic0iaLbW8Tm3EQkglWvndib2xJvx2zwfQ/640?wx_fmt=png&from=appmsg)

**PyPDF解析结果:**

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1ny3jIbrBerDy0ZRolwoBPvlKAiaeEvYPTgibbSALLMWXKiaDsJrhIZfe1g/640?wx_fmt=png&from=appmsg)

结果不出所料，**MagicPDF直接把PyPDF按在地上摩擦...**

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUk7Csn0E5A7R5kcqCt7p1b4BFuQV8YrwgDlp4CGzcheqpueRzJFZdUtsmIl6dwffiagy3S142hw4Q/640?wx_fmt=jpeg&from=appmsg)

  

通过更多的测试，我们也总结了二者在PDF文档解析中备受关注的多个角度对比结论：

  

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nBMOBjasDx8uIchpTKATe93LZcp3jicok4znxb3ribzo2swHEic3Y0IEIA/640?wx_fmt=png&from=appmsg)

**单独的文档解析环节比拼，****MagicPDF胜出——1:0****。**

  

✦

•

✦

**问答效果**

  

我们为本次评测选择了两种较为复杂的场景，分别是基于复杂表格问答和基于复杂问题的问答。

  

**案例1：基于复杂表格提问**  

“3月15日政府发行国债的净融资量是多少？”

  

● MinerU：  
提取表格结构 → 表头文字精准对应 →大模型秒答"2595.70亿元"

● PyPDF：  
把表格拆成散装文字 → 对不上 → 回答"融资量为2220.7.00亿元“（幻觉模式）

  

这一案例较为考验大模型对于表格结构的理解能力，但由于表格解析成先前那个样子，复杂表格这一环节PyPDF理所当然的指望不上了... **MagicPDF胜出——2:0**。

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nMFlfLwct3ur18VuqHNRynIaLyh9f70GAVibsWA5MNCwbBXp6fuOmbWQ/640?wx_fmt=png&from=appmsg)

更多案例请看：

  

  

**案例2：基于复杂结构的提问**  
“关于珀莱雅的投资建议？”  
  

● MinerU：  
跨页拼接文本+分离穿插表格 → 语义完整性MAX → 生成专业建议

● PyPDF：

丢失关键段落+表格文字粘连 → 大模型东拼西凑 → 回答当场翻车

  

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nxlNQZxulNN5zwbenwmLNGlTiac1jVib6NC4xnF3rcaf9nwb3LApeAgpQ/640?wx_fmt=png&from=appmsg)

  

更多案例请看：

  

  

**3:0**啊...除了“残忍”二字，已经找不到别的词能够形容这场PK了。同时，能够这么快完成效果验证，除了小编的聪明才智（不是）MagicPDF的强力支持，还有懒懒猫（LazyLLM中文名）短短几行代码就能把这个复杂应用构建出来，简直是妙上加喵，喵喵妙~🐱

  

  

**2**

  

**进阶优化方案****——**

**充分利用MinerU输出的多元信息**

**让RAG更懂你的文章**

  

除了以上最基本的使用，我们还带来了一些使用技巧，助力开发者更好的玩转MagicPDF。

  

**📌****坐标追踪模式：给每行文字装上GPS**

在某些讲求严谨性的专业场景中，RAG 系统不仅需要 "知道答案"，更要 "解释答案的来龙去脉"。这意味着 **AI 不仅要能检索到正确的答案，还要能够提供强有力的****证据链，指向原文中的具体位置**。例如，在法律、财务、医学等领域，AI 需要做到 **"可溯源"**，让用户不仅能获取答案，还能直接看到它是如何得出的。

  

想象一个法律检索场景，律师问 AI 某个合同条款是否允许提前终止，RAG 系统不仅要回答 "允许"，还需要指着合同第8页第3段第5行说："就是这里！" 这极大增强了 AI 生成内容的可信度，使其更加符合专业场景的**严谨性和透明性**要求。

  

对此，**MinerU 已经支持行级别的位置信息**，但当前版本默认不输出这些细节信息。不过，这并不妨碍我们自己挖掘和利用它！通过重写部分函数，我们可以深入解析 MinerU 的底层数据结构，**精确提取 block 级别和 line 级别的位置信息**，并以结构化的方式返回。这一能力将极大提升 RAG 系统的可解释性，使其能够支持**精准文本定位、高亮展示、证据链构建、可视化分析**等高级应用。

    # add patchs to magic-pdf

  

**【部分修改】：**

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nSRhtqPCiaGwKPEAia21p4TyLlNLl7thqQRkAqEW1eYiay0IppSFGH5InQ/640?wx_fmt=png&from=appmsg)

接下来介绍一种简单利用坐标信息的方式，在RAG pipeline中插入一个模块实现：根据目标文档的召回块画出box并保存，待问答后查看，就可以精准定位到你的问答依据！

    def draw_pdf_bbox(nodes, query, **kwargs):

  

接下来将其插入到pipeline流程中：

![](https://mmbiz.qpic.cn/mmbiz_png/vD6gfhrGGSx9m3Y40m1MJA9P59ftDK1nIwVtoZibczau2yksOibianfaCo739mK4PE1ZEWtGxWhqx1x1k0jib5fSMg/640?wx_fmt=png&from=appmsg)

  

效果请看：

  

**📌****定制精细化的本文分块策略：告别"切香肠式"文本处理**

  

MinerU 能够输出丰富的元信息，这为 RAG应用提供了极大的灵活性。传统的文本切分方法通常采用固定长度或简单的句子切割，这种方式容易破坏语义完整性，导致信息割裂，影响 RAG 问答的内容质量。而 MinerU 的元信息可以用于构建更加智能的内容结构化分块策略，确保每个分块都保持完整的语义单元，提升检索与生成的准确性。

  

在 MinerU 中，我们可以自定义更加灵活的分块方式，以适应不同的业务场景。例如，项目中提供了一种基于章节标题进行分块的通用算法，在实际应用中，可以结合业务需求进一步优化分块策略，确保信息的完整性。例如：

**1\. 招股书处理**

传统切分：固定字数切分，可能导致"业务概览"和"财务数据"混杂，信息断裂。

优化方案：按 “业务概览 → 财务数据 → 风险因素” 进行模块化分块，保证业务逻辑清晰，不破坏上下文连贯性。

  

**2\. 学术论文分析**

传统切分：可能导致假设、实验和数据分析混在不同块中，使得推理链断裂。

优化方案：按照 “假设 → 实验 → 数据 → 结论” 进行切分，确保逻辑链条完整，提高生成答案的可靠性。

  

**3\. 医疗报告解析**

传统切分：可能会将影像描述与诊断意见分离，使得问答系统难以精准匹配。

优化方案：按 “检查项目 → 影像描述 → 诊断意见” 切割或组合，确保影像结论与描述保持一致，提高问答准确度。

  

假设有一份 CT 影像报告，内容如下：

    患者姓名：张三  

  

**1\. 传统固定长度切分（错误示例）**

    分块 1：患者姓名：张三 检查项目：胸部 CT 影像描述：双肺下叶可见多发小结节

❌问题：影像描述和诊断意见被拆开，导致问答系统在生成答案时可能无法准确关联病变特征和医生建议。

  

**2\. MinerU 元信息辅助的结构化分块（优化示例）**

    患者姓名：张三  

✅优化点：每个块都是完整的语义单元，不会因固定长度切割导致信息断裂。

  

在LazyLLM搭建的rag框架中自定义切分算法只需继承NodeTransform并且将该类注册到document的分组中：

    class MagicPDFTransform(NodeTransform):

  

  

总结

  

以上就是基于**LazyLLM融合MinerU**实现PDF解析与RAG的应用与进阶，让PDF解析**从 “机械拆分” 迈向 “智能重构”**，更多高级玩法有待探索。

以上代码请参考项目 👉

https://github.com/jisyST/LazyRAG-Mineru#

**项目结构：**

  

欢迎添加小助手，进**MinerU交流群**

及时掌握更多动态！

  

![活码.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD73YXswn0XWT4bLm7ClibnIcHJtZnNo5k8ZZlJYQ0S7knjYKHXILd6amZAO3UTULPiardEya7yrCJ5g/640?wx_fmt=jpeg&from=appmsg)

  

文中资料和链接请点击“阅读原文”获取，提取码“1234”~

  

**相关阅读：**

[

多语言语料库万卷·丝路2.0开源，数据模态全面升级，搭建文化交流互鉴AI桥梁

2025-03-22

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWpiaQyypfXugnluAuNdTb2xbwXGXEm21O9eEukHmxlcaXsroDrQJFBNCGGGVCAVxssO82WpqDFBhA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550189&idx=1&sn=cf85998f0df64b5454504cf22589caca&scene=21#wechat_redirect)

[

MinerU大上新！桌面客户端、新版API、国产化适配版全都有，更多功能等你解锁

2025-01-21

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUKVun2ZibS4hY5pJBgBL1SwjZwQnCpZGXK3S5NjReNlpg01xwpV4rvW676SChOO9uSwTzzQRWdhGA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549851&idx=1&sn=0c3208dfa19356b9044d2ff7d6fa6b93&scene=21#wechat_redirect)

[

多语言语料库“万卷·丝路”发布，AI赋能共建“一带一路”

2025-01-09

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXk2oA4FMPVDMdcDVCU27qrcoZJcm8XvX9zEvQMy5Nico74zGOeIyvq1Doc1Zr5ly2RYm8TavQR3rg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[不是吧？这么好用的开源标注工具，竟然还有人不知道…](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

[2024-08-22](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6jsZJmjym44k1KnuBibIibwV47VtuvqyerwKmT7UnBgAp4eL1Uqic7ulsE0NcPnlKtRNSGyGjiasYDiaw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

  

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言