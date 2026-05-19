     手把手教你，Stanford Drone 数据集的正确打开方式 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

手把手教你，Stanford Drone 数据集的正确打开方式
===============================

原创 专注于AI 数据的 OpenDataLab 2022-05-26 18:20 上海

> 原文地址: [https://mp.weixin.qq.com/s/Qf4aficPPQNooYuGC-VeGg](https://mp.weixin.qq.com/s/Qf4aficPPQNooYuGC-VeGg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

前面几期，为大家介绍了[多目标跟踪任务及数据集资源](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247489152&idx=1&sn=d2c30825e40506bfd6e2b30a291f29b5&chksm=c10f8462f6780d745d2222d391bf52d76cf607be69e07ea99e794fbb6a076a0327ba3623e983&scene=21#wechat_redirect)，也梳理了[无人机与AI结合的相关应用](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247490676&idx=1&sn=d6be72fdb975a5f539ca9a399ac91e1c&chksm=c10f8e96f678078055faf81f51c31407a4eccb47ff4054801daedf62424c391fd467b9e99448&scene=21#wechat_redirect)。

  

其中，采用灵活轻便、视角开阔的无人机进行多目标跟踪任务已经成为一大研究热点，其可以广泛应用于智能交通、智能安防等场景。

  

在做无人机多目标跟踪相关模型训练时，我们经常会用到 Stanford Drone 数据集，这一期，就给大家详细解读一下。

  

**目录指引**

  

1\. 数据集简介

2\. 数据集详细信息

3\. 数据集任务定义及介绍

4\. 数据集结构解读

5\. 数据集下载链接

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**数据集简介**

**发布方：**Stanford University Computational Vision and Geometry Lab (CVGL)

  

**发布时间：**2016

  

**发布版本：**08/01/2016

  

**背景：**

作者发现以往的数据集存在以下的问题：

1\. 只收集某个目标类别的移动轨迹；

2\. 只收集某些交互方式下的数据；

3\. 在人为的场景下收集。

  

因此作者收集这批数据用于研究**多真实场景多目标类别下人们的轨迹模式。**

  

**简介：**

Stanford Drone 数据集使用无人机在校园拥挤的时间段以俯视的方式收集了8个不同的场景下20k个物体的轨迹交互信息，每个物体的轨迹都标注唯一的 ID ，使得该数据集十分适合用于：

  

**1\. 目标轨迹预测；**

**2\. 多目标跟踪。**

  

（网站和文章在这个部分的描述会有所不同，文章里说收集了6个场景，后面应该扩展成8个，所以网站描述为8个场景，现在能下载到的数据集也是包含8个场景的数据）

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集详细信息**

**1\. 数据量及标注情况**

数据集的所有数据都是有标注的。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5icjG8Hibksgq77nfBxGwjjyb0UnIjibQK2EzBKiaggmWck3T8bJtL8KicZPAYAQGyKmGy4UQpEib4d8QA/640?wx_fmt=png)

  

**2\. 标注类别**

数据集的标注包含6个类别：

● Biker: 骑单车的人

● Pedestrian: 行人

● Skater: 用滑板的人

● Cart: 拉手推车的人

● Car: 汽车

● Bus: 巴士

  
**3\. 可视化**

每个目标都会有一个 2D 框标注，并且带有该目标的类别和唯一 ID。在图中不同的类别用不同的颜色标识。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD5icjG8Hibksgq77nfBxGwjjygTFw09T0WzcZBCIicGNj8gNJTpIt3UanFPV8vlGFEvIRqARtXLjs1uA/640?wx_fmt=jpeg)

图1：场景为 Gates 下的样例图

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**数据集任务定义及介绍**

**1\. 轨迹预测**
------------

**● 轨迹预测定义**

给定一段时间内目标已知的移动轨迹，预测未来一段时间内目标的位置。

  

**● 轨迹预测评价指标，由以下三个指标构成**

a. 整个预测轨迹的误差

b. 最后预测点的误差

c. 由于躲避碰撞而产生轨迹偏移的误差

  

**2\. 多目标跟踪**
-------------

**● 多目标跟踪定义**

给定需要检测的目标一段时间内的视频数据，需要先逐帧检测出目标，然后将各个帧的目标检测结果连接形成轨迹。（具体介绍可见：[多目标跟踪任务科普](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247489152&idx=1&sn=d2c30825e40506bfd6e2b30a291f29b5&chksm=c10f8462f6780d745d2222d391bf52d76cf607be69e07ea99e794fbb6a076a0327ba3623e983&scene=21#wechat_redirect)）

  

**● 多目标跟踪评价指标构成**

**a. 多目标跟踪准确率（MOTA）：**

主要考量假阳性（False positives），目标丢失（Missed targets）和标识改变（Identity switches）的情况。

  

**b. 多目标跟踪精确度（MOTP）：**

主要考量真实目标与预测目标的平均距离。

  

**c. 主要跟踪和主要丢失（MT & ML）：**

计算主要（多于80%的帧里）跟踪的轨迹数量和主要（少于20%的帧里）已丢失的轨迹数量。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

**数据集文件结构解读**

**1\. 目录结构**

    Stanford Drone dataset

‍

  

**2\. 标注文件内容样例及内容解析**

    0 211 1038 239 1072 10005 1 0 1 "Biker"

    标注文件内容从左到右的字段对应以下由上到下的字段：

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

**数据集下载链接**  

**1\. 原数据集格式问题**

数据为CSV格式，对于每个字段信息需要通过阅读README做对应的映射，不够直观。

  

在实际开发中与其他数据集之间缺乏统一组织结构标准和标注格式标准，会导致：

● 预处理脚本花样百出；

● 共享效率低，需要同时共享处理脚本；

● 难以跨数据集检索；

● 数据集合并成本较高；

● 难以开发统一的可视化工具。

  

**2\. 数据集下载**

OpenDataLab平台为大家提供了完整的数据集信息、直观的数据分布统计、流畅的下载速度、便捷的可视化脚本，欢迎体验。

https://opendatalab.com/88

  

  

**参考资料**

\[1\]官网：https://cvgl.stanford.edu/projects/uav\_data/

\[2\]论文：A Robicquet, A Sadeghian, A Alahi, et al. Learning social etiquette: Human trajectory understanding in crowded scenes. In ECCV, 2016

(PDF获取链接：https://link.springer.com/chapter/10.1007/978-3-319-46484-8\_33)

  

  

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