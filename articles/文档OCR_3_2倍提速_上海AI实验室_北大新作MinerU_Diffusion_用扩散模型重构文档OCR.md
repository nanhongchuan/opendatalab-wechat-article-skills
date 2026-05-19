     文档OCR 3.2倍提速！上海AI实验室&北大新作MinerU-Diffusion，用扩散模型重构文档OCR \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

文档OCR 3.2倍提速！上海AI实验室&北大新作MinerU-Diffusion，用扩散模型重构文档OCR
======================================================

原创 机智流 OpenDataLab 2026-03-30 15:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/QuWdkGCxAuzSG4lUCYrRXg](https://mp.weixin.qq.com/s/QuWdkGCxAuzSG4lUCYrRXg)

本文转载自：机智流

![](https://mmbiz.qpic.cn/mmbiz_jpg/sjXXsjYTibx498T3WGSAzI48kH2aBAiazWtVdSzDrzBWliaxsKJ1XKMQK4wBeia6BvuuOGDrWQ3Mhs2Rxd9m5TTyH3oEaw7f5icj6OwunPE9toIA/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)

图片由 AI 生成

在数字化浪潮中，光学字符识别（OCR）技术早已超越了简单的“看图识字”，演变为对复杂文档（如学术论文、财务报表、法律文书）进行结构化解析的核心工具。现代OCR系统需要从一张图片中，精准地提取出文本、表格、公式、版面布局乃至阅读顺序，并将其还原为机器可读、可处理的格式。

近年来，基于视觉-语言大模型（VLM）的端到端方法已成为主流，它们通常采用“视觉编码器+自回归语言解码器”的架构（如MinerU2.5和[PaddleOCR-VL](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247547596&idx=1&sn=1b07d83b66c942c16538bfd794814e93&token=1608351168&lang=zh_CN&scene=21#wechat_redirect)），将图像编码后，像人类阅读一样从左到右、逐词逐句地生成文本序列。

尽管这种自回归范式取得了显著成功，但其内在的“顺序生成”特性，正成为制约文档OCR迈向更高效率与更强鲁棒性的关键瓶颈。想象一下，解析一份长达数十页、包含复杂表格和数学公式的报告，自回归模型必须严格地一个接一个地预测token，这不仅导致推理速度与输出长度线性相关，带来难以忍受的延迟，更严重的是，一旦在生成长序列的早期出现错误，这个错误会像多米诺骨牌一样向后传递和放大。此外，这种从左到右的生成模式，无形中让模型过度依赖其从海量文本中学到的“语言先验”和“常识”来“猜测”后续内容，而非纯粹基于图像视觉证据。**当文档内容语义混乱（如经过随机打乱）或视觉质量不佳时，模型的性能便会急剧下降**。

那么，文档内容的生成，其本质真的必须是严格从左到右的吗？

近日，上海人工智能实验室与北京大学的研究团队对此提出了根本性质疑，并在论文《MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding》中给出了颠覆性的答案。他们指出，自回归的顺序生成只是将二维文档结构序列化的一种“人为约定”，而非文档内容本身的内在属性。文档OCR更应该被看作一个**“逆渲染”**问题：给定一个渲染好的文档图像（结果），去反推其背后的结构化文本序列（源头）。这个过程天然是全局的、并行的。

基于这一深刻洞见，团队提出了 **MinerU-Diffusion**——一个统一的、基于扩散模型的文档OCR解析框架。它毅然抛弃了传统的自回归解码，转而采用在视觉条件控制下的并行扩散去噪过程。这一转变带来了革命性的优势：**在保持甚至提升识别精度的同时，实现了高达3.2倍的解码加速，并显著降低了对语言先验的依赖，增强了模型的纯视觉OCR能力。**

![](https://mmbiz.qpic.cn/mmbiz_png/sjXXsjYTibx553Od69OhAq2aHIdTDf2L35jFYjWxw9gQ8ZmnnZb5mjY1HRvjE97H6xic4Dib03Yib3iaEu33FI9wrUzxGqOw9YRURxa11OHrst9I/640?wx_fmt=png&from=appmsg#imgIndex=2)

_图1：MinerU-Diffusion的解码效率对比。(a) 通过置信度阈值控制解码并行度，相比MinerU2.5实现最高3.26倍加速。(b) 在精度-效率权衡曲线上表现优异。_

*   **论文链接**：https://arxiv.org/pdf/2603.22458
    
*   **代码仓库**：https://github.com/opendatalab/MinerU-Diffusion
    
*   **模型下载**：https://huggingface.co/opendatalab/MinerU-Diffusion-V1-0320-2.5B
    
*   **PaperScope 解读**：https://www.paperscope.ai/hf/2603.22458
    

自回归之殇：效率与鲁棒性的双重瓶颈
-----------------

当前主流的文档OCR VLM模型，如MinerU2.5、PaddleOCR-VL等，其核心解码过程与ChatGPT生成对话并无二致：基于之前已生成的所有token，来预测下一个token。这种模式在创作开放性文本时是合理的，但对于文档OCR这一任务，却存在天然的错配。

首先，**效率瓶颈**显而易见。解析一个包含数千token的长文档，模型需要进行数千次顺序前向计算，无法利用现代硬件的并行计算能力，导致耗时随文档长度线性增长，难以满足实际应用中对实时性或高吞吐量的需求。

其次，也是更本质的问题，在于**任务形式的错配**。高质量的OCR本应极度依赖图像中的视觉证据来进行字符级识别。然而，自回归范式在无形中将OCR任务“包装”成了一个语言模型条件下的文本续写任务。模型在解码时，强大的语言模型先验会不自觉地“脑补”内容。当图像模糊、排版奇特或内容本身不符合常规语义时（例如，一份被随机打乱单词顺序的文档），模型更容易“相信”自己基于语言知识的猜测，而非真实的图像信号，从而导致幻觉错误和错误的累积传播。

论文中提出的“语义打乱”基准测试证实，**当语义结构被破坏时，自回归OCR系统的性能会大幅下降**，这暴露了其脆弱性根植于自回归解码固有的因果分解方式，而非仅仅是数据或训练策略的问题。

逆渲染新视角：用扩散模型重塑OCR
-----------------

上海AI实验室与北大的团队重新审视了OCR的任务本质。他们将一个文档视为一个由文本、布局标记、表格分隔符、数学运算符等组成的**统一结构化token序列**。这个序列虽然以一维形式表示，但其背后对应的是二维的文档空间结构。token之间的依赖关系主要源于空间排列、版式规则和格式约束，而非一个内在的、不可违背的因果生成顺序。

因此，他们将文档OCR重新定义为 **“视觉条件下的逆渲染”** 。这是一个贝叶斯推理问题：在给定文档图像（作为部分且可能含有噪声的证据）的条件下，推断最有可能的潜在结构化token序列。自回归解码只是对这个后验分布的一种参数化方式（强加了一个固定的因果顺序），而**扩散模型提供了另一种更自然、更结构契合的近似方法**。

扩散语言模型（如Masked Diffusion）的工作方式截然不同：它从一个完全被`[MASK]`标记覆盖的序列开始，通过多轮迭代，逐步根据视觉条件和已预测的部分内容，并行地更新所有被掩码的位置，最终还原出完整序列。这与“逆渲染”的思想完美契合——从一团混沌（全掩码）开始，在视觉蓝图的指引下，逐步、并行地恢复出整个结构。

![](https://mmbiz.qpic.cn/mmbiz_png/sjXXsjYTibx5Kib6LxK7cH0yiavOcXJ4BxzUC69ZCHc92OIECok36EgEicHq0nDyETRozZbRRb8vrpUweuic3cX91zLRkiake27IXkYyaMptiaOJ0U/640?wx_fmt=png&from=appmsg#imgIndex=3)

_图2：扩散解码过程示意图。模型在视觉条件指导下，并行地、迭代地重构结构化文本。黑色为已确认token，红色为正在更新，黄色仍被掩码。这与自回归从左到右的解码形成鲜明对比。_

更重要的是，对于OCR任务，图像内容与文本之间通常存在近乎确定性的映射关系，语义歧义有限。这使得扩散模型所依赖的“条件独立性”假设（给定输入和部分已观察序列，每个token可以被独立预测）变得非常合理，从而为**安全、高效的并行解码**奠定了理论基础。

MinerU-Diffusion的核心创新：块注意力与课程学习
-------------------------------

然而，直接将标准的全注意力扩散模型应用于长文档OCR会面临计算复杂度过高、长程位置不稳定等问题。为此，研究团队设计了精妙的MinerU-Diffusion架构。

### 1\. 块注意力扩散解码器：兼顾并行与稳定

MinerU-Diffusion没有采用计算成本高昂的全注意力机制，而是引入了**块注意力**。它将整个输出序列划分为连续的块。在块与块之间，它保留了一种粗粒度的自回归结构（即前一个块作为后一个块的条件），这为解码过程提供了结构锚点，防止了长序列对齐漂移。而在**每个块内部，则进行完全并行的扩散去噪**。这种“块间自回归，块内扩散”的混合因子化设计，在保持并行效率优势的同时，确保了生成的稳定性和结构性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sjXXsjYTibx7MV4Wh5sF8VmpCibBceZu3wMuBz7ctvPUfzWKmrf0lRnOzmg8z3EsfO4qHUTLRgmUbgzCkIXCziciciaNaiaDjoN1bglnbTgwzygRw/640?wx_fmt=jpeg&from=appmsg#imgIndex=4)

_图3：MinerU-Diffusion的训练示意图。左：目标序列被随机掩码，模型仅预测掩码位置。右：结构化块注意力掩码，允许块内双向注意力，块间因果注意力。_

### 2\. 不确定性驱动的两阶段课程学习

扩散模型的“任意顺序”建模特性使其训练比自回归模型更不稳定，对数据噪声更敏感。为此，团队提出了一套**两阶段课程学习框架**。

*   **第一阶段：多样性驱动的基础学习**。在大规模、多样化的基础数据集上进行训练，旨在建立稳健的跨领域泛化能力和视觉-语义对齐。
    
*   **第二阶段：不确定性驱动的边界细化**。在模型收敛后，通过多次随机推理，筛选出那些模型预测不一致、不确定性高的“困难样本”。这些样本往往包含拥挤的版面、模糊的边界或复杂的结构。随后，通过AI辅助人工流程对这些硬样本进行高精度标注，并以此为核心，结合一部分基础数据，对模型进行精细化微调。这个阶段显著提升了模型在挑战性案例上的边界精度和鲁棒性。
    

实验验证：更快、更准、更鲁棒
--------------

研究团队在多个权威基准上对MinerU-Diffusion进行了全面评估，包括OmniDocBench（全文档解析）、CC-OCR/OCRBench（表格识别）和UniMER-Test（公式识别）。

在OmniDocBench上，MinerU-Diffusion在完全自动（无真实布局先验）的设置下取得了极具竞争力的总体分数。当提供真实布局信息时，其性能与当前顶尖的自回归模型（如MinerU2.5、PaddleOCR-VL）并驾齐驱，证明了其强大的内容识别能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sjXXsjYTibx6HabjOkZp9RnT0x3ebOiaqsN7Na88PYOWgTg8iaMIibZ7AYmzWKwgFBkZ4G1c2jxKDhaouVShuyp8dbZygoCibBsfyFZia1G4E12vU/640?wx_fmt=png&from=appmsg#imgIndex=5)

如下图所示，通过动态置信度阈值调节解码并行度，MinerU-Diffusion在保持93%以上精度的同时，实现了**2.1倍的解码加速**；在精度超过90%时，更可达到**最高3.2倍的加速**。这彻底改变了长文档OCR解析的速度格局。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sjXXsjYTibx4icfZOjxnSttcsZQyboOpliatVhqlZxJ4oUH8uuXSXiboSqb5LYNGendx1C8e4Bou7ngbY2T1th6yCscpCibII3AyOPYxKwxllu3g/640?wx_fmt=png&from=appmsg#imgIndex=6)

在团队提出的“语义打乱”基准测试中，随着文档语义被破坏的程度加深，自回归模型的性能直线下降，而MinerU-Diffusion的性能则保持基本稳定（图4）。这强有力地证明了，MinerU-Diffusion减少了对语言先验的依赖，其识别能力更多地扎根于**对视觉信号本身的忠实解读**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sjXXsjYTibx556ruKJTB96icsA2CL6dRy8ibFzRTDk9ZyuibNP0FeLv8PicVx8LfOayDZQu4Ysq0Du9lTMUPRpM7UKSL6SYD6SeN3W0G3BNicSX1s/640?wx_fmt=png&from=appmsg#imgIndex=7)

_图4：语义打乱基准测试结果。随着语义失真程度增加，自回归解码器性能急剧下降，而扩散解码器保持稳定，显示出更强的视觉识别能力。_

未来展望与开源贡献
---------

MinerU-Diffusion的工作标志着文档OCR领域的一个重要范式转变。它挑战了“顺序生成是OCR唯一解”的固有观念，并通过严谨的论证和扎实的实验，展示了扩散并行解码在这一领域的巨大潜力——不仅是效率的提升，更是朝着更本质、更鲁棒的“视觉理解”迈出的关键一步。

这项工作由上海人工智能实验室和北京大学的研究者共同完成，相关代码和模型已在开源社区发布：

*   **论文链接**：https://arxiv.org/pdf/2603.22458
    
*   **代码仓库**：https://github.com/opendatalab/MinerU-Diffusion
    
*   **模型下载**：https://huggingface.co/opendatalab/MinerU-Diffusion-V1-0320-2.5B
    

随着扩散模型在语言和视觉领域的持续发展，我们有理由相信，像MinerU-Diffusion这样的创新框架，将推动文档智能处理技术进入一个更高效、更可靠的新时代，为数字化办公、档案管理、金融分析等众多下游应用注入强大动力。

  

  

\> 本文由 Intern-S1 等 AI 生成，机智流编辑部校对

  

\-- 完 --

[![](https://mmbiz.qpic.cn/mmbiz_jpg/sjXXsjYTibx70U7ib315kJF01Ydq3HSQPzqgu2pAT6YOwWUSZPciaYjD7YFpDpBbWQGo2n07VLRGYsCOUvOkjNgbk6Q6q2R8msMI24PllVtaMU/640?wx_fmt=jpeg&from=appmsg#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247555177&idx=2&sn=fa1d5fdbb465c3febbecd57fd5d1e19b&scene=21#wechat_redirect)

加入机智流 Pro，1 天一块钱，AI 能力指数级增长时代，不掉队。机智流 AI 团队将燃烧远超人类的智能的 AI Tokens 驱动 AI Agents 军团带来「与你有关」「对你有用」的高质量资讯/研报。

**机智流推荐阅读**：

1. [OpenClaw一个月实测经验分享（零经验小白上手指南）](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247556399&idx=1&sn=906d286791f6347d42401807cfb6e776&scene=21#wechat_redirect)‍

2. [内存带宽不再卡脖子！港科大团队推出ZipServ，无损压缩竟让LLM推理速度翻倍](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247556374&idx=1&sn=3d863c865efc654fbf5705b1d60213fe&scene=21#wechat_redirect)

3. [InCoder-32B：首个面向工业场景的代码大模型，性能超Claude](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247556309&idx=1&sn=f15013b4d5c135bf379205db393be9a5&scene=21#wechat_redirect)

4. [Vibe coding 闲谈：真的有必要写 spec 吗？聊聊两个误解](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA==&mid=2247556260&idx=1&sn=9d931ab678238a0e588c36be1054dd3b&scene=21#wechat_redirect)

关注机智流并加入 AI 技术交流群，不仅能和来自大厂名校的 AI 开发者、爱好者一起进行技术交流，同时还有[HuggingFace每日精选论文](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg2NzU4MDgzMA==&action=getalbum&album_id=3868686648833392643#wechat_redirect)与[顶会论文解读](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg2NzU4MDgzMA==&action=getalbum&album_id=3364952487610515463#wechat_redirect)、[Talk分享](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg2NzU4MDgzMA==&action=getalbum&album_id=3498375500882444291#wechat_redirect)、[通俗易懂的Agent知识与项目](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg2NzU4MDgzMA==&action=getalbum&album_id=3811420779526078464#wechat_redirect)、[前沿AI科技资讯](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg2NzU4MDgzMA==&action=getalbum&album_id=3450545909535277057#wechat_redirect)、[大模型实战教学活动](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg2NzU4MDgzMA==&action=getalbum&album_id=3574938029309542409#wechat_redirect)等。

在「机智流」公众号后台回复下方标红内容即可加入对应群聊：

*   cc | 大模型技术交流群
    
*   hf | HuggingFace 高赞论文分享群
    
*   lc｜LangChain 技术交流群  
    
*   code | AI Coding 交流群
    
*   具身 | 具身智能交流群
    
*   硬件 | AI 硬件交流群
    
*   推理 | AI 推理框架交流群
    
*   智能体 | Agent 技术交流群
    

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言