     AAAI2025 |OpenDataLab三大成果：城市环境多模态大模型评测、创新遥感图-文分析、CRaFT优化LLM拒绝机制 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AAAI2025 |OpenDataLab三大成果：城市环境多模态大模型评测、创新遥感图-文分析、CRaFT优化LLM拒绝机制
===============================================================

原创 潜心钻研的 OpenDataLab 2025-02-25 19:26 上海

> 原文地址: [https://mp.weixin.qq.com/s/YEI4TCdM2NF-oVp1bGuDJQ](https://mp.weixin.qq.com/s/YEI4TCdM2NF-oVp1bGuDJQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/58FUuNaBUjp3ENs4GNialjINjFvg1KnUks76DmetcXO7ZoL3Z0vkiczC1Dib9U3lzfr2k8ZPNibosNfCVvsoyI156A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

AAAI由国际人工智能促进协会（Association for the Advancement of Artificial Intelligence, AAAI）主办，是人工智能领域历史最悠久、内容覆盖最广的国际顶级会议之一，也是中国计算机学会（CCF）推荐的A类国际学术会议。近日，第39届AAAI公布了2025年论文录用结果，**上海人工智能实验室OpenDataLab团队在多模态大模型评测、遥感图像理解与知识提取、语言大模型安全调优领域的研究成果受到认可，共有三篇论文被会议录用。**下面是论文列表及介绍：

**No.1** 

**UrBench：多视角城市场景下大型多模态模型的综合基准测试**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVugMPJFE1kcdIxYSBYj55CCRqMiare3TxMYBPdnibsUdLRNHnvOPk5NVU82Zg78zjkpLN6Fb8gMIFw/640?wx_fmt=png&from=appmsg)

  

随着人工智能技术的飞速发展，大型多模态模型（LMMs）在多个领域展现出了卓越的能力。然而，在城市环境这一特定领域，对 LMMs 的评估仍存在不足。大多数现有的基准测试仅关注于单一视角下的区域级城市任务，无法全面评估 LMMs 在复杂城市环境中的表现。为此，上海人工智能实验室联合中山大学等多家单位，推出了 UrBench，这是一个专为评估 LMMs 在多视角城市场景中表现而设计的综合基准测试。

  

UrBench 包含了 **11.6K** 个精心策划的问题，涵盖了区域级和角色级的 **4 个任务维度**：地理定位、场景推理、场景理解和对象理解，共计 **14 种任务类型**。在构建 UrBench 时，研究者们不仅利用了现有数据集中的数据，还额外从 **11 个城市**收集了数据，并采用跨视角检测 - 匹配方法创建了新的注释。借助这些图像和注释，研究者们整合了基于 LMM、基于规则和基于人类的方法，构建了大规模、高质量的问题集。

  

对 21 个 LMMs 的评估结果显示，当前的 LMMs 在城市环境中存在诸多不足。即使是表现最佳的 GPT-4o，在大多数任务中也落后于人类，从简单的计数任务到复杂的定向、定位和对象属性识别任务，平均性能差距达 17.4%。此外，该基准测试还揭示了 LMMs 在不同城市视角下表现出不一致的行为，尤其是在理解跨视角关系方面。

**论文链接：**

_https://arxiv.org/pdf/2408.17267_

  

**UrBench数据集下载：**

_https://opendatalab.com/zhoubaichuan/UrBench_

  

**No.2** 

**VHM：适用于遥感图像分析的多功能且诚实的视觉语言模型**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVugMPJFE1kcdIxYSBYj55CxshMUKOCdjQftke6npVyoN8owaibPKCCpxtzoVF6v8At3axeqSEEqWw/640?wx_fmt=png&from=appmsg)

  

在遥感领域，视觉语言模型（VLMs）的应用研究逐渐兴起，旨在以更智能、更人性化的方式增强遥感图像分析能力。然而，现有的遥感图像 - 文本数据集和指令数据集存在一些局限性，如图像注释内容稀疏，仅关注少数突出对象及其关系，且指令数据集仅包含关于图像中真实对象的事实性问题，导致 VLMs 容易产生虚假回答。  

针对这些问题，研究者们开发了 VHM，这是一个多功能且诚实的视觉语言模型。VHM 基于一个大规模的遥感图像 - 文本数据集 VersaD 和一个包含事实性和欺骗性问题的诚实指令数据集 HnstD。VersaD 的注释内容丰富，提供了关于图像属性、对象属性和整体场景的详细信息，使 VHM 能够全面理解遥感图像并执行多样化的遥感任务。HnstD 则通过包含欺骗性问题，防止 VHM 对无意义的查询产生肯定回答，确保其诚实性。

  

在实验中，VHM 在场景分类、视觉问答和视觉定位等常见任务上显著优于多种视觉语言模型，并在建筑矢量化、多标签分类和诚实问答等未被充分探索的任务上表现出色。

  

**论文链接：**  

_https://arxiv.org/pdf/2403.20213_

  

**VHM\_VersaD数据集下载：**

_https://opendatalab.com/OpenDataLab/VHMData_  

  

**No.3** 

**拒绝感知指令调优中的确定性知识流动**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVugMPJFE1kcdIxYSBYj55CfgebOlRXeNvVuKUbiaTCBEQD8DveuH0lHsYTlKqAFxAGCWLZp30UZtg/640?wx_fmt=png&from=appmsg)

  

本文提出了一种名为 Certainty Represented Knowledge Flow for Refusal-Aware Instruction Tuning (CRaFT) 的方法，旨在解决大型语言模型（LLMs）在拒绝意识指令调整（Refusal-Aware Instruction Tuning, RAIT）过程中出现的过度拒绝问题。RAIT 通过将训练数据中未知问题的响应修改为“我不知道”，增强了LLMs的可靠性并减少了幻觉。然而，这种方法可能导致LLMs过度拒绝它们本可以正确回答的问题，即过度拒绝问题。CRaFT 通过引入响应确定性来选择性地过滤和修改数据，减少静态冲突，并通过初步排练训练来表征LLMs知识状态的变化，帮助缓解微调过程中的动态冲突。通过在开放式问答和多项选择题任务上的广泛实验，结果表明CRaFT可以提高LLMs在RAIT过程中的整体性能。此外，本文还分析了现有拒绝意识指标的不足，并引入了真实帮助分数（Truthful Helpfulness Score, THS），以平衡可靠性和帮助性，全面评估LLM性能。

  

**论文链接：**  

_https://arxiv.org/pdf/2410.06913_

  

**CRaFT数据集下载：**

_https://opendatalab.com/OpenDataLab/CRaFT_

  

\- End -

**相关阅读：**

[

新年新突破：MinerU 开源工具1.0.0 版本发布，功能升级与兼容性提升，完成昇腾技术认证

2025-01-10

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAX1cSzzcgqgekdnQgcmm4oia0TAf0icJ26kaIVvGEkqAM8wrBJGvjdDeVYkyab5eiaz9xmtBH9UkG5qQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549710&idx=1&sn=ec64c86cfe0751fc78d74db79fa85362&scene=21#wechat_redirect)

[

多语言语料库“万卷·丝路”发布，AI赋能共建“一带一路”

2025-01-09

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXk2oA4FMPVDMdcDVCU27qrcoZJcm8XvX9zEvQMy5Nico74zGOeIyvq1Doc1Zr5ly2RYm8TavQR3rg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[

小工具如何影响大模型？MinerU四个月获2万星标！OpenDataLab用户破10万

2024-12-05

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaV4aNQ1sKoNTsNwZibpiadkONfsyUmpricMMNWIf9V6QIcEf9leq6giaJ9xA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549458&idx=1&sn=296de8cace3047a9a2faebb6f61695e3&scene=21#wechat_redirect)

[

上海人工智能实验室大模型中心 | 全球招聘

2024-11-12

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXnHSa53PEJIj7ibXib1kJnduh9icBX5VGrvjCIAV1Yib3ZdXWnh8p8zC3oPibdlPH1yvMnhI9nicegxL2w/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247548246&idx=1&sn=43e054a06b4f3db074ac8d369b26b616&chksm=c124a049f653295fbaaed9541aa8d351efdade89efdb7b3431ec47b3fc28f906fb3c5c0cea3a&scene=21#wechat_redirect)

[

不是吧？这么好用的开源标注工具，竟然还有人不知道…

2024-08-22

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6jsZJmjym44k1KnuBibIibwV47VtuvqyerwKmT7UnBgAp4eL1Uqic7ulsE0NcPnlKtRNSGyGjiasYDiaw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言