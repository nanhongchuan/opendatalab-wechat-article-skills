     上海AI实验室发布MinerU2：通专融合路线如何补齐AI-Ready数据的最后一公里 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

上海AI实验室发布MinerU2：通专融合路线如何补齐AI-Ready数据的最后一公里
===========================================

原创 OpenDataLab 2025-08-07 14:59 上海

> 原文地址: [https://mp.weixin.qq.com/s/JbEuJShAiYW1Vb7rv\_a4tw](https://mp.weixin.qq.com/s/JbEuJShAiYW1Vb7rv_a4tw)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

### 导言：

当前，大模型训练的竞争焦点正从“数据规模”转向“数据质量与差异化”方向。如何高效精准地挖掘高质量私域数据成为关键挑战。为解决这一难题，**上海人工智能实验室（上海****AI****实验室）**于去年7月开源智能文档解析引擎**MinerU**，旨在将复杂文档精确地转化为可用于大模型训练的AI-Ready数据。

经一年潜心研发，基于通专融合技术路线，**采用****全新架构****的****MinerU2****正式推出****，**其凭借**0.9B精巧参数量**，在多语言与复杂文档解析精度上实现突破，**同级别开源模型综合评分第一**。**MinerU2在**性能、速度跃升的同时，将可解析场景延伸至科学数据领域，补齐AI-Ready数据的最后一公里，缩窄AGI促进科学发现的鸿沟，已成为[『书生』科学多模态大模型Intern-S1](https://mp.weixin.qq.com/s?__biz=MzkzNzIyNDg4MQ==&mid=2247562142&idx=1&sn=3230cc018598abc9fe51b2af8fde5232&scene=21#wechat_redirect)开源工具链中的重要一环。

目前，MinerU深度集成于『书生』科学发现平台Intern-Discovery和AI地球科学家智能体系统EarthLink，为科研人员提供高效的文档解析与数据提取服务，极大提升了文献处理和科学研究的效率。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

  

**从“量变”到“质变”：**

**AI-Ready数据成为大模型**

**下半场核心竞争力**

随着模型技术发展，互联网数据趋同性导致通用大模型同质化，细分专业化成为深入行业落地的必然路径，这些数据常存在于私域，且以文档形式最为普遍。数据竞争正从“粗放式扩张”转向“精细化挖掘”，从私域数据中构建高质量AI-Ready数据成为竞争关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWBNkx3esjVNr2VtRgpf9vlydGsWEgFppG36HHvz1eMCt4NsZdT9TEqgh1QLPfYYTsr14KZETt6fQ/640?wx_fmt=png&from=appmsg)

AI-Ready 数据成为大模型下半场核心竞争力

而在私域数据中解析文档和构建AI-Ready数据时，面临着三重结构性挑战：

*   **格式复杂多样：**私域数据的来源多样，数据形态格式复杂，对文档解析能力提出挑战
    
*   **高精度要求：**关键领域对数据精度要求高，微小误差可能引发决策偏差与业务风险
    
*   **高速度需求**：数据解析只是大模型研发与落地的第一步，每个环节对速度的容忍性有限
    

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

  

**MinerU2：基于Intern‑S1**

**拓展科学领域****AI****‑Ready数据**

**构建能力**

在此背景下，上海AI实验室于去年7月推出开源智能文档解析引擎MinerU，支持高精度解析文档元素，支撑构建高质量AI-Ready数据。经过一年的潜心研发，上海AI实验室团队联合北京大学团队，以全新技术架构推出MinerU2——**端到端多模态文档解析大模型**，位列同级别开源模型综合评分第一，解析精度和速度大幅提升，有力突破了前文提及的三重结构性挑战。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWBNkx3esjVNr2VtRgpf9vlupLiadU1Kot8WaJJt42gzQBUI9tcG8VhxIHysewibIZVWpZTbdRlG9sg/640?wx_fmt=png&from=appmsg)

MinerU 相较于同级别开源模型在Benchmark 上的性能对比

MinerU2解析准确率较前代提升22%，实现 “全尺寸・真高清”解析，能精准解析学术论文、教科书等复杂版面。其采用的模型参数量仅0.9B，性能比肩72B大模型，可在消费级显卡单卡上流畅运行。通过集成自适应缩放、SGLang等技术，显著提升推理效率，解析速度较上一代提升6倍。它在精准识别文本、布局、表格基础上，**还能高精度提取数学公式、物理符号、化学分子式和化学反应**，支撑高质量AI-Ready的语料构建管线，将可解析场景延伸至科学数据领域，补齐AI-Ready数据的最后一公里，缩窄AGI促进科学发现的鸿沟，现已成为『书生』科学多模态大模型Intern-S1开源工具链中的重要一环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWBNkx3esjVNr2VtRgpf9vlNrhSz6gfedPwugIh397BAmgSOaVau0Y4NMN0RudGiaAib9UcbRNoR6xQ/640?wx_fmt=png&from=appmsg)

“全尺寸・真高清” “小模型・大能量” “深优化・高性能”

MinerU2的能力突破，**植根于上海AI实验室在基础理论与科学数据领域的长期战略投入：**

*   **“通专融合”技术路线作为理论指导：MinerU2以“通专融合”作为核心技术路线，致力于打造面向科研任务的“革命性工具”，促进科学知识的结构化理解与重组，为解析高度复杂的科学文档提供坚实的工具支撑。**
*   **OpenDataLab平台提供生态支撑：**充分利用OpenDataLab平台汇聚的**7700+多领域PB级数据集及核心科学数据资源**，结合实验室在数据核心技术方面的持续积累，为模型训练与优化提供了丰富、高质量的专业数据与技术保障。
    

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTl2ENUU0R7ribTJ9eIjdpZayeZMbQwdUUiaWKMmHpvtLcPAlyibPGRC7CQ/640?wx_fmt=other&from=appmsg)

**从 GitHub明星到产业基石：**

**MinerU 构建AI-Ready产业生态**

MinerU项目以卓越的技术实力从开源社区脱颖而出，多次蝉联GitHub平台的Python Trending榜首，斩**获超4万星标**，领先同期Llama3的2.9万星标，充分体现了开发者生态的高度认可与广泛影响力。

在国产化适配方面，MinerU深度对接昇腾AI-910B平台，显著提升OCR处理效率——实现单页处理时间从分钟级压缩至2秒，效率提升达60倍，为国产AI技术落地提供有效保障。

MinerU目前向开发者提供了多样化的部署与使用形态，包括开源本地部署、桌面客户端/网页端、在线API接口服务以及MCP企业级服务，全面适配主流AI开发/使用平台如 Dify、CherryStudio、Sider与ModelWhale等。

目前，MinerU已深度接入上海AI实验室[『书生』科学发现平台Intern-Discovery](https://mp.weixin.qq.com/s?__biz=MzkzNzIyNDg4MQ==&mid=2247561991&idx=1&sn=3154255828066bbfba3e8b653c6e7629&scene=21#wechat_redirect)和AI地球科学家智能体系统EarthLink平台提供文档解析服务。在 Intern-Discovery中，其内置的论文元分析模块利用MinerU进行深度文档解析与信息提取，为科研人员生成高质量数据表格与分析报告，显著提升了文献处理效率。在 EarthLink中，MinerU文档解析工具则能够智能解析科学实验计划，为地球科学家提供无需编程的气候数据分析与建模能力，有效应对大数据处理难题，助力科研人员专注于科学探索。

MinerU不仅是连接大模型与垂直场景的技术桥梁，更是构建开放协同的AI产业生态的坚实基石。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWBNkx3esjVNr2VtRgpf9vl9J854m9hSAbh4WjcukTnbN9MHoB3jmwClsCibfWSZdvcQThMySdGGcw/640?wx_fmt=png&from=appmsg)

MinerU 良好的体验，丰富的生态

展望未来，MinerU 将持续以 “Tokenize Everything” 为愿景，不断突破异构数据智能解析的边界，全力推动AI-Ready数据转化进程。届时，海量异构数据中蕴含的万亿价值不仅将得到更加充分的释放，也将为通用人工智能的底层数据根基注入强劲动能。

**更多MinerU 相关信息，欢迎访问以下地址**👇

MinerU官网：

https://mineru.net/

**MinerU桌面客户端**：

https://mineru.net/client

**在线****API****申请**：

https://mineru.net/apiManage/token

**GitHub链接：**

https://github.com/opendatalab/MinerU

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&randomid=mxdr6vmu&tp=webp)

END  

  

**相关阅读：  
**

  

  

[MinerU 教程第三弹：零基础使用 n8n 调用 MinerU MCP 搭建文档处理自动化系统](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550718&idx=1&sn=4fbf1dbec848be4af80cb8fbf5ebf4dd&scene=21#wechat_redirect)

2025-06-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nWke27IPxyhdsybajr2niaAZiaaJkZhwia9bQF2Zqmy5uqqicm6nxiafibvxw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550718&idx=1&sn=4fbf1dbec848be4af80cb8fbf5ebf4dd&scene=21#wechat_redirect)

[MinerU教程第二弹丨MinerU 本地部署保姆级“喂饭”教程](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

2025-05-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUUOH1ib8viafCJ0mFGr96SWphia1CXYlB7PYcd0mOyDymiaPiboxic4YrUJMsYFiaqZ4mJWtY8VxpqumSuQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

2025-05-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2DfiaWj7tD6u36J9MUptoIn8mjrdEE46UKxxIePWjHAujAAXkRVZR4rA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[Dify、n8n、扣子、Fastgpt、Ragflow到底该怎么选？超详细指南来了【好文推荐，附MinerU实用教程】](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550805&idx=1&sn=4b73bf0c9f9cc85ab3ed4cf36a22acd9&scene=21#wechat_redirect)

2025-06-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUniaALHa5jYSxXR991CavbDvPXicgJSx3AmxRq7DY4ZRXq5RMczgD9H9fZLfgRqjkKXkrgmr3uRSibg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550805&idx=1&sn=4b73bf0c9f9cc85ab3ed4cf36a22acd9&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言