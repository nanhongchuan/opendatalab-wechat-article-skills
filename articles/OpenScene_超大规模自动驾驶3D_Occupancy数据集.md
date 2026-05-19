     OpenScene：超大规模自动驾驶3D Occupancy数据集 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

OpenScene：超大规模自动驾驶3D Occupancy数据集
=================================

原创 OpenDriveLab OpenDataLab 2023-08-08 18:31 上海

> 原文地址: [https://mp.weixin.qq.com/s/Nlleuv4ut-dvoxrfSZlcQw](https://mp.weixin.qq.com/s/Nlleuv4ut-dvoxrfSZlcQw)

纯视觉BEV感知开启了自动驾驶方案研究的热潮，**Occupancy** 则进一步扩展了纯视觉自动驾驶系统的通用场景感知能力。但现有的Occupancy数据集，如Occ3D、SurroundOcc、OpenOccupancy等，**数据规模仍然很小**（6小时左右）。对于自动驾驶大模型来说，海量数据是必不可少的。

  

**01**

**OpenScene：服务自动驾驶**

**通用模型的****下一代数据集**

  

  

OpenScene是自动驾驶领域**超大规模的3D Occupancy数据集**，数据时长超过**120小时**，覆盖了拉斯维加斯、波士顿、匹兹堡、新加坡四个城市的场景，其数据多样性能促进自动驾驶大模型在不同的场景中的泛化能力。相比于现有的Occupancy数据集，OpenScene具有规模大、场景复杂、标注精准等特点。

  

数据集：

_https://github.com/OpenDriveLab/OpenScene_

_https://openxlab.org.cn/datasets/OpenDriveLab/OpenScene_

  

  

### **● 超大规模自动驾驶3D Occupancy数据集**

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnML9TueArI0ibYeVPFWFwjoYnfjftcF85wuoWELoiczozkIdFvMMzEiaSx0nKa2kD3Iol59T1BEoEZhQQ/640?wx_fmt=png)

\- Occupancy标签融合的LiDAR帧的时长是20秒

\- Flow标签包含每个Occupancy Grid的运动方向和速度信息

\- 完整的语义标签将在下一版本中发布

###   

### **● 赋能****自动驾驶大模型**

> 什么形式可以更好地建模自动驾驶场景?

相比现有数据集，OpenScene具有**Occupancy Flow标签**，预测信息的引入有利于缩小**决策制定**和**场景表示**之间的鸿沟。另外OpenScene为每个前景体素提供了语义标签，帮助通用模型更加全面地理解复杂多变的驾驶场景。

  

**● 任务及评估指标**

**1\. 大模型多任务评测**。

考虑到多视角图像和Occupancy标注，需要一个统一的大模型Backbone来有效地处理多种下游任务，我们提出OpenScene指标（OSM）用于总结大模型在各个方面（检测、分割、预测等）的性能。

  

**2\. 大规模Occupancy Prediction**。

给定来自环视相机的大量图像，预测场景中每个体素的Occupancy和Semantics。

  

**02**

**OccNet：通用场景表征解决方案**

**和效果展示**

题目：_Scene as Occupancy_

论文：

_https://arxiv.org/abs/2306.02851 (ICCV 2023)_

代码：

_https://github.com/OpenDriveLab/OccNet_

**● 表征解决方案**

我们认为**Occupancy是3D场景的一种通用表示**，能够促进自动驾驶中感知、规划等多种任务。OccNet包括**Reconstruction of Occupancy**和**Exploitaion of Occupancy**两个阶段。首先从环视图像中重建Occupancy，学习统一Occupancy特征，然后在Occupancy特征基础上完成语义补全、3D检测分割、预测、规划等多种自动驾驶任务。

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnML9TueArI0ibYeVPFWFwjoYnQesPBs2YbEpRsvAnWVAy5a8vPw53S3lcAGCntv0YoKmG7Q7OGzZsnA/640?wx_fmt=png)

  

OccNet：通用场景表征解决方案

**● 效果展示**

![](https://mmbiz.qpic.cn/mmbiz_gif/SLE456SxnMLrvVQ6NR41phibqRAkCuCIQS2EMoknOKtowGWoomdFydWuTjmIErDbIvQefyvWwUXV3tWq8G9TLdg/640?wx_fmt=gif)

OccNet从环视图像中预测3D Occupancy并学习统一表征，促进感知和规划等后续任务，实现与基于激光雷达的方法相匹配的结果。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/SLE456SxnML9TueArI0ibYeVPFWFwjoYnCDiazFkL9RmLdFOnOKicicDMr1vHD93h72Lf2SnHtrcnG2aiax8SicLtCdQ/640?wx_fmt=jpeg)

Occupancy可以更好地描述施工的车辆或者交通标志等形状不规则的对象。

  

**03**  

**下一步：2024自动驾驶挑战赛**

作者团队将于八月底公布2024年自动驾驶挑战赛的更多细节。欢迎持续关注OpenDriveLab的动态和相关工作。

挑战赛网站：

_https://opendrivelab.com/AD24Challenge.html_

  

**此外，CVPR 2023自动驾驶挑战赛****OpenLane Topology****和****3D Occupancy Prediction****赛道的评测系统已经重新开放，更多详情请关注:**

**_https://opendrivelab.com/AD23Challenge.html_**

\-END-

更多公开数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言