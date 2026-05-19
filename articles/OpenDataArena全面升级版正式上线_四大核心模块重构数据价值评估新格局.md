     OpenDataArena全面升级版正式上线，四大核心模块重构数据价值评估新格局 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

OpenDataArena全面升级版正式上线，四大核心模块重构数据价值评估新格局
========================================

原创 爱学习的 OpenDataLab 2025-12-23 18:50 上海

> 原文地址: [https://mp.weixin.qq.com/s/eD9rNbm532zH0p6vdpWilA](https://mp.weixin.qq.com/s/eD9rNbm532zH0p6vdpWilA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：  

为破解长期以来学界与业界**难以对数据进行价值量化**的困局，上海人工智能实验室（上海AI实验室）OpenDataLab团队在今年8月开源了首个全面、公正的后训练数据价值评测平台——**OpenDataArena(ODA)**。该项目致力于将数据选择从“盲目试错”的炼丹术，转变为一门可复现、可分析、可累积的严谨科学。

在初版系统发布后的数月间，项目通过团队内部及小范围社区用户的深度使用，完成了高强度的技术验证与功能打磨。伴随着评测规模、工具链和分析能力的持续扩展，近期，**我们终于迎来了ODA的全面升级——一个结论更系统、功能更完整、视角更多元的正式版本**，该项目面向全体开发者开放。

  

项目主页：https://opendataarena.github.io/

开源工具：https://github.com/OpenDataArena/OpenDataArena-Tool

数据集：https://huggingface.co/OpenDataArena/datasets

报告链接：https://arxiv.org/pdf/2512.14051

ODA的核心理念非常明确：数据价值必须通过真实的训练来检验，而非主观的臆测。为此，我们**立足于全新发布的正式版本，对平台进行了体系化的深度重构**，由四个相互支撑的核心模块组成了这套完整的数据评测基础设施。这标志着ODA已经从最初的功能验证阶段，发展成为可以对数据价值进行系统化评测的重要平台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXmBEbaufxlnOUjXxqWfEbk9G5PqzrRxu5auYns60gX9k5hKT6Yx8CPqlPicjybiczjTo8YXkB2QZOA/640?wx_fmt=png&from=appmsg)

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

数据价值排行榜

首先，ODA项目打造了**数据价值排行榜。通过构建一套统一的训练与评测流程，让数据**在固定的模型规模（如Llama3、Qwen2/3 7-8B）和训练配置下，对来自不同领域的文本及多模态数据进行横向评测。

评测覆盖**通用、数学、代码、科学与长链推理等**能力维度，这使得数据价值能直接通过下游任务（如数学、代码、推理等）的实际表现来量化，而非主观判断。目前，ODA平台已经从初版仅仅只有文本数据的评测，扩展到了**多模态数据集的质量评测**，并以最先进的Qwen3-VL作为真实训练的基准模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXmBEbaufxlnOUjXxqWfEbkl7PtFGsicpH59DYxA3eBzqbKdzPoibyIPf5nJYjTTyLl4J0wQcStbmPA/640?wx_fmt=png&from=appmsg)

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  

数据血缘探索器

其次，针对数据界常见的“近亲繁殖”问题，ODA全新发布“**数据血缘探索器”**。它像绘制族谱一样，清晰地刻画出数据集之间的继承、混合与蒸馏关系。通过结构化建模与可视化展示，研究者可以直观地看到不同数据集之间的高度重叠与依赖关系，看到社区中被反复复用的核心数据源，以及更清晰的发现潜在的训练–测试污染与“近亲繁殖”问题。这一能力让“为什么某些数据集长期霸榜”不再是经验结论，而是可以被**结构性解释**的现象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXmBEbaufxlnOUjXxqWfEbkPGMLiaSBYNIP2UF3VEp2P38ribIzGFJz5jNC7M9gqn2ECD7oStTlKqDA/640?wx_fmt=png&from=appmsg)

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTl2ENUU0R7ribTJ9eIjdpZayeZMbQwdUUiaWKMmHpvtLcPAlyibPGRC7CQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)  
**多位数据评分器**

除了看模型结果，ODA还从数据本体出发，对数据质量进行**细粒度刻画**。ODA提供了一个细粒度的评分框架，基于模型评估、LLM-as-a-Judge与启发式指标等多种方法，从指令复杂度、响应质量、多样性等维度对数据进行深度剖析，生成每份数据的专属“体检报告”，并已对**千万级样本的评分结果进行开源**。这使得研究者不仅能判断“哪份数据更有效”，还能进一步分析它为什么有效。值得一提的是，在初版的基础上，ODA多维数据评分器目前已经扩展支持**80+种多维度的评分器**，支持用户一键方便的对所需要的数据维度进行打分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXmBEbaufxlnOUjXxqWfEbkJaWPrtMp0aU8yk9J9GmhVwnvVvDtEXe0s9xNmiaHiacoiaZ73ENiaSSsicg/640?wx_fmt=png&from=appmsg)

### 

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)  

全开源评测工具箱

此外，为了促进社区共建，ODA**完全开源**了其训练、评分和可视化工具，覆盖从模型微调到结果复现的完整流程，以及上述精细化的数据评价打分器。ODA工具支持用户**一键复现结果**，或对自己私有数据进行标准化评测，实现真正意义上的横向对比。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXmBEbaufxlnOUjXxqWfEbkXfj3WpybGd9rBs5r3vvLSQNNFpXnlzI5kgS6D9hOZ0B6ESqHic2Iflw/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWQD0sPFKj42EdX95eD3ByOCq4fgcJia6p2gEDLEm8m3BrjQqAvUpPOmVa13nrgZUjZPBUWuFhpwzA/640?wx_fmt=png&from=appmsg)

**硬核发现：那些被忽视的数据真相**

在对120多个主流数据集进行超过600次训练和4000万条数据的深度分析后，OpenDataLab团队得出了一系列具有指导意义的“硬核”结论，足以重塑业界对高质量数据的认知：

1.  **解答质量比问题复杂度更关键：**实验发现，单纯增加问题的复杂度并不能有效预测数据价值。相反，解答的长度（推理过程的充分性）与最终质量呈强正相关，这在数学和科学类任务中尤为突出。
    
2.  **代码数据的“异类”属性：**搞代码模型不能照搬数学的逻辑。代码讲究简洁精准，长篇大论反而会损害效果。这意味着通用的评分标准在代码领域经常失效，必须建立针对性的评估体系。
    
3.  **开源数据“近亲繁殖”严重：**ODA的数据血缘分析显示，社区反复依赖的核心数据源比较有限（例如GSM8K被多次复用），由此造成了严重的数据同质化。借助数据血缘分析，更极端的发现是，数据污染越来越严重：大量训练样本直接与测试集发生重叠。
    
    **“少即是多”的局限性：**尽管LIMA等研究曾宣称少量精选数据即可成功，但 ODA的实验证明这极度依赖模型底座的先天能力。如果底座一般，过少的数据量会导致性能崩塌。真正稳健的路径是追求“高质量且具规模（High-Density Volume）”的数据配方。
    
4.  **为什么有些数据集能霸榜？**以AM-Thinking-distilled为代表的超大规模聚集型数据集，能够同时在数学与代码任务上取得明显的优势，关键原因在于其跨领域融合能力。它通过递归方式整合了**435个数据节点**，显著提升了数据分布的多样性与互补性。
    
    **数据可以弥补底座差距：**这是一个令人振奋的发现。即使Llama3.1和Qwen 2.5 之间存在显著的底座分差，只要用上如 OpenThoughts3-1.2M 这样的高质量微调数据，这个差距几乎可以被抹平。可以说，好的数据配方真的能让模型“逆天改命” 。
    

**未来展望**

OpenDataArena的远景，绝不仅满足于建立一个排行榜，更致力于将数据研发从“玄学”推向可复现、可分析的“科学”。未来，ODA将持续进化，探索智能体数据，金融、医疗等垂直领域的深层价值。

在这个数据决定AI上限的时代，唯有手握科学的标尺，才能精准丈量每一份数据的真实重量！

  

END  

  

**相关阅读：  
**

  

  

[MinerU又双叒更新了！化学解析×多模式翻译等多种功能上线！文档解析处理爽到飞起！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

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