     AI Spot 第 2 期丨ACL 2024 字节专场直播，与多位研究员在线畅聊 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI Spot 第 2 期丨ACL 2024 字节专场直播，与多位研究员在线畅聊
========================================

原创 豆包大模型团队 OpenDataLab 2024-08-20 10:46 上海

> 原文地址: [https://mp.weixin.qq.com/s/sha2NRTo\_sVoEdSiSfCTWQ](https://mp.weixin.qq.com/s/sha2NRTo_sVoEdSiSfCTWQ)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5A7BypJO7OGKhibwTAatdE7BhGPsDPUUxCBecv9wDJKPWf2wEbnKYwJPtJHz05byaOYGoCf86nhnw/640?wx_fmt=png)

由 OpenDataLab 联合书生·浦语、OpenMMLab 社区共同发起，Datawhale、极市平台、稀土掘金和机器之心共同参与的 **AI** **Spot 学术分享会**即将来袭！AI Spot 聚焦 AI 领域前沿工作，邀请顶会论文一作亲临分享，交流 AI 前沿研究、审视 AI 发展趋势，共同拓展认知边界。

第二期 AI Spot 分享会将在 **8 月 20 日**晚（19:00-21:00）带来精彩的直播分享。本次作为字节合作专场，5 位来自字节豆包大模型团队的研究人员将分享在 **ACL** **2024** 上发表的最新工作，分享**内容覆盖 LLM、NLP、多模态等方向，更有 Outstanding Paper 神秘嘉宾参与分享**，欢迎大家点击下方按钮预约观看明晚的直播！

  

 **活动议程** 
==========

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5A7BypJO7OGKhibwTAatdE7nCSiaBMjkRyFpe55tAlE1rbJbo1P4mQiaichMZfsZPwGB771HkXJGCTGw/640?wx_fmt=png)

 **精选论文解读** 
============

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSbPiaLibUiaWlqR8g0UJnQPIpYA2QDn5OMoo1Tx7Y3jGpy2zhjkBiacCmKA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> **RepCodec：一种用于语音离散化的语音表示编解码器**  
> 
> 论文地址：https://arxiv.org/pdf/2309.00169

随着大型语言模型（LLMs）近期的快速发展，离散语音标记化在将语音注入 LLMs 中发挥重要作用。然而，这种离散化导致信息的丢失，从而损害整体性能。为提高这些离散语音标记的性能，我们提出了 RepCodec，这是一种用于语义语音离散化的新型语音表示编解码器。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSibUSkRfiauXFqBZtTfKVHq4ARLwXhXcJ01vGLMVyFnFiaLKgEFD4XQR2w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)Framework of RepCodec

  

与重建原始音频的音频编解码器不同，RepCodec 通过从诸如 HuBERT 或 data2vec 等语音编码器重建语音表示来学习 VQ 码本。语音编码器、编解码器编码器和VQ码本共同形成了一个将语音波形转换为语义标记的流程。大量实验表明，RepCodec 凭借其增强的信息保留能力，在语音理解和生成方面显著优于广泛使用的 k-means 聚类方法。此外，这种优势在各种语音编码器和语言中都存在，肯定了 RepCodec 的鲁棒性。该方法可以促进语音处理方面的大型语言模型研究。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSChNQSZEjUjlkfX0EMPjXsa3V89RtVLE7OPXW9sicSVK41rOoqyrFKeQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> **DINOISER：通过噪声操纵增强的扩散条件序列生成模型**
> 
> 论文地址：https://arxiv.org/pdf/2302.10025

虽然扩散模型在生成诸如图像和音频等连续信号方面取得了巨大成功，但在学习像自然语言这样的离散序列数据仍然存在困难。尽管最近一系列文本扩散模型通过将离散状态嵌入为连续状态隐空间来规避离散性这一挑战，但它们的生成质量仍然不尽人意。  

  

为了理解这一点，我们首先深入分析基于扩散模型的序列生成模型的训练过程，并确定了它们的三个严重问题：（1）学习失败；（2）缺乏可扩展性；（3）忽略条件信号。我们认为这些问题可以归结为嵌入空间中离散性未完全消除的缺陷，其中噪声的规模起决定性作用。

  

在该工作中，我们提出了 DINOISER，通过操纵噪声来增强用以序列生成的扩散模型。我们在训练阶段以一种受最优传输启发的方式，自适应地确定采样噪声规模的范围，并在推理阶段鼓励该模型通过放大噪声规模来更好地利用条件信号。实验表明，基于所提出的有效的训练和推理策略，DINOISER 在多个条件序列建模基准上优于先前扩散序列生成模型的基线，进一步的分析也验证了 DINOISER 可以更好地利用条件信号来控制其生成过程。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSBIScRHwQSQhTITyew9QFVtqVNUMIMhJdeDNKLwJ0egCGWlbYEg7wjA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> **通过减少冗余加快视觉条件语言生成的训练**
> 
> 论文地址：https://arxiv.org/pdf/2310.03291

我们推出了 EVLGen，这是一个为具有高计算需求的视觉条件语言生成模型的预训练而设计的简化框架，利用了冻结的预训练大型语言模型（LLMs）。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSxVx60pxvwTZicSOibkicbAe2icMWiaZ65ClrVbFbr6ZiaG9yKVE35KjiaK5Tw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Overview of the EVLGen

  

在视觉语言预训练（VLP）中的常规方法通常涉及一个两阶段的优化过程：一个初始的资源密集型阶段致力于通用的视觉语言表示学习，重点在于提取和整合相关的视觉特征。随后是一个后续阶段，强调视觉和语言模态之间的端到端对齐。我们新颖的单阶段、单损失框架通过在训练期间逐渐合并相似的视觉标记，绕过了计算要求很高的第一个训练阶段，同时避免了 BLIP-2 类型模型的单阶段训练所导致的模型崩溃。逐渐合并的过程有效地压缩了视觉信息，同时保留了语义丰富性，在不影响性能的情况下实现了快速收敛。

  

实验结果表明，我们的方法将视觉语言模型的训练速度提高了 5 倍，而对整体性能没有明显影响。此外，我们的模型仅使用 1/10 的数据就显著缩小与当前视觉语言模型的性能差距。最后，展示了我们的图像 - 文本模型如何通过新颖的软注意力时间，标记上下文模块无缝适应视频条件语言生成任务。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiacNdRrd43J5KZbSxodmxvS3qGicf837Xsye3Q4cpcJX6wbxssfxW9Y9FXmLq4Z4ib4EibPIN83rj73A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> **StreamVoice：用于实时零样本语音转换的可流式上下文感知语言建模**
> 
> 论文地址：https://arxiv.org/pdf/2401.11053

流式零样本语音转换（streaming zero-shot voice conversion）是指能够实时将输入语音转换成任意说话人的语音，且仅需要该说话人一句语音作为参考，且无需额外的模型更新。现有的零样本语音转换方法通常是为离线系统设计，难以满足实时语音转换应用对于流式能力的需求。近期基于语言模型（language model, LM）的方法在零样本语音生成（包括转换）上展现出卓越的性能，但是需要整句处理而局限于离线场景。  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSJp6IwqjTibtWVWhc46E5O66f3KBvJgCDqzjSx6wFcCibhklTqPDrVoCw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)The overall architecture for StreamVoice

在该工作中，我们提出 StreamVoice，一个新的基于流式 LM 的零样本语音转换模型，实现针对任意说话人和输入语音的实时转换。具体来说，为了实现流式能力，StreamVoice 使用上下文感知的完全因果 LM 以及时序无关的声学预测器，同时自回归过程中交替处理语义和声学特征消除了对完整源语音的依赖。

  

为了解决流式场景下不完整上下文所导致的性能下降，通过两种策略来增强 LM 对于未来和历史的上下文感知能力：1）教师引导的上下文预知（teacher-guided context foresight），通过教师模型来总结当下和未来准确的语义来指导模型对缺失上下文的预测；2）语义掩蔽策略，鼓励模型从先前损坏的语义输入实现声学预测，增强对于历史上下文的学习能力。实验表明，StreamVoice 具有流式转换能力，同时实现了接近非流式 VC 系统的零样本性能。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSKSe7R5eDicljSEtchGlsFHtzIbPYsxgnZOc5grzqNgvgO6phCtficEFQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> **G-DIG：致力于基于梯度的机器翻译多样化和高质量指令数据选择**
> 
> 论文地址：https://arxiv.org/pdf/2405.12915

大型语言模型（LLMs）在一般场景中展现出了非凡的能力。指令微调使它们能够在各种任务中与人类保持一致。然而，指令数据的多样性和质量仍然是指令微调的两个主要挑战。对此，我们提出了一种新颖的基于梯度的方法，为机器翻译自动选择高质量和多样化的指令微调数据。我们的关键创新在于分析单个训练示例在训练过程中如何影响模型。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSIVqCm4CJrGZhiazKV22DrlXjsxTqWpjR6fRte0yeTvgCJhwvwIFicwAQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

 Overview of G-DIG

  

具体来说，我们借助影响函数和一个小型高质量种子数据集，选择对模型产生有益影响的训练示例作为高质量示例。此外，为了增强训练数据的多样性，我们通过对它们的梯度进行聚类和重新采样，最大程度地增加它们对模型影响的多样性。在 WMT22 和 FLORES 翻译任务上的大量实验证明了我们方法的优越性，深入的分析进一步验证了其有效性和通用性。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuialuJplZsibXWPmHuicsqznTuwa47dnmBy9XViaZgw3LvcvMqhRUjFubsl2412N8iaWtNPMJQYZ1Pdd7Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> **GroundingGPT：语言增强的****多模态** **Grounding 模型**
> 
> 论文地址：https://arxiv.org/pdf/2401.06071

多模态大语言模型在不同模态的各种任务中都展示出了出色的性能。然而此前的模型主要强调捕获多模态输入的全局信息，因此这些模型缺乏有效理解输入数据中细节的能力，在需要对输入细致理解的任务中表现不佳，同时这些模型大多存在严重的幻觉问题，限制了其广泛使用。

  

为了解决这一问题，增强多模态大模型在更广泛任务中的通用性，我们提出了 GroundingGPT，一种能够实现对图片、视频、音频不同粒度理解的多模态模型。我们提出的模型除了捕获全局信息外，还擅长处理需要更精细理解的任务，例如模型能够精确定位图像中的特定区域或视频中的特定时刻。为了实现这一目标，我们设计了多样化的数据集构建流程，从而构造了一个多模态、多粒度的训练数据集。在多个公开 benchmark 上的实验证明了我们模型的通用性和有效性。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuialuJplZsibXWPmHuicsqznTu9JtE9zSB9vIOWMlvS4t3kGLLe9kO8eK1ZwtZ76nMqqT09TogtfQ6UA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> **ReFT：基于强化微调的推理**
> 
> 论文地址：https://arxiv.org/pdf/2401.08967

一种常见的增强大型语言模型（LLMs）推理能力的方法是使用思维链（CoT）标注数据进行有监督微调（SFT）。然而，这种方法并没有表现出足够强的泛化能力，因为训练仅依赖于给定的 CoT 数据。具体地，在数学问题的相关数据集中，训练数据中每个问题通常只有一条标注的推理路径。对于算法来说，如果能针对一个问题学习到多种标注的推理路径，会有更强的泛化能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/IrH3BAPESuiacNdRrd43J5KZbSxodmxvSiaLuibCAXicmSr7exuLnvvZ6NTok9KcBqjCk70fdWgc9rB38zRA2pfEAg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)  
Comparison between SFT and ReFT on the presence of CoT alternatives

为解决这个挑战，以数学问题为例，我们提出了一种简单而有效的方法，称为强化微调（Reinforced Fine-Tuning，ReFT），以增强 LLMs 推理时的泛化能力。ReFT 首先使用 SFT 对模型进行预热，然后采用在线强化学习（在该工作中具体是 PPO 算法）进行优化，即对给定的问题自动采样大量的推理路径，根据真实答案获取奖励，以进一步微调模型。

  

在 GSM8K、MathQA 和 SVAMP 数据集上的大量实验表明，ReFT 显著优于 SFT，并且通过结合多数投票和重新排序等策略，可以进一步提升模型性能。值得注意的是，这里 ReFT 仅依赖与 SFT 相同的训练问题，而不依赖于额外或增强的训练问题。这表明 ReFT 具有优越的泛化能力。

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言