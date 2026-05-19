     经典、常用的视频对象分割数据集——DAVIS 2016解读 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

经典、常用的视频对象分割数据集——DAVIS 2016解读
=============================

原创 专注于AI 数据的 OpenDataLab 2022-11-24 18:45 上海

> 原文地址: [https://mp.weixin.qq.com/s/bNdc-ujHU3GS4wtw1QpElA](https://mp.weixin.qq.com/s/bNdc-ujHU3GS4wtw1QpElA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

********计算机视觉领域中和目标有关的经典任务有三种：分类、检测和分割。关于分割任务，前面给大家分享了****************[50个常用的语义分割数据集](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247509723&idx=1&sn=6cc837b0273806342d0d7e4cd4c02a23&chksm=c10c3439f67bbd2f5c3076fa9b654b57ea02f659ff7a4f910539e5ac9436176bbf6d7e0fb5a7&scene=21#wechat_redirect)，同时讲解了[大规模图像二分类分割数据集DIS5K](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247508491&idx=1&sn=4f93eca92e91e8f0bb3e14a72cd6cc4f&chksm=c10c30e9f67bb9ffb7058ecad42748094042d5421da0c90d9cf4a9f4b5b758838819ae236767&scene=21#wechat_redirect)。********

********本期我们将着眼于视频对象分割任务，为大家带来经典的、常用的 DAVIS 2016 数据集解读。快来看看吧~********

  

**目录指引**

  

1\. 数据集简介

2\. 数据集详细信息

3\. 数据集任务定义及介绍

4\. 数据集文件结构解读

5\. 数据集下载链接

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**数据集简介**

**发布方：**

****ETH Zurich; Disney Research****

  

**发布时间：****2016**  

  

**背景：**

********在计算机视觉中，物体检测与分割是经典的任务之一，其目的是在于找到目标物体在图像中的准确位置，并使其准精度达到象素级。****************针对这一任务，DAVIS数据集被设计和构建出来，并能够重现真实的视频场景：如相机抖动、背景杂波、闭塞和其他复杂情形等。********

  

**简介：**

********DAVIS2016由50段高质量，全高清的视频序列组成，包含有1080P和480P两种分辨率，每种共有3455个标注帧。****************考虑到计算复杂度，每个视频时长2-4秒。********

  

********对于视频中的每一帧，该数据集都提供像素级别的物体边缘标注，以二进制掩码的方式手工创建分割，表现为稠密的黑白图像。每个视频帧都对应了一个标注图片，标注图片的文件名与视频帧文件名保持一致，并且对两种分辨率的视频帧都进行了标注。********

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集详细信息**

**2.1 标注数据量**

**训练集**：30段视频的帧图像，共2079帧；

**验证集**：20段视频的帧图像，共1376帧。

  

具体的数据分割情况如下表所示：  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn53NfR1mvVuGY6RtSLzGhQboqiapSMyP0j7P7KmicAqDIEzP4neiaicJZicgA/640?wx_fmt=png)

  

**2.2 标注类别**

数据集共有50个视频，每个视频有一个具体的实体分割目标，分别是：bear, blackswan, bmx-bumps, bmx-trees, boat, breakdance, breakdance-flare, bus, camel, car-roundabout, car-shadow, car-turn, cows, dance-jump, dance-twirl, dog, dog-agility, drift-chicane, drift-straight, drift-turn, elephant, flamingo, goat, hike, hockey, horsejump-high, horsejump-low, kite-surf, kite-walk, libby, lucia, mallard-fly, mallard-water, motocross-bumps, motocross-jump, motorbike, paragliding, paragliding-launch, parkour, rhino, rollerblade, scooter-black, scooter-gray, soapbox, soccerball, stroller, surf, swing, tennis, train.

  

**2.3 可视化**

下图是将视频帧中的图片与标注的轮廓放在一起的示例，图中被标注的部分就是前景中需要被分割的实体。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn5f5HibLSyXr44WjOyjibCTz7gWNEdRw1Y8uwChGlLDj5kLqmqOicmicHelA/640?wx_fmt=png)

  

下图是将标注图像单独列出的示例。图中黑色部分是要被忽略的背景，而白色部分则是需要被关注和追踪的物体。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn5LkQia7Frm4ytVMMHl0gTT008s0adY2LGX4lDkhBM1BYdRafTo8wDFEw/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**数据集任务定义及介绍**

**3.1** **视频目标/对象分割**
---------------------

**● 视频对象分割的定义**

视频对象分割是指在给定的一段视频序列的各帧图像中，找出属于特定前景对象的所有像素点位置区域。

**●** **视频对象分割**评价指标****

\- **区域相似性** (Region Similarity, J)：

区域相似度是mask (M) 与ground-truth (G) 之间的交集，即预测分割的区域与真值的交并比，如下公式所示。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn5362shC3xtxtK7XodA1pBJgHyibEZiakrfx2Q6N1BibzRlOx4rLaUgJOuw/640?wx_fmt=png)

\- **轮廓精度**(Contour, F): 

轮廓的 F-measure值。预测得到的mask轮廓表示为 c(M)，真值轮廓边界表示为c(G)。利用\[4\]中提到的双点图匹配方法，可以计算c(M)和c(G)相比得到的轮廓准确率和轮廓召回率Pc和Rc，进而可以计算得到轮廓的 F-measure 值，得到轮廓精度结果，公式如下。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn5HuDBDSBo7AO3Z3x8NNffib2HMOFN6eO4sRHRYhsl6TB8rrnG9Vhypdg/640?wx_fmt=png)

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

**数据集文件结构解读**

****4.1 数据集目录结构****

    DAVIS2016/  

**（左右滑动查看）**

**4.2 标注文件****格式**

**a. 媒体文件格式**

180P的视频是由分辨率为1920x1080的.jpg后缀的每帧图像文件构成，480P的视频是由分辨率为854\*480的.jpg后缀的每帧图像文件构成。

  

下图示例中展示了名为“bear”视频中的一帧图像，其中熊是需要分割的实体。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn5boWib4vWVbggtYPnjWic7OdnQj1WmXrON6tLlVtg7IE3DZ0aMkDLQsbw/640?wx_fmt=jpeg)

  

**b. 标注文件格式**

180p分辨率的标注文件是由分辨率为1920\*1080的png图片构成，480p分辨率的标注文件是由分辨率为854\*480的png图片构成。

  

下图为对应上面视频帧图像的标注文件，白色为前景，即需要分割的目标物体，黑色代表背景。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn58fTYGLIFib5emtzz7DwL5mbfS9EbZXbEMUankJEic4EYTRCJeXzuphVg/640?wx_fmt=png)

  

**c. 存储数据分割 segment 划分方式的文件**

如下图所示，txt文件中存储了视频帧图像文件和与之对应的标注文件的存储路径。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7FG3OtDUcZrqIabcEGuGn5cJuhkgQ5nDUPLsg0fFpiborm12ZfRW9QawZ2PLvpiaJjNvCQd4WA0d3g/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

**数据集下载链接**

OpenDataLab平台为大家提供了 DAVIS2016 数据集完整的数据集信息、直观的数据分布统计、流畅的下载速度、便捷的可视化脚本，欢迎体验。

https://opendatalab.org.cn/DAVIS\_2016

（点击原文查看）

  

  

**参考资料**

\[1\] 官网：https://davischallenge.org/

\[2\] 数据集下载：https://davischallenge.org/davis2016/code.html

\[3\] F Perazzi, J Pont-Tuset, B McWilliams, et al. A benchmark dataset and evaluation methodology for video object segmentation, in CVPR. 2016: 724-732.

\[4\] D Martin, C Fowlkes, and J Malik. Learning to detect natural image boundaries using local brightness, color, and texture cues. TPAMI, 26(5), 2004. 4

  

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