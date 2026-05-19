     激光雷达（LiDAR）点云数据知多少？ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

激光雷达（LiDAR）点云数据知多少？
===================

原创 专注于AI 数据的 OpenDataLab 2022-04-19 16:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/YpUovWJWDrIuZMCj86hBJw](https://mp.weixin.qq.com/s/YpUovWJWDrIuZMCj86hBJw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

  

近几年，不少车企纷纷推出智能车型，落地L2~L4等级的辅助驾驶技术，提供自动泊车、自动巡航、低速自动驾驶功能；另外还有许多机构在无人车、自动驾驶船舶等领域取得不错的研究成果。

  

这些都得益于“自动驾驶”技术的发展，为智能交通创造了更多的可能。

  

  

在自动驾驶系统中，激光雷达作为环境感知设备，其采集的点云数据对三维目标检测、反馈周围是否有障碍物、距离前车有多远等起着重要作用。

下面给大家具体介绍一下。

  

  

****01****  

**什么是激光雷达点云数据**

激光雷达（LiDAR）点云数据，是由三维激光雷达设备扫描得到的空间点的数据集，每一个点都包含了三维坐标信息，也是我们常说的X、Y、Z三个元素，有的还包含颜色信息、反射强度信息、回波次数信息等\[1\]。

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD69JoUeNJwKqy3MkBYaiar8ZTKz8icRRSPHTxSXnkXVuCGXbiatjTfGx5KMwG7ykAQtvtzVYCBhk6Okw/640?wx_fmt=jpeg)

点云信息示意（图源：网络）  

它们是如何产生的呢？

  

  

****02****  

**激光点云数据的采集方式**

激光点云数据，由车载激光扫描系统向周围发射激光信号，然后收集反射的激光信号得来的，再通过外业数据采集、组合导航、点云解算，便可以计算出这些点的准确空间信息。

  

看上去一个简单的数据获取，其实包含了较为复杂的设备结构及数据采集过程。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD69JoUeNJwKqy3MkBYaiar8Zra83LzJe9J38FDebh29v90vN2XECQczSyIiaUwqkp2sZtzIt1RVYWZQ/640?wx_fmt=jpeg)

一种典型的激光雷达传感器系统组成（图源：参考资料\[2\]）  

  

比如，就车载激光扫描系统而言，包括了激光扫描仪、CCD相机、惯性测量装置（IMU）、里程计（DMI）、全球定位系统(GPS)、计算机及控制单元等。

  

另外，由于三维激光雷达传感器的系统结构特点与工作原理，使其具有固定范围的水平视角和垂直视角，所以在数据采集、分析过程中，需要对水平分辨率和垂直分辨率进行分析，考虑每个数据点之间的距离精度，根据结果为后续点云数据处理方法的相关参数提供设置参考\[2\]。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD69JoUeNJwKqy3MkBYaiar8ZTbY1ydrNSibibKo30nukpAsIndRDicpiaibKXCafKVQ6Aym8fxOYxcGuibww/640?wx_fmt=png)

KITTI点云数据预览效果（图源：参考资料\[3\]）

  

  

****03****  

**三维激光点云数据特点**

三维激光雷达传感器采集的场景点云数据，一般具有以下典型的特征\[2\]：

  

**1\. 稀疏性**

与固定尺寸的二维图像中固定的像素数量截然不同，三维激光点云本质上是一种低分辨率的离散化采样，此外，环境场景的不同也会导致固定线数的激光雷达采集到的不同数量的点，这些均导致了点云数据固有的稀疏性。

  

**2\. 无序性**

与二维图像的像素排列严格有序不同，点云数据是无序的向量的集合，其中的点不具有固定的排列顺序，任何一种排序组合的方式进行输入描述，其代表的都是同一组点云数据。

  

**3\. 空间分布不均匀**

随着检测距离的增加，具有固定水平和垂直角度分辨率的激光雷达的距离检测精度在不断降低。具体表现为距离激光雷达传感器越近的物体，其表面被采集的点的数量就越多，其对应的点云也就越稠密，反之，距离越远，对应的点云也越稀疏。

  

**4\. 表示信息的有限性**

由于场景中三维物体的自遮挡，使得激光雷达只能检测到三维物体的一部分表面，这也导致了点云数据只能表示物体的一部分几何信息。

  

  

****04****  

**三维点云数据集**

通过深度传感器如激光雷达对环境场景进行数据采集，并且进行数据标注，最后形成的一定规模的数据集。可用于自动驾驶技术领域相关算法和计算机视觉算法的验证与性能评估。比如常用的KITTI数据集。

  

那三维点云数据可以用来干什么？

  

  

****05****  

**三维点云数据的应用方向**

三维点云在自动驾驶领域中的应用可以分为以下两个方面：

  

*   基于场景理解和目标检测的实时环境感知和处理；
    
      
    
*   基于可靠定位和参考的高精度地图和城市模型的生成和构建。
    

  

  

****06****  

**数据集资源**

OpenDataLab平台已经上架KITTI系列数据集，并且对KITTI tracking、KITTI object等数据集进行了标准化，提供了丰富的数据集信息、统一的脚本格式、流畅的下载速度，快来体验吧！

  

**· KITTI2012**
===============

https://opendatalab.com/datasets/66

  

**·** **KITTI Tracking**
========================

https://opendatalab.com/datasets/129
====================================

**· KITTI Object**

https://opendatalab.com/datasets/130

  

**· KITTI Flow 2015**

https://opendatalab.com/114

  

**· KITTI Flow 2012**

https://opendatalab.com/160

  

**· KITTI Scene Flow 2015**

https://opendatalab.com/112

  

**· KITTI Stereo 2015**

https://opendatalab.com/116

  

**· KITTI Stereo 2012**

https://opendatalab.com/159

  

**· KITTI Odometry 2012**

https://opendatalab.com/161

  

  

**参考资料：**

\[1\]https://mp.weixin.qq.com/s/mN95DvNj2CCvPoxDJUkVuA

\[2\]张杰. 基于激光雷达点云的船舶目标检测方法研究\[D\].哈尔滨工程大学,2021.

\[3\]https://blog.csdn.net/qq\_16137569/article/details/118873033

  

  

  

\- End -

文章来源：网络整理，如有侵权，请联系删除。

  

  

**扫码入群,了解更多**

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