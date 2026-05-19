     4B模型如何逆袭30B？开源MMFinReason框架：用高质量合成数据，实现多模态推理能力越级提升 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

4B模型如何逆袭30B？开源MMFinReason框架：用高质量合成数据，实现多模态推理能力越级提升
==================================================

原创 OpenDataLab 2026-02-27 17:04 上海

> 原文地址: [https://mp.weixin.qq.com/s/IYtyAIFPwxYAIozqf5eBxQ](https://mp.weixin.qq.com/s/IYtyAIFPwxYAIozqf5eBxQ)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

文章首发于：机器之心

长期以来，开源多模态模型在复杂推理任务上，始终与 GPT-4o、Gemini 等顶尖闭源模型存在一道难以逾越的鸿沟。

  

社区开发者们逐渐意识到，核心痛点或许不在于模型架构的精进或者模型参数的规模。真正的瓶颈，在于高质量、思维链（CoT）密集的推理数据极度匮乏。

  

在纯文本领域，DeepSeek-R1 的成功已验证了高质量后训练数据（Post-training Data）的威力，但在多模态领域，我们面对的是横亘在眼前的「两座大山」：

  

1.  数据失衡：现有开源多模态数据仍以简单 VQA 与自然图像为主，而对于真正具有高推理价值的数据，如 STEM 图表、逻辑谜题、复杂视觉符号等数据不仅少，而且标注成本极高。
    
2.  推理质量参差不齐：即便现有的「推理数据」也存在推理过程短、模版化，标注粒度不足、缺乏中间验证、视觉与逻辑推理割裂的问题。
    

  

为了填补这一空白，上海 AI 实验室 OpenDataLab 研究团队正式开源了 MMFineReason 框架。这既是一套全流程 100% 基于开源生态、可复现的多模态推理数据合成 Pipeline，同时也开源了由此方法构建的包含 1.8M 高质量样本、5.1B Token 的大规模数据集。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqHaSNtibjCPE6tq7yne1rMPNTATGcRRq3csvsGPSwy8iafCOOxo5UTsMoF7vOEGuYnjw8Z9eO1duAfZ9nz5R9eoTQZnYtmlPXOps/640?wx_fmt=png&from=appmsg#imgIndex=1)

*   论文标题：MMFineReason: Closing the Multimodal Reasoning Gap via Open Data-Centric Methods
    
*   Huggingface 论文：https://huggingface.co/papers/2601.21821
    
*   项目主页：https://mmfinereason.github.io/
    
*   数据集 & 模型：https://huggingface.co/collections/OpenDataArena/mmfinereason
    

  

小模型，大性能：高效数据选择的强大优势

  

先来秀一秀性能结果。团队很惊喜的发现，MMFineReason 的出现，标志着多模态模型进入了「以小博大」的新阶段。

  

实验数据显示，MMFineReason-4B 模型基于 Qwen3-VL-4B 训练而成，其推理能力不仅超越了 Qwen3-VL-8B-Thinking，性能更是直逼 30B 参数规模的 Qwen3-VL-30B-A3B-Thinking。

  

更令研究团队惊喜的是，同样基于同尺寸底座训练的 MMFineReason-8B，表现更加优秀：它直接击败了 Qwen3-VL-30B-A3B-Thinking 和 Gemini-2.5-Flash，并开始向 GPT5-mini-High 及 Qwen3-VL-32B-Thinking 等顶级模型发起冲击。

  

值得强调的是，这种「跨级碾压」的性能跃迁并非来自新的模型结构设计，也不是通过更复杂的训练技巧实现的，而几乎完全源于数据层面的变化 —— 尤其是推理数据的结构化程度与单位样本中的有效推理密度。

  

更进一步，团队还发现通过难度感知过滤，能实现极高的数据转换效率：仅使用总量 7%（约 123K）的高难度精选子集数据，即可媲美全量 1.8M 数据相当的性能表现。

  

因此，当数据被有效筛选、难度与模型能力精确对齐时，数据选择本身就成为决定参数效率的核心杠杆。

  

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHqM3XHmPMwQXk4JYE1YItEDdj3tIbmJ54N2OfRxttxVtz4eaq6V8LaD89K38Y9icTBmNZwXZEFlW7nJqkd14LeqeFice3tmuhSc/640?wx_fmt=png&from=appmsg#imgIndex=2)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqG9ExXO8mQWSDkkzRhOYiaWaFvrQToR9YsY68rkBdnrYXNqI7BYPth7HLzPWBpgtTu8dNHBSicyokX3saWdY412B6VxrMkAbK4Eg/640?wx_fmt=png&from=appmsg#imgIndex=3)

揭秘「Closed-Source Level」数据管线：完全开源的数据生产线

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqEopL4QgYGUFq1P1e8iatujJpoSpSY9T1ETuLUv1VN451qIQj8VialibUyOjKiaDrNHOhGkVJI5UoEsFm8wJs6bumibtuyvp50iabLao/640?wx_fmt=png&from=appmsg#imgIndex=4)

不同于依赖黑盒 API 的传统方案，MMFineReason 构建了一套完全开源的透明且高效的 Pipeline，全流程 100% 基于开源模型。整个流程主要通过三个阶段来实现高质量数据的生产：

  

1.  数据标准化：首先从源头定义「什么是可推理任务」，对 STEM、Puzzle、图、几何、科学表等多领域数据进行标准化处理并统一 Schema，并进行严格的清洗。
    
2.  推理蒸馏：利用 Qwen3-VL-235B-Thinking 作为老师模型进行推理蒸馏，并严格遵守四阶段推理框架：「视觉感知 → 逻辑推导 → 中间验证 → 结论确认」，从而来生成详细且具备「视觉落地」能力的 CoT 推理轨迹。
    
3.  双重过滤：为了确保训练的高效性，团队引入了双层筛选机制，第一是正确性过滤，确保答案与推理过程严格一致；在剔除低质量 CoT 的基础上，进行难度感知（Difficulty-Aware）过滤，专门筛选出对 Qwen3-VL-4B 小模型具有高「训练价值」的样本，即「小模型稳定失败」的样本，从而避免了无效数据的堆砌。
    

  

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGibCcnAqwUlRVdegUslNpEC8Qn6MGKfibiaxftjlfjIm5a0zMSrw77dWDUVPDIaVTmVSJfANLBx3OGvEya8ibl5gn7hqXEuAyX4Rs/640?wx_fmt=png&from=appmsg#imgIndex=5)

最终，研究团队得到了 MMFineReason-1.8M（正确全量）， MMFineReason-586K（正确且去掉过于简单样本），以及 MMFineReason-123K（正确且最困难样本）三个高质量数据集。

  

MMFineReason-1.8M：专为「深度推理」打造的高质量多模态数据

  

与其说 MMFineReason 是一个常规的 VQA 数据集，倒不如将其定义为一个专为多模态大模型准备的「硬核思维训练场」。在当前多模态领域普遍陷入「数据饥渴」与「思维链断层」的背景下，该项目展现出了极具辨识度的核心特征。

  

首先，MMFineReason 在思维深度上实现了质的飞跃。相比 HoneyBee 等同类数据集，其平均思维链（CoT）长度达到了惊人的 2,910 tokens，规模足足是前者的 2.7 倍。这种长路径推理数据的引入，本质上是让模型告别了简单的「直觉判断」，转而掌握一套详尽且具象的「视觉 - 逻辑」推导范式。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqH0yF646qEZbPxsklfOXPsdOiawmbTvD6tVSWGSDYtwxfeZZDL55v3vQVmdicroPYbCvsnJ9UK1ETYBt35IVInHdSibK6TOaXxU90/640?wx_fmt=png&from=appmsg#imgIndex=6)

在领域分布上，研究团队展现出了鲜明的去平庸化导向，坚决拒绝易于「刷分」的简单样本，转而深耕高难度逻辑腹地。

  

数据集中，数学领域以 79.4% 的绝对占比强化了符号推理根基，涵盖了几何、微积分等深度学科；13.8% 的科学数据则聚焦于复杂的物理、化学图表分析；此外，数据集还引入了 4.6% 的谜题与游戏数据，通过抽象模式识别与策略博弈，不断试探并挑战开源模型的智商上限。

  

![](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGo5K2yZxEucsEuMsGf7u91ibzJAdic22Aic7Siclia6UYq0PwAgwPAicA2ianSOobbHetjho4hJjwIibOOrL2WiaEVPeMJUOdG8jhOWiatM/640?wx_fmt=png&from=appmsg#imgIndex=7)

图为 MMFineReason 数据集的数据分布情况。可以看到数据集的领域覆盖了数学、谜题与游戏、几何 / 微积分、图表与复杂科学等。

  

更具深远意义的洞察在于这种高强度训练带来的「协同提升效应」。实验结果打破了专项训练会削弱通用能力的固有认知：当模型在 STEM 和逻辑难题上进行深度钻研时，其在一般性 VQA 任务上的表现反而得到了同步增强。这种以点带面的能力释放，再次印证了高质量逻辑链条才是驱动模型性能跨级演进的真逻辑。

  

结语与展望

  

MMFineReason 的开源，证明了在多模态领域，当模型架构逐渐收敛、参数规模的边际收益不断下降，决定能力差距的，不再是模型有多大，而是「数据是否真的教会模型如何推理」。通过精细化的数据工程，小参数模型完全有潜力在复杂推理任务上对抗甚至超越大参数模型。

  

这不是一次规模的胜利，而是 Data-Centric 方法论的胜利。我们期待未来在多模态开源大模型的路上，能用更高效、更高价值的数据来促进社区的进步。

  

目前，该项目已在 Huggingface 及 GitHub 全面上线，为开源社区提供了从数据到工具链的完整支撑。

  

🔗 开源地址

📄 论文：**MMFineReason: Closing the Multimodal Reasoning Gap via Open Data-Centric Methods**

🌐 项目主页：

https://mmfinereason.github.io/

  

🤗 数据 & 模型：

https://huggingface.co/collections/OpenDataArena/mmfinereason

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END  

  

**相关阅读：  
**

  

  

[总激励200万！2026 MinerU数据智能与前沿语料挑战赛正式启幕，筑基 AGI4S 高质量语料新高地！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

2026-02-06

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbgD2vP9QPR0XKXLQTSUt6ledgMJyDU6v5WQXrCSpFS4CHCKTChAANic5J0mG9aDyYJZ1icuQ3BflZELSOUP8HDyy1iasz49ianpYo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

[MinerU-RAG 开发者指南——利用 MinerU API 找回文档“灵魂”，开启高保真 RAG 好思路](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551579&idx=1&sn=8eac203a03ea31f4e115c55bb92f0432&scene=21#wechat_redirect)

2026-02-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAYIw6gt8Km6PiajPs6R3oC9HUGxp3OiaLrsqp7PSxLerRcluzcVh9ibK4jsnK5XfTO1q5V2QdhXNzUOmKd0GWQebCFNT2zXLHIDvE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551579&idx=1&sn=8eac203a03ea31f4e115c55bb92f0432&scene=21#wechat_redirect)

[领跑 AI-Ready 数据赛道：MinerU 全面深度适配主流国产算力，持续扩容生态版图](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551531&idx=1&sn=6d13d9fd5561fba5ae62a2af83d3ff1f&scene=21#wechat_redirect)

2026-02-10

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbAiatjCgctictxTmgAoyqBaE1ZiatJLib065zr3icTFKOweUUqUdobmvWu8s7NKeE4l2ZMU7wPbKycoVT4icDRB4TkNWEH3SEJAAPO8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551531&idx=1&sn=6d13d9fd5561fba5ae62a2af83d3ff1f&scene=21#wechat_redirect)

[如何科学地“设计”微调数据？一次关于后训练数据价值评测平台（ODA）的完整验证](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551483&idx=1&sn=c48e3effbf638e1da18662d7f7f69652&scene=21#wechat_redirect)

2026-02-03

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVjrL9P0GcVnPInOFfib5Q5Oag4Eosr3eWLWtUtyH04iamTT5D3musGQL2KgJBZ2Pe7Is0yclGuPNvw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551483&idx=1&sn=c48e3effbf638e1da18662d7f7f69652&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言