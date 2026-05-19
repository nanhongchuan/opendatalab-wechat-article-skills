     TrackingNet：最经典大规模、多样化的单目标跟踪数据集 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

TrackingNet：最经典大规模、多样化的单目标跟踪数据集
===============================

原创 专注于AI 数据的 OpenDataLab 2022-07-07 20:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/0PtZFblv1jpXwqS8uF6akw](https://mp.weixin.qq.com/s/0PtZFblv1jpXwqS8uF6akw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

  

除了多目标跟踪任务外，研究经典的、通用的单目标跟踪任务对于整个跟踪领域的发展有重要意义。

  

本期给大家介绍一个包含包含超过３万个视频，共有27个目标类别，视频数量和标注数量比以往的跟踪数据集更大的数据集——TrackingNet。该数据集进行了训练集和测试集的划分，提供的大规模训练视频能够有效地缓解当前跟踪领域的训练数据不足的问题。

  

**目录指引**

  

1\. 数据集简介

2\. 数据集详细信息

3\. 数据集任务定义及介绍

4\. 数据集文件结构解读

5\. 数据集下载链接

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**数据集简介**

**发布方：King Abdullah University of Science and Technology**

  

**发布时间：**2018

  

**背景：**

**作者发现当前的目标跟踪社区缺少一个大规模的自然场景下专门用于训练目标跟踪模型的数据集；现有的数据集很多没有明确的训练集/测试集的划分。**

  

**简介：**

TrackingNet是一个大规模的目标跟踪数据集，包含了30643个视频片段，平均每个视频片段时长16.6s。从140个小时提取的14431266帧图像都使用了bounding box进行标注。

  

TrackingNet比之前的最大的同类型数据集大两个数量级以上。该数据集囊括了自然场景下的各种情形，包含了各种帧率，分辨率，上下文场景以及目标类别。与之前的目标跟踪数据集不同，TrackingNet分为训练集和测试集两部分，作者仔细地从Youtube-BoundingBoxes中选择了30132个训练视频，并且自己构建了511个与训练集分布相似的视频构成测试集。

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集详细信息**

**1\. 标注数据量**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7G8ErOF1wXQnInHXNCz48CU2Hv5jp4QSOUdSH5xJo3OKzncHyNJQEnxOX3TRWHqE3zmtuyVSEXew/640?wx_fmt=png)

  

与其他数据集的对比情况如下图，图中横坐标为数据集中视频数量，纵坐标为视频的平均帧数，圆形的尺寸与数据集中标注的bounding box数量成正比：  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7G8ErOF1wXQnInHXNCz48CkicaghTugj7wtuRaPUne4LARWoiaKxgzSn9mZR1cpv23c5nicaRCkrtCQ/640?wx_fmt=png)

  

**2\. 标注类别**

尽管数据集中被标注的目标包含了多个类别，但是在TrackingNet的标注文件中只提供了矩形框标注，并没有提供每个目标的类别。

  

**3\. 数据集的构建方式**

**● 从YT-BB中构建训练集**

Youtube-BoundingBoxes（YT-BB）是一个用于目标检测的大规模数据集，其中包含了大约380000个视频片段，每一帧都标注了bounding box，这些视频直接从YouTube上采集，涵盖了各种分辨率，帧率和时长。

  

YT-BB中包含了23个目标类别，为了构建目标跟踪数据集，作者将其中不会运动类别（盆栽、厕所）排除。由于person类别占了所有标注数量的25%，作者根据其上下文场景，将person类别细分为了7个不同的类别，最终，TrackingNet的目标类别统计情况如下图所示：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7G8ErOF1wXQnInHXNCz48CqwYKcuqJAOne6s0LKW6dBwcpV539Zibs2UJfdfsbJEUQ4ohrYSjMsuw/640?wx_fmt=png)

  

为了保证数据集中视频的质量，作者按照下述步骤过滤掉了90%的视频，具体步骤为：

1\. 过滤掉时长小于15秒的视频；

2\. 只保留覆盖图像范围不超过50%的bounding box；

3\. 只保留包含的的bounding box有合理移动量的视频片段。

  

经过上述过滤后，最终训练集中共有320132个视频片段，这些片段被分到了12个训练子集当中，每个子集包含了2511个视频，每个子集都保留了原始的YT-BB的类别分布。

  

原始的YT-BB的标注是粗粒度的，只有1fps，为了提高标注密度，作者使用DCF tracker将视频每秒间的前向跟踪结果和后向跟踪结果进行加权平均得到最终的细粒度标注结果。

  

**●** **从YT-CC中构建测试集**

出来训练集，作者还构建了一个全新的数据集用来测试，其中包含了511个视频，这些视频是从YouTube上采集的，能够反映出训练集目标类别的分布情况，每个视频都遵循了Creative Commons licence，所以作者将该数据集简写为 YT-CC。

  

然后作者使用了 Amazon Mechanical Turk workers 和 VATIC 工具，将 YT-CC 进行细粒度的标注，最终构建出了 TrackingNet 测试集。

  

TrackingNet 测试集中，每个视频都被标注了一些属性，属性列表如下：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7G8ErOF1wXQnInHXNCz48CpH9sajfMhcS136goiaCiaibTJHwBquDfaoTicBzpM8IXyqd2o4K6o1Uxjg/640?wx_fmt=png)

  

其中前5个属性是通过分析视频中的bounding box的变化自动标注的，后10个属性则是通过人工标注的。测试集的属性标注方便研究者更好地分析模型在不同场景下的效果。数据集中这15个属性的分布情况如下图所示：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7G8ErOF1wXQnInHXNCz48Cc378Cfar9bKZtKEY7zqCXZ6x8TaVgxQcicEeNEpCntKm6FvudQGPicrQ/640?wx_fmt=png)

  

**4\. 可视化**

每段视频都在每一帧用矩形框标注一个单目标：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7G8ErOF1wXQnInHXNCz48CUoibh7qt7EXlqsWVn41xHjG0Ra57T3mvRtMdH7exApicIFadU8XK3oDQ/640?wx_fmt=png)

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**数据集任务定义及介绍**

**1\.** **单目标跟踪**
-----------------

**● 任务定义**

在单目标跟踪（Single Object Tracking, SOT）任务中，在视频的第一帧中会给出目标的bounding box，模型的目标则是在视频的后续所有帧中定位该指定目标，因此单目标跟踪任务属于detection-free 跟踪任务。

  

**●** **评价指标**

**success（S）**，该分数通过计算ground truth和prediction bounding box的IoU得到，计算公式如下：  

其中  为模型预测的bounding box，  为ground truth bounding box。在验证模型时，会根据不同的IoU阈值（在文中称为Overlap threshold），计算出对应阈值的success rate，并画出横坐标为阈值，纵坐标为success rate的曲线，最终通过该曲线的AUC来对模型的性能进行排序。

  

* * *

**precision（P）**，该分数通过计算ground truth和prediction bounding box中心点之间的距离得到，计算公式如下：

其中  为模型预测的bounding box的中心坐标，  为ground truth bounding box的中心坐标。在验证模型时，会根据不同的距离阈值（在文中称为Location error threshold），计算出对应阈值的precision，并画出横坐标为阈值，纵坐标为precision的曲线，最终通过阈值为20的precision来对模型的性能进行排序。

  

* * *

  

**normalized precision**（  ），该分数使用ground truth bounding box的尺寸对precision   进行标准化，计算公式如下：

其中  表示构建对角矩阵，  ，  分别是ground truth bounding box的横坐标和纵坐标。在验证模型时，会根据不同的normalized precision阈值（在文中称为Normalized distance error threshold，范围限制在0到0.5之间），计算出对应阈值的precision，并画出横坐标为阈值，纵坐标为precision的曲线，最终通过该曲线的AUC来对模型的性能进行排序。

  

各模型在TrackingNet上的表现：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7G8ErOF1wXQnInHXNCz48CyibcXvExkYDBiacWgHSt5S47e4NOPt3FlSWicVRicvibueu0tlyLw5EMFwA/640?wx_fmt=png)

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

**数据集文件结构解读**

**1\. 数据集存在的问题**

● 只提供了目标的矩形框，未提供目标的类别，视频的属性等信息；

● 测试集未提供全部帧的标注，只提供了每个测试视频的第一帧的矩形框标注信息，如果要在测试集上测试，需要将模型在测试集上的推理结果上传到http://eval.tracking-net.org/featured-challenges/39/participate才能查看验证结果。

  

****2\. 数据集目录结构****

首先需要对初始的数据集压缩文件进行解压，解压脚本如下：

    #!/bin/bash

（左右滑动查看）  

  

**解压后的数据集目录结构如下：**

    dataset_root/                   # 数据集中包含了TEST，TRAIN_0，TRAIN_1，...，TRAIN_11，一共13个目录，代表了一个测试集和12个训练子集

**（左右滑动查看）**

**3\. 标注文件****格式**

**● 训练集标注文件格式**

在 TRAIN\_0 到 TRAIN\_11 的12个训练集目录中，每个标注 .txt 文件都提供了其对应视频的每一帧的矩形框标注，具体格式如下：

    308.00, 1.00,173.00,275.00

每一行为视频的对应帧中目标的矩形框的 \[x,y,w,h\]，即矩形框左上角的横坐标，纵坐标与矩形框的宽和高。

  

**● 测试集标注文件格式**

在测试集TEST目录中，每个标注 .txt 文件只提供了对应视频的第一帧的矩形框的标注，具体格式如下：

    1,79,307,186

表示视频第一帧中的目标的矩形框的 \[x,y,w,h\] ，即矩形框左上角的横坐标，纵坐标与矩形框的宽和高。

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

**数据集下载链接**

OpenDataLab平台为大家提供了‍TrackingNet数据集完整的数据集信息、直观的数据分布统计、流畅的下载速度、便捷的可视化脚本，欢迎体验。击原文链接可查看。‍

  

https://opendatalab.com/TrackingNet/download

  

  

  

**参考资料**

\[1\]官网：https://tracking-net.org/

\[2\]论文：M Muller, A Bibi, S Giancola, et al. Trackingnet: A large-scale dataset and benchmark for object tracking in the wild, in ECCV, 2018: 300-317.

(PDF下载链接：‍https://arxiv.org/abs/1803.10794）

\[3\]下载：https://drive.google.com/drive/folders/1gJOR-r-jPFFFCzKKlMOW80WFtuaMiaf6

  

  

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