     如何科学地“设计”微调数据？一次关于后训练数据价值评测平台（ODA）的完整验证 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

如何科学地“设计”微调数据？一次关于后训练数据价值评测平台（ODA）的完整验证
=======================================

原创 OpenDataLab 2026-02-03 18:48 上海

> 原文地址: [https://mp.weixin.qq.com/s/8OnHjTicCiuco9Tc9PDlPw](https://mp.weixin.qq.com/s/8OnHjTicCiuco9Tc9PDlPw)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

在大模型后训练阶段，SFT（监督微调）数据的构建至关重要。然而，长期以来，这一过程业界的通行做法往往依赖“直觉”或“试错”，即多收一点、再筛一轮、训一次模型、看下效果，然后再调整。这个过程不仅成本高昂，而且很难回答一个根本性问题——哪些数据是真的“有用”的，为什么？

  

为了摆脱“盲盒式”微调，急需建立一套科学的数据效能评估方法，用以成为数据生产的“指南针”。

  

日前，上海人工智能实验室 OpenDataLab 团队发布最新技术报告 《Closing the Data Loop: Using OpenDataArena to Engineer Superior Training Datasets》。基于 OpenDataArena 项目所提供的数据多维价值分析，团队提出了一种全新的范式：利用 [OpenDataArena](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551296&idx=1&sn=fbfdebef9a56864458181274309c824e&scene=21#wechat_redirect) (简称“ODA”) 的评测反馈，将数据集构建从“随机艺术”转变为“确定性的工程” 。

  

🧾 技术报告： 

https://arxiv.org/pdf/2601.09733

🧰 ODA-Tool 自动化工具箱：

https://github.com/OpenDataArena/OpenDataArena-Tool

🔗开源数据集（ODA-Math/Mixture）： 

https://huggingface.co/datasets/OpenDataArena

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)  

从“评测看结果”到“评测参与生产”

  

传统的 SFT 流程，本质上是一个开环系统：数据收集 → 模型训练 → 评测分析。评测往往只发生在最后，用来“看效果好不好”，却很少反向影响数据本身的构造逻辑。这也是为什么数据调优经常变成“黑盒试错”。

  

ODA 的核心设计目标，是把这条链路真正闭合起来。在这篇报告中，OpenDataLab团队将 ODA 的工作流完整跑通为一个闭环过程：评测 → 排名 → 数据工程 → 再评测。  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWuh4LLtic6jyjaYZ93fesicC0AQjjEStvPDtxD63UZhOmdJicc0douAcRhfzABQuvxI0swJiceRmBdoA/640?wx_fmt=png&from=appmsg)

  

这里的关键变化在于：评测不再只是一个分数，而是被明确用作数据筛选与配比的决策信号；排行榜不再只是模型展示，而是用于衡量不同数据源在特定能力上的真实贡献。这一步，使得数据构造第一次具备了工程意义上的“可解释性”和“可复现性”。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)  

一次平台级验证：ODA 能不能真的“指导造数据”？

  

为了避免引入额外假设，团队在实验中严格遵循一个原则来构造数据：数据构造过程尽可能只依赖 ODA 提供的评测与工具信号。

  

（一）数学推理场景：ODA-Math-460k

在数学推理任务中，我们完全通过 ODA 跑通了一条工程化的数据构造路径。

  

首先是数据源选择。不再凭经验判断“哪些数学数据集可能有用”，而是直接利用 ODA 的跨模型评测结果，对现有数学数据集进行横向比较，从中筛选出在数学能力上真实有效的数据源，将表现最佳的 20 个数学数据集快速聚合成一个包含 1140 万 样本的初始数学问题池。

  

接下来是数据筛选与压缩。ODA-Tool 提供了极其丰富的多维评估器，能够从复杂度、多样性、语义分布、奖励模型评分等多个维度对数据价值进行深度剖析。我们系统比较了不同筛选信号在数学场景下的效果，实验发现，相比传统的复杂度或启发式指标，基于模型表现的 pass-rate 信号更能反映模型的“学习前沿”，也更有利于预测训练收益。

  

在这一标准的指导下，团队剔除了模型已经熟练掌握的简单样本，同时避免引入不可解或噪声数据，最终将数据池从千万级工程化压缩到 46 万条高信息密度样本。尽管规模缩小了 25 倍，但每一条留存数据都处于模型的“黄金学习区”，具有极高的信息增量。

  

整个过程不是一次性调参，而是严格遵循 ODA 的评测 → 反馈 → 再评测的闭环完成的。

  

（二）通用混合全域场景：ODA-Mixture 的构造逻辑

在通用能力场景中，ODA 的作用更接近一个“数据调度系统”。面对海量候选数据，ODA 提供了一个关键视角：

  

用数据效率（Data Efficiency）衡量单位样本带来的模型收益。

  

基于 ODA 的总榜单，我们发现一些体量极小的数据集，比如 LIMO，在多个模型上的单位增益显著高于常规大规模数据。这类数据自然成为混合集的“锚点底座”。

  

同时，而针对锚点可能覆盖不足的能力维度，我们不再盲目扩充数据规模，而是直接通过 ODA 的子领域榜单，定位到对应能力最有效的数据来源，进行定向补充。具体来说，预算受限时，调度 “难度优先采样” 策略。利用 ODA-Tool 进行聚类后，在每个簇内优先抽取长思维链样本，通过重尾分布强行拉升模型的逻辑深度；而当目标是刷新 ODA 榜单天花板时，切换为 “多样性感知采样” 。ODA-Tool 此时的任务是确保语义空间的全覆盖，通过平衡采样消除特定分布带来的偏见 。

  

数据“加什么、不加什么、加多少”，都由评测信号直接驱动，而非经验判断。整个过程采用的“锚点+补丁”策略，思想极为简单，而且实现也非常方便，为数据构造提供了轻量化的一条路径。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)  

结果并非终点，评估驱动的闭环才是持续进化的关键

  

通过ODA 闭环工程化流程的引入，为 SFT 数据构建带来了实质性的效率飞跃。比如ODA-Math-460k 仅用不到一半的数据量，便超越了 1.2M 规模的 OpenThoughts-3，并在 AIME、HMMT 等高难度基准上取得了非常领先的结果。ODA-Mixture-100k/500k 更是在18+ 综合评测中取得了显著的优势，超过现有 SOTA 结果 5 个点以上，实现了“数据全能王”的特性。特征聚类分析显示，ODA 引导的采样策略比传统的启发式筛选拥有更均衡、更广阔的语义覆盖面 。这些结果非常好的证明了 ODA 平台能够带来的数据评估、数据构造的优势。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWuh4LLtic6jyjaYZ93fesicCVs354icD52KGnL4zAzpvmGuTad8xRnv9n2MSibpn61esAXEkBq0E7Zibw/640?wx_fmt=png&from=appmsg)

  

但这篇报告更重要的结论并不在于模型取得的具体 SOTA 结果，而在于验证了 ODA 作为一个平台，确实可以稳定地支撑引导高质量 SFT 数据的生产。这意味着，SFT 数据构造不必再完全依赖经验和反复试错；数据规模不再是唯一变量；评测可以成为数据工程中的“控制信号”。

  

写在最后

相比于发布数据本身，跑通标准化且可复用的数据工程链路才是报告所展示的研究意义所在。OpenDataLab团队希望通过 ODA 助力社区跨越“经验式收集”阶段，步入“精准化设计”时代，将 SFT 数据构建转化为一项逻辑透明、效能可控的科学工程任务。

  

🔗 资源下载：

● 技术报告： 

https://arxiv.org/pdf/2601.09733

● ODA-Tool 自动化工具箱：

https://github.com/OpenDataArena/OpenDataArena-Tool

● 开源数据集（ODA-Math/Mixture）： 

https://huggingface.co/datasets/OpenDataArena

  

  

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

[告别“炼丹玄学”：上海AI实验室推出首个大模型数据竞技场OpenDataArena](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551160&idx=1&sn=e65922d91d636610950a639a8b7201f3&scene=21#wechat_redirect)

2025-08-25

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAX4MPr4HTUGUznzZOTIt4jdXfGf5V8fyfDh0myShrn5fn1qia6pSQ7loITSlL0yXhKtAIAgmNtTm9Q/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551160&idx=1&sn=e65922d91d636610950a639a8b7201f3&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言