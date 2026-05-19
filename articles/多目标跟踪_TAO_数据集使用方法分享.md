     多目标跟踪 TAO 数据集使用方法分享 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

多目标跟踪 TAO 数据集使用方法分享
===================

原创 专注于AI 数据的 OpenDataLab 2022-06-09 18:35 上海

> 原文地址: [https://mp.weixin.qq.com/s/\_qjj\_RVsxyDm9theGwk1Lw](https://mp.weixin.qq.com/s/_qjj_RVsxyDm9theGwk1Lw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD7DYzsibeib72U1ZfgFhMIWsXqvt2ILN8Lniarq1Wnf1GqU1BO5IDnZ2xJicSLchAmZWNkWM1aFyPXzkg/640?wx_fmt=gif)

  

  

之前给大家分享了[多目标跟踪任务及5个相关数据集](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247489152&idx=1&sn=d2c30825e40506bfd6e2b30a291f29b5&chksm=c10f8462f6780d745d2222d391bf52d76cf607be69e07ea99e794fbb6a076a0327ba3623e983&scene=21#wechat_redirect)，其中提到的TAO数据集很受小伙伴们欢迎，今天就带大家一起来看看。

  

**目录指引**

  

1\. 数据集简介

2\. 数据集详细信息

3\. 数据集任务定义及介绍

4\. 数据集结构解读

5\. 数据集下载链接

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**数据集简介**

**发布方：**Carnegie Mellon University, Inria, Argo AI

  

**发布时间：**2020

  

**背景：**

在多目标跟踪领域类别往往来自自动驾驶和视频监控中特定的几个类（车辆、行人、动物等），忽略了真实世界的大多数物体。

  

众所周知，COCO等类别丰富的大规模数据集极大的促进了目标检测领域的发展，故此，来自CMU等单位的学者推出一个类似COCO的类别多样化的MOT数据集（TAO），用于跟踪任何物体，以期改变多目标跟踪的现状。

  

**简介：**

TAO数据集由2907个不同环境的高清视频组成，平均长度36.8秒，包含833个类别，对比现有的公开目标跟踪数据集，TAO数据集样本种类更加丰富。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集详细信息**

**1\. 标注数据量**

**训练集：**500段视频，包括534092个 jpg图像

**测试集：**1,419段视频，包括1502450个 jpg图像

**验证集：**993段视频，包括1045668个 jpg图像

**2\. 标注类别**  

数据集中对象的标注共有833个类别：其中488个类别和LVIS这个数据集相同；数据集总共包含2907个不同环境的高清视频；TAO中的数据来源于7个其他数集：ArgoVerse，BDD，Charades，LaSOT，YFCC100M，AVA，HACS。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7DYzsibeib72U1ZfgFhMIWsXolFAcyLBzO0FbuDUIYgwLicOr8GwzEVK6UN032gbibzkK7wCJGddQTkw/640?wx_fmt=png)

  

  

**3\. **可视化****

下面是 TAO 的原视频的部分样例的标注结果，原始视频数据来源于  Charades, LaSOT 和 ArgoVerse三个数据集。  

  

  

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**数据集任务定义及介绍**

**1\. 多目标跟踪**
-------------

**● 任务定义**

在给定的一段视频中识别与跟踪多个目标。

  

**● 评估**

**a. 评估过程**

在第    帧，ground truth 为  ，预测结果 hypothesis 为  ，其中每个  与每个  都属于一个特定的轨迹，即可能已经出现在此前的若干帧中。

  

对于  ，若交并比  ，则二者可建立关联（relationship），其中  为预设的阈值，在 TAO中为  。

  

若  在第  帧匹配（matched），且在第  帧可建立关联，则在第  帧直接进行匹配。

  

对于剩余未匹配的 ground truth 和 hypothesis，基于建立的关联关系，计算最大二分匹配。

  

仍未匹配的 ground truth 为 False Negative，仍未匹配的 hypothesis 为 False Positive。

  

若  与  匹配，且此前最近的一次匹配对象为  ，则  在第  帧发生一次 identity switch (IDSW)。

  

**b. 评价指标**

TAO竞赛所用的评价指：

https://motchallenge.net/results/TAO\_Challenge/

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7DYzsibeib72U1ZfgFhMIWsX4sLbDIGU3UJQMSt96UpJUUhXztibX8MR5oA3GIqxnTR82HhG46jSzmw/640?wx_fmt=png)

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

**数据集文件结构解读**

**1\. 目录结构**

    dataset_root/

  

**2.** **标注文件及其他文件说明**

● **标注的json文件格式如下：**

**以 train.json 文件为例，其他 test 和 validation 的标注文件信息类似。train.json中其注释文件中的内容就是一个字典数据结构，包括以下7个字段：videos，annotations，tracks，images，info，categories，licenses。**

**训练数据的标注样例如下：**

    { 

  

**整体字段结构**

    {

  

**各字段解析**

    videos: {

**即每行为一个半分钟左右的视频文件名。其他txt文件如tao\_argoverse.txt、tao\_ava.txt 同理。**

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

**数据集下载链接**

OpenDataLab平台为大家提供了完整的数据集信息、直观的数据分布统计、流畅的下载速度、便捷的可视化脚本，欢迎体验。点击原文链接查看。

  

https://opendatalab.com/TAO

  

  

**参考资料**

\[1\]官网：https://taodataset.org/

\[2\]论文：A  Dave, T Khurana,P Tokmakov, et al. Tao: A large-scale benchmark for tracking any object. in ECCV, 2020. Springer, Cham, 2020: 436-454.

\[3\]Github：https://github.com/TAO-Dataset/tao

  

  

  

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