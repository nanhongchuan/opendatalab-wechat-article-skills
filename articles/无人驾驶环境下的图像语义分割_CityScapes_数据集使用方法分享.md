     无人驾驶环境下的图像语义分割 CityScapes 数据集使用方法分享 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

无人驾驶环境下的图像语义分割 CityScapes 数据集使用方法分享
===================================

原创 专注于AI 数据的 OpenDataLab 2022-06-14 18:15 上海

> 原文地址: [https://mp.weixin.qq.com/s/AhUQ7VMVwaFSnQpRB7qMcg](https://mp.weixin.qq.com/s/AhUQ7VMVwaFSnQpRB7qMcg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD7DYzsibeib72U1ZfgFhMIWsXqvt2ILN8Lniarq1Wnf1GqU1BO5IDnZ2xJicSLchAmZWNkWM1aFyPXzkg/640?wx_fmt=gif)

  

  

CityScapes是目前自动驾驶领域最具权威性和专业性的图像语义分割评测集之一，其关注真实场景下的城区道路环境理解，任务难度更高且更贴近自动驾驶等热门需求。

  

今天就带大家一起来看看。

  

**目录指引**

  

1\. 数据集简介

2\. 数据集详细信息

3\. 数据集任务定义及介绍

4\. 数据集结构解读

5\. 数据集下载链接

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**数据集简介**

**发布方：**Daimler AG R&D, TU Darmstadt, MPI Informatics

  

**发布时间：**2015

  

**背景：**

聚焦于城市街道场景的语义理解。

  

**简介：**

CityScapes数据集有以下特点：

● **标注多样**，包含实例分割、语义分割、多边形框等三种标注；

● **类别复杂**，30+类别，同时包含group和class两个维度描述；

● **场景差异**，涵盖50个城市、不同季节、不同时段（白天）；

● **体量庞大**，拥有5000精标注图片和20000粗标注图片。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集详细信息**

**1\. 标注数据量****（以精标注为例）**

**训练集：**2975张图像

****验证集：**500张图像**

**测试集：**1525张图像

  

这里每一张图片都同时拥有三个标注文件（实例分割、语义分割、多边形框标注）。

  

**2\. 标注类别**

标注的30+类别及其所在的组如下所示：

  

Group

Class

flat

road · sidewalk · parking+ · rail track+

human

person\* · rider\*  

vehicle

car\* · truck\* · bus\* · on rails\* · motorcycle\* · bicycle\* · caravan\*+ · trailer\*+

construction

building · wall · fence · guard rail+ · bridge+ · tunnel+

object

pole · pole group+ · traffic sign · traffic light

nature

vegetation · terrain

sky

sky

void

ground+ · dynamic+ · static+

  

其中，\*表示部分区域连在一起的实例，会作为一个整体来标注，比如"car group"；+表示该类别不包含在验证集中，并被视为无效的。

  

**3\. **可视化****

精标注的可视化效果如下所示：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6jy7tz44BpDib66D60FoO7JMGtLaSmAlB3IVSMRXbjagqpTe2aDPgiaPW6N63UaGDH1Dj7da25teKw/640?wx_fmt=png)

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**数据集任务定义及介绍**

**1\. 语义分割**
------------

**● 任务定义**

场景解析是将整个图像密集地分割成语义类，其中每个像素都被分配一个类标签，例如树的区域和建筑物的区域。

  

**●** **场景解析评价指标**

通常用于语义分割的四个指标指标：

**Pixel Accuracy（像素准确度，PA）**：表示正确分类的像素的比例。

  

**Mean Pixel Accuracy（平均像素准确度，MPA）**：表示所有类别中正确分类的像素比例的平均。

  

**Mean Intersection over Union（平均交并比，MIoU）**：表示预测像素和真实像素之间的交并比，在所有类上平均。

  

**Weighted IoU（加权交并比，WIoU）**：表示按每个类的总像素比加权的交并比。

  

**2\. 实例分割**
------------

**●** **任务定义**

实例分割是检测图像中的对象实例，并进一步生成对象的精确分割掩码。它与场景解析任务的不同之处在于，场景解析中没有分割区域的实例概念，而在实例分割中，如果场景中有三个人，则需要网络对每个人区域进行分割。

  

**● 实例分割评价指标**  

实例分割一般有以下几个评价指标：

**Average Precision（平均精度，AP）**：准确率的平均值，其中准确率P = TP/（TP+FP）。

  

**Pixel Accuracy（像素准确度，PA）**：表示正确分类的像素的比例。

  

**Mean Pixel Accuracy（平均像素准确度，MPA）**：表示所有类别中正确分类的像素比例的平均。

  

**Mean Intersection over Union（平均交并比，MIoU）**：表示预测像素和真实像素之间的交并比，在所有类上平均。

  

**Weighted IoU（加权交并比，WIoU）**：表示按每个类的总像素比加权的交并比。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

**数据集文件结构解读**

**1\. 目录结构**

目录结构（这里以精标注的为例）：

    dataset_root/

  

**2.** **标注格式**

Cityscapes数据共有两种标注格式，分别是实例分割及语义分割所采用的**分割图格式（.png文件）**，以及**多边形边框的json格式（.json文件）**。

**其中，png文件为灰度图片，尺寸和原始图片尺寸相同，其像素上的灰度值对应原始图片对应像素的类别id（或实例id），实例分割图中实例id对应的类别id则需要同时结合语义分割图中相同像素坐标的类别id来获取。**

**分割图的可视化效果图可参考前文可视化部分。**

**json标注的文件格式如下所示：**

    {

  

**其中包含的字段如下：**

属性名称

含义

数据类型

imgHeight

图像高度

int

imgWidth

图像宽度

int

objects

实例列表

list

label

类别名称

str

polygon

边界点坐标

list

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

**数据集下载链接**

OpenDataHub平台为大家提供了CityScapes数据集完整的数据集信息、直观的数据分布统计、流畅的下载速度、便捷的可视化脚本，欢迎体验。

  

点击原文链接可查看。

https://opendatalab.com/CityScapes

  

  

**参考资料**

\[1\]官网：https://www.cityscapes-dataset.com/  

\[2\]论文：M. Cordts, M. Omran, S. Ramos, T. Rehfeld, M. Enzweiler, R. Benenson, U. Franke, S. Roth, and B. Schiele, The Cityscapes Dataset for Semantic Urban Scene Understanding, in CVPR, 2016.

(论文下载链接：https://www.cityscapes-dataset.com/wordpress/wp-content/papercite-data/pdf/cordts2016cityscapes.pdf）

\[3\]Github：https://github.com/mcordts/cityscapesScripts

  

  

  

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