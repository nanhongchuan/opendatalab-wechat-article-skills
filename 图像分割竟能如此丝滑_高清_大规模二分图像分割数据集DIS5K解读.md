     图像分割竟能如此丝滑、高清？大规模二分图像分割数据集DIS5K解读 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

图像分割竟能如此丝滑、高清？大规模二分图像分割数据集DIS5K解读
=================================

原创 专注于AI 数据的 OpenDataLab 2022-10-27 16:00 上海

> 原文地址: [https://mp.weixin.qq.com/s/2kT0GVvuoDXLA9KRrG2UHg](https://mp.weixin.qq.com/s/2kT0GVvuoDXLA9KRrG2UHg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

**近期，苹果手机 iOS 16正式发布，其中“一键”提取图像主体功能让人眼前一亮，让我们看到了 AI 高效抠图的无限可能。**

**如果这个技术能泛化到工业场景、3D建模、3D渲染等使用，那将极大提高工作效率和效果。**

**今天，就来给大家介绍一个具有高精度标注的数据集DIS5K，可用于高精度的模型训练。快来看看吧。**

**目录指引**

  

1\. 数据集简介

2\. 数据集详细信息

3\. 数据集任务定义及介绍

4\. 数据集文件结构解读

5\. 总结

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**数据集简介**

**发布方：**

**MBZUAI, TUM, ETH Zurich, Terminus Group**

**发布时间：****2022**  

**官网：**

**https://xuebinqin.github.io/dis/index.html**

**Github：**

**https://github.com/xuebinqin/DIS**

**背景：****旨在从自然图像中分割出高精度的物体。**  

**简介：******目前，由于准确性和鲁棒性问题，大多数分割模型在那些对准确性和鲁棒性要求很高的应用中仍然不太适用，如：手术机器人，制造业等，这限制了分割技术在更广泛的应用中发挥更重要的作用。****

****为了解决这个问题，图像二类分割(Dichotomous Image Segmentation, DIS)作为一项新的任务被提出，该任务旨在从自然图像中分割出高精度的物体。与语义分割相比，提出的 DIS 任务通常侧重于具有单个或几个目标的图像，这使得从中获得每个目标的更丰富准确的细节更加可行。****

****为了研究DIS任务，研究人员创建了******一个大规模、可扩展的DIS数据集****DIS5K******，该数据集包含 5,470 张高分辨率图像和高精度的二值分割掩码。对DIS任务和DIS5K数据集的研究有助于多个应用方向的发展，如：图像去背景，艺术设计，模拟视图运动，基于图像的AR应用，基于视频的AR应用，3D 视频制作等。****

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD5T593XEGnasxNKqObHicsKN6HNVJfRqnTmoKQ4eERPGBd60DOr3raL6O1aowLyI7UAe6UApdVh2jg/640?wx_fmt=jpeg)图片来源：https://github.com/xuebinqin/DIS

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集详细信息**

**2.1 标注数据量**

**训练集**：3000张图像  

**验证集**：470张图像

**测试集**：共计2000张图像，分为四个子集，测试难度级别依次递增。具体来说，首先将2000幅测试图像按照其结构复杂性IPQ和边界复杂性Pnum的乘积 (IPQ × Pnum) 升序排序。然后，将 DIS-TE分为4个子集 (即, DIS-TE1∼DIS-TE4)，每个子集包含500张图像，代表4个测试难度等级。

  - DIS-TE1: 500张图像

  - DIS-TE2: 500张图像

  - DIS-TE3: 500张图像

  - DIS-TE4: 500张图像

  

**2.2 标注类别**

分为22个组，共计225个类别。标注类别的可视化图如下：

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD42Eiccice1Avozy3mGORJaUwTRlDBlkAtmagl15I08V5sq3fgdJYflbYPeKcm9UFPRPUg3zDYib2lMg/640?wx_fmt=jpeg)图片来源：https://xuebinqin.github.io/dis/index.html

**2.3 可视化**

标注的可视化效果如下所示：

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD42Eiccice1Avozy3mGORJaUwbGbpGvmCI2UL9gEkDMRhX06v6ufQgSCNyPMiau1ARaz0YhHcuVc5cqQ/640?wx_fmt=jpeg)图片来源：https://xuebinqin.github.io/dis/index.html

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**数据集任务定义及介绍**

本小节介绍了图像二类分割，并与语义分割进行了对比，方便读者理解两者之间的异同点。

  

**3.1 语义分割**
------------

**● 任务定义**

语义分割是将整个图像密集地分割成语义类，其中每个像素都被分配一个类标签，例如树的区域和建筑物的区域。

  

示例图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD42Eiccice1Avozy3mGORJaUwm6ePZQzuGiaIaIAxYsNvMsoOL0sY2svukTVicfs5AKrgkZpd7aYp3BJA/640?wx_fmt=png)图片来源：https://zhuanlan.zhihu.com/p/422122048

**●** **评价指标**

通常用于语义分割的四个指标：

– **Pixel Accuracy**（像素准确度，PA），表示正确分类的像素的比例；

  

– **Mean Pixel Accuracy**（平均像素准确度，MPA），表示所有类别中正确分类的像素比例的平均。

  

– **Mean Intersection over Union**（平均交并比，MIoU），表示预测像素和真实像素之间的交并比，在所有类上平均。

  

– **Weighted IoU**（加权交并比，WIoU），表示按每个类的总像素比加权的交并比。

  

**2\.** **图像二类分割**
------------------

**● 任务定义**

图像二类分割是将图像分割成前景和背景，前景就是某个类别的物体，背景就是除了这个物体外的所有像素都当做背景。

  

DIS5K的每张图像是采用像素级精度手工标记。平均每张图像的标记时间约 30分钟，有些图像的标记时间长达10小时。值得注意的是，有些标注的真值(GT)掩码在视觉上接近图像抠图真值。标注对象有透明的和半透明的，并采用高达单个像素的二进制掩码进行标记。这也体现了标注的高精度，是能够让模型预测出高精度物体的前提。  

  

示例图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD42Eiccice1Avozy3mGORJaUwO0Lb9wBAcSvJNzSHPxFKiao3rl7ZF8BibXChibsicTVw7VSgV9KGUdGoAQ/640?wx_fmt=png)图片来源：https://xuebinqin.github.io/dis/index.html

说明: Image:原始图像，GT:标注的png图像，Ours：预测的结果。

  

****●** **评价指标****

为了提供相对全面和无偏的评估，本文采用6个不同的度量，从不同的角度来评估模型性能。包括：

\- **最大F-measure**(F mx β ↑) \[1\]

\- **加权F-measure**(F w β ↑)\[1\]

\- **平均绝对误差**(M ↓) \[4\]

\- **结构度量**(Sα ↑)\[2\]

\- **平均增强对准度量**(Em ϕ ↑)\[3\]

\- **人工矫正量**(HCEγ ↓)

  

这里重点介绍一下**人工矫正量HCE**指标，其他的指标可以参考相关的论文。

  

给定一个预测分割概率P ∈ R(W×H×1)及其对应的GT掩码G ∈ R(W×H×1)，现有的指标，如 IoU、边界IoU、F-measure\[1\]、边界F-measure和MAE\[4\]，一般通过基于P和G之间的数学或认知一致性 (或不一致性) 计算得分来评价预测结果P的质量。换句话说，这些指标描述了P和G之间的“差距”有多显著。然而，在许多应用中，评估填补“缺口”的成本比衡量“缺口”的大小更重要。

  

人工校正量(HCE)，它衡量了在现实应用中校正错误预测结果以满足特定的精度要求所需的人力。根据本文的标注经验，常用的操作主要有两种:(1)沿目标边界点的选取，形成多边形；(2)基于区域内相似像素强度的区域选择。这两个操作都对应于一次鼠标点击。

  

因此，这里的HCE是由鼠标点击次数来量化的。为了纠正错误的预测掩模，操作人员需要沿着错误预测目标的边界或区域手动采样主导点，以纠正假阳性(FP)和假阴性(FN)区域。

  

如下图所示，FNs和FPs根据其相邻区域可分为  、  、  和  两类。

  

为了校正  区域，其与TN相邻的边界需要人工标记主导点(下图中-b)。同样，为了校正  区域，本文只需要在TP区域附近标注其边界即可(下图中-d)。TP包围的  区域(下图中-c) 和TN包围的  区域 (下图中-e)，可以通过一键选择区域，轻松校正。因此，修正下图中 (b-e)中故障区域的 HCE为10(在(b)和(d)中需要点击6次和2次，在(c)中需要点击1次，在(e)中需要点击1次)。  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD42Eiccice1Avozy3mGORJaUwrPSQeQ93jwicl3UcDR1ia7UeCr70uMtXia3mI9Jf6DAcic3h52aKhwOCnw/640?wx_fmt=png)图片来源：https://arxiv.org/pdf/2203.03041.pdf

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

**数据集文件结构解读**

****4.1 数据集目录结构****

    dataset_root/

**（左右滑动查看）**

**4.2 标注文件****格式**

标注的内容存放在两个位置：  

**a. 文件名称中隐含一部分标注内容。**

仅以一个具体的文件名称为例进行说明。例如：文件名为"9#Entertainment#5#Swing#341645836\_03035b9697\_o.jpg"的文件，以"#"作为分割符，可以分割成一个数组,假设数组名称为arr。则arr内容如下：

    arr = ["9", "Entertainment", "5", "Swing", "341645836_03035b9697_o.jpg"]

**（左右滑动查看）**

arr\[0\]: 组别id, 这里的值是"9"

arr\[1\]: 组别名称，这里的值是"Entertainment"

arr\[2\]: 当前组别内的类别id,这里的值是"5"

arr\[3\]: 当前组别内的类别名称，这里的值是"Swing"

arr\[4\]: 当前文件的名称的唯一标识。

  

说明：该数据集共计22个分组，分组id从1开始，所以组别id的值范围是\[1, 22\]

  

每个分组内的类别个数不固定，但是类别id的值都是从1开始，假设组别m内有n个类别记为变量g\_m\_n,则组别m内类别id值的范围是\[1, g\_m\_n\]。

  

**b. 图像分割标注采用png格式，存储在对应的png图片中。**

还以文件名为"9#Entertainment#5#Swing#341645836\_03035b9697\_o.jpg"的文件为例，对应的png文件为对应的gt目录的"9#Entertainment#5#Swing#341645836\_03035b9697\_o.png"，读取这个png图片内容，展示如下：  

    # png内容如下：

9#Entertainment#5#Swing#341645836\_03035b9697\_o.jpg和对应的png标注可视化如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD42Eiccice1Avozy3mGORJaUwBb4IRht3wg0zDOx6OCBRUc5ofyE1fZAyYgMTeRZx7YxH2cVVjJhX3g/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD42Eiccice1Avozy3mGORJaUwicq9vShibFPuLSr1bqovicuoqv9suNGoOaLQZX9LicnUGEXrdsl7z5iaTjg/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

**总结**

DIS5K是一个大规模、可扩展的 DIS 数据集，DIS 任务侧重于具有单个或几个目标的图像，这有利于从中获取更丰富准确的细节。

  

该任务的目的是从自然图像中分割出高精度的对象。这项工作将会极大促进有精细分割要求的应用。

  

**参考资料**

\[1\] Margolin, Ran, Lihi Zelnik-Manor, and Ayellet Tal. "How to evaluate foreground maps?." Proceedings of the IEEE conference on computer vision and pattern recognition. 2014.

\[PDF\]https://openaccess.thecvf.com/content\_cvpr\_2014/papers/Margolin\_How\_to\_Evaluate\_2014\_CVPR\_paper.pdf

  

\[2\] Fan, Deng-Ping, et al. "Structure-measure: A new way to evaluate foreground maps." Proceedings of the IEEE international conference on computer vision. 2017.

\[PDF\]https://arxiv.org/pdf/1708.00786.pdf

  

\[3\] Fan, Deng-Ping, et al. "Enhanced-alignment measure for binary foreground map evaluation." arXiv preprint arXiv:1805.10421 (2018).

\[PDF\]https://www.ijcai.org/proceedings/2018/0097.pdf

  

\[4\] Qin, Xuebin, et al. "Basnet: Boundary-aware salient object detection." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2019.\[PDF\]https://openaccess.thecvf.com/content\_CVPR\_2019/papers/Qin\_BASNet\_Boundary-Aware\_Salient\_Object\_Detection\_CVPR\_2019\_paper.pdf

  

\[5\] Qin X, Dai H, Hu X, et al. Highly Accurate Dichotomous Image Segmentation\[J\]. arXiv preprint arXiv:2203.03041, 2022.

\[PDF\]https://arxiv.org/abs/2203.03041

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD6qphXr7bQ0U7ic1ntZ7MDWicGcqPIst1vpnqNLwViamgdvtSbK1xtlDYSA9XgohzFVRqUPbPePDqd0g/640?wx_fmt=jpeg)

**作者丨******杜坤明****

有智者，万事兴

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