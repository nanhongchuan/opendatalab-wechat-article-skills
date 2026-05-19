     多目标跟踪（MOT）数据集资源整理分享 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

多目标跟踪（MOT）数据集资源整理分享
===================

原创 专注于AI 数据的 OpenDataLab 2022-05-10 22:11 上海

> 原文地址: [https://mp.weixin.qq.com/s/4deJTB-gr-7ldckUEmbXvA](https://mp.weixin.qq.com/s/4deJTB-gr-7ldckUEmbXvA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

  

我们已经生活在一个被摄像头和视频包围的世界里，从手机、汽车、无人机到各类监控设备，随处可见摄像头的“身影”。

  

据前瞻产业研究院2020年的报告分析，预计到2025年全球摄像头镜头的出货量将超过120亿颗。

  

面对海量的摄像头及其产生的视频素材，如何利用具有深度学习功能的 AI 技术，高效、智能地处理、挖掘信息，已成为一项非常有价值的课题。

  

  

****01****  

**目标跟踪简介**

视频目标跟踪技术（也称为：目标跟踪、视觉跟踪），作为计算机视觉领域中基础的、重要的研究方向之一，可广泛应用在交通管理、安防监控、自动驾驶、机器人、体育赛事转播等领域，其已成为一大研究热点。

  

![](https://mmbiz.qpic.cn/mmbiz_gif/kreLtv4rmOxzIw8GnQoXBd8s4lcJoic1PsqLP5bt7A7ZkzofwKpMepeSTiabZKUV5Kj760AaV9jpoxqbp63WZRkA/640?wx_fmt=gif)

图源：网络

  

  

****02****  

**目标跟踪分类**

● 根据跟踪的目标数量，目标跟踪任务可分为**单目标跟踪（SOT）**和**多目标跟踪（MOT）**；

● 根据背景状态，可分为**静态背景**下的目标跟踪和**动态背景**下的目标跟踪；

● 根据摄像头数量，可分为**单摄像头跟踪**和**多摄像头跟踪**；

● 根据任务计算类型，可分为**在线跟踪**、**离线跟踪**；

  

更多分类可参考下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7hnQbr6H3X2OTw5ict4NTDJXs72kTjbDMicqMKr7SNOOHeJOjX45iaWp81ZCZEGe2gmY4U0eGyOLtEg/640?wx_fmt=jpeg)

目标跟踪纵览（图源：参考资料\[1\]）

  

其中，多目标跟踪作为计算机视觉中的一项中级任务，仍然是一项具有挑战性的任务，因为它需要同时解决目标检测、轨迹估计、数据关联和重识别问题。

  

另外它也是许多高级任务的基础，如姿态估计、动作识别和行为分析等。

  

让我们一起来看看。

  

  

****03****  

**什么是多目标跟踪任务**

多目标跟踪与单目标跟踪是一组相对的概念。

  

单目标跟踪是指，在视频的初始帧画面上框出单个目标，预测后续帧中该目标的大小与位置。该目标始终位于视场中，并且对目标种类无限制。

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD7hnQbr6H3X2OTw5ict4NTDJ7oHAMOARaAKX7XYBlAJliavcysncUQe0EibZfjKicBafiauNDQm1R12KWg/640?wx_fmt=gif)

单目标跟踪示意（图源：网络）

  

而多目标跟踪是在事先不知道目标数量的情况下，对视频中的行人、汽车、动物等多个目标进行检测并赋予ID进行轨迹跟踪。不同的目标拥有不同的ID，以便实现后续的轨迹预测、精准查找等工作。\[2\]

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD7hnQbr6H3X2OTw5ict4NTDJtAUzdfRpZHG3l29vj676wKLR500W6v9NCaZLRpzMgyccNibfGDiabI2A/640?wx_fmt=gif)

多目标跟踪示意（图源：网络）

  

  

****04****  

**多目标跟踪方法步骤**

多目标跟踪主要分为以下四个步骤：\[3\]

**1\. 对象初始化**

首先对各个视频帧中的新出现的对象进行建模，即对象初始化；

  

**2\. 检测与特征提取**

其次根据建立的模型进行对象检测，获得初始对象序列的特征；

  

**3\. 相似度计算**

根据得到的特征，在后续帧中重复寻找目标对象进行相似度度量；

  

**4\. 数据关联**

根据相似度度量结果对目标进行关联，获得一系列的对象轨迹。

  

  

****05****  

**多目标跟踪任务难点**

相对于单目标跟踪，多目标跟踪面临着更加复杂的问题包括频繁的遮挡、轨迹的管理、相似的外观和多目标间的相互影响。

  

在实际的应用场景中，需要面对存在的各种复杂变化（以行人跟踪为例）：

**1\. 目标自身的变化**

目标的颜色变化（行人的衣服颜色变化），目标的尺度变化（离摄像头的远近）和目标的形态变化（行人的站立、蹲与躺）等。

  

**2\. 外界环境的变化**

光线明暗的变化、目标所处环境的多样性、目标的消失与出现和目标的遮挡问题。

  

这些复杂变化会影响跟踪对象与背景环境的区分度，从而进一步影响多目标跟踪算法的跟踪效果和结果的好坏，所以需要恰当地处理这些变化来提高多目标跟踪的准确性。

  

  

****06****  

**多目标跟踪常用数据集**

目前多目标跟踪领域的重要基准是MOTChallenge，作为上传并公布多目标跟踪方法研究成果的公共平台，其拥有最大的公开行人跟踪数据集。\[4\]

  

其提供的数据集包括：MOT 15、MOT 16、 MOT 17、MOT 20，这些数据集都提供了训练集的标注，训练集与测试集的检测，以及数据集的目标检测结果，主要侧重于密集场景下行人跟踪任务。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7hnQbr6H3X2OTw5ict4NTDJTotibvSz5n4JtAOj2Uvmm7uWMYTy4oyZ31ZYx1huvZ0LIxMWlrsBAlg/640?wx_fmt=png)

MOT系列数据集的视频序列及其主要属性（图源：参考资料\[4\]）

  

另外还有近几年出的TAO数据集，是一个类似COCO的多样化的MOT数据集，其中包含2907个不同环境的高清视频，平均长度半分钟，包含833个类别，比现有的数据集高出一个数量级。

  

  

****07****  

**多目标跟踪数据集资源**

OpenDataLab平台已经上架了多目标跟踪（MOT）系列数据集，提供了丰富的数据集信息、流畅的下载速度，快来体验吧！

  

**·** **MOT15**

https://opendatalab.com/73

  

**· MOT16**

https://opendatalab.com/72

  

**· MOT17**

https://opendatalab.com/71

  

**· MOT20**

https://opendatalab.com/70

  

**· TAO**

https://opendatalab.com/125

  

  

**参考资料：**

\[1\]https://arxiv.org/abs/1912.00535

\[2\]https://www.bilibili.com/read/cv12115742

\[3\]文成宇. 复杂场景行人的多目标跟踪方法\[D\].中国矿业大学,2021.

\[4\]徐涛,马克,刘才华. 基于深度学习的行人多目标跟踪方法\[J\]. 吉林大学学报(工学版),2021,51(01):27-38.

  

\- End -

  

**下期预告：MOT20数据集详细解读**

**分享、点赞加速更新速度哟![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7hnQbr6H3X2OTw5ict4NTDJtia3HQxIwibVWFVo7m5oJQZvibt5BdRBwaMKgbU9AV5D8iaV8hDeQwf2yQ/640?wx_fmt=png)**

  

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