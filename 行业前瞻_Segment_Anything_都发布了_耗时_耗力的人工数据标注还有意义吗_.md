     行业前瞻｜Segment Anything 都发布了，耗时、耗力的人工数据标注还有意义吗？ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

行业前瞻｜Segment Anything 都发布了，耗时、耗力的人工数据标注还有意义吗？
=============================================

原创 张子千 OpenDataLab 2023-04-13 17:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/RDFEaVBireV4zS041KgTKQ](https://mp.weixin.qq.com/s/RDFEaVBireV4zS041KgTKQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

本文已获授权，部分有删改。来源：Xtreme1

自 2012 年以来，**深度学习技术**变革引起的人工智能热潮，这股势头已经持续十年。在去年底 **ChatGPT** 的出现，**大模型的超能力**完全展现在大众的视线中，将人工智能行业又推向了一个全新的发展阶段，许多研究者更是惊呼“**ChatGPT 爆火后，NLP 技术不存在了**” \[1\]。因为过去的自然语言专家，有着擅长于自己的领域，有人专门做文本分类、有人专门做信息抽取、有人做问答、有人做阅读理解，而在**大模型范式下**，一个大语言模型就能实现多种NLP任务的完美统一。

  

计算机视觉（CV）领域，大家也都密切关注着“大一统”模型，所谓的“**ImageGPT**”以及“**多模态 GPT**”的发展。

就在上周，4 月 5 日 **Meta** 发布了**Segment Anything Model（SAM）——第一个图像分割基础模型**，可以称得上是当前最先进的一种图像分割模型，其将NLP领域的prompt范式引进CV，让模型通过prompt一键抠图，在照片或视频中对任意对象实现一键分割，并且能够零样本迁移到其他任务\[2\]，这意味着**图片大模型时代**已经来临。

  

同时，让人不禁发问，学术界和商用落地场景使用的、耗时耗力的人工标注的标准答案（Ground truth）是否还有存在的必要？

_全文 **2,217** 字，读完需要 **4** 分钟  
_

文末有图像分割开源数据集推荐

  

  

 什么是图像分割？

**图像分割（****Image** **Segmentation****）**是图像处理中的一种技术，也是计算机视觉领域核心任务之一。它是预测图像中每一个像素所属的类别或者物体，输出不同类别的像素级掩码。简单来说，就是将图像中的每个像素标注为属于哪一个对象，比如人、车、树等等，并精细地标注出每个物体的具体位置和形状。

  

大体上，图像分割可以分为三个子任务: **实例分割 (instance segmentation)** 、**语义分割 (semantic segmentation)** 、**全景分割 (panoptic segmentation)**，这三个子任务都有着大量的算法与模型。他们在计算机视觉、医学影像处理、数字艺术等领域都有广泛的应用。

![](https://mmbiz.qpic.cn/mmbiz_gif/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2RzVVJtYNRx90g6icxn1BwkLHyN4HtacsbYsRb6Kyr0qZrcsP3pBV7ibKA/640?wx_fmt=gif)

目标检测与语义分割标注

  

  

“Segment Anything”项目发布了什么？

Meta 发布了“**Segment Anything Model（SAM）**”和相应的数据集**（SA-1B）**，这是一项**新的图像分割****任务**、**模型**和**数据集**。

**核心亮点：**

**1\.** 该模型被设计和训练为可提示性（promptable），支持文本、关键点、边界框等多模态提示。你可以用一个点、一个框、一句话等方式轻松分割出指定物体；甚至接受其他系统的输入提示，比如根据AR/VR头显传来的视觉焦点信息，来选择对应的物体；

  

**2\.** 可以非常灵活地泛化到新任务和新领域。积累了大量学习经验的SAM 已经能够理解对象的一般概念，不要额外训练，即可对不熟悉的物体和图像进行全自分割标注，可以为任意图像或视频中的任何对象生成掩码；

  

**3\.** 对于稠密的图片，仍然有非常好的分割效率和效果；

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4Bn3WKGmMfH1WxI2TtIiajRcI2LqkRdAlHHSy9NgBaumMYN8NsNg5060X7AQovtMv7Sg3VwPgy7TQ/640?wx_fmt=png)

**4\.** 使用高效的SAM模型构建了迄今为止最大的分割数据集SA-1B，包括超过 1 亿个 Mask 图和 1100 万张符合许可证的图片。为模型提供了充足的训练数据，有望成为未来计算机视觉分割模型训练和评测的经典数据集。

![](https://mmbiz.qpic.cn/mmbiz_png/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2Rk7N82U7vcqQkibMQVjrM2xpAajvDr3WPeQD00Ek7bp1icZNvjtffRA6Q/640?wx_fmt=png)

要知道，以往创建准确的分割模型“需要技术专家通过 AI 模型训练和大量人工精细标注数据进行高度专业化的工作”。而Meta 创建 SAM，旨在减少对专业培训和专业知识的需求，让这个过程更加“平等化”，以求推动计算机视觉研究的进一步发展。

  

  

 Segment Anything Model 的效果如何？

Meta 表示，SAM 已经掌握了对物体的一般概念，能为任何图像或视频中的任何物体生成 Mask，即使在训练过程中没有遇到过这些物体和图像类型。SAM 足够通用，覆盖了广泛的用例，并可在新的图像“领域”（例如水下照片或细胞显微镜图像）上直接使用，无需额外训练（这种能力通常称为零样本迁移）。

![](https://mmbiz.qpic.cn/mmbiz_png/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2Ra9JWUPgiaIl2gbeYIlHd580Ed96aYPEiaLFQU0n0pOsmVZtzujexL5OA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2RzwicVhKpQHGQBhQ0SOAtNkiaJGibLm5krFwImUHHj7R40cTuIiciaCyNUlw/640?wx_fmt=png)

 SAM与人工标注的对比

  

  

 我们所看到的挑战与机遇

**市场上早有相似的技术**

在此之前我们见过很多不错的分割工具，例如 Photoshop 软件或 IOS 系统中自带的抠图功能，它们都能生成不错的效果，也用不错的交互体验提高了图像处理的效率，与SAM模型有着类似的功能。

![](https://mmbiz.qpic.cn/mmbiz_gif/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2RkbZ7ibWL6IB3ndF8eGQo6QqCR5POwmGqE0OXtcjw4esSdrMicYMqy1uA/640?wx_fmt=gif)

在 iOS 16 及更高版本中，您可以将照片的主题抠图出来，然后复制或共享

  

**开源数据集的“标准答案（Ground truth）错误百出**  

图像算法工程师在商业项目中，经常会要求标注员重新标注开源数据集，这花费了不少的成本。这主要是原因是开源数据集的“标准答案（Ground truth）”并不标准，其中存在这大量的标注错误。

![](https://mmbiz.qpic.cn/mmbiz_png/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2ReqJbmuopNAnjMy7yy7ic1rq53vz48YJgibn0qiaYsveTpJBhXj2zd24Bg/640?wx_fmt=png)

对于一些细分场景的研究时，这些人工标注是不能达到数据质量的要求的。例如，一位工程师在做交通灯的场景相关研究时发现，COCO 等数据集的标注错误是非常明显的。这些问题也存在于其它的知名数据集，例如 CIFAR-100 和 ImageNet。数据标注是一项容易出错的艰巨任务，其原因既有模糊的标注要求文档说明，也有人为主观判断不一致性等。SAM模型同样也存在部分漏标、误标问题。

![](https://mmbiz.qpic.cn/mmbiz_png/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2RibOsqJOHSEbvBkufyrqGNhgWwcn4vx3bneFBpicqTfas3e2ANicwLz7sg/640?wx_fmt=png)

COCO 数据集关于红绿灯的错误标注

  

**无法胜任于专业领域**

因此，前文提到的 SAM 与人工标注的比较时，它已经非常接近或者在某些数据分割的表现超越了人工标注结果时，我们只是惊讶——为什么开源数据集的质量这样差？相信也没有人会 100% 使用 ChatGPT 回复的结果，放在自己的文章中，我们在其中不得不接受那些很有道理但是扭曲了事实的“胡说八道”。通用大模型所训练的专业数据不够时，也无法满足项目的需求。在一些严谨的学科，例如在医学诊断，自动驾驶，安防等领域，我们是无法容忍这样的错误的。对于专业领域、非通用型图像，SAM标注不够理想。

![](https://mmbiz.qpic.cn/mmbiz_png/IYRh6cxLmF0icJqFn80TTiaa9XbnVIsF2RlEmsBASfBYLUictNBbibPHNVqD3CfkiaNm6KeoJs2Qy4UbVxm9JOVZsaQ/640?wx_fmt=png)

SAM 在医学方面的数据标注并不理想，这要求具有专业背景的医生来完成此项工作

  

**其他挑战**

这里还有类似于 ChatGPT 已经遇到的算力问题和数据安全。在实际环境中，很多上线的小型模型也无法承受过大的运行成本等。

  

**机遇**

确实，随着人工智能技术不断的发展，传统的 NLP、CV 技术未来可能会逐渐淘汰。未来的研究方向应该聚焦于更深层次、更抽象的框架下进行思考和探索。

**● 接受并利用尖端技术**：革命性的新技术所带来的不应是对行业的惶恐的绝望，我们要试图去理解并利用它，这些新范式将帮助我们提高已有的生产效率，从而为未来的技术创新奠定坚实的基础。在很多细分赛道，专业的人士仍需继续深耕。

**●** **软件开源**：AI 技术的迅猛发展得益于开源的理念，它让每个人可以站在巨人的肩膀上，这也是我们打造 Xtreme1 的初衷：

_https://github.com/xtreme1-io/xtreme1/_

_Xtreme1 是全球首个开源多模态训练数据平台，通过提供 AI 赋能的软件工具、数万项目提炼的本体中心和丰富的数据治理特性，来加速多模态训练数据的处理效率，进而提高 AI 工程师的建模效率。特别是在 2D & 3D 多模态融合数据方面，标注效率的提升可达 72%。自 2022 年 9 月 15 日正式开源以来，Xtreme1 平台已经在 2022 年 12 月 15 日成为了 LF AI & DATA 托管项目。_

**● 数据开源**：没有优秀的数据，AI 是无法正确运作的。我们最近也在研究全球首个多模态数据，涵盖了最新的传感器设备以及精准地人工标注数据，敬请期待~

  

  

 SA-1B下载脚本与图像分割评测数据集

最后，分享SA-1B数据集快速下载脚本及其评测数据集资源：

**● 下载代码：**

    cat ~/fb-sam.txt | parallel -j 5  --colsep $'\t'  wget -nc  -c  {2}    -O {1}

（滑动查看）

注：fb-sam.txt是跳过标题行的_数据集 txt_ 的文件副本。浏览器访问：amz.fun/2\_n0i

  

**● 评测数据集资源（部分）：**

**ADE20K**

_https://opendatalab.com/ADE20K\_2016_

  

**NDD20 (Northumberland Dolphin Dataset 2020)**

_https://opendatalab.com/NDD20_

**LVIS**

_https://opendatalab.com/LVIS_

  

**STREETS**

_https://opendatalab.com/STREETS/download_

  

**VISOR**

_https://opendatalab.com/VISOR_

  

**WoodScape**

_https://opendatalab.com/WoodScape_

  

**TrashCan**

_https://opendatalab.com/TrashCan_

  

**PIDray**

_https://opendatalab.com/PIDray_

  

**GTEA (Georgia Tech Egocentric Activity)**

_https://opendatalab.com/GTEA_

本文作者｜张子千 Nico  

本期封面图来自 Segment Anything | Meta

  

**引用**

\[1\] ChatGPT爆火后，NLP技术不存在了. 

_https://mp.weixin.qq.com/s/FknHZ\_FFdwdofp5vn9ot3g_；

\[2\] Segment Anything. 

_https://ai.facebook.com/blog/segment-anything-foundation-model-image-segmentation_；

\[3\] Create and share photo cutouts on your iPhone. 

_https://support.apple.com/en-us/HT213459_；

\[4\] The Mislabelled Objects in COCO. 

_https://www.neuralception.com/mislabelled-traffic_；

\[5\] How I found nearly 300,000 errors in MS COCO. 

_https://medium.com/@jamie\_34747/how-i-found-nearly-300-000-errors-in-ms-coco-79d382edf22b_；

\[6\] 感谢OpenDataLab提供的数据集支持，更多数据集请访问：

_https://opendatalab.com；_

\-END-

更多公开数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言