     ​neuralsim概念预览:「现实级」街景三维重建/编辑/仿真渲染，迈向自动驾驶数据闭环 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

​neuralsim概念预览:「现实级」街景三维重建/编辑/仿真渲染，迈向自动驾驶数据闭环
=============================================

原创 郭建非 OpenDataLab 2023-01-10 18:00 上海

> 原文地址: [https://mp.weixin.qq.com/s/edspSZ7cYPG2asj\_R\_n7AQ](https://mp.weixin.qq.com/s/edspSZ7cYPG2asj_R_n7AQ)

本文授权转载自上海人工智能实验室 智能交通平台团队

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dNPSbkyB8btSianQhiacXlRVX3eAsPouKr0pm8qMtiaCJ9GT50Yl0BZgpMQIgJspDbUjmUd15JibJgQXw/640?wx_fmt=gif)

  

大家好，我是郭建非，是3DNR团队的负责人与 tech leader。

  

在本文中，我将为大家介绍团队过去一年中围绕「神经渲染技术在自动驾驶领域应用」的一些思考和研究成果。并且向大家展示团队自研的现实级三维重建/编辑/仿真渲染框架——neuralsim 的部分阶段性成果。该框架将在不久的将来完成开源。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**自动驾驶传感器仿真，****是落地的下一步棋**

_********No.1.1********_  

******为什么需要自动驾驶传感器仿真？******

近年来，自动驾驶技术发展突飞猛进，很多在实验室中的实验性项目已经逐步走向市场大众。然而时至今日，自动驾驶技术仍然难以做到完全无人，甚至无法保证基本的安全性。究其根本，在于真实道路环境无限丰富，无法被穷举、预测，存在着大量难以预测的边界难例（Hard Corner Case）。

  

为了解决这个问题，大量自动驾驶公司通过海量路测来提高对边界难例的覆盖率，企图通过遍历这些危险场景来提高自动驾驶系统的实际安全性能。然而，想要通过路测来获得足够多的边界难例，往往需要付出巨大的代价：**难例的触发效率呈边际效应递减，而每一次触发都有可能导致一起重大交通事故**。

  

这些客观条件都在限制着我们利用真实车辆在真实世界中完成海量路测和边界难例的覆盖挖掘，而通过**「仿真测试」**以低成本获得边界难例数据逐渐被认为是解决自动驾驶落地难的不二法门。

  

早期的仿真测试主要针对决策规划模块进行，然而边界难例不止存在于决策规划系统中，感知系统也仍然存在无穷无尽的边界难例。

  

2016年，一辆搭载着自动驾驶系统的汽车径直撞向了一辆半挂卡车，驾驶员当场殒命。事后调查分析，自动驾驶系统误以为白色的卡车车厢是明亮的天空，导致避障算法失效并产生灾难性后果。足以窥见针对感知系统的传感器数据仿真有时甚至比决策规划仿真更为重要。

![](https://mmbiz.qpic.cn/mmbiz_png/Pwo1UJ0K2dNPSbkyB8btSianQhiacXlRVXlONBibF1bAK6xGDAIsDhUpnXxDiaMw05YBic5UPGDBuyR4OQMbIG2t1Xw/640?wx_fmt=png)  
新闻：Details About the Fatal Tesla Autopilot Crash Released (businessinsider.com) https://www.businessinsider.com/details-about-the-fatal-tesla-autopilot-accident-released-2017-6

  

_****No.1.2****_  

**基于神经渲染的重建、编辑与传感器仿真框架**

目前已有诸如 VTD、51 SimOne等针对感知系统的仿真和测试平台。这些平台大多基于游戏引擎，利用基于物理渲染的传统图形学管线进行仿真渲染。然而，这种传统方法存在一系列问题。

  

由于图形和当前游戏管线的技术限制，构建超真实的 3D 场景成本高昂，自动化程度低，需要大量人力的介入，且周期较长。针对这个问题，部分方案引入摄影测量等传统 3D 重建技术，来重建真实城市道路场景，但受限于自动驾驶真实数据本身的特点，难以完成全场景的稠密重建和高质量的真实渲染，需要进行人为二次修正和加工。此外，也有通过过程生成等 3D 图形技术，实现自动化生成城市场景的方式，但这种方式同样在复杂性、真实度上都和真实驾驶场景存在较大差异。

  

为此，**3DNR团队（基础算法）联合商汤绝影团队（业务拓展优化），构建了一套直接利用真实车端数据的隐式重建和编辑仿真方案**。我们的方案将实车采集的多视图像、激光雷达数据转化为神经网络表示的3D场景库和3D数字资产库，基于隐表面神经体渲染技术，能够渲染以假乱真的相机图像、激光雷达点云，实现「现实级」三维重建和仿真。并且，场景中的要素能够自由地组合控制、轨迹编辑，泛化出新的场景，通过批量仿真渲染，可以产生高一致性的2D/3D传感器数据和2D/3D/4D语义真值标注，以服务于感知系统的测试和训练，迈向自动驾驶数据闭环。我们致力于通过直接实现尽可能全自动的、高一致性的三维重建，大大减少渲染仿真数据与真实场景的领域差异，通过 sim≈real 的思路直接避免 sim2real 的 gap。

![](https://mmbiz.qpic.cn/mmbiz_png/Pwo1UJ0K2dPPBYia5gby1iauHHmZwax9uibpjHEb0xjicX7DabG4TuvuYxUeKlrPhribRbeQf9iciclHQV0C3kfT0Jmow/640?wx_fmt=png)  
整体工作思路

  

在下文中，我将依次按照「照片级前背景联合重建」「高效的传感器仿真&语义真值仿真」「场景编辑与数据闭环」 三个章节的顺序来介绍我们的工作。

![](https://mmbiz.qpic.cn/mmbiz_png/Pwo1UJ0K2dPPBYia5gby1iauHHmZwax9uibeqGVF67xGQmib5LUbbY2qTqfo5WERuucicOfRtLCRPtj0OKKmTDBJEzg/640?wx_fmt=png)  
整体成果概览  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**照片级前背景联合隐式三维重建**

_****No.2.1****_  

**多帧多模态多视图三维重建**

我们可以直接利用实车采集数据，实现对真实街景的前背景联合三维重建。为了方便与学界业界交流对比，我们直接使用 waymo 公开的学术开源数据集 waymo-perception 数据集进行效果展示。

waymo-perception 数据集包含约800个训练集序列，我们挑选了其中3-4个序列进行展示；每个序列长度200帧左右，我们使用序列原始数据中的 前向、左前、右前 3个机位的环视相机图像数据 和 顶部激光雷达数据，以及对应的传感器内外参数据、自车位姿数据进行多视图三维重建。

  

以 waymo perception - 405841xx 序列为例：

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dOFHAS2VUWErBS2UbqLVIy5pv9om3I5ozibrGialV2m6SYmfcfOVHXOSs1Z5VXLsc63icLDZtw3Qm7GA/640?wx_fmt=gif)  
waymo perception - segment 405841xx  
原始数据（节选）真值

  

我们的多视图重建方法主要利用多帧图像数据进行；激光雷达数据主要是为地面的高度和三维结构补充必要的消歧信息，因此并不要求激光雷达涵盖相机的全部视野。对于我们使用的 waymo-perception 数据集而言，在上图中也可以看到，如果将激光雷达点云投射到相机图像中，激光雷达点云只涵盖了图像下半部分的视野。

  

下面的视频展示了该场景下我们的隐式三维重建的质量和神经渲染的效果。可以看到，我们的方法能够实现以假乱真的三维重建和渲染质量。

  

如果场景中包含动态要素（如他车、行人），大多数传统的针对纯静态场景的多视图重建工作将不再适用。但是，如果说「没有街景背景不能称作自动驾驶」，那么「**没有丰富的前景物体参与交通更不能被称之为自动驾驶**」。

  

因此，我们显式地区分构建了整体的静态背景和动态前景两套3D表征，并设计了一套高效的多物体可微渲染框架。并且，我们通过预先针对前景物体类别构建3D类别先验的方式，解决了前景少视角重建的病态问题，实现了只依赖三维跟踪检测框标注（3D Tracklet）、无需2D图像分割标注，即可对场景中的前景和背景进行联合的隐式三维重建。

  

以 waymo perception - 767010xxx 序列为例：

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dOFHAS2VUWErBS2UbqLVIy5mbHJuHIK4dvwWL7UXPCzAl3nia1thicPl4FHelbKXkOk7A9ZS7CZaacQ/640?wx_fmt=gif)  
waymo perception - segment 767010xx  
原始数据（节选）真值

  

在下面的视频中可以看到，即使面对包含动态前景物体的复杂街景数据序列，我们可以在前景和背景均达到较高的重建质量和渲染效果。

  

下面的视频中，展示了在更多的 waymo-perception 序列场景下，我们的方法在完整重建后再回放渲染的效果：

  

_****No.2.2****_  

**背景新视角合****成**

除了回放再渲染外，验证重建质量的另一个重要方式是新视角合成（Novel View Synthesis）。在下面的视频中，展示了让自车在重建好的场景中自由地螺旋穿梭前进时的多模态传感器渲染仿真效果：

  

_****No.2.3****_  

**前景新视角合成**

不止背景，重建好的前景也可以进行新视角合成，如下图所示：  

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dOFHAS2VUWErBS2UbqLVIy5RyjJFfNm1b1YKj0MNdKftTOXwaNics5rJVTO7svZEf0xRqdJBxV1P7g/640?wx_fmt=gif)

  

自动驾驶场景下，前景物体普遍面临观测视角少、不均匀的问题。直接对前景物体从头开始（learn from scratch）的三维重建是个高度病态的问题。

  

因此，我们利用开源类别泛化多视数据集，预先构建了三维生成模型（3DGAN），构建了车辆、行人等交通参与要素的3D形状与外观的类别先验。这样的生成模型可以理解为一个 「实例个数=∞」 的数字资产库（i.e. 每一个随机噪声对应一个独特实例）。

  

之后，即可利用三维生成模型的逆向过程，在这个数字资产库中可微地 “检索” 出一个符合实际观测的实例，完成少视角重建过程，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dOFHAS2VUWErBS2UbqLVIy5kdlmXdLL1xPdgEscXFublIEGIQ1CzdYictz7Os6jCeIzU7My1b7UjVQ/640?wx_fmt=gif)

在我们的实际应用中，上述前景重建过程和背景的重建是同时进行的。得益于先前构建的3D类别先验，我们的方法能够只依赖3D跟踪检测框标注进行前背景联合重建，而不需要图像实例分割。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**高效的传感器仿真和语义真值仿真**

不同于 NeRF 原始的体密度 (Volume density) 形状表达，我们选择和拓展了 对仿真编辑和图形引擎更友好的 SDF 隐表面表示 (e.g. NeuS），使得场景的3D几何表示有明确的表面定义和深度概念。

  

在下图中，我们利用相机对隐表面神经渲染得到的深度，直接对相机2D像素升维得到3D点云，然后将每一帧的相机图像对应的3D点云拼接在一起，进行可视化展示。可以看到，我们的隐表面神经渲染技术具有较高的多视一致性。

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dOFHAS2VUWErBS2UbqLVIy5pwYZDJPWGOfavpVrlkrCoWCKN8hqZaw71VWZJH3ib7Jbw1ueNRRrDicA/640?wx_fmt=gif)

利用重建得到的高一致性的3D场景几何与3D场景外观，我们得以仿真高度真实的新传感器的数据。  

  

_****No.3.1****_  

**相机模型仿真渲染**

利用重建好的场景，我们可以仿真渲染新的相机模型的图像。在下图中，展示了我们将 waymo 序列原相机的 51° 的视场角逐渐提升到 109°，并加上一定的超广角畸变后，对一个109°视场角的超广角相机模型进行仿真渲染。

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dOFHAS2VUWErBS2UbqLVIy5allVx0icQdMmCTzgAHZnKsL0cXSFSegBIKibaHDRzZUDiaLsqsxJcmtEw/640?wx_fmt=gif)

  

_****No.3.2****_  

**激光雷达模型仿真渲染**

利用与现实高度一致的场景与物体的3D几何形状，我们可以对不同于原序列的新的激光雷达模型进行仿真渲染。在下面的视频中，我们对重建好的 waymo-767010xxx 序列，仿真渲染8款不同于原序列的激光雷达模型的点云数据。这些新的激光雷达模型包括机械旋转式、固态、棱镜式等多种不同类型。

  

_****No.3.3****_  

**2D/3D/4D语义仿真**

得益于我们设计的多物体渲染框架，我们还能够仿真产生多帧的2D/3D的语义真值标注。

  

根据相机渲染过程中，逐2D像素对应的3D光线和不同物体3D几何的相交关系和顺序，可以渲染产生图像2D实例分割标注；同理，根据激光雷达渲染过程中，逐LiDAR光束和不同物体3D几何的相交关系和顺序，可以渲染产生激光雷达点云3D实例分割标注。

  

在下面的视频中，针对重建好的 waymo-767010xxx 序列，展示了我们方法仿真渲染图像、仿真渲染多帧图像2D实例分割标注、仿真渲染多帧LiDAR 3D实例分割 (i.e. 4D语义标注) 的效果：

  

_****No.3.4****_  

**高效渲染与仿真**

我们在神经体渲染底层技术栈中铺设了若干基础建设式的创新。我们吸纳了分层局部隐式神经表征的思想，设计了分块表征与块间连续性保证算法，并利用自举更新的占用格对体渲染中的光线采样过程进行加速。这些创新除了让我们达到前文所展示的重建质量外，还使得我们的神经渲染过程达到接近实时的效率。

  

下图简单展示了我们的重建方法的分块表征以及可鼠标交互的实时神经渲染：

![](https://mmbiz.qpic.cn/mmbiz_gif/Pwo1UJ0K2dPPBYia5gby1iauHHmZwax9uibWS1aLkibuwwFIhYGFjzK6FsyUkHnMwoHjxga8vTejFRkGZO3llzSP4w/640?wx_fmt=gif)

我们针对前景设计的3DGAN模型同样实现了一套利用占用格的批量(batched)光线采样加速算子，显著提升了前背景多物体联合渲染的效率。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**场景编辑与数据闭环**

_****No.4.1****_  

**随意的可控显式/隐式编辑**

我们的方法将前景和背景都解耦地视作独立的可渲染物体。因此，我们可以对场景中的任一物体模型进行随意的操作和编辑，如下面视频所示：

  

除了前面展示的针对场景中物体的显式编辑方式外，我们也初步探索了在语义层面的风格化编辑，如下面视频所示：

  

_****No.4.2****_  

**轨迹编辑与场景泛化**

结合动态场景库和轨迹规划算法，我们还可以对场景中的自车和他车进行更符合常理的编辑，即仿真新的驾驶行为。

  

在下面的视频中，我们依次展示了「左车突然切入(cut in)」，「右车闯红灯」，「前车急停追尾」 3种不同的场景编辑方式，渲染其在 “平行宇宙” 中的虚拟交通事件。

  

以其中的「左车突然切入(cut in)」场景为例，下面这个视频展示了对编辑后的场景的多模态传感器仿真结果：（相机、深度传感器、8款激光雷达模型）

  

在今后，我们可以更进一步地利用实车数据扩充3D场景库、扩充前景数字资产库，从而泛化出更多新的物体组合和场景序列。搭配前述 「一次重建、终身受用」的新相机、新激光雷达模型仿真渲染范式，我们的方案最终能够按照给定的场景、给定的物体组合、给定的轨迹、给定的传感器模型定制化地渲染出海量高度真实的传感器数据和语义真值，从而逐渐达成我们构想的通过传感器数据仿真大大提升自动驾驶测试效率和质量的愿景。  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

**写在最后**

神经渲染技术作为新兴领域，成功地构建起了场景表征与成像过程之间的可微桥梁，能够很好地结合不同领域的先验知识，使得图像相关的机器学习研究逐渐走向可解释、可控可编辑的3D语义时代。我们坚信，不仅仅是自动驾驶，神经渲染技术将在越来越多的领域走向成熟应用。

  

我们3DNR团队将继续以自动驾驶数据闭环为理想目标，沿途下蛋挖掘攻关基础学术关键点，并秉持开源和共享精神，与学界业界共同学习共同进步。

  

此外作为联动，商汤绝影团队也将发表他们的宣传文章，感兴趣的读者还可关注下方公众号名片，阅读商汤绝影团队相关介绍内容。

  

后续，3DNR团队将进一步介绍分享更多技术细节内容，并陆续发表相关学术论文、开源 neuralsim 等相关项目代码，感兴趣的同学可以持续保持关注、加入我们。沟通交流、简历投递指路：

**guojianfei@pjlab.org.cn**

  

文中出现的自动驾驶相关数据集，欢迎到OpenDataLab下载、体验：**https://opendatalab.org.cn/**。  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言