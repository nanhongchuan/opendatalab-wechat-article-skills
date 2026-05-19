     CVPR 2023 演讲分享 | 上海人工智能实验室青年科学家 何聪辉 博士解密最新 OpenDataLab \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

CVPR 2023 演讲分享 | 上海人工智能实验室青年科学家 何聪辉 博士解密最新 OpenDataLab
======================================================

原创 专注于AI 数据的 OpenDataLab 2023-06-26 16:17 上海

> 原文地址: [https://mp.weixin.qq.com/s/Lygm0d1aMOrikE1BnmQMiA](https://mp.weixin.qq.com/s/Lygm0d1aMOrikE1BnmQMiA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)  

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7oHuZcCoUp6603oibJ8Lq28lrTyg9QBtzQnYYDVXulDh03JkYQdbD4EVgexNfNKu4WFezqrdq31zA/640?wx_fmt=png)**

  

上周，万众瞩目的计算机视觉行业盛事 CVPR 落下帷幕。在本届 CVPR 上，OpenDataLab 联合 OpenMMLab 成功举办了一场 Tutorial，非常荣幸地邀请了5位重磅嘉宾分享。

  

其中，上海人工智能实验室青年科学家、OpenDataLab 开源项目创始人何聪辉博士重点介绍了 OpenDataLab 平台及最新开源数据集工具相关研究工作。接下来，和小编一起了解最新的 OpenDataLab 吧。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**AI 大模型时代的数据平台**

随着信息技术的快速进步，内容消费方式也在不断地变革。我们见证了音频、视频、文档工具等，从过去单一的工具形态演化到现在多样化的音乐、视频、电子书、APP等内容平台。**在科研领域，关键的“生产要素”——论文、代码等也正在以内容平台的形式逐步形成开放社区，信息获取更加轻松、便捷**。

  

对于当前的人工智能时代，数据已经成为 AI 发展的重要内容，**所以一个聚合、高效的数据集内容平台成了必然之需**。在此背景下，上海人工智能实验室青年科学家 何聪辉 博士带领团队研发了 OpenDataLab 人工智能开源数据平台，旨在为 AI 研究人员和开发人员提供易于访问、贡献简单且易于共享的标准化开放数据集，推动数据开放共享，提升 AI 开发效率，助力国产大模型发展。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**OpenDataLab最新内容**

OpenDataLab作为一个开源数据集社区，提供了丰富多样、高质量的数据集生态内容：

  

01

**海量开源数据集资源**

目前OpenDataLab已收录了包含CVPR/IEEE等顶会顶刊、大语言模型评测/预训练、多模态大模型、AIGC、自动驾驶、智慧医疗、经典Benchmark、CV算法框架OpenMMLab常用等热门专题在内的**5,415个高质****量公开数据集。**

  

数据集类型十分丰富，涵盖**30多种数据类型，50多种标注类型，可以支撑800多种任务类型，覆盖20多个应用场景**。平台在国内设置了站点，支持全球用户一键查询与免费高速下载。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7oHuZcCoUp6603oibJ8Lq28OZ7Ric04icNc8zEao594rIzWScjTgeScmic6FBBhiacfmLF8dW5cSRicsAQ/640?wx_fmt=png)

体验地址：https://opendatalab.org.cn/

  

02

**数据处理开源工具包**

OpenDataLab 提供了一系列便捷的数据处理开源工具包，帮助用户快速、自主地完成数据获取、预处理、清洗、标注等任务。

  

在这里，你可以通过多种灵活的数据采集方式，完成“棘手”的大型数据集下载。平台不仅提供了可根据索引下载原图的工具，帮助你成功下载Laion-5b 类型的数据集；另外提供了一行代码下载原始数据的脚本，让你轻松获取 SA-1B 数据集。

Laion-5b下载工具：  

https://github.com/opendatalab/laion5b-downloader

SA-1B一键下载脚本：  

https://github.com/facebookresearch/segment-anything/issues/60

  

团队发布了支持各种任务的数据采集工具包，具有以下特点：

**● 配置灵活：**支持数据、标签、采集形式的灵活配置

**● 对话评价：**支持交互式实时对话、在线模型评估和多工具配置

**● 多模态数据采集：**灵活配置图文对、图像问答等形式的数据采集和审核

**● 视频工具：**视频字幕和捕获，支持多模式和生成模型的数据准备

  

同时，**OpenDataLab 推出了一款中文的开源数据标注工具——Label U，具有小巧、灵活、通用的特点**。目前具备拉框、多边形、标点、标线、分类、描述等图像标注能力，能够支持目标检测、图像分类、实例分割、文本转写、轮廓线检测、关键点检测等计算机视觉任务场景，通过工具的自由组合即可自定义标注任务，支持COCO、MASK格式数据导出；支持快速集成于其他平台，助力用户开发自己的标注工具。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7ibpQLKIRkDBhsPPTawhiaazHDiceuOOWVhBW2ILZ5yfjDAfAKplPVLXkSbY9YQkicX80Eg1mU4KXQNw/640?wx_fmt=png)

**Label U 开源地址**：

https://github.com/opendatalab/labelU  

  

03

**数据描述语言**

面对多样化的数据格式及组织形式，费时费力的数据格式转化、脚本撰写的工作，**OpenDataLab研发了一套统一的描述语言 DSDL (Data Set Description Language)**，作为新一代人工智能数据集描述语言, 旨在解决AI数据集格式不统一导致的使用不方便问题。最终目标是在未来做到不同任务、不同模态数据间互通互联，推动人工智能进一步发展。

  

**DSDL语言具有以下几个特性：**

**● 通用性**

该语言主要目的是提供一种统一表示的标准，可以覆盖各个领域的人工智能数据，而不是基于特定的一种任务或者某个领域设计。该语言应该可以用一致的格式来表达不同模态和结构的数据。

**● 便携性**

写完无需修改，随处分发。数据集描述可以被广泛的分发和交换，不需要修改就可以在各种环境下使用。这一目标的实现对于建立开发繁荣生态至关重要。为此我们需要仔细检查实现细节，使其对底层设施或组织无感知，从而去除基于特定假设的无必要依赖。

**● 可拓展性**  

在不需要修改核心标准的情况下可以拓展表述的边界。对于C++或者Python等编程语言，应用边界可以通过使用链接库或者软件包得以显著拓展，而核心语法可以在很长的时间内保持稳定。基于链接库和包，可以形成丰富的生态系统，使对应语言可以长时间保持活跃度和发展。

  

**OpenDataLab 已上架116个DSDL标准化数据集：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7ibpQLKIRkDBhsPPTawhiaazpdkxUibcicLVtpLAIu0icMcGicFSqCvZDS9SwsaAoUX4ORjrRIxA8X21JQ/640?wx_fmt=png)

**DSDL详细介绍及进阶玩法，请访问：**

https://opendatalab.github.io/dsdl-docs/getting\_started/overview/

  

以上就是本次分享简介，更多精彩内容，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言