     超详细 BEV 感知技术研究综述、BEV 感知实用工具箱Toolbox 及相关数据集分享 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

超详细 BEV 感知技术研究综述、BEV 感知实用工具箱Toolbox 及相关数据集分享
============================================

原创 OpenDriveLab OpenDataLab 2023-02-16 17:21 上海

> 原文地址: [https://mp.weixin.qq.com/s/MmpNx55YMkSgTtFr952t2w](https://mp.weixin.qq.com/s/MmpNx55YMkSgTtFr952t2w)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

BEV（Bird’s-eye-view） 感知研究对自动驾驶领域影响巨大，关于 BEV 你需要了解哪些内容，本文通过 BEVPerception Survey 为你揭晓答案

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0icHTz7ibCqTK8dhFnof6yVSGk9sWSD0CMibkTjyaktcIGImMQqD0Wib8JKw/640?wx_fmt=png)

  

在自动驾驶领域中，让感知模型学习强大的鸟瞰图（BEV）表征是一种趋势，并且已经引起了工业界和学术界的广泛关注。相比于之前自动驾驶领域中的大多数基于在前视图或透视图中执行检测、分割、跟踪等任务的模型，鸟瞰图（BEV）表征能够让模型更好地识别被遮挡的车辆，并且有利于后续模块（例如规划、控制）的开发和部署。

  

可以看出，BEV 感知研究对自动驾驶领域具有巨大的潜在影响，值得学术界和产业界长期关注并投入大量精力，那么 BEV 感知到底是什么？自动驾驶的学术界和工业界大佬又都在关注 BEV 感知的什么内容？本文将会通过**BEVPerception Survey**为你揭晓答案。

  

BEVPerception Survey 是上海人工智能实验室自动驾驶**OpenDriveLab 团队**与**商汤研究院**合作论文 《Delving into the Devils of Bird's-eye-view Perception: A Review, Evaluation and Recipe》 的实用化工具呈现方式，**分为基于 BEVPercption 的最新文献研究和基于 PyTorch 的开源 BEV 感知工具箱两大板块**。

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0ic16IW018Pd6Rpnw4SUZreJuxRlx0QiaQvPWEq8I5OeSfKLSIt9Unaamg/640?wx_fmt=png)

● 论文地址：https://arxiv.org/abs/2209.05324

● 项目地址：https://github.com/OpenPerceptionX/BEVPerception-Survey-Recipe

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

******概要解读、技术解读******

BEVPerception Survey 最新文献综述研究主要包含三个部分 ——**BEV 相机、BEV 激光雷达和 BEV 融合**。BEV 相机表示仅有视觉或以视觉为中心的算法，用于从多个周围摄像机进行三维目标检测或分割；BEV 激光雷达描述了点云输入的检测或分割任务；BEV 融合描述了来自多个传感器输入的融合机制，例如摄像头、激光雷达、全球导航卫星系统、里程计、高清地图、CAN 总线等。

**BEV 感知工具箱**是为基于 BEV 相机的 3D 对象检测提供平台，并在 Waymo 数据集上提供实验平台，可以进行手动教程和小规模数据集的实验。

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0iciaicicficojsBaCjkJ2ZoD9bZTQSgXgBNp4ybxPL8XnpnKf3JiblEoP2cww/640?wx_fmt=png)

图 1：BEVPerception Survey 框架

具体来说，BEV 相机表示用于从多个周围相机进行 3D 对象检测或分割的算法；BEV 激光雷达表示用点云作为输入来完成检测或分割任务；BEV 融合则是用多个传感器的输出作为输入，例如摄像头、LiDAR、GNSS、里程计、HD-Map、CAN-bus 等。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**BEVPercption 文献综述研究**

_****No.1****_  

**BEV 相机**

BEV 相机感知包括 2D 特征提取器、视图变换和 3D 解码器三部分。下图展示了 BEV 相机感知流程图，在视图变换中，有两种方式对 3D 信息进行编码 —— 一种是从 2D 特征预测深度信息；另一种是从 3D 空间中采样 2D 特征。

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0icfzkgVSfbmsOod6xn3RicZabwKaZIJdByC1I37BrqPsZX0Qx1Sicp0FgA/640?wx_fmt=png)图 2：BEV 相机感知流程图

对于**2D 特征提取器**，2D 感知任务中存在大量可以在 3D 感知任务中借鉴的经验，比如主干预训练的形式。   

**视图转换模块**是与 2D 感知系统非常不同的一方面。如上图所示，一般有两种方式进行视图变换：一种是从 3D 空间到 2D 空间的变换，另一种是从 2D 空间到 3D 空间的变换，这两种转换方法要么是利用在 3D 空间中的物理先验知识或利用额外的 3D 信息监督。值得注意的是并非所有 3D 感知方法都有视图变换模块，比如有些方法直接从 2D 空间中的特征检测 3D 空间中的对象。

**3D 解码器**接收 2D/3D 空间中的特征并输出 3D 感知结果。大多数 3D 解码器的设计来自基于 LiDAR 的感知模型。这些方法在 BEV 空间中执行检测，但仍然有一些 3D 解码器利用 2D 空间中的特征并直接回归 3D 对象的定位。

  

_****No.2****_  

**BEV 激光雷达**

BEV 激光雷达感知的普通流程主要是将两个分支将点云数据转换为 BEV 表示。下图为 BEV 激光雷达感知流程图，上分支提取 3D 空间中的点云特征，提供更准确的检测结果。下分支提取 2D 空间中的 BEV 特征，提供更高效的网络。除了基于点的方法能在原始点云上进行处理外，基于体素的方法还将点体素化为离散网格，通过离散化连续的 3D 坐标提供更高效的表示。基于离散体素表示，3D 卷积或 3D 稀疏卷积可用于提取点云特征。

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0icxfcB3tVqicOiaHIJT4HazKEhn0ltaGRXP4t8pbkLgGUPdc0UsrS127yA/640?wx_fmt=png)图 3：BEV 激光雷达感知流程图

  

_****No.3****_  

**BEV 融合**

BEV 感知融合算法有 PV 感知和 BEV 感知两种方式，适用于学术界和工业界。下图展示了 PV 感知与 BEV 感知流程图的对比，两者的主要区别在于 2D 到 3D 的转换和融合模块。在 PV 感知流程图中，不同算法的结果首先被转换到 3D 空间中，然后使用一些先验知识或者手工设计的规则进行融合。而在 BEV 感知流程图中，PV 特征图会被转换到 BEV 视角下，然后进行 BEV 空间下的融合从而得到最终的结果，因而能够最大化保留原始特征信息，避免过多的手工设计。

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0ic4I9wUBk2udxKttBMfX1luicRu9leD4GujWxYaeGOZ9f5zHbb7NUje4g/640?wx_fmt=png)图 4：PV 感知（左）与 BEV 感知（右）流程图

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**适用于 BEV 感知模型的数据集**

针对 BEV 感知任务存在很多的数据集。通常数据集由各种场景组成，并且每个场景在不同数据集中的长度不同。下表总结了目前学界常用的数据集。我们可以从中看到 Waymo 数据集相比其他数据集有着更多样的场景以及更丰富的 3D 检测框的标注。

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0iccBuiaxwicURhZGLMnSopNfOB8PKdYZFdNQqxV5nbl4SMmfWtYoDBWRug/640?wx_fmt=png)表 1：BEV 感知数据集一览

然而目前学界并没有针对 Waymo 开发的 BEV 感知任务的软件公开。因此我们选择基于 Waymo 数据集进行开发，希望可以推动 BEV 感知任务在 Waymo 数据集上的发展。

  

上述提到的自动驾驶BEV 感知公开数据集已在OpenDataLab平台上架，欢迎大家下载、体验。扫码直达 ↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5SRto4d9KLtNudWvDV5cBIiaiayc6xtQIy6ibEJP40xNHnygBtClZJSvoHYOiae2xkSicwDbHF5NiaYq7A/640?wx_fmt=png)

浏览器访问：https://opendatalab.com/?industry=7360

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**Toolbox - BEV 感知工具箱**

BEVFormer 是一种常用的 BEV 感知方法，它采用时空变换器将主干网络从多视图输入提取的特征转换为 BEV 特征，然后将 BEV 特征输入检测头中得到最后的检测结果。BEVFormer 有两个特点，它具有从 2D 图像特征到 3D 特征的精确转换，并可以把它提取的 BEV 特征适用于不同的检测头。我们通过一系列的方式进一步提升了 BEVFormer 的视图转换质量以及最终的检测性能。

  

在凭借 BEVFormer++ 取得**CVPR 2022 Waymo Challenge 第一名**后，我们推出了**Toolbox - BEV 感知工具箱**，通过提供一整套易于上手的 Waymo Open Dataset 的数据处理工具，从而集成一系列能够显著提高模型性能的方法（包括但不限于数据增强，检测头，损失函数，模型集成等），并且能够与领域内广泛使用的开源框架，如 mmdetection3d 以及 detectron2 兼容。与基础的 Waymo 数据集相比，BEV 感知工具箱将使用技巧加以优化改进以便不同类型研发人员使用。下图展示的是基于 Waymo 数据集的 BEV 感知工具箱使用示例。

  

![](https://mmbiz.qpic.cn/mmbiz_png/KmXPKA19gW88pocDknAD0icJnjgNzkN0icfvdJoZJaMftxCrsY49h54UxsttBC5aX7GAwDGxMKcPuYzic28e99a3Q/640?wx_fmt=png)图 5：基于 Waymo 数据集的 Toolbox 使用示例

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

**总结**

● BEVPerception Survey 总结了近年来 BEV 感知技术研究的总体情况，包括高层次的理念阐述和更为深入的详细讨论。对 BEV 感知相关文献的综合分析，涵盖了深度估计、视图变换、传感器融合、域自适应等核心问题，并对 BEV 感知在工业系统中的应用进行了较为深入的阐述。

  

● 除理论贡献外，BEVPerception Survey 还提供了一套对于提高基于相机的 3D 鸟瞰图（BEV）物体检测性能十分实用的工具箱，包括一系列的训练数据增强策略、高效的编码器设计、损失函数设计、测试数据增强和模型集成策略等，以及这些技巧在 Waymo 数据集上的实现。希望可以帮助更多的研究人员实现 “随用随取”，为自动驾驶行业研发人员提供更多的便利。

  

我们希望 BEVPerception Survey 不仅能帮助使用者方便地使用高性能的 BEV 感知模型，同时也能成为新手入门 BEV 感知模型的良好起点。我们着力于突破自动驾驶领域的研发界限，期待与学界分享观点并交流讨论进而不断发掘自动驾驶相关研究在现实世界中的应用潜力。

  

  

\- End -

  

欢迎关注我们

了解更多精彩干货

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言