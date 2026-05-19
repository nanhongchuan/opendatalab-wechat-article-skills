     SAM-Med2D：打破自然图像与医学图像的领域鸿沟，医疗版 SAM 开源了！ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

SAM-Med2D：打破自然图像与医学图像的领域鸿沟，医疗版 SAM 开源了！
=======================================

原创 通用医疗GMAI OpenDataLab 2023-09-07 18:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/4zO21ztwlt8kHqGqhAXMqQ](https://mp.weixin.qq.com/s/4zO21ztwlt8kHqGqhAXMqQ)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzloGjJfzBqQOKib2fqXRXRxOEibXZlu4siaABBNsCTfJQ1aOMTm8mzXT4sryCKdsELqSNHF8mzUqTecA/640?wx_fmt=png)

由于医学图像和自然图像之间存在较大差异，以及缺少大规模医学图像基准数据集，这是导致AI在医学领域进展缓慢的原因之一。构建大规模基准数据集和可靠的基线模型，能够推动AI在医疗领域的快速发展，加速医疗向更通用的方向转变。欢迎感兴趣的读者加入群聊与作者讨论！（二维码见文末）

  

**论文:** 

_https://arxiv.org/abs/2308.16184_

**开源代码（点击“阅读原文”直达）:** 

_https://github.com/OpenGVLab/SAM-Med2D_

**Gradio demo:** 

_https://openxlab.org.cn/apps/detail/litianbin/SAM-Med2D_

  

SAM-Med2D 文章和代码公开3天内，获得多家媒体报道，在推特阅读量突破十万。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibVgOSFUBXAQaB5rKUMKD3PQDWYuDDnYNxHiaUiamjnq6ocbvTy9nXzybw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibyAMNT7kBhGgE4txxc84weBDf4ibwLJibIq9b4MfqRHpEAabCibKEnjNvQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibDKHwIvCuw7BsT3lcHl8fuPmTiaTcic5fXVOhUDCuZUnAczibLicibA5ujMQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibk3ic8C0J3DicKVUZuUOulZnmjluIlP6lfnOBP8gLIBkXzuYDicxb1b4yg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibDt1n1pLkNCmOCJmCh2R9LsJU4Eq5GicqRatZJ7LazvOAy3QRaYV68MQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibDJoQWUxfXky5FnM8lmbRLdibzGSIeZJfrasBAmmPYlvT5vVBPcC8Afw/640?wx_fmt=png)

左右滑动查看媒体报道

  

  

自然图像VS医学图像

  

  

众所周知，**ImageNet**的出现极大推动了基于深度学习的人工智能的发展。它为计算机视觉领域提供了一个大规模的数据集和强大的基线模型，使得研究者们能够在**自然图像**分类、分割、检测等任务上取得了突破性的成果。**Segment Anything Model (SAM)**代表了自然图像分割领域最先进的研究进展。然而，直接将预训练的SAM应用于医学图像分割，效果并不理想。这种限制主要源于自然图像和医学图像之间存在显著的领域差异。**SAM的训练数据（图1a.上）完全来自于高清自然图像，导致其缺乏医疗领域的特定知识**。

  

**医学图像和自然图像存在显著差异，本质就是成像方式完全不同**：自然图像是以自然光为光源，通过手机、相机等设备转换为RGB格式的图像，像素值范围也是0-255之间；医学图像是通过特定的协议和扫描仪收集的，其展现方式因其特定的临床目的而各异，包括电子、激光、X射线、超声波等，成像都不是RGB图，其像素值范围从几千到几十万不等（见图1a右侧柱状图）。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibzOcRibCsJlKMhWeW1icptOMWm7NZBNFhGF0NTibyYeo2BVtSRefV9ElSw/640?wx_fmt=jpeg)图1a. 自然图像（上）与医学图像（下）对比

另外，**由于标注成本高且标注质量参差不齐，导致医学图像在不同医院和临床研究中的质量存在很大差异。**上述挑战导致医学图像和自然图像在数据量、数据质量上存在显著差异。图1b比较了公开的自然图像数据集和医学图像数据集的数据量规模差异。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibQFicOn5g1H77oywT38ibibSrVbsXwSluaAZPjnrANTRxdficIKvrDt91Mg/640?wx_fmt=jpeg)

图1b. 医学图像和自然图像数据量规模差异

基于以上问题，**医学领域缺乏大规模基准数据集和可靠的基线模型的支持。我们的目标是填补这一空白，推动AI在医疗领域的快速发展，加速医疗向更通用的方向转变。****为了实现这一目标，我们研发了SAM-Med2D****。**首先，团队收集了迄今为止最大最全的医学图像分割数据集，它由**4.6M**张图片和**19.7M** masks组成，涵盖了当前公开可用数据集中几乎所有对象类型，弥补了SAM缺乏医学领域知识的问题。在此数据基础上，作者团队全面微调了SAM：在同等分辨率时，FT-SAM在Bbox提示模式下实现了11.93％的提升；SAM-Med2D实现了17.67％的提升。在单点提示模式下，SAM-Med2D相较于SAM表现出了压倒性的优势 (18.94% vs. 70.01%)。**在单点提示模式下，SAM-Med2D表现出了压倒性的优势 (18.94% vs. 70.01%)**。

  

SAM-Med2D三大亮点

**1.最大规模的医学图像分割数据集：**作者团队收集并整理了一个庞大而全面的医学图像数据集，涵盖了多种临床分割任务和图像模态。这使得SAM-Med2D在训练过程中能够获得更准确和具有代表性的医学图像信息，弥补了 SAM 在医学领域数据不足的问题。

  

**2.更全面的微调方案：**相对于现有的医学SAM方法，作者对SAM的三个重要组成部分都进行了微调，使SAM-Med2D能够更好地适应医学图像的特殊特征和变化，提高分割结果的准确性和稳定性。图2对比了最近基于SAM的微调方法。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVWB1CibMYIa6Zcu1gHZb9vqoYRicQ8f9m9CicllqjOYic1cnys3sIibnXQXQ/640?wx_fmt=png)

图2: SAM-Med2D是一种全面的微调方法，支持对医学图像进行多种提示来生成mask

  

**3.优异的**医学图像分割**性能：**对SAM-Med2D从不同维度进行了全面的性能评估。结果表明，SAM-Med2D在各种医学图像分割任务中表现出色，在同等分辨率时，FT-SAM在Bbox提示模式下实现了11.93％的提升，而SAM-Med2D实现了17.67％的提升。在单点提示模式下，SAM-Med2D表现出了压倒性的优势 (18.94% vs. 70.01%)。

  

迄今为止最大最全

的医学图像数据集

  

  

01

**数据准备**

大模型成功的经验告诉我们，数据量对于模型的学习至关重要。通过学习更多的数据，模型可以获得更加丰富的领域知识，并更好地适应不同的应用场景。尽管SAM已经在超过1B的masks上进行了训练，但其训练集与医学领域的数据相比存在较大的差距，这也是SAM在医学领域表现不理想的原因之一。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVX2dcEiaPkQEALakKBXVwUQG0YzibHUDCGPUcxyJJeF95iccqPTSU3Qukg/640?wx_fmt=png)

图3：本研究所使用的数据集概述。(a) 总共 31 个主要器官及其相应的解剖结构，\* 表示数据集中存在病变标签。(b) 呈现了模态的分布及其在数据集中的相应比例 (以对数缩放)。(c) 按解剖结构分类的图像和masks的数量，以及包含数据集的总数

  

为此，作者团队收集整理了**迄今为止最大的医学图像分割数据集**，它由4.6M张图片和19.7M masks组成。图3(b)显示了该数据集10种不同的成像模式和对应的数据占比。根据解剖学结构和是否包含病灶将数据集分为5个大类，即Head and Neck、Thorax、Abdomen、Pelciv、Contains lesions，图3(c)显示了这些类别的图片和masks数量。我们从这些数据集中的271种标签中整理和汇总出31种主要的器官（图3 (a)），这涵盖了当前公开可用数据集中几乎所有对象类型，弥补了SAM缺乏医学领域知识的问题。此外，引入了9个MICCAI 2023数据集（包含约0.52M图片和1.31M masks）验证模型的泛化性。我们相信，通过更加全面、多样化的训练数据，SAM将更好地适应医学图像领域的复杂性和特殊性，为医疗健康领域的应用提供更加准确和可靠的技术支持。这也将为医学图像分割领域的研究和发展带来新的机遇和挑战。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVx1HnKzAsIcBwjPvCfOmSMJ4LrCTXyHH3iaPicyddZnic523GpfD7ZI9xQ/640?wx_fmt=png)

图4: SAM-Med2D概览。我们冻结图像编码器，并将可学习的适配器层合并到每个 Transformer 块中，以获取医学领域的特定领域知识。我们使用Point、Bbox 和Mask信息微调提示编码器，同时通过交互式训练更新解码器的参数

02

**从SAM到SAM-Med2D**

在这项工作中，作者对SAM进行了微调，微调后的方法称为SAM-Med2D，它可以有效地扩展到医学图像领域。如图4所示，SAM-Med2D由三个主要组件组成：image encoder、prompt encoder和mask decoder。该框架允许在不同提示下为同一图像生成不同的mask。对于**image encoder**，在微调时冻结了原始图像编码器中的所有参数，并为每个Transformer块部署了一个Adapter层。对于**prompt encoder**，考虑三种提示模式进行微调 (Point、Bbox和Mask)。与MedSAM，MSA等基于SAM的微调方法相比保留了更完整的提示功能，增强了其在医学成像领域的适用性。对于**mask decoder**，没有对其结构做任何更改，在训练期间保持每一次迭代都更新其参数。为了使模型具有歧义感知能力，每个prompt会同时预测多个mask（默认为三个）。

  

与SAM和其他交互式分割方法相同，作者模拟交互式分割的方式对SAM-Med2D进行训练。每个批次的数据需要迭代9次，在第一次迭代时等概率选择一个前景点或Bbox作为稀疏提示，前景点从GT中随机样点，Bbox为GT的最大外接矩形框，对每个坐标中进行最大值为5个像素的偏移。需要注意的是，除第一次迭代时模型同时更新Adapter层、prompt encoder和mask decoder的参数外，后续的迭代仅更新mask decoder的参数。从第二次迭代开始，将上一次迭代生成的mask和GT之间的误差区域随机选择1，3，5或9个点作为后续的稀疏提示，并将上一次迭代生成的低分辨率特征图映射到\[0,1\]的范围内作为当前迭代的密集提示。同时，在最后一次迭代和任意一次中间迭代只输入密集提示以鼓励模型从所提供的Mask中受益。

  

03

**评估SAM-Med2D**

  

进行全面的性能评估能助力科研社区更深入地理解影响算法感知医疗对象能力的因素，进而改进方法并提升其在实际应用中的效能。然而，以往的评估工作受制于数据量有限以及缺乏通用医疗图像分割方法的瓶颈，导致评估几乎都局限在小规模数据集和有限的类别上，无法充分揭示算法的优势和适用范围。为填补这一研究空白，作者全方位、多维度地对SAM-Med2D进行了评估，为未来的研究者提供交互式分割方法的基准标准。

  

在模型方面，选择了SAM作为基础模型，并从其交互方式中选择了两种直观的提示模式（Bbox和Point）对SAM-Med2D进行评估。这样的选择是因为Bbox和Points是常用的交互方式，同时可以作为简单高效的标注手段。通过评估SAM-Med2D在这两种提示模式下的性能，我们可以深入研究它们在医学图像分割任务中的优势和不足。

  

在数据方面，作者评估了SAM-Med2D在MRI、CT、超声等10种不同模态医学图像上的表现。这样的综合评估将使研究者能够了解SAM-Med2D在特定模态下的优势和挑战，并揭示其在多模态图像中的潜在应用能力。然后，考虑到不同解剖学结构和器官具有各自独特的形态、特征和变化模式，作者对SAM-Med2D在4种解剖学结构和31种主要器官上的表现进行了评估。这样的评估有助于深入了解SAM-Med2D在不同场景下的性能差异，并能够有针对性地改进方法以应对特定结构和器官的挑战。最后，作者也高度重视SAM-Med2D的泛化能力，在9个MICCAI 2023数据集上进行了测试。这些数据集代表了来自不同来源、不同机构或不同设备采集的医学图像，具有多样性。通过在这些数据集上评估SAM-Med2D，能够验证其在泛化到新数据上的能力。

  

实验结果

  

01

**定量评估**

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVryWGsYZpEo01HPQQjhFFHm3gxI3ZeIWLhS0mQ8WzLEnDmYVFOvpHvA/640?wx_fmt=png)图5: SAM、FT-SAM (仅微调decoder)和我们的SAM-Med2D在测试集上的实验结果![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVOQgb8Nff61X7fv6xCmOicOFg96gTiaty9iaWKBykUN3jamBUFqFJOAwQA/640?wx_fmt=png)图6: (a) 从解剖学结构角度比较四种方法的分割性能。(b) 从成像模式角度比较四种方法的分割性能![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVlGCDiawRUNkuHTdytasBqicmvOONKLkbYsKn6CxNtmIxAIskdg4E6jdQ/640?wx_fmt=png)图7: FT-SAM 和 SAM-Med2D 在 31 个器官中的分割性能比较![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DV8bWVkOWRRYHAP67cYtCfqmxuiaq2q4mpsicbJ6tvq8D7cosJdEel6qEg/640?wx_fmt=png)图8: 在 9 个 MICCAI2023 数据集上进行泛化验证，其中“\*”表示不加adapter层参数的 SAM-Med2D

02

**定性评估**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVBoLypz6P6YLxictoO96CL35jhQBwMWOasj8diciaOhxibPabLPHfaqKweg/640?wx_fmt=png)

图9: 定性比较SAM-Med2D和SAM。前三行描述了不同模态的分割结果，而后三行描述了不同解剖结构的分割结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrznmqsp3LIEF4wj7icq24X0DVa4AVkhl6lFSB2PhqR6n1heB6QUgHSdOIAsqXIUmzf52B232sweZziaQ/640?wx_fmt=png)图10: 单个图像多目标分割结果融合, 仅可视化 1 Point提示的结果。右边为SAM的分割结果  

总结

SAM-Med2D通过在大规模医学图像数据集上微调来适应各种医学图像场景。与预训练的SAM相比取得了令人满意的性能改进和泛化能力。在同等分辨率时，FT-SAM在Bbox提示模式下实现了11.93％的提升，而SAM-Med2D实现了17.67％的提升。在单点提示模式下，SAM-Med2D表现出了压倒性的优势 (18.94% vs. 70.01%)。

  

作者还对不同模型在解剖学结构，不同成像模式和主要器官维度进行了综合评估，SAM-Med2D在各方面优于预训练的SAM和FT-SAM。此外，在9个MICCAI 2023数据集的泛化实验证明了在大规模数据集上预训练的模型具有强大的领域可迁移性。尤其是使用点提示模式时，SAM-Med2D可以更快地生成所需的mask，甚至优于其他方法使用 Bbox 提示模式的结果。未来作者团队将继续扩大数据规模、增加提示策略使SAM-Med2D具备医疗领域的“everything”能力。同时，SAM-Med2D的代码和预训练模型将开放给社区使用，希望这项工作能让医学计算机视觉领域的研究人员受益。

  

欢迎医院、研究院、高校、公司等机构的合作，请邮件联系hejunjun@pjlab.org.cn

  

**扫描下方二维码加入SAM-Med2D社群**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzmczjxyx9JvUjGK1srS5lKibiciaoQys44EvmJhMaWiaQEEWC9OaibsoP1kBJgb2FkwWl5Ha4C1T2eFUXg/640?wx_fmt=jpeg)

  

\-END-

更多医疗影像公开数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言