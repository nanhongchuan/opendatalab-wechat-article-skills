     挑战更高难度的多目标跟踪，MOT20数据集使用指南 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

挑战更高难度的多目标跟踪，MOT20数据集使用指南
=========================

原创 专注于AI 数据的 OpenDataLab 2022-05-12 19:59 上海

> 原文地址: [https://mp.weixin.qq.com/s/yjU6ZRvrfNd1oPFZfBwTAQ](https://mp.weixin.qq.com/s/yjU6ZRvrfNd1oPFZfBwTAQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

上一期为大家介绍了多目标跟踪任务及其常用的数据集：[多目标跟踪（MOT）数据集资源整理分享](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247489152&idx=1&sn=d2c30825e40506bfd6e2b30a291f29b5&chksm=c10f8462f6780d745d2222d391bf52d76cf607be69e07ea99e794fbb6a076a0327ba3623e983&scene=21#wechat_redirect)。

  

其中最新发布的行人数据集MOT20，环境更复杂、人群更密集，任务难度更大。这一期，给想挑战的朋友，详细介绍一下。

  

**目录指引**

1\. 数据集简介

2\. 数据集详细信息

3\. 数据集任务定义及介绍

4\. 数据集结构解读

5\. 下载链接及可视化脚本

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**数据集简介**

**发布方：**Dynamic Vision and Learning Group at TUM Munich, Germany

  

**发布时间：**2020

  

**发布版本：**MOT20

  

**背景：**相比于此前的多目标跟踪（multi-object tracking）数据集，MOT20关注人群密集的场景，其视频最多可达单帧 246 人。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集详细信息**

**1\. 数据量及标注情况**

数据集共包含 8 个视频片段，分别来自三个不同的场景，4 个视频片段用于训练，4 个视频片段用于测试。每个视频片段均以视频帧的形式提供，8 个视频片段总共包含 13410 帧，其中训练视频 8931 帧，测试视频 4479 帧。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6eg5d28Cg8icuedjT8L8iaU3Pu8css40ROhpEwBibMQKpzoicDVwA5btcXCicHJfcbNeILVjWtM3muNYA/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6eg5d28Cg8icuedjT8L8iaU32mbhicyg3uU6SrTaspB03icEExDD43PuPubQP1UIhGMDnibbeaicohvwQA/640?wx_fmt=png)

  

数据集提供每个视频帧上的矩形框标注，其中测试数据的标注不公开。训练数据平均每帧包含 127.04 个行人（pedestrian）矩形框标注，测试数据平均每帧包含 115.52 个行人矩形框标注。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6eg5d28Cg8icuedjT8L8iaU3nX561BmZsH5Liars5rTUy2CILh5Q3oMOiastia9TOEuibYeaNhUIPKZDaQ/640?wx_fmt=png)

  

除了行人，数据集还包含其他类型的矩形框标注，如非移动交通工具（non motorized vehicle）等。在评测时仅考虑行人类型的标注，不考虑其他类型。

  

除了标注信息外，数据集作者在训练数据上训练了一个以 ResNet101 为 backbone 的 Faster R-CNN 作为 baseline，并提供训练和测试数据上逐帧检测行人的结果（注：在竞赛中，如果参赛者要使用基于检测的跟踪方法，只能使用官方提供的检测结果）。

**2\. 标注类别**

数据集的标注包含以下五种标注类别：

● Pedestrian

● Non motorized vehicle

● Static person

● Occluder on the ground

● crowd

  
**3\. 可视化**

下面是 MOT20-03 的原视频、标注结果、检测结果，平均每帧 130.42 个行人。

  

原视频

  

标注结果  

  

检测结果  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**数据集任务定义及介绍**

**多目标跟踪**
---------

**● 任务定义**

在给定的一段视频中识别与跟踪多个目标。（具体介绍可见：[多目标跟踪任务科普](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247489152&idx=1&sn=d2c30825e40506bfd6e2b30a291f29b5&chksm=c10f8462f6780d745d2222d391bf52d76cf607be69e07ea99e794fbb6a076a0327ba3623e983&scene=21#wechat_redirect)）

  

**● 评估**

**评估过程**

在第  帧，ground truth 为  ，预测结果 hypothesis 为

  ，其中每个  与每个  都属于一个特定的轨迹，即可能已经出现在此前的若干帧中。

  

对于  ，若交并比  ，则二者可建立关联（relationship），其中  为预设的阈值，在 MOT20 中为  。

  

若  在第  帧匹配（matched），且在第  帧可建立关联，则在第  帧直接进行匹配。

  

对于剩余未匹配的 ground truth 和 hypothesis，基于建立的关联关系，计算最大二分匹配。

仍未匹配的 ground truth 为 False Negative，仍未匹配的 hypothesis 为 False Positive。

若  与  匹配，且此前最近的一次匹配对象为  ，则  在第  帧发生一次 identity switch (IDSW)。

  

**指标**  

MOT20 竞赛所用的评价指标：

https://motchallenge.net/results/MOT20/

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6eg5d28Cg8icuedjT8L8iaU3HrBGHbrL44J8pJmicCp2QoYhpJjoXptWTEUibXjib3CmjxfJLh6DD6hIA/640?wx_fmt=png)

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

**数据集文件结构解读**

**1\. 目录结构**

    dataset_root

  

**2\. 元信息格式**

**● seqinfo.ini 文件内容如下：**

    [Sequence]

  

**3\. 标注格式**

**● gt.txt 标注格式如下：**

    1,1,199,813,140,268,1,1,0.83643

每行包含九个字段，用逗号分隔，含义如下：

**frame number**：帧号

  

**identity number**：物体编号，同一物体在整个视频片段中具有唯一的编号

  

**x\_min**：2D 矩形框左上角横坐标  

**y\_min**：2D 矩形框左上角纵坐标

  

**width**：2D 矩形框宽度

  

**height**：2D 矩形框高度

**flag**：当前标注在评估中是否被考虑，若 flag = 1，则考虑当前标注，若 flag = 0，则忽略。

  

**category**：标注物体类别 ID，数据集中出现的 ID 及对应类别包括：

    1: Pedestrian

    6: Non motorized vehicle

    7: Static person

    11: Occluder on the ground

    13: crowd

**visibility**：物体可见程度，取值在 0~1 之间，有些物体会被遮挡，取值越低，遮挡越严重。

  

**● det.txt 标注格式如下：**

    1,-1,757,692,96,209,1,-1,-1,-1

每行包含十个字段，用逗号分隔，前六个主要字段含义如下：

**frame number：**帧号

  

**此字段**恒为 -1

  

**x\_min**：2D 矩形框左上角横坐标

  

**y\_min**：2D 矩形框左上角纵坐标

  

**width**：2D 矩形框宽度

  

**height**：2D 矩形框高度

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

**下载链接及可视化脚本**  

OpenDataLab平台已经上架了MOT20数据集，为大家提供了完整的数据集信息、流畅的下载速度、可视化脚本、快来体验吧！  

  

**1\. MOT20数据集资源**

https://opendatalab.com/70

  

**2\. MOT20数据集可视化**

    import argparse

**参考资料：**

\[1\]Dendorfer, P., Rezatofighi, H., Milan, A., Shi, J., Cremers, D., Reid, I., Roth, S., Schindler, K. & Leal-Taixé, L. MOT20: A benchmark for multi object tracking in crowded scenes. arXiv:2003.09003\[cs\], 2020., (arXiv: 2003.09003).

\[2\]https://motchallenge.net/data/MOT20/

  

  

  

\- End -

  

  

**还有哪些你关心的话题？**

**扫码入群,欢迎交流 ![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6qKD9WCiaOd8HjSjiaMeTBNgCrp5PMqHnMAft2j0rj5bfyIzEajecZWhadWjhISZN7EquicHRHReYiaA/640?wx_fmt=png)** 

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