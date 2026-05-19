     硬核！自动驾驶如何做数据标注？特斯拉EP3 Auto Labeling深度分析 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

硬核！自动驾驶如何做数据标注？特斯拉EP3 Auto Labeling深度分析
=======================================

原创 OpenDataLab 2022-08-11 19:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/xaBy8XrMZCcT98e-0GXBdA](https://mp.weixin.qq.com/s/xaBy8XrMZCcT98e-0GXBdA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

作者丨上海人工智能实验室 自动驾驶团队

OpenDataLab已获授权转载

  

在自动驾驶行业，大家都说数据很重要，最近一篇文章 “万字综述：如何打造自动驾驶的数据闭环？”又一次彻底地翻炒数据闭环算法迭代体系这一概念，那么本文我们就来说说Tesla 的数据系统是怎么搭建的。

  

**【要点速览】**

**Tesla对自动标注的技术和要求：**  

  

● 首先是在Vector Space上的标注, 需要对数据做出分析处理，数据标注工具的搭建；

● 一个离线大模型对数据进行标注，车载模型相当于对大模型进行蒸馏；并且拥有强大的数据采集能力；

● 核心技术方面：三维重建与视觉SLAM等算法。

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD48YvaFC1pcSkRJPXqyJaRm5v0icMQ2icSpoD3tXl1WFicNWaokKpW92RRx77ibYPwLofvn2KICdicPraw/640?wx_fmt=jpeg)

  

下面我们就来为这三点慢慢展开。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**特斯拉高级主管提供的信息**

首先我们recall一下特斯拉高级主管Andrej Karpathy在2021 CVPR上对特斯拉自动驾驶现状讲解时提供的信息。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD48YvaFC1pcSkRJPXqyJaRmGLKI01MiblDVmGKbdRMCfyJ1goVF8tua0T684skWrgDAoZ0URVpFMDg/640?wx_fmt=jpeg)

  

**● 要想成功训练出一个网络，对数据的需求特征：**

1\. 你需要有大量的数据，这里可以指成千上万个视频片段；

2\. 需要有Sanity Check, 需要干净的数据，数据的标注需要涵盖深度、速度、加速度信息；

3\. 需要多种多类的数据，即使在同一个简单场景跑一万年，实际上的作用也不大，更重要的是需要大量的corner cases。

  

**● 整体的数据闭环体系：**

数据采集 → 搭建数据集 → 自动+人工标注 → 送入模型训练 → 量化部署到车端上。

  

**● 重视Data labelling：**

在整个特斯拉自动驾驶里面，Data labelling可能比网络部分还要重要，因为数据这一块容易用一些技巧去提升效果。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**特斯拉数据标注策略的演变**

一开始tesla选择和第三方公司合作，但很快就发现标注效率很低，并且沟通的成本很高，后来他们选择自己建立标注团队，也实现了比较好的产出。

  

我们可以从图片的下方看到数据标注量在后面时间段产出都比较稳定。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwIOpFIhw2nLHibf6PLTlEEPBnEeexacvaRMZgfFrHFnicQfgKgK20c5hw/640?wx_fmt=png)

  

**我们猜测其中有两点起到了作用：**

1\. Tesla自主开发了一个数据标注平台，包括数据标注工具与数据分析工具;

2\. 公司自己组建了一个千人标注团队，（不确定是否都是全职）专门负责数据的标注。

  

 _**NO.1**_ 

****早期的2D平面标注****

  

回到最初，Tesla是在2D的平面上对数进行精细的标注， 例如上图，不仅对车道线+朝向，红绿灯，行人做标注，连对锥形雪糕筒，左边路面的拖拉机，大卡车也会去做标注（估计归类为construction）。

  

但是对于这种方法， Tesla就发现这么一张一张去标注不太work， 并且一直这么标也不知道什么时到终点。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwemoicQDMdnNXdpqWLMYLRblmIjliazIociauUkAQUpFBKYW5dibYa4mXtQ/640?wx_fmt=png)

2D 标注demo

  

 NO.2 

**4D Space + Time Labelling**

  

接下来Tesla马上转变到一个4D Space + Time Labelling 的标注模式，在我们看来其实像一个vector space 下 3D 标注 + 时间序列，加入时间序列主要作用是知道前面发生了什么，把前面的东西保留，可以将信息投到后面，例如3D版的CVAT。

  

整个思想是，在3D空间下标注，然后再投到8个摄像机里面，简单来说，可以理解为 amount of the labels in 3D space (vector space) = ⅛ amount of labels in 8 camera views (image space)。这里可能会涉及到2D标注与3D标注之前的成本问题，很明显我们都知道标注一张2D的图像会比标注一张3D的图像成本低，但如果是 8张2D的图像对比1张3D的图像，从Tesla 的做法来看，是标注1张3D图像的成本效果要比较好。

  

但其实即使你标注获得了8倍的数据，对自动驾驶而言也还是不够用的。我们在之前的图片也看到，在CVPR2021 WAD的时候， Tesla 有60亿个标注，和1.5 Pentabytes (PB) 的数据，如果单单利用人工劳动力去标注，是不大可能做到如此庞大的数据量的。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwHI2MKWYR2tB8tiaUn9FYPiaYp3g9bYicPhJGq85sQtRW1yrqyV9eyxdgw/640?wx_fmt=png)

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**特斯拉**的auto-labeling分析****

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwQBHib9mRMKGYic7hVUQIKb53PibFXicJVjfd1Qv6kH3wvbfmtkvL6C1ibrA/640?wx_fmt=png)

  

这是Tesla Auto-Labelling 的整个pipeline, 它会有视频片段，大概就是10s到60s的视频，这些视频来源可以是他们车队采集，或者是shadow mode 上传的，这些视频片段包括了图像，IMU,GPS,Odometry(里程计)的数据，压缩成一个个packages，传到服务器上面。

  

然后服务器上面会有Offline Neural Networks, 离线神经网络，这里相当于一个大规模模型，是他们针对图像上的物体做的。

  

检测识别精度会比较准，会对不同的camera输出的图像做预处理，可以输出semantic segmentation, depth estimation，还可以多帧之间点matching的结果；

  

接着通过一个机器人行业流行的AI 算法，在我们看来就是利用nerf，SLAM等算法，把整个三维场景重建出来，然后构建出不同的label, 有道路的重建，动态/静态物体的重建，这样就可以打包成不同的labels，其实label这一模块是依托于大模型的输出的，所以tesla 在整个autolabelling 和网络训练的过程，其实是让车端运行的neural network去蒸馏大网络的输出，是这样的一个过程。

  

接着我们会有一个问题：tesla是怎么重建道路的呢？或者会有疑问，检测网络是有了（HydraNet），然后数据是怎么获得的呢？

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwsqKMyGs4uJ1RICep5O637yxn8lZTQ8Vh8se10T5IHhvJ4DvttZlhkg/640?wx_fmt=png)

  

首先会用一个隐式MLP(multilayer perceptron)表示道路，然后给每一个道路(x,y)的request，然后可以收获 Ground Height, Lane Line, Crub, Asphalt(沥青), crosswalk 等信息，可以视为BEV视角下的一个栅格化表示。

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwAjMMyRFOpPhuwzc4tmDY08EbcnLsQKLSS7Xd1tyL8ibwr8HBdW9PE3A/640?wx_fmt=gif)

  

获得这些信息之后，我们可以把他们投影到8个camera上，如上图右上的地方，相当于对每一个点作分类处理，如车道线。右下的图片是大模型对右上图做的一个Segmentation的结果，当3D投影结果跟2D 重合的时候，我们就认为我们道路重建准确。

为了让大家更加理解这个过程，其实这个过程是基于一篇 paper，ECCV 2020 NeRF的 paper, (Mildenhall, Ben, et al. "Nerf: Representing scenes as neural radiance fields for view synthesis." ECCV, 2020.)

  

Nerf 所解决的是一个什么问题呢？可以看到图片中下放nearest input 这一部分，有一些离散的，不同视角下的一些输入，然后我们的目的是输出一个三维重建的图，作为物体的重建。

  

然后nerf对物体的重建的过程也比较有意思，一般我们表示一个物体，例如会用match去表示，或者用各种显式去表示，但这篇文章并没有用一种显式的方式去表示，而是用一个多层神经网络，即MLP，去表示物体的本身。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwp5umPKPlhWtxg1GEMgWuhD1WRZWZMLrA7mszqFZlru1Bpld9WZrFYg/640?wx_fmt=png)

  

如上图左边，当我们有(x,y,z,θ,ϕ)，即三维空间点x,y,z，以及视角θ,ϕ；如图(a)，在每条射线上的每个点，都带着(x,y,z)，以及(θ,ϕ)信息，通过MLP后输出RGB信息，如果我们采集的点越来越多，我们得到更多不同的RGB，这样我们就可以把整个物体重建出来，也就是说我们要让这个网络过拟合某一个特殊的场景，其实这个MLP表示的就是这个场景本身。

  

在图(b)中，我们在不同视角下会有一ground truth(真值)，即不同视角下的图片。然后当图(b) output 中 2D 的投影与我们的真值吻合的时候，我们就可以认为这3D的modelling 建立得比较好。然后从input隐式3D，通过MLP,到2D的过程，这一流程其实也就是一个渲染的过程。用到了Volume Rendering, 并且整个pipeline是可导的，保证了rendering loss function 可以把梯度反向传播回到MLP，不断地去优化我们的模型，模型就会逐渐贴近我们的这个三维物体。

  

这个过程里面，有一点很重要，就是MLP这个模型，可以理解为物体本身，如果对应到Tesla 方案上，MLP就是道路本身(一个隐式表示)。

  

可能说的有点散了，我们现在来梳理一下，具体来说：

  

为什么要这么做呢？因为我们需要一ground truth 来给Tesla vision去训练， 然而我们又怎么去建立这个ground truth 呢？

  

答案：借鉴NeRF的思想，这过程有几处具有挑战的地方：

1\. 在场景重建的时候，我们需要获得每一个摄像头的位置信息，比如说我们需要知道每个摄像头的外参，这里TESLA可能是通过SLAM(camera+IMU)来获得相机在帧与帧之间的转移矩阵；

  

2\. 第二个挑战是要保证渲染的过程是一个可微渲染，这样才能对道路模型进行梯度优化。

Restructuring the Road 结果：重建的结果还是挺好的。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwo9oZ96X5ic5ZIhF93QpCLOQKXWTnEKxhr61SianEGyQeQ1UArCHPb0Pw/640?wx_fmt=png)

Restructuring the Road 结果
-------------------------

  

---

**● Static Objects 静态物体标注**
---------------------------

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwDS8VicTR6fUKPiaTEyFoaKYI9wb3ZfcPm5clywU9jmUHls6yDkGNJoibA/640?wx_fmt=gif)

‍  

整个静态物体的构建过程，其实就是一个SLAM，然后把地图重建出来。建完图后，我们可以把地图当作psudo lidar了，可以用lidar算法去做目标检测等任务。当然，也可以人工去标注，但tesla 大概率是大模型做auto labeling, 然后人工去做refine。

  

**● Dynamic Objects 动态物体标注**
----------------------------

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD48YvaFC1pcSkRJPXqyJaRmumXXMib3OnReLLfYzx11GzdkiblQqcGvoqVZicjbFGvDvw9uFRicj5giaNg/640?wx_fmt=jpeg)

  

对于动态物体的标注，如运动的车辆等：

1.首先第一个，用psudo lidar 的方式，构建出深度信息。tesla 在这方面估计会有很多大模型，并且利用自监督的深度估计算法去得到距离信息，据发布会说这效果也做得挺好。

  

2.利用radar，直接得出深度信息。因为在auto-labeling 的过程中，其实是离线的，所以可以用到前后帧的信息，即事件发生之前，与之后的信息模型都能知道，可以做一个全局优化。

  

并且在离线训练的状态下，也没有实时的要求，tesla 在这过程可以上一些复杂的算法，来达到更加好的效果。  

  

3\. 然后Tesla 通过 Static objects & Dynamic objects 的方法，对路面及行人信息做出标注。由于离线训练，可以知道当前帧前后的信息，所以即使行人被车挡住了，跟进时序信息，也可以追踪车后的行人。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD48YvaFC1pcSkRJPXqyJaRm5Bx6NaaWhNAURqWCRLHGl6fUdhjVNHWKCo6qZqOQ0R7kMWzQ7xY6sQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjw3UQYsxibeWeR91Amcfs1S8NJXtOyF4OHpsibnAnibEMLMHwaEqYvvM2Eg/640?wx_fmt=gif)

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

****车辆自动标注调研****

关于车辆标注，我们也找了一些自动化标注的资料：Zakharov, Sergey, et al. "Autolabeling 3d objects with differentiable rendering of sdf shape priors." CVPR 2020

  

详情请看：

https://www.youtube.com/watch?v=VQcDcYsWk00

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD48YvaFC1pcSkRJPXqyJaRmedX6mpjeAIHzgQH7cu7VhP7eo73I0dNEr7T6KTukgJ3NJ3ROLUaPFA/640?wx_fmt=jpeg)

  

TRI的这篇工作中，首先使用车辆的三维模型训练一个SDF模型(类似Nerf，也是三维场景的一种表示)，该SDF模型含有latent code(上图中的SDF vector)。通过修改latent code，可以控制车辆的形状，以生成不同的车型。

  

  

当获取到输入图像后，首先进行segmentation，并预估一个车辆的初始位置。根据车辆的初始位置及SDF模型，可以渲染出车辆在图像上的投影。结合车辆的segmentation，车辆位姿及其二维投影，可以构建出2D、3D两个loss。对loss做梯度下降，优化SDF vector及车辆位姿。

  

当车辆投影在二维上跟分割结果重合、三维上和lidar点重合时，车辆的形状及位姿较为准确，从而获取车辆的三维标注信息。作者使用该方法在KITTI数据集上生成的数据，在BEV指标下达到了人工标注的性能。

  

**● Auto-labeling Datasets 预览**
-------------------------------

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwe85UHHavVRDtpvEFiayibk0XWdhQnI2OXiaVmiaxljCNDKSHUJdvjibRe8A/640?wx_fmt=gif)

  

我们可以看到整个clip相当于对整个场景做三维重建了，然后最近有一趋势，即把车身信号，image，lidar point cloud, prediction, 等数据都整合到一起，形成一段video clip，这我比较方便我们去train multi-task model。

  

特斯拉的数据集包含了车的位置，行人的位置，以及周围场景信息，算是比较丰富的数据集。目前学术界所开源的自动驾驶数据集并没有这么丰富，例如waymo open datasets 普遍是一段一段的，perception and prediction模块之间的标注也没有集合到一起。Nuscene虽然有给到各种数据，但也不是那么让人满意。

  

这里我们PerceptionX 先宣传一波我们自建的数据集OpenLane，集合了当前自动驾驶数据集未涉及到的标注任务，是 community 首次推出真实场景 3D 车道线标注；同时也是规模最大的、同时包含了车道线和物体检测等内容，方便后续感知任务的扩展。

  

OpenLanes数据集下载链接：

https://opendatalab.com/OpenLane

（点击阅读原文查看）  

  

**● Removing radar:**
---------------------

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD48YvaFC1pcSkRJPXqyJaRmelXTqn1yAql6ibyncV7fIGOucQITa59hqc3bK0Ud6BiaQoibk6aU2f87Q/640?wx_fmt=jpeg)

  

这里仍然不得不提到特斯拉利用autolabeling pipeline在自动驾驶上去雷达的举措，相信有很多文章也提到过，radar跟camera在一些场景下会产生矛盾，例如在高速通过拱桥的时候，桥是静态物体，但路面的车是动态物体，radar检测到的桥容易mismatch并错误认为车也是静态物体，然后tesla自动驾驶在高速上减速了。

  

但这不是重点，重点是右边的部分，要去掉radar，就需要camera做得比radar要好，但在右边这种一系列的大雾场景，传统的相机做的检测、深度估计任务确实没有radar好，这种问题可以怎么解决呢？

  

Tesla 派了一庞大的车队，采集了1万+恶劣天气场景的video clips, 然后通过auto-labeling pipeline，一周内就标注完了，然后送到网络里面去训练，最后得到的效果如下所示：

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwPYib7ryLib0FibcKKLrpG80BR2OUR78hBSdBUcmjW506RYIU8uLgu4RWw/640?wx_fmt=gif)

  

正是因为特斯拉拥有开篇总结的三点自动标注的技术和要求，才能在短时间内收集大量且在特殊场景的数据，对数据进行快速(自动)标注，达到模型快速迭代，快速解决corner cases的效果，应对了第一段我们提到的“打造自动驾驶的数据闭环”中的核心技术。

  

  

来源：PerceptionX 知乎

https://www.zhihu.com/people/PerceptionX

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4SdbtPY3lAIre5yCb5zEjwiaUia6nCAibO72KzRcx9wEDmNrXkIFRqRHPoOaAcbw7mZmGGDeWEcIkQg/640?wx_fmt=png)

  

\- End -

  

**还有哪些你关心的话题？**

**扫码入群,欢迎交流** ![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6qKD9WCiaOd8HjSjiaMeTBNgCrp5PMqHnMAft2j0rj5bfyIzEajecZWhadWjhISZN7EquicHRHReYiaA/640?wx_fmt=png)

最新数据集上架动态

最全数据集内容解读

最牛大佬在线答疑

最活跃的同行圈子

……

  

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7NEyym4C8KBFplT20DM2vqAUAysVwzco8icviaYQ6McYIHep7ythBW0oZic97dXnhS6LbnoyibAqCbLQ/640?wx_fmt=jpeg)

添加小助手微信，发送“入群”，等待邀请

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言