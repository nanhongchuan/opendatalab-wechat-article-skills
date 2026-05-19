     MinerU-Diffusion发布：我们想重新回答，文档 OCR 到底该怎么做 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU-Diffusion发布：我们想重新回答，文档 OCR 到底该怎么做
========================================

原创 OpenDataLab 2026-03-27 21:15 上海

> 原文地址: [https://mp.weixin.qq.com/s/BitYKl0HepwugzjnitT6QQ](https://mp.weixin.qq.com/s/BitYKl0HepwugzjnitT6QQ)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

在大模型、知识库和智能文档应用快速发展的今天，OCR 已经不再只是一个“把图片里的文字识别出来”的基础工具。对科研论文、财报、专利、合同等高价值文档来说，OCR 的效果直接决定了后续信息抽取、知识建库和智能问答的质量。也正是在这一过程中，我们越来越清楚地意识到，文档 OCR 面临的核心问题，已经不只是“能不能识别”，而是“能不能以更高效率、更强稳定性和更好结构一致性，把复杂文档真正解析出来”。

  

长期以来，行业中相当一部分 OCR 系统仍沿用自回归解码范式，将文本识别建模为从左到右逐 token 生成的序列问题。这是一种成熟而常见的技术路径，但我们认为，它与文档 OCR 的任务本质并不完全一致。文档并不是天然的一维文本流，而是包含阅读顺序、页面布局、表格、公式等信息的二维视觉对象；最终输出的文本，本质上更像是对这些结构的线性化还原，而不是一次语言意义上的“创作”或“续写”。正是这种任务本质与建模方式之间的错位，使得传统路径在实际应用中逐渐暴露出推理串行、误差累积、过度依赖语言先验等问题。

  

基于这样的判断，上海人工智能实验室 OpenDataLab 团队（我们）提出了 MinerU-Diffusion——一种基于掩码扩散语言模型的OCR框架。我们希望改变的，并不是传统 OCR 流程中的某一个局部模块，而是更底层的建模思路：不再把文档 OCR 主要看作语言驱动的序列生成问题，而是将其重新定义为一种在视觉约束下逐步恢复文本结构的“逆向渲染”过程。换句话说，我们更关注模型如何依据整页文档的视觉信息，把原本已经存在于文档中的结构化文本并行恢复出来，而不是依赖固定顺序去逐步“猜测”下一个 token。

  

🧾 论文链接：  

https://arxiv.org/abs/2603.22458  

⭐ 开源仓库：

https://github.com/opendatalab/MinerU-Diffusion

🔗 开源模型：   

https://huggingface.co/opendatalab/MinerU-Diffusion-V1-0320-2.5B

 🧰在线demo： 

https://huggingface.co/spaces/opendatalab/MinerU-Diffusion-V1-0320-2.5B

  

MinerU-Diffusion 与 MinerU2.5 对复杂文档解析速度对直观对比

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15)  

当行业还在逐字生成时，我们选择从“恢复结构”出发

  

围绕这一思路，MinerU-Diffusion 采用**离散扩散解码**来替代**传统自回归解码**。与行业中更常见的串行生成方式不同，扩散解码不依赖严格的从左到右顺序，而是在多个位置上同时进行预测与修正，使文本在视觉信息和上下文约束下被逐步还原。我们认为，这种方式更符合文档 OCR 的任务特征：文档中的 token 关系主要受空间结构约束，而不完全来自语言上的因果依赖。因此，采用并行恢复的方式，不仅更自然，也更有机会同时提升效率和全局一致性。

  

这也是 MinerU-Diffusion 与行业通行做法最核心的区别。传统方法的优势在于路径成熟、工程经验丰富，但它天然受到串行解码的约束，面对长文档、复杂版式以及大规模生产场景时，速度和成本压力会更加明显；同时，在表格、公式、跨行排版等结构化内容中，一旦前序 token 预测出现偏差，错误也更容易沿生成链路逐步放大。**相比之下，我们的方法更强调直接利用整页视觉证据和全局结构信息，减少对语言先验补偿的依赖，从而在复杂结构场景下获得更稳定的表现。**

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAaCNFibiavUMOrNjMmCdaNgWln75yOjKTg7GvR861HfrgibWEH8oq7zWiblJuibZKibnO6eqwROWapznXQunCLeD0abnsiaKrFYE7s7X4/640?wx_fmt=png&from=appmsg)

图1：扩散解码在视觉条件约束下，从被掩码的标记中逐步重建结构化文本：黑色标记已确认，红色标记正在更新，黄色标记仍处于掩码状态，这实现了具有全局一致性的并行生成，与自回归的从左到右解码形成对比。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAZOC70sicIWRU5Do27eq0yz7dYeGNrQ7sbzEpXfxictXWyCMSUynu6d3a9BZXFsA0tEJzJ0ROKduO7JnGsTTQbMRkGzESdPibB2RM/640?wx_fmt=png&from=appmsg)

图2：MinerU-Diffusion的训练过程。左图：对目标标记序列进行随机掩码处理，形成部分可见的输入，模型在视觉和提示条件的约束下仅对掩码位置进行预测。右图：训练过程中使用的结构化块注意力掩码，其中标记在每个块内进行双向注意力计算，对所有先前的块进行因果注意力计算，这使得块内能够进行并行扩散优化，同时保留块间的粗略自回归结构。

###   

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)  

更快，不靠牺牲精度来换

### 从公开结果来看，这一路径带来了较为明显的实际收益。MinerU-Diffusion 的 TPS （Throughput Per Second）最高可达到 MinerU2.5 的 3.26 倍；在 99.9% 相对精度下，仍可实现 2.12 倍加速；在 98.8% 相对精度下，可实现 3.01 倍加速。2.5B 参数模型在基础配置下，相较 1.2B 自回归模型实现了 5.1 倍推理速度提升。对真实业务场景来说，这意味着我们并不是单纯为了追求速度而牺牲质量，而是在尽可能保持高精度的前提下，显著缓解了文档解析中的时延和成本压力。

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAbRFkuVbkgia2DEhWdDydCmS0AiaTcqULOyDia2xG3KFJlVPumhtRTZ6cMNToYricgyrr6JFnWxpM2Tg6r8iacJ5FWEBN5FTZtTQtfE/640?wx_fmt=png&from=appmsg)

图3：MinerU-Diffusion通过阈值控制提供了灵活的精度-吞吐量权衡。与MinerU2.5相比，它的TPS（Token Per Seconds）最高可达3.26倍，同时还提供了实用的trade-off point，例如在99.9%的相对精度下实现2.12倍的加速，以及在98.8%的相对精度下实现3.01倍的加速。

  

除了速度，稳定性同样重要。在 Semantic Shuffle 语义扰动测试中，随着扰动程度增加，基于自回归解码的模型性能下降更为明显，而 MinerU-Diffusion 整体表现更稳定。这个结果说明，我们的方法在预测时更直接依赖视觉信号，而不是主要依靠语言先验来“补全”结果。对于复杂文档解析而言，这种差异具有很强的现实意义，因为企业和科研场景真正关心的，往往不是平均条件下的表现，而是在复杂版面、异常排版和受扰动输入条件下，系统是否仍然能够保持可靠输出。

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAaicARrYbibiaLvGlQM28k2Dstawcstt872ApGsye6EiaibVQ660qalY1f6ck7rOkvz7CUa5QnUTE1qJ6mPHEiayXlCfj4Z63ytib5zZU/640?wx_fmt=png&from=appmsg)

图4：不同失真程度下的Semantic Shuffle基准测试结果。

  

为了兼顾并行恢复能力和结构一致性，我们在训练过程中还引入了结构化块注意力机制，在块内进行双向注意力计算，同时在块间保留有序约束。我们这样设计，并不是为了单纯增加模型复杂度，而是希望在提升并行效率的同时，依然维持长文本结构上的整体连贯性。因为对文档任务来说，真正有价值的从来不是孤立的字符识别能力，而是能否把页面中的层级、顺序和结构一起稳定还原出来。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)  

我们想证明的，是文档 OCR 可以有一条新路径

###   

从更大的视角看，MinerU-Diffusion 的意义并不只是一次性能优化。我们更希望它能够说明**，文档 OCR 这类任务未必必须沿着行业已经熟悉的****自回归****语言生成****路径继续演进。**对于文档解析而言，如果问题的本质是从二维视觉结构到一维文本序列的确定性映射，那么更贴近任务本质的建模方式，理应来自视觉驱动的结构恢复，而不只是语言驱动的顺序生成。我们认为，**这种重新定义，不仅有助于提升复杂版面理解、表格与公式识别、结构化信息抽取等能力，也会为 RAG 知识库构建等下游应用提供更可靠的底层支持。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAaSrxVvL0DfUwHoty94Qddeibez7SYl9LHlPd3EdlYVcibibYFZB4FnT45Y711L94XrbPn1qjP6I6gbhOjQmiaApHTDhGUyt9aWK9c/640?wx_fmt=png&from=appmsg)

图5：文档 OCR 逆渲染推理过程在不同解码方法下的概述。模型将二维文档图像映射为一维的 token 序列，并通过自回归方法和基于扩散的方法进行解码。

  

对我们而言，MinerU-Diffusion 的价值不只是“更快了一些”，而是证明了一条新的技术路径是可行的：当我们不再把 OCR 简单视为生成文本，而是把它看作恢复结构，很多长期被视为理所当然的瓶颈，就有机会被真正改写。这也是我们希望通过这项工作传递出的核心信息——在文档智能进入更深应用阶段的当下，重新理解问题本身，往往比单纯优化旧路径更重要。

  

  

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

[MinerU再次更新，网页解析功能上线！URL一键变Markdown，文档处理再无边界](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551428&idx=1&sn=1f5c63f9755ad714925fd0f9cbb87c61&scene=21#wechat_redirect)

2026-01-21

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVetPrwHQ2AaqicYicsIpeRruauBOGxvNMJVicq1g29v7FdVJuicqcQAeXBEdJZcibsiaYnxRtpUvrIJGSw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551428&idx=1&sn=1f5c63f9755ad714925fd0f9cbb87c61&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言