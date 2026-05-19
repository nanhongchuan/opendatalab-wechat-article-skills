     基于PySpark的10亿级数据集LAION-5B元数据快速处理实践（全文分享） \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

基于PySpark的10亿级数据集LAION-5B元数据快速处理实践（全文分享）
========================================

原创 喻佳、张文坚 OpenDataLab 2023-06-02 15:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/rbxdosRiBTIfR2hpjxSQ6A](https://mp.weixin.qq.com/s/rbxdosRiBTIfR2hpjxSQ6A)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**推荐语**

  

多模态大模型训练如火如荼展开，但以LAION-5B为代表的大规模多模态数据集获取却成了一个令人头疼的问题。

  

OpenDataLab两位工程师在浦数 AI Talk做了非常实用的LAION-5B下载经验分享，我们整理了其**演讲内容、Parquet文件**、**图片下载工具**，希望能对大家下载同类数据集提供帮助和参考。以下为全文内容：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**数据集背景**

根据历史研究发现，随着训练数据增加时，ALIGN、BASIC、Turing Bletchly、FLORENCE和GLIDE等大型多模态视觉语言模型在新的缺少样本标签的数据集上也有很强的迁移能力，而且性能还在稳定提高。但这些模型需要数十亿的图文数据才有达到良好的效果，到2022年为止，还没有十亿规模的公开图文对数据集。

  

直到LAION-5B发布，该数据集由5.85Billoin CLIP过滤的图像文本对组成，它为多模态预训练提供非常重要的“燃料”。

（之前我们写过LAION-5B数据集解读，戳此回顾：[80TB！58.5亿！世界第一大规模公开图文数据集LAION-5B 解读](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247506841&idx=1&sn=84eabf54e0e2637d1d59ceffb3b33c47&chksm=c10c497bf67bc06d0eb7546cd5552323300248c0f8ece505b4dfcaf10b8a887472d7d12c55bb&scene=21#wechat_redirect)）

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**LAION-5B 数据集结构**

根据官方文件统计，LAION-5B数据有5,860,068,373个样本，按照语言被官方划分为3个子数据集，分别是：

  

**1\. laion2b-en**：2.32 billion of these contain texts in the English language

_https://huggingface.co/datasets/laion/laion2B-en_

**2\. laion2b-multi**：2.26 billion contain texts from 100+ other languages

_https://huggingface.co/datasets/laion/laion2B-multi_

  

**3\. laion1b-nolang**：1.27 billion have texts where a particular language couldn’t be clearly detected

_https://huggingface.co/datasets/laion/laion1B-nolang_

  

其中每个数据集官方提供了原始图片的URL，可以根据URL下载图片文件，以及些URL上的标签。

  

这部分元数据被存储在parquet文件中。样例parquet文件结构如下：

    data_sample

（左右滑动查看）

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**Parquet元数据处理**

在官方下载parquet元数据时，发现以下几个小问题：

  

**1\.** similarity、aesthetic\_score等指标分布在多个parquet文件中，字段分散、类型不统一，需要多次下载。使用时需要先关联组合查询，TB级的文件处理速度慢，需要高配置的服务器进行处理；

  

**2\.** parquet文件中图片存储路径规则不明确，通过parquet过滤筛选图片时，无法关联下载图片的存储路径和其它字段；

  

**3\.** parquet文件中parquet\_id、hash等字段重复，影响图片的唯一索引；

  

**4\.** 通过url下载的图片格式未知（有webp、jpg、png、avif等多种格式），影响下载图片的预览和存储。

  

为了满足不同场景的数据使用需求，保证图片唯一索引ID，我们对官方的parquet文件进行了关联合并、字段补充等操作，形成一张字段丰富的“宽表”，数据表结构与字段设计如下：

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5iaZ73YGExGpuzzMboicD8JFRQepUvXN9qJWs0nr4KDEOa0RFKicKVEhRak9KFwLZ8LbTFAyvEUSLWg/640?wx_fmt=png)

上表中，最后一列是parquet文件来源，表示字段对应的parquet文件。

  

这里使用了官方的3处parquet文件，数据预览、下载链接如下：

  

**1\. 初始Laion5B**

_https://huggingface.co/datasets/laion/laion2B-en_

_https://huggingface.co/datasets/laion/laion2B-multi_

_https://huggingface.co/datasets/laion/laion1B-nolang_

  

**2\. Joined: with punsafe and pwatermark**

_https://huggingface.co/datasets/laion/laion2B-en-joined_

_https://huggingface.co/datasets/laion/laion2B-multi-joined_

_https://huggingface.co/datasets/laion/laion1B-nolang-joined_

  

**3\. Laion-aesthetic**

Laion aesthetic is a laion5B subset with aesthetic > 7 pwatermark < 0.8 punsafe < 0.5 See

_https://huggingface.co/datasets/laion/laion1B-nolang-aesthetic_

_https://huggingface.co/datasets/laion/laion2B-en-aesthetic_

_https://huggingface.co/datasets/laion/laion2B-multi-aesthetic_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**处理流程及步骤**

下面聊聊“宽表”的加工处理过程，有需求的朋友可参考对官方的原始parquet进行处理。嫌麻烦的同学，可以交给OpenDataLab，在网站下载处理好的parquet文件。

（滑到本文末，获取OpenDataLab处理好的parquet下载链接。）

  

因为parquet文件数据量较大，有几个TB，这里我们使用了大数据集群进行了分布式处理。

**● 使用的技术栈有：**

Spark/Hadooop/Hive/HDFS/Impala

  

**● 集群硬件配置：**

服务器3台，48core Cpu, 750GB Memory, 4TB Hard disk

  

**● 数据处理过程和流程图如下**：  

**数据输入：**

\- 下载官网parquet文件，并load到Hive表

\- 解析下载的图片，判断图片类型，形成id, image\_path, image\_suffix的映射文件

**数据处理：**

\- 读取Hive表数据，通过PySpark对Hive表的数据进行分布式join关联操作

**数据输出：**

\- Hive结果表导出为parquet格式文件，并上传至OSS/Ceph存储

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD4hv4KvURdmTAatBL1tWExGW6AzeIyCD0rax3IJjyBHqBWKQSsOZFrCQOQbibnTBvctsbMjib6qh9tA/640?wx_fmt=png)

为了方便数据处理，这里对数据表进行简单的分层

**\- ODS层：**原始parquet文件load Hive后的结构化数据表，其中表2是对表1字段进行了裁减，表3是下载图片相关的信息。因为官方parquet文件只提供了下载url链接，我们并不知道图片类型和后缀，所以对下载的图片文件进行程序判定，识别出图片类型，对应image\_suffix字段，image\_path是图片的存储路径。

  

**\- DMD层：**通过对表2、3、4进行join关联操作，生成中间表6

  

**\- DMS层：**将中间表6与含有punsafe、pwatermark信息的表5进行关联，得到最后的结果表7

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6O1iaFibOTPxmvwNrgVXOxmxKTvGYFhWibOT82ic66gNpRAHK1icvEV5kLtea1licOYecWGHMb7uiaDwZxA/640?wx_fmt=jpeg)

（点击查看大图）

  

数据处理操作和代码示例如下：

  

  

 Data load

主要操作是将parquet文件load到Hive表，load操作完成后，得到图中的1、3、4、5四张Hive表。  

以初始parquet文件load为例，示例代码如下。

    import os

  

  

  

 Data processing

数据处理过程主要包括数据表裁减、hash join操作。

  

因为表1的数据量较大，存在字段冗余，这里对表1的部分字段进行裁减得到表2。

  

表2、3、4的join代码如下，先将图片的sample\_id、licenese、nsfw、image\_suffix、aesthetic\_score字段，按hash值进行关联，合并成一张表。

  

因为需要使用file\_name作为Hive表二级动态分区，也避免大量数据join导致OOM，这里按dir\_name分别进行join操作，不同的分区修改对应的dir\_name即可。

    join_sql = """

  

表5与表6通过hash字段进行join，得到result结果表7。

    sc = spark.sparkContext

  

  

 Data write

最后将Hive结果表导出为snappy压缩格式的parquet文件，再上传到对象存储就可以使用了。

    sc = spark.sparkContext

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

**LAION-5B媒体图片下载工具**

在OpenDataLab网站下载到parquet文件后，可以根据这份元数据下载对应的图片文件。

现在，我们也开源了LAION-5B图片下载代码，github开源地址如下：

_https://github.com/opendatalab/laion5b-downloader_

  

耗时25天，目前下载的图片总量为5065377962张（因url链接和网站原因，部分图片无法下载），总存储量为300+TB。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtyHJJpqJIq57a7pOL1tj9uccwf8Ahoe4CzlrjJKlmYUYDGsLxq47vpg/640?wx_fmt=png)

**Parquet不可不知（附下载链接）**

在对官方parquet进行处理时，发现了数据中的几个小问题，也同步你知。

  

**1\.** 初始LAION-5B parquet文件中sample id字段重复度较高，有同学使用sample\_id字段作为唯一索引，为了避免数据问题，建议使用hash替换。

  

我们来看看sample\_id的重复情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7EHYZoRRQgXG2xxZuf38S4qIECicWUWZ3HR8Oq1k0nYTMoLEstcmTuUMCaQDfpZRYiamgLTia1NwAdQ/640?wx_fmt=png)

当然，hash在按laion2b-en、laion2b-multi、独立分类的子集中共有6条重复值，laion1b-nolang无数据重复。在使用时注意下即可，hash值重复情况如下表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7EHYZoRRQgXG2xxZuf38S4SoWz1E5x24wQJLr2ibFA3WCAz5yEib3ibUJLchTaFkUwKWLF26EZRu67Q/640?wx_fmt=png)

**2\.** 3个分类子集的图片精确数量如下，可以用来对比图片是否有缺失问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7EHYZoRRQgXG2xxZuf38S453uaickASuDibmyGiayVjmo3Y2mZAnSByDOudv2VNzADl4yxYxXTJWwJw/640?wx_fmt=png)

最后，有需要的同学可以在OpenDataLab下载处理好的parquet文件。

OpenDataLab parquet文件下载链接：

_https://opendatalab.com/LAION-5B_

  

  

\-END-

更多公开数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言