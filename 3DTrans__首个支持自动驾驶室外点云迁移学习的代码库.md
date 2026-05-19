     3DTrans: 首个支持自动驾驶室外点云迁移学习的代码库 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

3DTrans: 首个支持自动驾驶室外点云迁移学习的代码库
=============================

原创 ZB OpenDataLab 2023-03-22 15:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/FaZqIswVTn328UDpsZr9wQ](https://mp.weixin.qq.com/s/FaZqIswVTn328UDpsZr9wQ)

作者丨上海人工智能实验室智能交通平台组（ADLab）

  

本文将为大家介绍上海人工智能实验室交通平台组ADLab的3DTrans代码库--首个自动驾驶室外3D点云迁移学习的代码库。此外3DTrans代码库还是Uni3D（CVPR-2023）和Bi3D（CVPR-2023）的官方实现代码库。

**Code Link:** 

https://github.com/PJLab-ADG/3DTrans

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

******3DTrans--首个支持多种迁移学习任务的3D室外点云代码库******

_********_********.********_1.1********__********.********_

**3DTrans可以做什么？**

**快速目标域自适应****：**

3DTrans可以仅使用无标注数据来提高3D感知模型对unseen domains的适应性。例如，3DTrans代码库支持ST3D\[1\]等多个无监督领域适配（UDA）方法。此外，3DTrans开发了许多新的UDA技术来解决不同类型的域偏移（如激光雷达引起的域差异以及物体大小引起的域差异），其中包括Post-SN、Pre-SN和Range-map Down-sampling/retraining操作。

  

**低成本目标域适应****：**

3DTrans可以从unseen domains中选择出信息量最大的子集样本，并以最小的成本为其进行标注。例如，3DTrans开发了**Bi3D**，它选择部分但重要的目标数据并以最小的成本对其进行人工标注，在高性能和低标注成本之间实现了良好的平衡。此外，3DTrans已经将几种典型的迁移学习技术集成到3D目标检测框架中。例如，3DTrans集成了TQS\[2\]、CLUE\[3\]、SN\[4\]、ST3D\[1\]、伪标注\[1\]、SESS\[5\]和Mean Teacher\[6\]等方法，以支持自动驾驶相关的模型跨传感器、跨场景的迁移。

  

**多数据集的联合训练****：**

3DTrans可以执行多数据集的3D目标检测任务。例如，3DTrans首次研发了多数据集3D目标检测框架--**Uni3D**，使当前的3D基线模型能够有效地从多个公开3D数据集中进行学习，提高了不同自动驾驶厂商、传感器、不同地点数据之间的复用性。

  

**多数据集支持****：**

3DTrans为Waymo、nuScenes、ONCE、Lyft和KITTI等多个公开数据集提供了统一的数据加载接口和数据增强方式，有利于研究跨数据集的3D感知任务。此外，为了消除3D室外点云数据的域差异，并获得可泛化的表示，3DTrans集成了一些经典的无标注预训练技术，来为目前3D基线检测模型提供更好的参数初始化。例如，我们集成了PointContrast\[7\]和SESS\[5\]来支持基于室外点云的预训练任务。

  

**多模型的可扩展性****：**

3DTrans可以快速完成新基线检测模型的UDA、ADA、SSDA、MDF等任务的支持。在不对代码和新基线检测模型结构进行重大更改的情况下，通过使用3DTrans，单数据集3D基线检测模型可以成功地迁移到带有域差异的新领域。

  

![](https://mmbiz.qpic.cn/mmbiz_png/yqIXRx1XSxWksOXvsQJahiclRWnCiaeiabnQk9woxicIo6xoVPfG7pP8e2CAtPu2NiaBaUvM0ugdNb8rNWbPs8XmWFw/640?wx_fmt=png)

3DTrans代码库不同模块输入输出关系图

  

  

_****_********.********_1.2_********.********_****_

**3DTrans的每个模块介绍**

3DTrans是一个轻量级、简单、自包含的开源代码库，用于探索面向自动驾驶的迁移学习技术，目前主要由四个功能组成：

1) Unsupervised Domain Adaptation (**UDA**) for 3D Point Clouds

2) Active Domain Adaptation (**ADA**) for 3D Point Clouds

3) Semi-Supervised Domain Adaptation (**SSDA**) for 3D Point Clouds

4) Multi-dateset Domain Fusion (**MDF**) for 3D Point Clouds

接下来，给大家详细介绍一下每个模块：

  

1.2.1  3DTrans@UDA

  

**● 入口链接：**

https://github.com/PJLab-ADG/3DTrans/blob/master/docs/GETTING\_STARTED\_UDA.md

  

**● 3DTrans代码库UDA基线算法的构建：**

  

3DTrans是面向自动驾驶场景迁移学习的代码库，最常见的迁移学习任务是UDA任务。其假设：模型可以接触到全量带标注的源域数据和全量无标注的目标域数据。3DTrans支持了ST3D\[1\]等最新的UDA 3D方法。同样，我们针对在3D自动驾驶场景下常见的两种领域差异，即LiDAR-beam variation和Object-size change，给出了LiDAR down-sampling retraining和Post/Pre-SN实现，来针对特定域差异来迁移3D感知模型。

\*详情见：https://github.com/PJLab-ADG/3DTrans/blob/master/docs/GETTING\_STARTED\_UDA.md

  

**● 3DTrans@UDA实验结果**

Waymo->KITTI：

![](https://mmbiz.qpic.cn/mmbiz_png/yqIXRx1XSxWksOXvsQJahiclRWnCiaeiabn0SKkUTAMUPNqibicCT0nnH2ichfp62dlLDFsBicj3M5vZnIrhPWxONribew/640?wx_fmt=png)

  

1.2.2  3DTrans@ADA

**● 入口链接：**

https://github.com/PJLab-ADG/3DTrans/blob/master/docs/GETTING\_STARTED\_ADA.md

**● 3DTrans代码库ADA基线算法的构建：**

  

3DTrans代码库**首次**支持了多种经典的ADA算法，包括TQS\[2\]，CLUE\[3\]以及我们的Bi3D，同时，利用TQS中的代码，可以轻易地实现query-by-committee、query-by-uncertainty等方法。

  

TQS\[2\]由transferable committee、transferable uncertainty和基于图像级特征的transferable domainness组成。在我们的复现中，我们使用CNN从BEV特征中提取场景级特征描述，并使用三个分类器头来构建committees。不同于以往使用熵来评估不确定度的工作，我们计算了客观分数和0.5的标记，这种打分方式不同于原来的TQS\[2\]，这是因为我们只关注单一类别，不能使用最高分和第二高分的差。此外，我们通过域鉴别器计算域得分，并设置为  \=0.75, \=0.4，这与TQS相同。为了与TQS保持一致，我们使用源域数据和选择的目标数据来微调在源域上训练的检测器。

  

CLUE\[3\]使用不确定性加权聚类来选择目标数据。按照这个思路，我们首先通过计算NMS后的预测熵来获得每帧的不确定性，然后用熵的平均值来表示帧级的不确定性。此外，利用CLUE\[3\]提出的加权K-Means和K个中心进行聚类，其中K表示当前采样时刻的标注预算。

  

**● 3DTrans@ADA实验结果**

Waymo->KITTI：![](https://mmbiz.qpic.cn/mmbiz_png/yqIXRx1XSxWksOXvsQJahiclRWnCiaeiabnh2RekB3OAMB35z8icJUicNfRXW1151Q7yAe2XyubgaNq7yTKVhBicpiaHA/640?wx_fmt=png)

  

1.2.3  3DTrans@SSDA

**● 入口链接：**

https://github.com/PJLab-ADG/3DTrans/blob/master/docs/GETTING\_STARTED\_SSDA.md

  

**● 3DTrans代码库SSDA基线算法的构建：**

  

3DTrans代码库同样支持了多种半监督算法，包括经典的SESS\[5\]和Pseudo-Label\[5\]算法。并且我们给出了在Domain Shifts的情况下，该如何使用上述半监督方法来部署模型到目标域。SSDA的技术路线是：源域预训练模型->在1%/5%的带标注目标域数据下微调->在半监督目标域数据下进行重训练。3DTrans支持的半监督算法如下：

  

SESS\[5\]是一种在Mean Teacher范式下，引导教师模型和学生模型对于输入数据的随机扰动来保持预测一致性的算法。它设计了一个特定的基于点的数据扰动方案和三种一致性损失，能够使网络生成更准确的进行检测。我们已经在代码库中复现了SESS并将其应用在了跨域检测中。

  

Pseudo-Label\[5\]是针对无标签数据非常经典的一种方法，即由初始模型推理无标注数据，从而产生大量伪标签，通过设计的阈值过滤，最终的伪标注数据与带标注数据共同监督网络的训练。我们在代码库中复现Pseudo-Label方法并将其与Mean Teacher框架结合，应用在跨域检测中。

  

**● 3DTrans@SSDA实验结果**

Waymo->nuScenes：![](https://mmbiz.qpic.cn/mmbiz_png/yqIXRx1XSxWksOXvsQJahiclRWnCiaeiabn8fseMPWmwz0gasDhiaoCfGbB55kbt7iaLm1NvKVe7icNAXwGan2TPSnBA/640?wx_fmt=png)

  

1.2.4  3DTrans@MDF

**● 入口链接：**

https://github.com/PJLab-ADG/3DTrans/blob/master/docs/GETTING\_STARTED\_MDF.md

  

********● 3DTrans代码库MDF基线算法的构建：********

  

3DTrans代码**首次**支持的3D场景下的MDF任务设定。MDF多域融合是指3D目标检测器在多个数据集上进行联合训练，并且需要尽可能同时在多个数据集实现较高的检测精度。需要注意，相比于Domain Adaptation(DA)领域中的Multi-source Domain Adaptation, 这里所提出的MDF任务不要求不同域之间是close-set闭集关系，即来自于不同域(或数据集)的类别分布式是可以不一致的。相比于Multi-source Domain Adaptation，MDF任务设定弱化了对于不同域之间的数据分布和类别分布的条件限制。

  

在3DTrans代码库中，我们构建了几种典型的MDF基线模型：

1）**Single-dataset training**：单数据集训练策略，难以部署到另外的数据集下。

  

2）**Direct Merging**：将不同数据集的数据直接合并，并且采用PV-RCNN or Voxel-RCNN等基线模型进行训练，见脚本：slurm\_train\_multi\_db\_merge\_loss.sh

3）**Uni3D训练**：将不同数据集的数据直接合并，并采用Dataset-shared Backbones + Dataset-specific Heads的方式进行训练，见脚本：slurm\_train\_multi\_db.sh

  

**● 3DTrans@MDF实验结果**（更多结果请参见代码库）

Waymo+nuScenes：

![](https://mmbiz.qpic.cn/mmbiz_png/yqIXRx1XSxWksOXvsQJahiclRWnCiaeiabn4P5RwU25nv6xwRdN1DYS0bJFyaxmFlCF6jkBmpXDzA4pJgXzA41syg/640?wx_fmt=png)

  

1.2.5  3DTrans@可视化介绍

**● 入口链接：**

https://github.com/PJLab-ADG/3DTrans/blob/master/docs/QUICK\_SEQUENCE\_DEMO.md

  

****● 3DTrans代码库UDA基线算法的构建：****

  

目前现有的一些3D点云代码库的可视化模块都是单帧可视化，缺乏针对时序数据的处理。为此，我们在3DTrans代码库中增加了Sequence-level时序级别的可视化UI工具，可视化效果非常直观。目前主要支持对Waymo，ONCE和nuScenes数据集的时序检测结果的可视化。**用户可以给定的一个序列ID，来产生对应的可视化内容****。**

![](https://mmbiz.qpic.cn/mmbiz_gif/yqIXRx1XSxWksOXvsQJahiclRWnCiaeiabncER716HpLJQK5dKp2NXJrbbQvcEianYnclMibHickv2icrkGflSZEcJsHw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/yqIXRx1XSxWksOXvsQJahiclRWnCiaeiabng76EIctgxRyoCcUNz1QAt94etcxN9cgdTiaJecy7x2WPUecWVN5YUDw/640?wx_fmt=gif)

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**Uni3D和Bi3D简要介绍**

_****_********.********_2.1****__****.****_

**Uni3D: CVPR-2023收录**

Uni3D是我们针对**MDF任务设定**，提出的一个通用的解决方案。其可以容易地部署到PV-RCNN、Voxel-RCNN等模型中。另外，我们近期发现其对PV-RCNN++、Centerpoint等基线模型同样有明显提升。详情参考：Uni3D: 首个多数据集3D目标检测框架（已开源)

  

_****_********.********_2.2****__****.****_

**Bi3D：CVPR-2023收录**

Bi3D是针对ADA任务设定，**首次**提出的在自动驾驶场景下主动学习解决方案。同样其可以以较低的标注代价来让自动驾驶感知模型适配的没有见过的目标域下。详情参考：[Bi3D: 首个主动领域适配3D目标检测算法（已开源)](http://mp.weixin.qq.com/s?__biz=MzkyNjQ0Njk0Mg==&mid=2247483664&idx=1&sn=d44300fece919c044af2d1bcf42a12af&chksm=c2366521f541ec37476da71e401486b0321c8c79c522541bcb83a566ab41069b27f18b46df15&scene=21#wechat_redirect)

[](http://mp.weixin.qq.com/s?__biz=MzkyNjQ0Njk0Mg==&mid=2247483664&idx=1&sn=d44300fece919c044af2d1bcf42a12af&chksm=c2366521f541ec37476da71e401486b0321c8c79c522541bcb83a566ab41069b27f18b46df15&scene=21#wechat_redirect)

[](http://mp.weixin.qq.com/s?__biz=MzkyNjQ0Njk0Mg==&mid=2247483664&idx=1&sn=d44300fece919c044af2d1bcf42a12af&chksm=c2366521f541ec37476da71e401486b0321c8c79c522541bcb83a566ab41069b27f18b46df15&scene=21#wechat_redirect)

[](http://mp.weixin.qq.com/s?__biz=MzkyNjQ0Njk0Mg==&mid=2247483664&idx=1&sn=d44300fece919c044af2d1bcf42a12af&chksm=c2366521f541ec37476da71e401486b0321c8c79c522541bcb83a566ab41069b27f18b46df15&scene=21#wechat_redirect)

‍[](http://mp.weixin.qq.com/s?__biz=MzkyNjQ0Njk0Mg==&mid=2247483677&idx=1&sn=3afb2bae0a1c27cf9cb2984affe01d2f&chksm=c236652cf541ec3a86e35031681b0ed9f8f8b022c0d428e5a46cafbb5abdc37edca0867c630c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**3DTrans正在做什么？**

最近火热的ChatGPT/GPT-4等大模型引发了我们对自动驾驶大模型的思考。众所周知，全面、多样的语料库是构建强大、通用的NLP或者跨模态大模型的基石。一些研究表明，如果可以获取到代表力强、差异性强的预训练数据，基础模型的参数量的增加是可以带来预训练性能的提升。

  

然而，在3D LiDAR自动驾驶场景下，由于不同厂商所提供的原始数据之间的差异很大，导致难以在自动驾驶领域获得一个unified dataset。因此，到目前阶段，我们认为在自动驾驶领域实现通用感知的一个必要路线是进行**unified dataset的构建**，或者是设计一个unified baseline model使得其可以在带有差异化的数据集中学习到一个**unified representations**。当然，Uni3D选择了后者。与此同时，我们也并没有放弃对前者的努力，Bi3D就是在探索如何从海量无标注的自动驾驶数据集中挑选出最优价值的数据，这个研究工作的最终目的实际上是为了从目前已知的多个学术数据集中挑选有价值样本，以最小的存储代价构建一个unified dataset。

  

近期，我们正在探索利用算法从海量自动驾驶数据中挑选出有价值的样本(多样性强、冗余度低)，进一步设计有效的解决方案来让模型可以在多源数据中学习到通用表征。“路漫漫其修远矣,吾将上下而求索”，探索自动驾驶感知模型跨传感器、跨数据集、跨任务的通用表征的路途漫长。我们欢迎有相同兴趣爱好的朋友交流、合作、加入我们！（[加入我们！](http://mp.weixin.qq.com/s?__biz=MzkyNjQ0Njk0Mg==&mid=2247483655&idx=1&sn=affe463cf26ba249f88f4408c8e1f5c1&chksm=c2366536f541ec20554241dded450fd0d82c9d0907b1f3419dfdbc8e991b2e7db0e1cdc1298b&scene=21#wechat_redirect)）

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**致谢与开发团队**

感谢闫翔超(Shanghai AI Laboratory)，袁家康(复旦大学)，费奔(复旦大学)，黄思渊(上海交通大学)和周鸿斌(Shanghai AI Laboratory)对开发3DTrans所做出的贡献。

  

3DTrans团队开发成员信息：

https://bobrown.github.io/Team\_3DTrans.github.io/

  

此外，我们的3DTrans代码库是基于OpenPCDetv0.5.2(https://github.com/open-mmlab/OpenPCDet/tree/v0.5.2)进行开发，感谢OpenPCDet开发团队的出色代码库。

  

同时，我们也想利用这个机会感谢ONCE开发团队(https://once-for-auto-driving.github.io/)，其公开的大规模数据集支持了3DTrans团队对AD场景下预训练任务的研究。

  

  

* * *

  

**参考文献：**

\[1\] Jihan Yang, Shaoshuai Shi, Zhe Wang, Hongsheng Li, Xiaojuan Qi. ST3D: Self-training for Unsupervised Domain Adaptation on 3D Object Detection.

\[2\] Bo Fu, Zhangjie Cao, Jianmin Wang, and Mingsheng Long. Transferable Query Selection for Active Domain Adaptation.

\[3\] Viraj Prabhu, Arjun Chandrasekaran, Kate Saenko, Judy Hoffman. Active Domain Adaptation via Clustering Uncertainty-weighted Embeddings.

\[4\] Yan Wang, Xiangyu Chen, Yurong You, Li Erran, Bharath Hariharan, Mark Campbell, Kilian Q. Weinberger, Wei-Lun Chao. Train in Germany, Test in The USA: Making 3D Object Detectors Generalize.

\[5\] Na Zhao, Tat-Seng Chua, Gim Hee Lee. SESS: Self-Ensembling Semi-Supervised 3D Object Detection.

\[6\] Antti Tarvainen, Harri Valpola. Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results.

\[7\] Saining Xie, Jiatao Gu, Demi Guo, Charles R. Qi, Leonidas J. Guibas, Or Litany. PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding

\-END-

更多自动驾驶数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言