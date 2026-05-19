     详解Latte：全球首个开源文生视频DiT \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

详解Latte：全球首个开源文生视频DiT
=====================

原创 视频生成组 OpenDataLab 2024-04-10 18:26 上海

> 原文地址: [https://mp.weixin.qq.com/s/H6CcdRvz1bP-OkbbHqQ\_wg](https://mp.weixin.qq.com/s/H6CcdRvz1bP-OkbbHqQ_wg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

来源：机器之心

**推荐语：**

今年初，OpenAI发布了Sora，视频DiT 模型得到了大量的关注和讨论。实际在去年底，上海人工智能实验室的研究团队联合南洋理工大学等机构即开源了一款与 Sora 技术相似的自研模型Latte，它是全球首个开源文生视频 DiT。一起来看看研究团队的解读吧！

设计稳定的超大规模神经网络一直是视觉生成领域的研究重点。DiT \[1\] 的成功为图像生成的规模化提供了可能性。然而，由于视频数据的高度结构化与复杂性，如何将 DiT 扩展到视频生成领域却是一个挑战，来自**上海人工智能实验室的研究团队联合南洋理工大学等机构**通过大规模的实验回答了这个问题。

  

早在去年 11 月，该团队就已经开源了一款与 Sora 技术相似的自研模型：**Latte**。作为全球首个开源文生视频 DiT，Latte 受到了广泛关注，并且模型设计被众多开源框架所使用与参考，如 Open-Sora Plan (PKU) 和 Open-Sora (ColossalAI)。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHkt3tWWljHVLKMlK9cansnbxzY06msL0ds52ibo6tT0evERaheRx6GqsXQ/640?wx_fmt=png&from=appmsg)

**开源链接：**

__https://github.com/Vchitect/Latte__

  

**项目主页：**

_h___ttps://maxin-cn.github.io/latte\_project/__

**论文地址：**

__https://arxiv.org/pdf/2401.03048v1.pdf__

先来看下Latte的视频生成效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/KmXPKA19gWibyG4LictRXQJ3XnNtka7UEMdxxeX55ibIZCx9WWjXmSzF0xyFLnH7H0JtSm1coibuhRkKSr2zTsDs3w/640?wx_fmt=gif&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****方法介绍****

总体上，Latte 包含两个主要模块：预训练 VAE 和视频 DiT。预训练 VAE 编码器将视频逐帧从像素空间压缩到隐空间，视频 DiT 对隐式表征提取 token 并进行时空建模，最后 VAE 解码器将特征映射回像素空间生成视频。为了得到最优的视频质量，作者着重探究了 Latte 设计中两个重要内容，(1) 视频 DiT 模型整体结构设计以及 (2) 模型与训练细节的最优设计（The best practices）。

  

  

 Latte 整体模型结构设计探究

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHktpAyDoUWwArhJjbcDTwnHgNibHnia8jC6WRcOmPBic4icf5AjcNMUJgGL1g/640?wx_fmt=png&from=appmsg)

图 1. Latte 模型结构及其变体

  

作者提出了 4 种不同的 Latte 变体 (图 1)，从时空注意力机制的角度设计了两种 Transformer 模块，同时在每种模块中分别研究了两种变体（Variant）：

  

**1.单注意力机制模块**，每个模块中**只包含时间或者空间注意力**。

*   时空交错式建模 (Variant 1): 时间模块插入到各个空间模块之后。
    
*   时空顺序式建模 (Variant 2): 时间模块整体置于空间模块之后。
    

  

**2.多注意力机制模块**，每个模块中**同时包含时间与空间注意力机制 (Open-sora所参考变体)**。

*   串联式时空注意力机制 (Variant 3): 时空注意力机制串行建模。
    
*   并联式时空注意力机制 (Variant 4): 时空注意力机制并行建模并特征融合。
    

  

实验表明 （图 2），通过对 4 种模型变体设置相同的参数量，变体 4 相较于其他三种变体在 FLOPS 上有着明显的差异，因此 FVD 上也相对最高，其他 3 种变体总体性能类似，变体 1 取得了最优异的性能，作者计划未来在大规模的数据上做更加细致的讨论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHkthjZAZ1q52Iic0JibKpdldSLYpTvOibI3YLL12bv7fhLibyrI6KXcsECWPg/640?wx_fmt=png&from=appmsg)

图 2. 模型结构 FVD

  

  

 Latte 模型与训练细节的最优设计探究（The best practices）

除了模型总体结构设计，作者还探究了其他模型与训练中影响生成效果的因素。

  

**1.Token 提取**：探究了单帧 token（a）和时空 token（b）两种方式，前者只在空间层面压缩 token，后者同时压缩时空信息。实验显示**单帧 token 要优于时空 token**（图 4）。与 Sora 进行比较，作者猜测 Sora 提出的时空 token 是通过视频 VAE 进行了时间维度的预压缩，而在隐空间上与 Latte 的设计类似都只进行了单帧 token 的处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHktP4J6PLSjCqEpmbRribzbt0RP4I6zor3O7fAS290bibjUO4drZE1CFbrA/640?wx_fmt=png&from=appmsg)

图 3. Token 提取方式，(a) 单帧 token 和 (b) 时空 token

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHktF0jFeueBaLv83VHdhIjj1PjlicrUsFo9zQ3mm6JfkMcJwmB5OjzUGibw/640?wx_fmt=png&from=appmsg)

图 4. Token 提取 FVD

  

**2.条件注入模式**：探究了（a）S-AdaLN 和（b）all tokens 两种方式 (图 5)。S-AdaLN 通过 MLP 将条件信息转换为归一化中的变量注入到模型中。All token 形式将所有条件转化为统一的 token 作为模型的输入。实验证明，**S-AdaLN 的方式相较于 all token 对于获得高质量的结果更加有效**(图 6)。原因是，S-AdaLN 可以使信息被直接注入到每一个模块。而 all token 需要将条件信息从输入逐层传递到最后，存在着信息流动过程中的损失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHkt0AcTULGpnPup1wsrJ1qSLzkO3YTEyia2iaUgHu23ychnh1eKnv51O8Mw/640?wx_fmt=png&from=appmsg)

图 5. (a) S-AdaLN 和 (b) all tokens

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHkt8OkzxcibR2ibgSUgWMfqHRCYR2TJWUP2F2IbpyxEI1rrjAWPrwNmCl7g/640?wx_fmt=png&from=appmsg)

图 6. 条件注入方式 FVD

  

**3.时空位置编码**：探究了绝对位置编码与相对位置编码。**不同的位置编码对最后视频质量影响很小**(图 7)。由于生成时长较短，位置编码的不同不足以影响视频质量，对于长视频生成，这一因素需要被重新考虑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHkttY5JaNaf2HTfLN0Wm2U7uk5qkJutGnQCqotfYmuDnpLNHyChylEkpA/640?wx_fmt=png&from=appmsg)

图 7. 位置编码方式 FVD

  

**4.模型初始化**：探究使用 ImageNet 预训练参数初始化对模型性能的影响。实验表明，**使用 ImageNet 初始化的模型具有较快的收敛速度，然而，随着训练的进行，随机初始化的模型却取得了较好的结果**(图 8)。可能的原因在于 ImageNet 与训练集 FaceForensics 存在着比较大的分布差异，因此未能对模型的最终结果起到促进作用。而对于文生视频任务而言，该结论需要被重新考虑。在通用数据集的分布上，图像与视频的内容空间分布相似，使用预训练 T2I 模型对于 T2V 可以起到极大的促进作用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHktXZiaj3hlEiakJYdVIhGx69bFDuHUxhLEPkpqJ1yagKHdKRTVPfzhLpKA/640?wx_fmt=png&from=appmsg)

图 8. 初始化参数 FVD

  

**5.图像视频联合训练**：将视频与图像压缩为统一 token 进行联合训练，视频 token 负责优化全部参数，图像 token 只负责优化空间参数。**联合训练对于最终的结果有着显著的提升**(表 2 和表 3)，无论是图片 FID，还是视频 FVD，通过联合训练都得到了降低，该结果与基于 UNet 的框架 \[2\]\[3\] 是一致的。

  

**6.模型尺寸**：探究了 4 种不同的模型尺寸，S，B，L 和 XL (表 1)。**扩大视频 DiT 规模对于提高生成样本质量有着显著的帮助**(图 9)。该结论也证明了在视频扩散模型中使用 Transformer 结构对于后续 scaling up 的正确性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHktfCoIwRd0ibl9icwicEYZnWjJBBm19p0OM2BKdUNtiaXexVMZDdpCe0wyHA/640?wx_fmt=png&from=appmsg)

表 1. Latte 不同尺寸模型规模

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHktt8AFQUtibJhe3Ur4lw4QFh0cFMDUCriaZxbZiamJz4ibvgbMGKTyh1S3Hg/640?wx_fmt=png&from=appmsg)

图 9. 模型尺寸 FVD

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

********定性与定量分析********

作者分别在 4 个学术数据集：FaceForensics，TaichiHD，SkyTimelapse 以及 UCF101进行了训练。定性与定量（表 2 和表 3）结果显示 Latte 均取得了最好的性能，由此可以证明模型整体设计是具有优异性的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHkt10zqhf4UEEscocl2CISQApgGs7KTkyMO4aj888DUuxJicO3qd8GcqUA/640?wx_fmt=png&from=appmsg)

表 2. UCF101 图片质量评估

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KmXPKA19gWibDT0JGB6qEve3zWjy6pHktzqyC6wrSOe3OTy3LLmJLuOLtcRdwpsZFVRicJzMN4E9dLQtP5eLzLyw/640?wx_fmt=png&from=appmsg)

表 3. Latte 与 SoTA 视频质量评估

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

********文生视频扩展********

为了进一步证明 Latte 的通用性能，作者将 Latte 扩展到了文生视频任务，利用预训练 PixArt-alpha \[4\] 模型作为空间参数初始化，按照最优设计的原则，在经过一段时间的训练之后，Latte 已经初步具备了文生视频的能力。后续计划通过扩大规模验证 Latte 生成能力的上限。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

********讨论与总结********

Latte 作为全世界首个开源文生视频 DiT，已经取得了很有前景的结果，但由于计算资源的巨大差异，在生成清晰度，流畅度上以及时长上与 Sora 相比还具有不小的差距。团队欢迎并在积极寻求各种合作，希望通过开源的力量，打造出性能卓越的自主研发大规模通用视频生成模型。

  

  

 相关数据集资源下载

**● UCF101**

_https://opendatalab.org.cn/OpenDataLab/UCF101_

  

**● SkyTimelapse**

_https://opendatalab.org.cn/OpenDataLab/Sky-Timelapse_

  

**● FaceForensics**

_https://docs.google.com/forms/d/e/1FAIpQLSdRRR3L5zAv6tQ\_CKxmK4W96tAab\_pfBu2EKAgQbeDVhmXagg/viewform_

  

**● TaiChi**

_https://github.com/AliaksandrSiarohin/first-order-model/blob/master/data/taichi-loading/README.md_

  

_参考文献_

_\[1\] Peebles, William, and Saining Xie. "Scalable diffusion models with transformers." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023._

_\[2\] Ho, Jonathan, et al. Imagen video: High definition video generation with diffusion models. arXiv preprint arXiv:2210.02303 (2022)_

_\[3\] Wang, Yaohui, et al. "Lavie: High-quality video generation with cascaded latent diffusion models." arXiv preprint arXiv:2309.15103 (2023)._

_\[4\] Chen, Junsong, et al. "PixArt-$\\alpha $: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis." arXiv preprint arXiv:2310.00426 (2023)._

* * *

  

以上就是本次分享，多模态开源数据集，请访问OpenDataLab官网

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言