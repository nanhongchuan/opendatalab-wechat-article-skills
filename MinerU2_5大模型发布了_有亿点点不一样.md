     MinerU2.5大模型发布了，有亿点点不一样 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU2.5大模型发布了，有亿点点不一样
=======================

原创 OpenDataLab 2025-09-30 15:31 上海

> 原文地址: [https://mp.weixin.qq.com/s/OAke8qjiiAGzwoL8QjDddA](https://mp.weixin.qq.com/s/OAke8qjiiAGzwoL8QjDddA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

日前，上海人工智能实验室（上海AI实验室）全面上线新一代文档解析大模型——**MinerU2.5**。作为MinerU系列的最新版本，MinerU2.5仅以**1.2B参数规模**，在布局检测、文本识别、表格识别、公式识别等核心任务上取得全面突破，在文档解析主流评测基准**OmniDocBench****、olmOCR-bench及Ocean-OCR上均取得优异成绩****，**超越Gemini2.5-Pro、GPT-4o、Qwen2.5-VL-72B等多模态通用大模型以及dots.ocr、MonkeyOCR、PP-StructureV3等文档解析专业模型和工具。  

  

在解析精度和解析观感上，MinerU2.5的解析效果显著提升，解析质量逐步逼近人工标注效果，实现了从“综合领先”到“全面领跑”的跨越，更以1.2B的精巧参数在大规模语料提取等实际生产力场景中兼顾高精度与高效率，展现出真正的落地应用价值。  

  

目前，MinerU在线产品已全面集成MinerU2.5文档解析大模型，并同步实现功能升级。此次迭代重点新增表格旋转识别、无线/少线表格解析及参考文献识别等能力；同时在中文公式、复杂数学公式及嵌套表格的提取与渲染方面进行了深度优化，显著提升了结果的准确性与可用性。通过本次升级，MinerU产品在科研、金融、教育等重点场景中展现出更强的适配性与支撑力，进一步拓宽了智能文档解析的应用边界，为高质量信息提取和RAG知识库构建提供了更加坚实的应用支撑。

**技术报告：  
**https://arxiv.org/abs/2509.22186

**开源项目：**https://github.com/opendatalab/MinerU

**开源模型：**https://huggingface.co/opendatalab/MinerU2.5-2509-1.2B

**在线使用：**https://mineru.net/OpenSourceTools/Extractor

从评测结果来看，在权威的OmniDocBench基准测试中，MinerU2.5取得结果最优（SOTA），在布局检测、文本识别、表格识别、公式识别等关键指标上超越Gemini 2.5-Pro、GPT-4o等国际顶尖模型，对比开源文档解析方案（如MonkeyOCR、PP-StructureV3），MinerU2.5在解析精度、结构完整性和格式自然度方面同样处于优势地位。相关评测结果已在团队最新公开的技术报告中发布。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUezicnz6302eMep9iau2dGkTS5XyIjSicnx9NTaRByuPxdb7s5VCEI7nrKib37T79dRlZaHwibQZDBuRw/640?wx_fmt=png&from=appmsg)

▲OmniDocBench中的评测结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUezicnz6302eMep9iau2dGkTmuwIZpuVYuYW2tYMpVkibYSsZgeBNE7W3sHrCtljEfYCo60TcFhsLiaw/640?wx_fmt=png&from=appmsg)

▲OmniDocBench中的评测排名

为了保证模型能够轻松处理不同来源、不同难度、包含不同元素的文档，科研团队精细设计了文档解析数据引擎，为模型预训练和微调阶段提供多样性、高质量数据。针对文档解析的预训练阶段，团队考虑从文档多样性、元素多样性、中英文数量均衡保证预训练数据的多样性，并通过多阶段模型筛选保证数据质量。在模型微调阶段，团队提出了基于推理一致性的迭代挖掘策略，针对一阶段预训练模型挖掘困难样本，并结合智能化标注及专家修正保证数据足够复杂、精准，有效提升模型在复杂样本上的解析能力。最终模型在复杂排版、复杂公式及复杂表格上性能显著提升，在其他普通样本上解析精度达到人工标注员水平。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXMXM6o4t4SnicUXzeaZA5D8wWib7zBrjTY83iahGmo6skia9DJGNmDNePqXvosia4K9sxVm3o9llsTxNw/640?wx_fmt=png&from=appmsg)

▲MinerU2.5 技术架构

在解析效率方面，MinerU2.5采用了QwenVL2系列的原生分辨率视觉编码器（675M）及0.5B的语言解码器，总参数量接近1.2B。在布局分析阶段，MinerU2.5将高分辨率文档图像下采样到1036\*1036 从而实现高效解析。在内容识别阶段，MinerU2.5仅需将切割的小区域元素进行原生分辨率编码解析，解析速度快、精度高、幻觉少。配合vLLM参数优化及工程优化，MinerU2.5在消费级显卡NVDIA 4090（48G）上达到每秒1.7页的解析速度，远超其他大模型解析方案，让高质量、低成本的解析方案成为可能。

**依托MinerU2.5文档解析大模型核心能力，MinerU在线产品全平台进行了升级。**本次迭代重点新增表格旋转识别、无线/少线表格解析、跨格式文档无损复制及参考文献识别等能力，同时针对中文公式、复杂数学公式与复杂嵌套表格进行了深度优化。

上述所有新增功能已全面融入多格式导出（JSON / Markdown）、复制、翻译、收藏等重要功能，实现即开即用、无缝体验。此外，MinerU产品导出的JSON文件中，保留了完整的页眉、页脚、页码、脚注、侧边文本等信息，方便开发者进一步处理使用，显著提升了文档智能解析的精度与适用性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXMXM6o4t4SnicUXzeaZA5D8l5OcCCOVia9ez0vMyM4Uc6B3euibTouCf7npF3icMdN0V9lopRYfBHc5Q/640?wx_fmt=png&from=appmsg)

▲在数学教材中的复杂公式解析任务中，传统方案常出现符号遗漏或结构破坏，而MinerU2.5能够准确识别长难公式，输出整洁的LaTeX代码，直接渲染为完整公式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXMXM6o4t4SnicUXzeaZA5D89RfSmkH8FlE6QvXRTrgshrRLnnwVOgD82POySo49EaKDdGZNkGp1pA/640?wx_fmt=png&from=appmsg)

▲在金融领域，对于一份模糊并包含合并单元格的财报，传统模型往往输出结构散乱，而MinerU2.5能够完整保持原始表格结构，无缝衔接跨页信息，并直接导出整洁的Excel文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXMXM6o4t4SnicUXzeaZA5D84LmQNwIZr6WcjMm8B5ickg1VwGj8ibG77lwHvDRLBe3MLfK5PuBUZ8Aw/640?wx_fmt=png&from=appmsg)

▲在学术论文的参考文献解析中，MinerU2.5不仅能够分割条目，还能精准提取作者、期刊、年份、DOI等元数据，输出为结构化JSON格式，远超其他方案的纯文本结果。

目前，MinerU2.5已同步上线HuggingFace、ModelScope及GitHub，提供模型下载、源码托管与在线Demo服务，全面支持科研人员、开发者和产业用户的多样化需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUezicnz6302eMep9iau2dGkTdYEuk3nSgToicEricosoDUicQia7ibFCyzT1I0j2iaSIoTMPfgU2yyxVvL0A/640?wx_fmt=jpeg&from=appmsg)

▲MinerU在线产品全线上新MinerU2.5文档提取大模型能力

在硬件生态建设方面，OpenDataLab团队坚持自主可控和开放协同并举，持续推进国产化适配和算力优化工作。当前，通过与DeepLink开展联合攻关，依托后者开放计算体系打通多后端算力通路，MinerU2.5系列能够在国产算力平台的千卡级生产环境中实现稳定部署和高效运行。MinerU2.5将与昇腾、沐曦、摩尔线程、寒武纪、海光等平台等国产算力平台完成深度适配，相关成果将以开源形式面向社会共享，同时针对高性能场景提供面向产业化的专业化支持。

面向多样化应用场景，MinerU已率先完成对Dify、N8n、扣子、FastGPT等主流Agent平台的插件开发与适配，并为钉钉、Cherry Studio、Sider等知名AI应用工具提供技术支持，保障其平稳接入与高效运行。下一步，团队将持续拓展国际国内主流平台和开发工具的适配覆盖，进一步加强与重点行业应用的深度融合，打造更加开放、兼容、可扩展的技术生态体系。

面向未来，MinerU将继续秉持“Tokenize Anything”的技术远景，持续拓展异构数据智能解析的广度与深度，加快推动数据向AI-Ready形态的高效转化。随着技术迭代与应用深化，分散复杂的多源数据价值将被更大程度激活，并为通用人工智能构筑坚实而高效的底层工具支撑。

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END  

  

**相关阅读：  
**

  

  

[高性能文档解析引擎MinerU再升级，全方位刷新行业SOTA，全面助力AI Ready数据自由](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551188&idx=1&sn=6fd9796aa6217ed6a4b6578529b95c31&scene=21#wechat_redirect)

2025-09-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWRzMSdUHib1jFW1yZbXWzHZ8cfMeAnFfDsBicTpzECoSq9n23fo3qEqp67ibV6oM7OoxEqCTywgEPMA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551188&idx=1&sn=6fd9796aa6217ed6a4b6578529b95c31&scene=21#wechat_redirect)

[告别“炼丹玄学”：上海AI实验室推出首个大模型数据竞技场OpenDataArena](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551160&idx=1&sn=e65922d91d636610950a639a8b7201f3&scene=21#wechat_redirect)

2025-08-25

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAX4MPr4HTUGUznzZOTIt4jdXfGf5V8fyfDh0myShrn5fn1qia6pSQ7loITSlL0yXhKtAIAgmNtTm9Q/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551160&idx=1&sn=e65922d91d636610950a639a8b7201f3&scene=21#wechat_redirect)

[战略科学家对话：AI+科学，数据和人才是关键](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551160&idx=2&sn=bf10d5a6dd753ee9c5d8acf2c2357de9&scene=21#wechat_redirect)

2025-08-25

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAX4MPr4HTUGUznzZOTIt4jd0y016CXy33wBicXaHmPx6p0wzqwIPc4iazfLAAsVoibHJUIGfeBTFM7dQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551160&idx=2&sn=bf10d5a6dd753ee9c5d8acf2c2357de9&scene=21#wechat_redirect)

[MinerU又双叒更新了！化学解析×多模式翻译等多种功能上线！文档解析处理爽到飞起！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

2025-08-08

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTyWAumU6Y7sdbgsxLgByGO8XbrzT7AOhs8LlQhV1ph0m76jjMmKVkhA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

[斩获ACL 2025最佳主题论文奖丨Meta-rater 框架，1% 算力锁定大模型最优数据](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550991&idx=1&sn=a7c4dc206735cda2cad1f78eb785d412&scene=21#wechat_redirect)

2025-08-06

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXO1p9hyFugKRoPbgtleLVDpxJMbOqnqRnK5ofAicTt6IOpuMjEX7NicSlELGG2EeIptRTgY19sLj6g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550991&idx=1&sn=a7c4dc206735cda2cad1f78eb785d412&scene=21#wechat_redirect)

[上海AI实验室发布MinerU2：通专融合路线如何补齐AI-Ready数据的最后一公里](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550992&idx=1&sn=5f53580545f1f6070e5242ab35cae86d&scene=21#wechat_redirect)

2025-08-07

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWBNkx3esjVNr2VtRgpf9vlV5iaGkUiaXPhgnb94tv1wfx2ahMq2icbHz0Bxkt7Y4NmONUJWYo57Fibibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550992&idx=1&sn=5f53580545f1f6070e5242ab35cae86d&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言