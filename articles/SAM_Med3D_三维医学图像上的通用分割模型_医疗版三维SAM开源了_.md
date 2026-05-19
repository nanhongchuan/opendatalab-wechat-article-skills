     SAM-Med3D：三维医学图像上的通用分割模型，医疗版三维SAM开源了！ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

SAM-Med3D：三维医学图像上的通用分割模型，医疗版三维SAM开源了！
=====================================

原创 OpenDataLab 2023-11-03 21:22 上海

> 原文地址: [https://mp.weixin.qq.com/s/KN\_VqZLG-dIhZYS-9GX3sQ](https://mp.weixin.qq.com/s/KN_VqZLG-dIhZYS-9GX3sQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**SAM-Med3D: 进一步加速数据和模型的生产与迭代**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmyL3icxtMQpteI6fFdy51ZTygLFhhzOCc2zjHpSbcolZotmQmWzUPkDg/640?wx_fmt=png)

  

医学图像和自然图像之间存在显著的差异，而且医学图像领域缺乏大规模的基准数据集，这是导致AI在医学领域进展缓慢的重要原因之一。通过构建大规模的基准数据集和可靠的基线模型，可以推动AI在医疗领域的快速发展，并加速医疗向更通用方向转变的进程。如果您对此话题感兴趣，欢迎加入群聊与作者团队一起探讨！

  

**论文：**

_https://arxiv.org/abs/2310.15161_

  

**开源代码**：

_https://github.com/uni-medical/sam-med3d_

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**二维模型很难扩展到三维，三维医学通用模型缺失**

最近提出的视觉基础模型 "Segment Anything Model"（SAM）是一种使用超过 10 亿个掩码（mask）进行训练的ViT模型，它在多个领域都展现出出色的零样本分割性能。SAM的兴起可以推动数据标注快速迭代，并为3D医学图像分析的发展提供新的机遇。然而，多项研究表明，由于医学图像知识的严重不足，将SAM直接应用于医学领域的有效性有限。解决这个问题的一种直接的方法是：将医学知识融入到SAM中。比如，MedSAM是一种典型示例，它通过使用110万个掩码（mask）对SAM的解码器（Mask Decoder）进行微调，从而使SAM能够通过边界框（Bounding Box）作为提示来更好地分割医学影像；SAM-Med2D则引入了适配器（Adapter）和约2000万个掩码（mask）对SAM进行了充分微调，从而在医学图像分割中表现出了卓越的性能。

  

然而，这些方法必须采用逐切片（slice）的方法来处理三维医学图像，也即，将三维数据从某个维度分解为二维切片，然后独立处理每个切片，最后将二维分割结果汇总为三维分割结果。这种方法忽略了切片之间的三维空间信息，因此在三维医学影像上表现不佳，这一问题可以从图1中的结果看出。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmp9ibicIQnlFP0EcMdTBM4CwibzOXDfvbDQ3OibTdhSx78Hkvl4ciax96VIA/640?wx_fmt=png)

图1：SAM 相关的模型在三维医学图像数据上的表现，SAM 和 SAM-Med2D 在空间上都出现了断层的现象，而 SAM-Med3D 在空间上具有更好的连贯性。

  

除了将SAM直接应用于三维数据，一些研究人员希望通过引入二维到三维的适配器（Adapter）来捕捉三维空间信息。如图2所示，这些方法通常在保持编码器（Image Encoder）不变的同时引入了三维适配器（Adapter），以使模型能够从三维图像中学习到三维空间信息。然而，这些方法存在两个主要限制：

  

**1\. 数据规模有限：**这些方法的模型通常只在有限的数据规模下进行训练（通常在1K到25K个mask范围内），并且只针对有限的目标类型。这限制了模型的泛化性能和适用范围。

  

**2\. 冻结的二维编码器：**现有的三维SAM-based模型一直坚守着冻结原始二维SAM编码器（Image Encoder）的设计范式，这限制了模型全面建模三维空间信息的能力，大大限制了SAM在三维医学图像处理领域的发展潜力。

  

因此，解决这些限制将需要更大规模的数据集、更广泛的目标类型，并且可能涉及新的架构设计来更好地应对三维医学图像的挑战。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmTL31UULtL6hBKUXRZCQRxuicT6Qp6gZHbOYLrvUy0Nxuqib15HkE4Qvg/640?wx_fmt=png)

图2：和现有其他方法的对比，SAM-Med3D 使用了更多的训练数据，包含更多的类别，数据具有更强的多样性，而且其模型具备完整的三维结构。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**SAM-Med3D尝试解决三维医学图像中数据、模型、评估三大问题**

_********No.1********_  

**数据层面**

首先，作者进行了三维医学图像数据集的广泛收集和标准化工作，创建了迄今为止规模最大的三维医学图像分割数据集。该数据集包含了2.1万个三维医学图像和13.1万个三维掩码（mask），共涵盖了247个不同的类别。这些数据来源于多个公开和私有的三维医学图像数据集。从图3可以清晰地看出，这一数据集的规模远远超过了现有最大的三维医学图像分割数据集，如TotalSegmentator和BraTS21，其规模扩大了10倍以上。

  

这一数据集的创建为进一步推动三维医学图像分割研究提供了丰富的资源和机会，有望帮助研究人员突破现有技术的瓶颈。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmicXlpSC17lDx8SRvVnxjhUaADvGWwiaCuh8DWsiadJdhA9fSCOt6r6mog/640?wx_fmt=png)

图3：（a）所有训练数据的类别统计词云图，共有 247 个类别。（b）不同三维医学图像数据集的图像（image）和掩码（mask）数量比较，作者收集的数据包含2.1万张三维图像和相应的13.1万个三维掩码，而 AMOS 和 TotalSegmentator 的图像数量不足2千，具有4种不同模态的 BraTS21 图像数量也不足1万。

  

_****No.2****_  

**模型层面**

作者提出了SAM-Med3D，这是一个所有参数均可学习的三维架构模型（无冻结的参数），如图3所示。此外，作者对SAM-Med3D的性能进行了全面评估。首先，作者使用了15个公共数据集来比较SAM、SAM-Med2D和SAM-Med3D。然后，他们从解剖结构、模态和类别等不同角度进行深入分析，多维度评估了这些模型在三维医学影像分割中的性能。此外，作者还验证了SAM-Med3D的迁移能力：将其编码器用作预训练模型，在多个全监督分割任务中进行了验证。

  

**综合全面的评估结果，SAM-Med3D具有以下两个主要优势：**

**a. 更高的效率**

SAM-Med3D的性能与在二维上微调的SAM相比更具竞争力，只需要更少的提示点便能达到更好的效果。与二维模型需要在每个切片上交互相比，SAM-Med3D确保了医生和专业人员可以用快得多的速度来更方便地进行图像分割，这大大提高了模型在实际医学应用中的效率。

  

**b. 广泛的分割能力**

SAM-Med3D具有广泛的分割能力，能够处理各种不同的目标和三维模态。这种多功能性凸显了SAM-Med3D在各种临床环境中的潜在适用性，显示了它在处理各种医学成像挑战方面的适应性和有效性。

  

这些优势使SAM-Med3D有望成为一个在三维医学图像分割领域实现重大进展的模型，有望为医学专业人员和研究人员提供更强大的工具来处理三维医学图像。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmMJBYuK3zxnMj4QibLla04UJ7GoLNlcXw5gic7uCmj7Ys9RibUlUQbfqkA/640?wx_fmt=png)

图4：具有完整三维结构的 SAM-Med3D。

  

**c. 评估 SAM-Med3D**  

性能评估对于深入了解算法的能力以及提高算法的有效性和适用范围至关重要。在医学影像领域，SAM相关模型的评估主要集中在二维医学图像上，如X射线或内窥镜图像，而在三维分割任务的评估方面存在明显的不足。考虑到在医学图像分析中，三维分割任务具有至关重要的作用，因此作者对SAM、SAM-Med2D（用于医学图像的最先进的微调版SAM）以及所提出的SAM-Med3D进行了全面评估，旨在为三维医学图像上的可提示分割任务设定一个基准。

  

在数据方面，如上所述，作者基于15个不同的公共数据集构建了一个具有代表性的三维医学图像验证集。该数据集涵盖了各种不同的目标和模态。这项评估将有助于我们从多个维度（包括模态、解剖结构、器官和病变）研究SAM-Med3D在三维医学图像分割任务中的性能。SAM-Med3D的评估包括以下几个关键点：

  

**● 总体性能比较和效率评估：**

作者比较了SAM、SAM-Med2D和SAM-Med3D在三维医学图像分割任务上的性能和效率，从分割准确度和速度上进行了对比。评估模拟了临床场景：采用点提示模式进行交互式分割，评估了模型在不同维度下的性能和效率。

  

**● 多维度的分析：**

除了整体性能指标外，评估还从多个维度来分析。这包括考察SAM-Med3D在不同图像模态、解剖结构、器官和病变下的性能。

**● 提示点数量和三维全局交互：**

作者考虑了二维和三维场景下不同提示点的数量以及交互方式。SAM-Med3D相对于二维方法 (SAM、SAM-Med2D) 表现出更高的可用性，同时只需要更少的提示点，因为它可以进行三维全局体积交互，而不是针对每个切片进行独立交互。

**● 迁移性评估：**

作者还测试了SAM-Med3D编码器的迁移性，验证了其在不同新的基准任务上的性能；其良好的迁移性表明，SAM-Med3D的图像编码器有望作为未来3D医学图像任务中的预训练模型。

这些评估角度提供了对模型全面的观察，有助于我们了解SAM-Med3D在三维医学图像分割任务中的性能、效率和潜力。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

******实验结果******

_****No.1****_  

**定量评估**

#### **● 总体表现**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcm0eexGTnHKGR9bEUMESvDmck5s8FXHsiadEqX3z4dMOibMouTmmz547iaw/640?wx_fmt=png)

图5：SAM-Med3D在使用更少点击次数的情况下，获得了更好的性能。N表示待分割目标包含的切片（slice）数目，通常10 ≤ N ≤ 200。T\_{inf}为N =100时所需的推理时间 (Inference time) 。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcm5yDFH2fO1Op08R6brIar3GvNh9XK3ibR66ZZVDggq9ClibmBlBunyynA/640?wx_fmt=png)

图6：从解剖结构和病变角度进行比较。A&T 表示腹部和胸部。SAM-Med3D只需10个提示点（最后一行）即可取得比SAM和SAM-Med2D更好的性能，而后两者往往需要上百个提示点。

####   

#### **● 不同模态上的比较**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmUL6FShxCWM5BsvEFkEz85KmKqwdNQw8hQ1iaZVDM64O6630gCVAeHRQ/640?wx_fmt=png)

图7：三张表格分别表示在不同模态下不同模型之间的性能比较。在不同的模态下，SAM-Med3D都表现出了极具竞争力的性能。值得注意的是，SAM和SAM-Med2D所用到的点是对应于切片的，也即points/slice；而 SAM-Med3d所用到的点是对应与体素的，也就是points/volume。这意味着，虽然横坐标轴都为1，3，5 points，但SAM-Med3D所需要的提示点远远少于SAM和SAM-Med2D（通常是它们的提示点数量的十分之一甚至百分之一）。此外，虽然SAM-Med3D并没有用到Ultrasound（US, 超声）图像进行训练（SAM-Med2D使用了该模态进行训练），它仍能取得和SAM-Med2D相当的性能。

####   

#### **● 主要器官和病灶上的比较**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmGXXhAgO4JpEBEQK2HHFViclGdlROVxPric32CIibfOuUWZ9omzk2XRg2A/640?wx_fmt=jpeg)

图8：SAM-Med3D与性能最好的二维微调SAM模型SAM-Med2D在34个主要器官和5种病变上的Dice系数比较。∗和∗∗分别代表可见病灶和未见病灶。

  

#### **●** **迁移性评估**

作者将SAM-Med3D预训练的ViT图像编码器迁移到UNETR中进行使用，发现能够获得效果上的提升，证明了作者提出的SAM-Med3D具有迁移能力，这将能够对三维医学图像领域的发展提供帮助。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcm7NbNg7243c5LWEJt0fn5cTowovgRBdmDFiapQiatia58cM5QOpIpdYibKQ/640?wx_fmt=png)

图9：全监督三维医学图像分割的可迁移性评估。作者利用SAM-Med3D的编码器作为预训练模型，在下游选择UNETR进行微调以评估预训练是否有效。

  

_****No.2****_  

**定性评估**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcmdibvXp2Xn3Q0icoFlzFTAZ17bYGmDNI0ruRJnib0eiaaBJLLVFfxNdwJzQ/640?wx_fmt=png)

图10：在不同的解剖结构中，针对不同数量的点，对SAM、SAM-Med2D和SAM-Med3D进行可视化。作者同时展示了轴切片和冠状切片/矢状切片来全面说明三维结果。其中“Abd&Tho”表示腹部和胸部。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5hfkJh0FiaB55xKbFTkagcm3XU2O0yFQaK8hrpEcrlM9edHXRbEhzY89lcN5e2q8QWI0zqY2w7RicQ/640?wx_fmt=png)

图11：在各种模式下，针对不同的点数，对SAM、SAM-Med2D和SAM-Med3D进行可视化。作者同时展示了轴切片和冠状/矢状切片来全面说明三维结果。

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

**总结**

在这项研究中，作者提出了SAM-Med3D，这是一种专门用于3D体素医学图像分割的三维SAM模型。SAM-Med3D在大规模的三维医学图像数据集上从头训练，其在不同组件中都采用了三维位置编码，直接整合三维空间信息，这使得它在体素医学图像分割任务中表现出卓越的性能。具体而言，**SAM-Med3D在提供仅一个提示点的情况下，相较于SAM在每个切片上提供一个提示点来说，性能提高了32.90%**。这表明它能够在更少的提示点的情况下，在体素医学图像分割任务中取得更好的结果，这证明了它出色的可用性。

  

此外，作者还从多个角度广泛评估了SAM-Med3D的能力。对于不同的解剖结构，如骨骼、心脏和肌肉，在提供有限提示点的情况下，SAM-Med3D明显优于其他方法。在不同的图像模态下，特别是核磁共振图像，通常需要比CT图像更多的提示点才能达到相同的性能，但SAM-Med3D在各种模态（包括核磁共振图像）、器官和病变下始终表现出色。此外，SAM-Med3D的可迁移性也在不同的基准任务上经过了验证，该模型表现出了很强的潜力，因此SAM-Med3D有望成为一种强大的三维医学图像Transformer的预训练模型。

  

需要强调的是，不仅仅在数值结果方面，在可视化的结果中，SAM-Med3D模型也表现出了更好的切片间的一致性和可用性。然而，三维模型在体积图像中的提示点变得更加稀疏，这增加了训练的难度。因此，如何更好地训练三维SAM仍然是需要进一步探索的领域，但这项研究为这一领域的未来发展提供了有力的方向和工具。

\-END-

**更多医疗开源数据集，欢迎访问OpenDataLab官网查看与下载：**

**扫码直达↓**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言