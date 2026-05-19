     ScienceMetaBench 开源：建立科学文献元数据提取的客观评测基准 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

ScienceMetaBench 开源：建立科学文献元数据提取的客观评测基准
======================================

原创 爱学习的 OpenDataLab 2026-01-23 18:32 上海

> 原文地址: [https://mp.weixin.qq.com/s/ftAj4jCy15LqffoLMDPkQw](https://mp.weixin.qq.com/s/ftAj4jCy15LqffoLMDPkQw)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：  
从科学文献 PDF 文档中提取作者、年份、摘要等元数据，构建高效索引与分析，并以此激活海量文档价值，能够直接帮助研究者、图书馆、企业及数据库平台等实现更高效的文献管理、资源数字化、AI知识库构建与数据聚合分析等。然而，面对排版复杂、元素多样的科学文献，如何客观地评估模型的元数据提取能力？

  

为此，上海人工智能实验室 OpenDataLab 团队推出了 ScienceMetaBench 科学文献元数据提取评测集，该基准旨在建立客观、统一的评估标准，助力社区衡量与比较各类前沿方法的实际性能。其开源不久，获得广泛关注，连续多日登顶 Hugging Face Trending 文档类数据集榜首。  
  

我们诚邀社区同仁使用此基准开展评测、对比与交流，共同推动科学文献智能处理技术的迭代与发展。  

  

🔗 立即体验

● 数据集地址：  

https://huggingface.co/datasets/opendatalab/ScienceMetaBench

● 评测工具代码 (Dingo)：

https://github.com/MigoXLab/dingo

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)  

评测集概览

多场景、多维度的深度覆盖

  

ScienceMetaBench 是一个专注于评估科学文献 PDF 元数据提取能力的评测集，涵盖了学术论文 (Paper)、教科书 (Textbook) 与 电子书 (Ebook) 三类典型语料 。在构建过程中，研究团队针对中英文双语环境进行了深度适配，确保元信息的提取逻辑与正文语种保持一致。

  

为了提升样本的代表性，团队结合了多数据源采样与 K-Means 图像聚类技术，力求覆盖更多元、复杂的排版样式。在标注环节，团队采用了“AI 预标注 + 人工修正”的高效模式，并参考了用于MinerU评测的OmniDocBench 权威评测基准，以确保数据质量与评测维度的专业性。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

评估体系

### 

### 

### 标准化、精细化的度量规范

  

为了确保评测结果的客观性与公平性，ScienceMetaBench 不仅提供高质量样本，更配套了一套标准化的评估逻辑。在相似度度量上，我们采用基于字符串编辑距离的算法来计算字段准确率，并在计算过程中忽略大小写差异，以力求真实反映模型的提取效能。同时，我们对数据进行了严格的规范化预处理：统一将作者与关键词的分隔符定为英文逗号，对 ISBN 进行了去符号化处理（去掉“-”连接符），并将出版时间标准化至年份（如 2016）。通过在 Qwen2.5-72B 等模型上的初步测试，我们发现不同字段（如 DOI 与 Abstract）的提取难度存在显著差异，这些精细化的反馈将为后续模型的针对性优化提供清晰的数据支撑。

  

数据格式示例（以论文类为例）：

下图展示了从学术论文 PDF 文件中提取的元数据字段示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXeBia5PrrQvpn5UgWiaBZx4lnz66zNX78bkKTq0iaCwF3j8CUrUPUbkpiaJdAt84fIMI20ibwiaZwibVAJA/640?wx_fmt=png&from=appmsg)

  

需要从论文首页提取以下关键信息：

    {

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)  

技术背景

### 

### 基于 MinerU 数据引擎的实践积累

  

ScienceMetaBench 的诞生离不开 MinerU 智能文档解析引擎的深厚积累。作为大模型时代的 AI-Ready 数据引擎，MinerU 在多模态文档解析领域准确率高达 99%，已为包括 Google Gemini 3 和 DeepSeek 在内的顶尖模型提供评测基准支撑。

  

如果您觉得这个项目对您的研究或工程有所帮助，恳请在 Hugging Face 和 GitHub 上为我们点个 **Star** 🌟！

🔗 立即体验

● 数据集地址：  

https://huggingface.co/datasets/opendatalab/ScienceMetaBench

● 评测工具代码 (Dingo)：

https://github.com/MigoXLab/dingo

  

END  

  

**相关阅读：  
**

  

  

[强强联手！MinerU携手沐曦完成适配，曦云C500推理性能加速60%](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551297&idx=1&sn=3b6a50dd0cb7570f8d26a093d8bb4e8b&scene=21#wechat_redirect)

2025-12-24

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUErF25RmMkX9p2nREV80RribvGPYw6MmAX2ibXhlcibtYRwN5PXZRib6cNCnNBRiaH16eSxgWxYsZnx0g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551297&idx=1&sn=3b6a50dd0cb7570f8d26a093d8bb4e8b&scene=21#wechat_redirect)

[OpenDataArena全面升级版正式上线，四大核心模块重构数据价值评估新格局](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551296&idx=1&sn=fbfdebef9a56864458181274309c824e&scene=21#wechat_redirect)

2025-12-23

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXmBEbaufxlnOUjXxqWfEbkU4tKoS0LwERCguzpWAvuvWZhqO0oh62AVwdDnXIxfSDchQwSM7Q89A/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551296&idx=1&sn=fbfdebef9a56864458181274309c824e&scene=21#wechat_redirect)

[打破桎梏！MinerU-HTML重构网页提取范式，开源超大规模高质量多语言语料AICC](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551242&idx=1&sn=ec6d3a0ef6b0cacbd6c020cd5bf96cc0&scene=21#wechat_redirect)

2025-11-26

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTqlCzSUPj4rBjYG74G5mX45ZMEGeERNI97ibMGOmvvKkWGMvEKtEkPhMdA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551242&idx=1&sn=ec6d3a0ef6b0cacbd6c020cd5bf96cc0&scene=21#wechat_redirect)

[MinerU又双叒更新了！化学解析×多模式翻译等多种功能上线！文档解析处理爽到飞起！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

2025-08-08

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTyWAumU6Y7sdbgsxLgByGO8XbrzT7AOhs8LlQhV1ph0m76jjMmKVkhA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言