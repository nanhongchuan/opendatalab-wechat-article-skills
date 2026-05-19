     CVPR 2024｜上交大 & 上海AI lab提出StoryGen: 开放式视觉故事生成 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

CVPR 2024｜上交大 & 上海AI lab提出StoryGen: 开放式视觉故事生成
=============================================

原创 CV开发者都爱看的 OpenDataLab 2024-03-15 20:16 上海

> 原文地址: [https://mp.weixin.qq.com/s/XKl6IS8vI7viUCb5Ip5ZKQ](https://mp.weixin.qq.com/s/XKl6IS8vI7viUCb5Ip5ZKQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

作者丨Whn丶nnnnn@知乎（已授权）

来源丨https://zhuanlan.zhihu.com/p/685449697

  

近年来，以扩散模型为代表的生成式AI模型能力日新月异，尤其是近期OpenAI的文本到视频的生成模型 Sora，展现出了惊人的超长上下文关注能力，实现了连贯一致的长视频生成。针对视频/图像序列生成过程中的一致性这一难题，上海交通大学与上海人工智能实验室联合团队，提出了利用AIGC技术进行故事讲述，探索了一项新颖且极富挑战性的任务——**开放式视觉故事生成**（open-ended visual storytelling）。和长视频生成任务相比，该任务可视为一项对计算资源需求更低，但同样关注一致性与连贯性的代理任务。具体来说，任务要求根据任意给定的故事情节，生成内容、角色和风格连贯的图像序列，可视为多场景复杂视频中连续关键帧的生成。

  

为此，团队提出了首个开放式视觉故事生成模型**StoryGen**。与以往泛化能力极其有限、只能针对有限角色/词汇生成的模型不同，StoryGen在训练完成后，**无需任何微调**即可泛化到训练时不可见的全新角色/故事剧本上，并生成**内容连贯**（coherent content）、**角色一致**（consistent character）的故事图像序列。除了技术上的创新，StoryGen的视觉故事生成能力也在儿童教育和文化传播领域具有巨大潜力。

  

研究论文《**Intelligent Grimm - Open-ended Visual Storytelling via Latent Diffusion Models**》已被国际知名会议_**Computer Vision and Pattern Recognition (CVPR) 2024**_ 接收。作者团队来自上海交通大学、上海人工智能实验室、美团。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFcsHLadCW8V47dhtWThVhvblSyCncNPIkD4mwEKqCOBAw7YibESd7vGkw/640?wx_fmt=png&from=appmsg)

项目主页:

_https://haoningwu3639.github.io/StoryGen\_Webpage/_  

论文链接:

_https//arxiv.org/pdf/2306.00973/_

代码模型链接：

_https://github.com/haoningwu3639/StoryGen_

数据集下载链接：

_https://opendatalab.org.cn/HaoningWu/StorySalon_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****Contributions****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFcEiaRqLIVYtHo3nh1hlovwf902Ocjm6OBeT4utsOvtIUNJAFzu9jfcibA/640?wx_fmt=png&from=appmsg)

**1.新颖模型**：我们提出了首个开放式视觉故事生成模型StoryGen，它是一种基于学习的自回归图像生成模型（learning-based auto-regressive image generation model），具有新颖的视觉语言上下文模块（visual-language context module），以扩散模型去噪过程的特征作为条件，能够在当前给定的text prompt和之前的image-caption pairs引导下生成连贯的图像；

  

**2.多样数据**：为了解决开放式视觉故事生成的数据短缺问题，我们从多个数据来源（YouTube视频和开源电子图书馆）中收集了大量文本-图像样本对序列（paired image-text sequences），并建立了一套完善的数据处理流水线，构建了一个具有多种多样人物、故事情节和风格的大规模数据集，命名为StorySalon；

  

**3.优异性能**：定量实验和人为评估彰显了我们所提出的StoryGen相较于以往的故事可视化（Story Visualization）及故事延续（Story Continuation）模型的优越性。

  

**4.解决痛点**：StoryGen一经训练，无需任何微调即可泛化到未曾见过的新角色，并生成内容连贯（coherent content）、角色一致（consistent character）的故事图像序列。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****Method****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFcl2YXxb7wyGjpTx6U8gHHgD4pcydGQphohu1UeD0IWjwBeZv4POqMkA/640?wx_fmt=png&from=appmsg)

**● 模型介绍**：我们提出的StoryGen模型基于Stable Diffusion-v1.5，使用扩散模型去噪过程中的特征（diffusion-denoising features）作为额外的上下文条件（context condition），通过并联的cross-attention层引导当前帧的生成，以自回归的形式逐步生成整个图像序列。模型的主要技术创新包括：

  

**a. 上下文条件提取**：我们为序列中已有的图像帧加噪，以其对应的文本为条件，使用StoryGen对其去噪并提取diffusion-denoising features，作为条件引导当前帧的生成过程。

**b. 条件引导的图像生成**：当前帧同时以对应的文本特征和已生成图像的diffusion-denoising features作为条件，使用视觉-文本上下文模块（Visual-Language Context Module），根据classifier-free guidance，进行多条件引导的生成。

**c. 多帧条件生成**：对于以多帧上下文作为条件的情况，我们根据与当前帧的时序距离远近，为已生成帧添加不同程度的噪声，作为天然的位置编码信息。

  

**● 模型训练**：

**a. 单帧-风格迁移**：我们首先以单帧的形式微调SDM的self-attention层，以保证模型的单帧生成能力和风格迁移；

**b. 多帧-条件生成**：随后将SDM的所有参数冻结，引入额外的上下文模块，以当前文本提示和前文的上下文信息作为条件，进行多帧形式的训练模型利用上下文条件的能力。

**● 模型推理**：在推理过程中，我们可以使用ChatGPT/GPT-4生成全新的剧本，将已有或生成的图像作为首帧，自回归地生成连续的图像序列。实验表明，我们的StoryGen能够生成与故事情节一致，且图像内容、风格、角色形象连贯的视觉故事，并且不需要任何微调或优化即可泛化到新的故事线/角色。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****Dataset****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFclh7zmxQWT43GickQZFY1PIgLRytAFY2vxD9HE3rUngHW4U9twIk3ZicA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFcBoGriaeNuBAKRbaa2EhfabTLzicUprrUib5iaazGicRkOx1XSGYrwDFLvSw/640?wx_fmt=png&from=appmsg)

**● 数据集介绍**：为了训练适合开放式视觉故事生成任务的StoryGen模型，我们构建了一个角色和类别丰富多样的大规模数据集，命名为StorySalon。

  

**a. 多样的数据源**：我们从视频（提供下载URLs）和开源电子书（遵循CC-BY 4.0许可证）中搜集了包含丰富人物、故事情节和艺术风格的视觉故事。

**b. 数据处理流水线**：我们构建了包括视觉帧提取、重复帧筛除、异常帧检测、视觉-语言对齐、视觉描述文本生成、文字检测和后处理等多个步骤的完善的数据处理流水线，将元数据处理为适合模型训练的形式。随着元数据的扩充，该流水线可以很容易地完成迁移，进而进一步扩充StorySalon数据集的规模。

  

**● 数据集优势**：相较于以往仅包含不到10个角色且词汇量和故事长度有限的数据集，我们的StorySalon数据集具有规模更大的词汇表，包含数百个类别的数千个角色，因而更适合开放式任务。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

****Experiments****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFc1bHrRY6Ikc9sOtxdef0mfeKiaspnXKLTUGtULpBbAGiclV7mic57HofyQ/640?wx_fmt=png&from=appmsg)

实验部分，我们考虑开放式视觉故事生成的两种子任务，即**故事生成**和**故事延续**，前者直接通过给定的故事线文本进行生成，后者除了文本条件外还提供序列中的第一帧作为图像条件信息。针对两种子任务，我们分别选择了合适的baseline进行比较定性和定量比较。

  

**● 评价指标**：以常用的FID、CLIP-Image score和CLIP-Text Score作为客观评价指标；

  

**● 人工评测**：考虑到上述指标不能全面地反映生成内容的质量，尤其是缺少对一致性（Consistency）的评价指标，我们还对上述模型和StoryGen进行了人工评测。

  

**a. 主观评分**：我们使用GPT-4生成了一定数量的全新故事线作为输入，使用各模型生成相应的视觉故事，由受试者从文本-图像对齐性、风格一致性、内容一致性、角色一致性和图像质量五个维度分别为结果打分；

  

**● 对比选择**：我们将不同模型生成的同一故事一同展示给受试者，从上述五个维度综合考虑，选择质量最佳的结果。

  

**● 结论**: 上表中的定量结果和下图中的定性结果有力证明了我们所提出的StoryGen能够生成高质量，内容、风格、角色一致的连贯视觉故事。更多可视化结果请参见我们的论文和附录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFcnRkIy7aDhpsgMTunDnchffjibNK5UrK1j1UWz9fuOMiaRHruLw8qtyFg/640?wx_fmt=png&from=appmsg)

**● 消融实验**：为了进一步证实我们所提出的使用扩散模型去噪特征作为条件的视觉-语言上下文模块的有效性，我们还将该模块直接插入到Stable Diffusion中，并在MS-COCO数据集上进行以参考图像为条件引导的图像生成。

  

● 定性和定量实验均表明我们所提出的上下文模块能够有效利用扩散模型去噪过程中的特征，比VAE、CLIP、BLIP features更适合保留参考图像中的细节信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFczfSW2NbvXnUqlibH2NBwE9965ibvOaP2LnyoGb967N6icH8qtNlgYpCiaA/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

****Visualization Examples****

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/gYUsOT36vfqjk11nGYRqPe6O0uvh1Q4b3zxuVfia41G75TB5Kia9k8fSey0Y2g29gO7Dre1mg509m5ia9cFoibjNkA/640?wx_fmt=gif&from=appmsg)

A story of a {white dog}. 具体文本故事线请参见我们论文的附录

  

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/gYUsOT36vfqjk11nGYRqPe6O0uvh1Q4bSicttPMkrerPCU07dJfCpN9msuQyWNp86JhdngRanbVQBJEGxQyfgNQ/640?wx_fmt=gif&from=appmsg)

A story of a {red-haired girl}. 具体文本故事线请参见我们论文的附录

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtyHJJpqJIq57a7pOL1tj9uccwf8Ahoe4CzlrjJKlmYUYDGsLxq47vpg/640?wx_fmt=png)

****Conclusion****

在这项工作中，我们探索了一个有趣且有挑战性的任务——开放式视觉故事生成，它需要生成模型能够基于给定的故事线生成讲述连贯视觉故事的图像序列。为此我们提出了基于学习的StoryGen模型，它可以根据前文的图像-文本上下文和当前文本提示作为输入，以自回归的方式生成连贯的图像序列，而不需要额外的微调。在数据方面，我们建立了完善的数据处理流水线，收集了一个名为StorySalon的大规模数据集，包括具有多种多样人物、故事情节和艺术风格的故事书。定量实验和人为评估表明，在图像质量、内容连贯性、角色一致性和视觉-语言对齐等多个维度上，我们所提出的StoryGen显著优于现有模型。

  

更多详细的技术细节可以参照我们的论文和附录，代码、模型、数据均已开源，欢迎大家交流！！！

  

* * *

  

StorySalon数据集，请访问OpenDataLab官网

扫码直达↓

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7f0Z65eialmdumDVhr9FuFcBJLGyarSQF6ic2Q6qc260pONIyVISy84mPKiazRPFLib0V8HI312Zks4A/640?wx_fmt=png&from=appmsg)

浏览器访问：

**https://opendatalab.org.cn/HaoningWu/StorySalon**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言