     收藏丨8个常用中文OCR数据集，附下载链接 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

收藏丨8个常用中文OCR数据集，附下载链接
=====================

原创 专注于AI 数据的 OpenDataLab 2022-06-07 19:45 上海

> 原文地址: [https://mp.weixin.qq.com/s/AItZNCHXID-GZRNpuaYT-g](https://mp.weixin.qq.com/s/AItZNCHXID-GZRNpuaYT-g)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

扫一扫识别文字、拍照翻译、拍照搜题、车牌自动识别……这些随处可见的功能，给我们的工作和生活带来了极大的便利，其背后都离不开OCR技术的支持。

  

  

随着深度学习技术的发展，智能OCR算法与应用也越来越丰富，对相关数据的需求也增加。

  

许多小伙伴反馈中文OCR数据集不好找，今天我们贴心地帮大家整理了8个常用的中文OCR数据集资源，记得收藏。

  

  

  

_********No.1********_  

**MSRA-TD500** **(MSRA Text Detection 500 Database)**

下载链接：  

https://opendatalab.com/MSRA-TD500

  

  

MSRA-TD500由华中科技大学于 2012 年在 CVPR 发布，是一个用于测试和评估多方向、多语言文字检测算法的自然图像数据集，包含500幅拍摄于室内（办公室和商场）和室外（街道）场景的自然图像。室内的图像主要包括标识、门牌和标牌等，室外的图像主要是路牌和广告牌等。图像的分辨率较高，介于1294\*864和1920\*1280之间。

  

该数据集由两部分构成：训练集、测试集。训练集中一共有300幅图像，通过随机抽样的形式从原始数据集中抽取出来。余下的200幅图像构成测试集。

  

数据集中的所有图像都经过完整标注。数据集的基本单元是文本行而非单词。  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKC6QvK6ClrH6BqBjT6DhLlvMIaFJ4UeXDHj7gqibJGpcgZqhFgA5PxRUg/640?wx_fmt=png)

MSRA-TD500数据集样例（图源：参考资料\[1\]）

  

MSRA-TD500数据集中的典型图像以及文字的标准矩形框 每一个矩形框对应一个文本行。红色的矩形框表示其中的文字被标记为“困难”。在MSRA-TD500数据集中，难以检测的文字（一般由低分辨率、模糊和遮挡等因素造成）会被标记为“困难”。

  

  

  

_********No.2********_  

**Chinses Text in the Wild(CTW)**  

下载链接：  

https://ctwdataset.github.io/  

  

由清华大学与腾讯共同推出的一个大型中文自然文本数据集（Chinese Text in the Wild，CTW）。该数据集包含 32,285 张图像和 1,018,402 个中文字符。

  

每张图像尺寸为2048\*2048，数据集大小为31GB。CTW以（8:1:1）的比例将数据集分为：

训练集（25887张图像，812872个中文字符）；

测试集（3269张图像，103519个中文字符）；

验证集（3129张图像，103519个中文字符）；

  

这些图像源于腾讯街景，从中国的几十个不同城市中捕捉得到。数据多样、复杂，它包含了平面文本、凸出文本、城市街景文本、乡镇街景文本、弱照明条件下的文本、远距离文本、部分显示文本等。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKCj7kVlHAq6cSAyrZc1Zv4w9vjXDWD8NXkIYCIzibIQRDYkeNjibv50BqQ/640?wx_fmt=png)

CTW数据集样例示意（图源：参考资料\[2\]）

  

对于每张图像，数据集中都标注了所有中文字符。对每个中文字符，数据集都标注了其真实字符、边界框和 6 个属性以指出其是否被遮挡、有复杂的背景、被扭曲、3D 凸出、艺术化，和手写体等。

  

  

  

_********No.3********_  

**Reading Chinses Text in the Wild(RCTW-17)**

下载链接：

https://rctw.vlrlab.net/dataset.html

  

  

ICDAR（国际文档分析和识别大会）在2017年发起了一项专注于中文检测和识别比赛项目（RCTW），RCTW-17为竞赛数据集，它由12263张包含中文的自然场景图片组成，其中大部分是直接由摄像头或手机拍摄，少部分为生成图像，并且每张图像至少包含一行中文。图像尺寸不规则，数据集大小为11.4GB。

  

数据的标注均通过标注工具手工标注完成，通过绘制四边形来标注一个文本行，而不是以单词为单位进行标注，每个文本行的内容以UTF-8字符串进行标注。在数据集中存在字体、布局和语言等多样性。

  

数据集划分为两部分：训练集和验证集。训练集包含8034张图片，测试集包含4229张图片。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKCiaAaOP3g7WtJPlsfEZTwXhgibulzNN0ia51gDxMZcPoRibVVj8ccFd2PJA/640?wx_fmt=png)

RCTW-17数据集样例示意（图源：参考资料\[3\]）

  

  

  

_********No.4********_  

**ICPR MWI 2018挑战赛**

下载链接：

https://tianchi.aliyun.com/competition/entrance/231685/information

  

  

ICPR MWI 大赛提供的包含2000张图像的官方数据集，主要由合成图像，产品描述，网络广告构成。该数据集数据量充分，中英文混合，涵盖数十种字体，字体大小不一，多种版式，背景复杂。数据集大小为2GB。其中训练集10000张，测试集10000张。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKCI2C0YibfKC8e3YIn8XV09wcRv3jdyhhDibPR2ApoUH6R0wf6e49d736w/640?wx_fmt=png)

ICPR MWI 2018数据集标注样例，红框代表标注的文本框（图源：参考资料\[4\]）

  

  

  

_********No.5********_  

**ShopSign**

下载链接：

https://github.com/chongshengzhang/shopsign

  

  

该数据由河南大学科研团队发布的，是一个大规模中英文自然场景文本数据集，其包含25770张街景中文招牌图像，196010条文本行。

  

ShopSign中的图像是在不同的场景（市中心到偏远地区）中使用50多种不同的手机拍摄。相比于CTW，其包含了4000张夜间图像，同时也包含了2516对图像来对一个sign获取水平和多视角的图片。其包含多种分辨率，包括3024\*4032、1920\*1080、2180\*720等。

  

CMT主要包含了几个主要发达城市，而ShopSign包含的地理范围广（北京、上海、厦门、新疆、蒙古、牡丹江、葫芦岛和河南省的一些城市和小城镇），包括许多街景车辆无法到达的郊区或小城镇。CMT使用了固定的拍摄角度，而ShopSign使用了多种角度进行拍摄。\[5\]

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKCNQHLIy81H6Hfdt2LTEe5d9ic34RR2hxVMtudLI9kT19ticvjSaKURtdQ/640?wx_fmt=png)

ShopSign数据集中广告牌样例示意（图源：参考资料\[5\]）

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKCCN0tUGIzrSPdxVUtJY2C13dKrA2FicXREHicmG6WgCkz1gYwiagW64BMg/640?wx_fmt=png)

ShopSign数据集中广告牌分类示意（图源：参考资料\[5\]）

  

注释包括了每个文本行的四边形边界框的坐标（顺序：左上、右上、右下、左下）以及相对应的文本行的相应文本。ShopSign仅仅处理广告牌上的文本。

  

  

  

_********No.6********_  

**ICDAR2019-LSVT**

下载链接：

https://github.com/chongshengzhang/shopsign

  

  

ICDAR 2019-LSVT（Large-scale Street View Text with Partial Labeling，弱标注大规模街景文字识别）国际学术竞赛公开的大规模弱标注场景文字数据集。

  

数据集采自中国街景，并由街景图片中的文字行区域（例如店铺标牌、地标等等）截取出来而形成。是首个提出弱标注数据的场景文字数据集，其中包括5万张精标注街景图像、40万张弱标注街景图像，总计45万张。

  

所有图像都经过一些预处理，将文字区域利用仿射变化，等比映射为一张高为48像素的图片。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKC2qd5qGooJibxiblfia0sjeGAKpzdJAX0uk1Tu2qQxe6aia1SURJkG6Gb1Q/640?wx_fmt=png)

LSVT数据集精标注示意（图源：参考资料\[6\]）

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKC3Iwf6NZnKOuvuoXANpFrUFlqzpJM5pGcjsNjBsP9GFUNviaNVcg07HQ/640?wx_fmt=png)

LSVT数据集弱标注示意（图源：参考资料\[6\]）

  

  

  

_********No.7********_  

**TotalText**

下载链接：

https://opendatalab.com/TotalText  

  

Total-Text是最大弯曲文本数据集之一-ArT（任意形状文本数据集）训练集中的一部分。该数据集共1555张图像，11459文本行，包含水平文本，倾斜文本，弯曲文本。文件大小441MB。大部分为英文文本，少量中文文本。其中训练集有1255张图像，测试集有300张图像。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKCK3yoG0vMkAruZdKYfc0Ih1VPCLeHVicJFwGibtUKqUcuotiayJhzoicgKw/640?wx_fmt=png)

TotalText数据集样例示意（图源：OpenDataLab）  

  

  

  

_********No.8********_  

**Caffe-ocr中文合成数据**

下载链接：

https://github.com/senlinuc/caffe\_ocr

  

  

共360万张图片，图像分辨率为280\*32，文件大小约为8.6GB。数据利用中文语料库（新闻+文言文），通过字体、大小、灰度、模糊、透视、拉伸等变化随机生成，字典中包含汉字、标点、英文、数字共5990个字符（语料字频统计，全角半角合并）。

  

每个样本固定10个字符，字符随机截取自语料库中的句子。按9:1分成训练集、验证集，测试集约6万张。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7YrgdNDSweibQyclCBzqzKCeDT8Oiaa2zoaBdeRqyv2yicpyqDEUjImpyU3ACtHk9Tic5BDhelLnyKlg/640?wx_fmt=png)

Caffe-ocr数据集样例示意（图源：参考资料\[7\]）  

  

  

  

**参考资料**

\[1\]http://www.iapr-tc11.org/dataset/MSRA-TD500/Detecting\_Texts\_of\_Arbitrary\_Orientations\_in\_Natural\_Images.pdf

\[2\]https://ctwdataset.github.io/

\[3\]https://arxiv.org/pdf/1708.09585v2.pdf

\[4\]https://tianchi.aliyun.com/competition/entrance/231685/information

\[5\]https://arxiv.org/pdf/1903.10412v1.pdf

\[6\]https://rrc.cvc.uab.es/?ch=16

\[7\]https://github.com/senlinuc/caffe\_ocr

  

  

  

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