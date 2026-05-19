     DocLayout-YOLO，让多样性文档布局检测更快、更准、更强 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

DocLayout-YOLO，让多样性文档布局检测更快、更准、更强
=================================

原创 热爱学习的 OpenDataLab 2024-10-29 20:00 上海

> 原文地址: [https://mp.weixin.qq.com/s/fYUhOJhUJ-WdCrIRK\_eJsg](https://mp.weixin.qq.com/s/fYUhOJhUJ-WdCrIRK_eJsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

布局检测是文档解析领域的核心任务之一，目标是精准定位文档中不同类型的元素（正文、标题、表格、图片等）。尽管布局检测已经研究很多年，但现有的布局检测算法多关注在论文类型的文档，当面对多样性的文档（如教材、考题、研报等）时，其检测效果还是不及预期。

  

上海人工智能实验室在2024年7月份开源的 **_PDF-Extract-Kit_** 中提供了使用多样性文档微调的 **_LayoutLMv3_** 模型，在众多类型的文档上均取得了不错效果，但其推理速度相对较慢。为了满足实时高质量的推理需求，作者团队近日推出全新布局检测模型 _**DocLayout-YOLO**_，**其推理速度相比于LayoutLMv3提升一个数量级，在A100上每秒可以处理85.5个页面，检测结果也更加精准。**一起来看看。

**DocLayout-YOLO GitHub主页:**

__https://github.com/opendatalab/DocLayout-YOLO__

**DocLayout-YOLO 论文：**

__https://arxiv.org/abs/2410.12628__

**DocLayout-YOLO Demo体验：**

__https://huggingface.co/spaces/opendatalab/DocLayout-YOLO__

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

****DocLayout-YOLO技术解析****

**_DocLayout-YOLO_** 基于YOLOv10模型，并从多样性文档预训练和模型结构优化方面对布局检测模型进行优化。

**● 多样性文档预训练**：DocLayout-YOLO文章中提出**Mesh-candidate Bestfit算法**，自动合成多样性的**文档布局检测数据集DocSynth-300K**，大幅提升模型在多样性文档上检测的鲁棒性；

**● 检测结构优化**：模型结构方面，针对文档元素尺度变化多样的特性，提出**全局到局部的可控感知模块**，更加灵活**适配不同尺度元素**，有效提升YOLO框架对文档元素检测效果。

  

  

 创新点1：基于Mesh-candidate Bestfit的多样性文档合成

  

当前的布局检测数据集类型较为单一，多数集中于论文文档，例如PubLayNet和DocBank。相比之下，其他类型的文档数据集（如DocLayNet、D4LA、M6Doc）数据量较小，仅适用于下游任务的微调和测试，而不适合用于预训练。为了解决这一问题，DocLayout-YOLO项目引入了**Mesh-candidate Bestfit算法。该算法将文档布局合成视作二维矩形拼图问题，通过在文档中不断搜索候选元素（candidate）和空闲块（mesh）的最佳匹配，生成多样化且美观的文档图像**。具体的合成流程可以参考论文中的图1（DocSynth-300K文档数据合成流程图）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVqglsuoMg2dX5MwITTfBwN1kXicyQanBjqtwE0iaLgAxtNgsS7vMAhmOR9ONOhUYibbqc6hJjJOcVXw/640?wx_fmt=png&from=appmsg)

图1 DocSynth-300K文档数据合成流程图

  

合成的数据集在风格上多样且视觉真实度高。布局方面，涵盖了单栏、双栏以及多栏混合文档；在文档风格上，包括论文、报纸、杂志等多种类型的页面。**DocSynth-300K**和现有文档布局检测预训练数据集相比，样式更加多样化，经过DocSynth-300K预训练的模型在多种下游实际文档类型也体现出更强的泛化性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVqglsuoMg2dX5MwITTfBwNTPORwYagc0qrpibnZnJGsk6OBicoLF7c5VkhU5RY9YnwKlicjIuXWMF7w/640?wx_fmt=png&from=appmsg)

图2 DocSynth-300K数据样例

  

目前DocSynth300K数据集已经上线OpenDataLab，

**DocSynth300K数据集：**

_https://opendatalab.com/zzy8782180/DocSynth300K_

**预训练模型**可以在🤗Huggingface获取**：**

_https://huggingface.co/juliozhao/DocLayout-YOLO-DocSynth300K-pretrain_

**DocSynth300K和预训练模型下载方法如下：**

snapshot\_download(repo\_id="juliozhao/DocSynth300K", repo\_type="dataset")

  

  

 创新点2：提出基于全局到局部的可控感知模块

针对文档图像中的尺寸变化挑战，DocLayout-YOLO中提出了**GL-CRM**，结合灵活可控制的**特征提取模块（CRM）**以及从全局到局部的**特征感知架构（GL）**，来实现对不同尺度元素的感知增强。

  

具体来说，**可控感知模块（Controllable Receptive Module，CRM）**，通过参数共享的卷积核，以及一系列不同膨胀率的分支，来提取不同粒度的上下文特征。除此之外，还通过一个特征选择模块，让模型学习到不同粒度特征的重要性程度，实现高效的特征选择和融合。

  

**全局到局部结构（GL）**，通过不同参数控制的CRM，实现从全局到局部的特征感知。针对于最浅层，通过较大卷积核和膨胀率 （） 最大程度保留尺寸较大元素中丰富的上下文纹理特征；在中间层，考虑到纹理特征减少，使用较小卷积核实现对中等尺寸物体感知 （） ；在最深层，考虑到语义信息占主要地位以及计算开销，使用基础瓶颈层作为轻量特征提取模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVqglsuoMg2dX5MwITTfBwNOKGXwcm8H2ia8ZZ0bXWeibpyUWYXo9VIxH3m8VMDXPfOGTyTQITIxjtQ/640?wx_fmt=png&from=appmsg)

图3 可控感知模块CRM

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVqglsuoMg2dX5MwITTfBwNtp2ibNZC3lkibLKickQOANowBclpJwcyumzbOHzXlhz8B3LOln2talSbw/640?wx_fmt=png&from=appmsg)

图4 全局到局部结构（GL）

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****效果展示****

  

DocStructBench评测集上不同方法推理速度及精度对比，DocLayout-YOLO综合效果最佳。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVqglsuoMg2dX5MwITTfBwNcl1KnyCIeTl9s0gOjVqVBgd8X9JNlKQjjZ5CFk3CXG0yZ5r6Ke4VUA/640?wx_fmt=png&from=appmsg)

  

DocLayout-YOLO适用于**多样性文档布局检测**，包括但不局限于**论文、教科书、试卷、幻灯片等多种文档类型**。

  

如下图所示，DocLaytout-YOLO在各种类型的文档上检测效果都很好，且速度极快，可以满足真实场景实时高质量需求。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVqglsuoMg2dX5MwITTfBwNC3x2GoiaVAo73Iz0Xq9LFymYFxG9LSEPibt6IRaOKay5T4qGibxnJlczw/640?wx_fmt=png&from=appmsg)

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****快速上手****

如果想体验DocLayout-YOLO实际检测效果，请试用HuggingFace上的\[🤗Demo\]：

_https://huggingface.co/spaces/opendatalab/DocLayout-YOLO_

  

如果想批量处理文档，请安装配置DocLayout-YOLO环境。

### **● 方法一：根据DocLayout-YOLO GitHub项目安装配置（仅能用于页面布局检测）**

    pip install doclayout-yolo==0.0.2

### 通过以下代码即可完成模型下载、加载，以及推理预测，并且保存结果：

    import cv2

  

### **● 方法二：使用PDF-Extract-Kit项目进行安装配置（可以使用各类SOTA文档解析算法）**

先按照项目README要求安装环境，再执行以下命令即可完成基于DocLayout-YOLO的布局检测以及提取。

    python scripts/layout_detection.py --config configs/layout_detection.yaml

  

**相关链接【欢迎点赞收藏】**

**DocLayout-YOLO GitHub主页:**  

_https://github.com/opendatalab/DocLayout-YOLO_

  

**DocLayout-YOLO 论文：**

_https://arxiv.org/abs/2410.12628_

  

**DocLayout-YOLO Demo体验：**  

_https://huggingface.co/spaces/opendatalab/DocLayout-YOLO_

**PDF-Extract-Kit (包含文档解析各类SOTA模型，使用便捷！)：**

_https://github.com/opendatalab/PDF-Extract-Kit_

**MinerU  (PDF转Markdown工具，超好用！)：**

_https://github.com/opendatalab/MinerU_

  

**不要吝啬你的star!**

**你的star是作者前进最大的动力！**

**快来点个star支持一下吧！**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7yjDpC9UfD4RCWcW9LvdDRgnguSOV8bygShpItrUdGdgB8tbfgcVndLIOHEB3Abg8vb5pI8FpzPzyrNrzxzZicg/640?wx_fmt=gif&from=appmsg)

  

**更多精彩数据内容，尽在OpenDataLab**

_https://opendatalab.org.cn/_

  

  

  

  

  

  

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言