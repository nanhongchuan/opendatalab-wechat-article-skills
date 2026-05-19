     登顶GitHub Trending，开源工具MinerU助力复杂PDF高效解析提取 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

登顶GitHub Trending，开源工具MinerU助力复杂PDF高效解析提取
=========================================

原创 MinerU OpenDataLab 2024-07-30 19:20 上海

> 原文地址: [https://mp.weixin.qq.com/s/5IRp9q0lby6cMPWbL-DS8A](https://mp.weixin.qq.com/s/5IRp9q0lby6cMPWbL-DS8A)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

在7月4日举行的WAIC 2024科学前沿主论坛上，书生·浦语2.5正式发布，面向大模型研发与应用的全链条工具体系同时迎来升级。在数据处理环节，**上海人工智能实验室（上海AI实验室）大模型数据基座OpenDataLab团队开源了全新的智能数据提取工具——MinerU**。

  

MinerU 不仅能将混合了图片、公式、表格、脚注等在内的复杂多模态 PDF 文档精准转化为清晰、易于分析的 Markdown 格式；同时支持从包含广告等各种干扰信息或者复杂格式的网页、电子书中快速解析、抽取正式内容，有效提高AI语料准备效率，助力各行业利用大模型、RAG等技术，结合学术文献、财务报告、法律文件、电子书籍等专业文档，打造垂直领域的新知识引擎。

  

**MinerU项目地址**

__https://github.com/opendatalab/MinerU（点击文末“阅读原文”直达）__

  

**PDF-Extract-Kit PDF模型解析工具链代码**

_https://github.com/opendatalab/PDF-Extract-Kit_

  

MinerU代码公开之后，凭借精准、快速的SOTA效果，媲美甚至超过商业软件的性能，获国内外多个技术大V点赞，GitHub Star累计飙升3000+，登顶GitHub Python Trending（2024年7月28日-29日），成为AI数据清洗中一个优秀的开源工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7KWFKPY6v8KOdkQaxsDXSSv2c7FvaeuP7tnI8sSsS1lbXn9XPDyYkAyMVJqX1JhvwPYTyqKNOrCg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7wibjydMrAxkbhm4ye7ZHVN5mS7NoDhj9YeniaNRlSn1T1P8Be3d9LlOemxtXadJ4yT7ibMQJXuibkdQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7wibjydMrAxkbhm4ye7ZHVNeSbArEQibK0ysRJPLC5GUheMO6sar0vPYxKswpnrSv5JFlNJxg0eibIg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7wibjydMrAxkbhm4ye7ZHVNuNSHiaguE7whaftYrZWZAlNhsm9uGJV1OgypHj8qXdJic3x5VjqDUlGw/640?wx_fmt=png&from=appmsg)

  

****一、MinerU功能介绍****

MinerU 可以将 PDF 转化为 Markdown 格式。支持转换本地文档或者位于支持S3协议对象存储上的文件。**主要功能包含**：

● 支持多种前端模型输入

● 删除页眉、页脚、脚注、页码等元素

● 符合人类阅读顺序的排版格式

● 保留原文档的结构和格式，包括标题、段落、列表等

● 提取图像和表格并在Markdown中展示

● 将公式转换成LaTex

● 乱码PDF自动识别并转换

● 支持CPU和GPU环境

● 支持Windows/Linux/Mac平台

（更多详细介绍，请[**点击此处**](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247537349&idx=2&sn=4a80e4ffd5dfd8feebaf0f4c41cecf67&chksm=c10cc027f67b49310870bbda4f5d78ed3af14cf9ac859f8caf72c606bdba8b478bb85a2d4a39&scene=21#wechat_redirect)查看）

  

（MinerU功能完整介绍视频）

  

**二、PDF提取流程及技术架构**

  

PDF文档相比网页、电子书等结构标准化的文件含有更多复杂的元素，处理更具挑战性和代表性，所以接下来，将以PDF为代表，重点介绍 MinerU 如何实现高质量文档数据提取。

  

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7wibjydMrAxkbhm4ye7ZHVNaYazoJrn0iaZjASmct0jXqJNBpqhKyqTHZtJhNIAjanaGLLSWF8iaZhA/640?wx_fmt=png&from=appmsg)**

（流程图）

  

**MinerU PDF文档提取，主要由4大环节构成：**

  

**● PDF文档分类预处理**

MinerU支持不同类型的PDF文档提取，包括文本型PDF、图层型PDF、扫描版PDF；初始阶段，输入PDF文档，系统会启用文档分类模块，提取PDF元数据，检测是否有乱码，是否是扫描版，进行PDF类型识别预处理。

（注：文本型PDF：文字可以复制；图层型PDF：文字不可复制，解析乱码）

  

**● 模型解析，PDF内容提取**

紧接着，利用高质量PDF模型解析工具链进一步对PDF文档进行Layout区块布局检测，准确定位标题、正文、图片、表格、脚注、边注等重要元素位置，与此同时，结合公式检测模型定位公式区域。最后结合高质量公式识别及OCR技术提取准确的文本、公式内容，存储到JSON文件中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7wibjydMrAxkbhm4ye7ZHVN8oveUvnxNYEu0BsZ8icOJpQjrjJLZXzGWH3qObl7Jh2YmMoorqUYkuA/640?wx_fmt=png&from=appmsg)

  

**● 管线处理，支持多种格式输出**

模型处理的数据会输入管线，进行后处理：确定块级别顺序，删减无用元素，依靠版面对内容排序、拼装，保证正文流畅。处理方式包括：坐标修复、高iou处理、图片、表格描述合并、公式替换、图标转储、Layout排序、无用移出、复杂布局过滤等。

  

管线处理好的文档信息会变为一个统一的中间态：middle-json（包含PDF解析出来的所有的信息），开发者可以按照使用需求自定义输出Layout、Span、Markdown、Content list等不同的格式。

（注：Content list是作者团队开发的一套列表样的序列结构格式，比Markdown格式能保留更多信息，可用于多模态、NLP等大模型训练）

  

**● PDF提取结果质检**

团队利用由论文、教材、试卷、研报等多种类型文档组成的人工标注的PDF自测评测集，对整个流程进行检测，保证每次开发调优、算法改进后，提取效果越来越好；同时利用可视化质检工具，将PDF提取结果进行人工质检与标注，再反馈给模型训练，进一步提升模型能力。

  

**详细项目全景图如下：**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7wibjydMrAxkbhm4ye7ZHVN4paGIx8zEiaypvn02g1ssk8wsiaticnPib3ZtmWXeO06xy1xd1Wf8cJiclA/640?wx_fmt=png&from=appmsg)**

  

**三、高质量PDF模型解析工具链**

MinerU PDF模型解析工具链 _PDF-Extract-Kit_，主要由四个关键模块组成：

**● 布局检测**：使用 _LayoutLMv3_ 微调出来的检测模型进行区域检测，如图像，表格、标题、文本等；

**● 公式检测**：使用基于 _YOLOv8_ 自研的公式检测模型进行公式检测，包含行内公式和行间公式；

**● 公式识别**：使用自研的 _UniMERNet_ 公式识别模型进行公式识别；

**● 光学字符识别**：使用 _PaddleOCR_ 模型进行文本识别；

  

在论文、教材、研报、财报等多样性的PDF文档上，MinerU的pipeline都能得到准确的提取结果，对于扫描模糊、水印等情况也有较高鲁棒性。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7KWFKPY6v8KOdkQaxsDXSSWtFuSr5LYz2JFp1x7mrkKGYpv6gtiaB1lrN9GTj5ZXQn7BLC9sINyDg/640?wx_fmt=png&from=appmsg)

（不同类型PDF提取效果示意）

  

**四、评测指标**

### 

### **● 布局检测**

### 作者团队将 MinerU 与现有的开源 Layout 检测模型做了对比，包括 _DocXchain_、_Surya_、_360LayoutAnalysis_ 的两个模型。而 _LayoutLMv3-SFT_ 指的是他们在_LayoutLMv3-base-chinese_ 预训练权重的基础上进一步做了SFT训练后的模型。论文验证集由402张论文页面构成，教材验证集由587张不同来源的教材页面构成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7KWFKPY6v8KOdkQaxsDXSSfibImpNgrOpPJFC5MPTjWEicbdGgqrKN8zzRApXRn51kUdJYicyPVORicA/640?wx_fmt=png&from=appmsg)

###   

### **● 公式检测**

### 作者团队将 MinerU 与开源的模型 _Pix2Text-MFD_ 做了对比。其中，_YOLOv8-Trained_ 是他们在_YOLOv8l_ 模型的基础上训练后的权重。论文验证集由255张论文页面构成，多源验证集由789张不同来源的页面构成，包括教材、书籍等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7KWFKPY6v8KOdkQaxsDXSSrLAGKJFySwMhrvQpKHYYhZmSwjPd5r03uZDkbkXwHAW0YAgBqpFWUw/640?wx_fmt=png&from=appmsg)

  

### **● 公式识别**

公式识别作者团队则直接使用了 _UniMERNet_ 的权重，没有进一步的SFT训练，其精度验证结果可以在其GitHub页面获取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7KWFKPY6v8KOdkQaxsDXSSfic8nyL0gC7twojNXTv5dicnIxc15HXH2tbAneuBX1x5dPwd3j2qLxYA/640?wx_fmt=png&from=appmsg)

###   

### **●光学字符识别**

### 使用了PaddleOCR 官方提供的权重，没有做进一步的训练和验证，因此不涉及验证代码。

###   

**评测结果显示，MinerU在布局检测、公式检测、公式识别多个维度上性能都远超其他开源模型，识别准确率也非常不错**。更多评测详情，请访问：

_https://github.com/opendatalab/PDF-Extract-Kit/blob/main/assets/validation/README-zh\_CN.md_

  

**五、MinerU部署及使用**

**MinerU完整部署及使用文档请访问：**

_https://github.com/opendatalab/MinerU_

  

**MinerU能力已集成在新一代大语言模型书生·浦语2.5（InternLM2.5）**中，可以与AI进行文档格式转化及内容问答交互，欢迎大家体验。

  

**更多开源数据处理宝藏工具，尽在 OpenDataLab GitHub仓库：**

_https://github.com/opendatalab_  

**还有超好用的多模态标注工具 LabelU：**

_https://github.com/opendatalab/labelU_

**多模态对话标注管理平台Label-LLM:**

_https://github.com/opendatalab/LabelLLM_

**不要吝啬你的star!**

**你的star是作者前进最大的动力！**

**快来点个star支持一下吧！**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7yjDpC9UfD4RCWcW9LvdDRgnguSOV8bygShpItrUdGdgB8tbfgcVndLIOHEB3Abg8vb5pI8FpzPzyrNrzxzZicg/640?wx_fmt=gif&from=appmsg)

  

欢迎扫码进大模型数据处理交流群，还有哪些需求，尽管提

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD73YXswn0XWT4bLm7ClibnIcHJtZnNo5k8ZZlJYQ0S7knjYKHXILd6amZAO3UTULPiardEya7yrCJ5g/640?wx_fmt=jpeg&from=appmsg)

**更多精彩数据内容，尽在OpenDataLab**

_https://opendatalab.org.cn/_

  

  

  

  

  

  

  

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言