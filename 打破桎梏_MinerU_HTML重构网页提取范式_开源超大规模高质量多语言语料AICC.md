     打破桎梏！MinerU-HTML重构网页提取范式，开源超大规模高质量多语言语料AICC \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

打破桎梏！MinerU-HTML重构网页提取范式，开源超大规模高质量多语言语料AICC
===========================================

原创 爱学习的 OpenDataLab 2025-11-26 18:35 上海

> 原文地址: [https://mp.weixin.qq.com/s/JxV9MWW5twPa-l0iIpX8XA](https://mp.weixin.qq.com/s/JxV9MWW5twPa-l0iIpX8XA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：  

数据质量是决定大模型能力的关键因素之一。大规模预训练语料库（如Common Crawl）主要依赖于网页数据。然而，长期以来，相关研究将优化重心放在下游的过滤和去重策略上，对HTML提取这一重要工作却未引起足够重视。

传统网页提取方法基于启发式规则，面对万亿规模网页数据难以优化和迭代。近期推出的基于模型的内容抽取方法无法高质量还原代码、公式等重要信息。

为此，上海人工智能实验室（上海AI实验室）OpenDataLab 团队提出了一个“将内容提取任务重构为一个序列标注问题"的方法，据此研发了能够进行语义感知的新一代网页提取工具—— MinerU-HTML。该工具采用两阶段提取方法，第一阶段利用模型从HTML DOM中标注出正文节点，第二阶段对正文节点结合HTML语法进行精细识别（特别是代码和公式），转换为结构化数据供下游使用。

与此同时，OpenDataLab 开源了用该工具构建的高质量语料AICC（AI-ready Common Crawl），建立了行业新标杆。该方法及工具后续可广泛应用于DeepResearch搭建、RAG构建、网页采集与解析等场景。

  

*   AICC 数据集 HuggingFace链接：https://huggingface.co/datasets/opendatalab/AICC
    
*   MinerU-HTML 在线demo 链接：https://opendatalab.com/ai-ready/AICC
    
*   技术报告链接：https://arxiv.org/pdf/2511.16397v1
    
*   模型链接：https://huggingface.co/opendatalab/MinerU-HTML
    

  

相较于基于传统启发式规则研发的网页提取工具，MinerU-HTML可以适应多样布局的网页提取。基于 MinerU-HTML 的提取能力，团队开源了规模达 7.3 万亿 tokens 的 AICC 多语言语料库，为学术界及产业界提供了高质量的大模型预训练数据基础。

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

AICC 语料库超越现有高质量语料库，建立新标杆

  

OpenDataLab 团队在包含7,887个标注网页的MainWebBench基准测试集上进行了评估，结果表明：MinerU-HTML在综合指标和结构化元素保留方面均建立了行业领先性能（SOTA）。而采用MinerU-HTML构建的AICC语料库，在下游任务中超越了RefinedWeb和FineWeb等公认的高质量语料库，这直接证明了高质量提取可以媲美甚至超越激进过滤策略带来的效益。不仅如此，AICC还在通用知识（General Knowledge）和阅读理解（Reading Comprehension）任务上均取得了最佳性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTqltQNfaia3pHQpJSYwppCF8hWeEdUmUG583uBcZxVJAdD6Tnv1Fly6Wsg/640?wx_fmt=png&from=appmsg)

图为技术报告中结构化元素提取器的性能对比。 上方表格展示了不同提取器在 WebMainBench-Structured 基准上的代码块（Code Edit）、公式（Formula Edit）和表格（Table TEDS）的相似度得分。下方表格展示了它们在 WCEB 基准上的准确率。MinerU-HTML 在所有测试中均表现最佳。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTql7MknE83GnePMen2h0uhX1oPPJjSqv4UiaDNzibHmVPW4icYsfkboedTHg/640?wx_fmt=png&from=appmsg)

MinerU-HTML在通用知识和阅读理解上的表现

具体来说，AICC语料库基于Common Crawl 2025年的两个快照，通过MinerU-HTML进行内容提取并转换为Markdown格式。为确保对比实验的公平性，其过滤流程完全沿用RefinedWeb的严格标准，包括去重、语言识别和安全过滤等环节。质量验证采用LLM-as-Judge方法对10,000对文档进行评估，结果显示AICC在72%的案例中更受青睐，且其提取内容平均长度达到Trafilatura版本的1.16倍，表明其不仅保留更多内容，且质量显著提升。

在下游任务表现方面，基于62B token的控量训练实验表明，AICC预训练模型在13项基准测试中平均准确率达到50.82%，展现出显著优势。具体而言，其性能优于Trafilatura提取的TfCC语料（49.74%，提升1.08个百分点）、RefinedWeb（49.13%，提升1.69个百分点）以及FineWeb（49.61%，提升1.21个百分点）。尤为突出的是，AICC在通用知识任务上提升1.93个百分点，在阅读理解任务上提升5.69个百分点，有力证明了高质量内容提取对模型能力的促进作用可与激进过滤策略相媲美，甚至更具可持续性。

上述表现，有力验证了HTML提取质量对下游性能的影响与过滤策略同样重要的猜想。

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**精细化两阶段流水线：模型驱动的网页内容提取方法**

  

MinerU-HTML采用了独特且高效的两阶段流水线设计，它将传统的网页内容提取升级为模型驱动的语义理解任务，核心流程首先是 Main-HTML 提取（语义化筛选主内容），随后是网页各类元素（图片、表格、列表、代码、公式、段落等）的格式化，最终输出大模型（LLM ）友好的 Markdown 格式文本。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTqluWfMb0HbDQiadbQBZnjvq2sQsUnibic49AomeqAC0arsmEJLbQiaXzxMog/640?wx_fmt=png&from=appmsg)

  

在第一阶段的 Main-HTML 提取中，旨在从原始、嘈杂的 HTML 中精准识别并剥离冗余信息（如广告和导航栏），只保留核心的主内容 (Main-HTML) 及其完整的结构。首先，为了应对原始 HTML 过于冗长和嘈杂的问题，系统首先将其转化为两种并行表示。简化 HTML (Simplified HTML) 是经过精简的输入，去除了非内容标签（如 <style>、<script>）并参照HTML开发规范进行块级分割，大幅减少了模型需要处理的 tokens 数量，提高了推理效率。同时，系统保留了映射 HTML (Mapping HTML)，它忠实于原始的块级结构，用于后期的内容重建。

随后进入内容分类，这一核心步骤通过一个0.6B 参数量的仅解码器语言模型 MinerU-HTML-Classifier 来完成。该模型对简化 HTML 中的每个语义块进行二分类标注，判断其是否为“main（主内容）”或“other（冗余）”。为确保输出的准确性，系统采用了约束解码（Constrained Decoding）完全消除了模型可能产生的幻觉和格式错误。

最后在后处理阶段， 根据模型的分类结果，系统将预测标签映射回映射 HTML，剔除被标记为“other”的冗余块，最终得到 Main-HTML，它是原始文档的有效 DOM 子树，保证了内容的忠实性。

在第二阶段——文档格式化中，提取出的 Main-HTML 需要转换为 LLM 友好的 Markdown 格式。此阶段采用两步转换：先是将 Main-HTML 解析为 JSON 格式的结构化内容列表，明确标注出标题、段落、代码块、公式、表格等 11 类语义单元，并存储其专属属性。然后针对每种元素类型设计专用转换规则，将其转化为 Markdown。例如，它确保了代码块保留缩进和语法标记，数学公式保留 LaTeX/MathML 完整语法，并区分处理简单表格（可转为 Markdown 格式）和复杂表格（有单元格合并）。通过这种中间表示方法，有利于数据表达和筛选，也使其能够按需转化为下游任务所需的格式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTqlmu3uE06N6zB4ibjh07aib9IQtyDdwWyoq9bB2WNwLzK8yaMicVvxQ0kAg/640?wx_fmt=png&from=appmsg)

技术报告中，关于Json格式的示例

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTl2ENUU0R7ribTJ9eIjdpZayeZMbQwdUUiaWKMmHpvtLcPAlyibPGRC7CQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

**万亿级网页的高效处理：模板感知优化策略**

为了能够在万亿规模网页上高效运行，MinerU-HTML 设计了模板感知优化策略。系统首先在最长子域名内对相似网页进行聚类（DOM Tree相似性）。然后在每个类别中挑选一个最具结构代表性的页面使用 MinerU-HTML 模型进行推理。最后，将模型对该代表性网页的分类结果迁移应用于所在分类内所有其他页面，从而实现大规模、高效率的 CPU 处理，大幅降低了对 GPU 资源的依赖。

  

上海AI实验室秉持开源开放的理念，通过MinerU-HTML的发布，进一步提升了业界大规模预训练语料库构建的质量基准，持续致力于持续构建多知识、多模态、标准化的高质量语料数据。

目前，MinerU-HTML所构建的AICC语料库demo已经上线，AICC数据集已经上架，旨在为学术界及产业界提供更符合主流中文价值对齐的预训练语料。为了更好地服务社区、精准把握用户对MinerU-HTML在线服务的使用场景，我们特此发起一份简短的调研问卷。 您的反馈对我们至关重要，它将直接影响我们是否尽快启动MinerU-HTML在线服务的开发与部署计划。

MinerU项目的功能持续拓展与性能的不断进步，将持续为大模型时代提供坚实、可靠、无限扩展的“Tokenize Everything”基础，共同建设一个包容、开放、有序、共享的人工智能大生态。

欢迎加入MinerU HTML 首批内测体验官，获取最新信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTqlPIEtUiaAYkd2bh2Omuy1CVTx81JvKJnl9u1EcLFGl8EarsOnrybWUbg/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END  

  

**相关阅读：  
**

  

  

[MinerU又双叒更新了！化学解析×多模式翻译等多种功能上线！文档解析处理爽到飞起！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551231&idx=1&sn=5c579ae2190b55d8282f2e9ec35e2399&scene=21#wechat_redirect)

2025-08-08

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTyWAumU6Y7sdbgsxLgByGO8XbrzT7AOhs8LlQhV1ph0m76jjMmKVkhA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

[上海AI实验室发布MinerU2：通专融合路线如何补齐AI-Ready数据的最后一公里](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550992&idx=1&sn=5f53580545f1f6070e5242ab35cae86d&scene=21#wechat_redirect)

2025-08-07

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWBNkx3esjVNr2VtRgpf9vlV5iaGkUiaXPhgnb94tv1wfx2ahMq2icbHz0Bxkt7Y4NmONUJWYo57Fibibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550992&idx=1&sn=5f53580545f1f6070e5242ab35cae86d&scene=21#wechat_redirect)

[新工具开源！Vis3大模型数据可视化利器：填 AK/SK 直接预览 S3 数据，JSON/视频/图片秒开！本地文件也可用](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550861&idx=1&sn=f7057a62647e879a194cce5938cc76ac&scene=21#wechat_redirect)

2025-07-04

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUn8yYtug9M9iaemDlEomWBrcUrHQ5KAguBYe2jqOz84Q8IsoY3G5pAERnnJTGOqWAIupGwRxibgFDA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550861&idx=1&sn=f7057a62647e879a194cce5938cc76ac&scene=21#wechat_redirect)

[Dify、n8n、扣子、Fastgpt、Ragflow到底该怎么选？超详细指南来了【好文推荐，附MinerU实用教程】](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550805&idx=1&sn=4b73bf0c9f9cc85ab3ed4cf36a22acd9&scene=21#wechat_redirect)

2025-06-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUniaALHa5jYSxXR991CavbDvPXicgJSx3AmxRq7DY4ZRXq5RMczgD9H9fZLfgRqjkKXkrgmr3uRSibg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550805&idx=1&sn=4b73bf0c9f9cc85ab3ed4cf36a22acd9&scene=21#wechat_redirect)

[MinerU × Cherry Studio：知识库再添动力！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550749&idx=1&sn=8e8668431c3d41c81b5071d0d37064c4&scene=21#wechat_redirect)

2025-06-17

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAV3ojk5ZyrEnaWN2SN1WCrUZ4z3BAvHsyficZwGUAMHiao25HvyMn5JNVpnUTiaicHqHnTNre2IPueNTQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550749&idx=1&sn=8e8668431c3d41c81b5071d0d37064c4&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言