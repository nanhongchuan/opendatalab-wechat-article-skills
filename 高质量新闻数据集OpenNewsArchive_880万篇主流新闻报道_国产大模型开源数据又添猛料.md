     高质量新闻数据集OpenNewsArchive：880万篇主流新闻报道，国产大模型开源数据又添猛料 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

高质量新闻数据集OpenNewsArchive：880万篇主流新闻报道，国产大模型开源数据又添猛料
=================================================

原创 热爱学习的 OpenDataLab 2024-05-15 14:22 上海

> 原文地址: [https://mp.weixin.qq.com/s/umCkf2hDkeaclBbS13km5A](https://mp.weixin.qq.com/s/umCkf2hDkeaclBbS13km5A)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

  

在构建国产大语言模型的道路上，高质量新闻是不可或缺的重要语料之一。这类语料集**准确性**、**逻辑性**、**时效性**于一体，同时包含**丰富的事实知识**，可以大幅提升模型的**文本生成质量**、**词汇表达能力**、**事件理解分析能力**以及**时序内容的适应性和预测能力**，使其在现实世界的应用中更加准确和可靠。

  

近日 ，为了更好地满足大模型研发的数据需求，大模型语料数据联盟开源了大规模、高质量新闻数据集——**开放新闻库数据集（OpenNewsArchive）****，提供了多个主流媒体来源、多种主题类型、共计880万篇新闻文章信息，为研究人员和数据科学家提供了丰富的文本数据资源**。一起来看看。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**开放新闻库介绍**

**（OpenNewsArchive）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6iagPYutnSRK8QqUSiaeIf8cjaBu15YrTBUUJQUU0o1b5UL6JDskpj33TiatuxOmd8Z8YY682DkBMmA/640?wx_fmt=png&from=appmsg)

  

**开放新闻库（OpenNewsArchive）****数据集******是由OpenDataLab联合蜜度、商汤等多家联盟机构进行开源开发，其中包含了880万篇新闻文章的信息，涵盖了各种不同主题和来源的新闻内容。每篇新闻文章包括字段如标题、内容、发布日期、语言等，且数据集的内容经过数据清洗去重等处理，为研究人员和数据科学家提供了丰富的文本数据资源。

  

**下载链接：**

_https://opendatalab.com/OpenDataLab/OpenNewsArchive_

  

  

 数据集亮点

**数据集具有三大亮点：**

**● 内容全面覆盖多个板块**：包含财经、健康、军事、体育、房产、社会、学术等多个板块分类的新闻内容，涵盖广泛。

**● 无毒性内容和价值偏见**：新闻内容不含有害信息或偏见观点，确保信息公正客观。

**● 保持新闻内容更新**：数据集中包含的新闻发布日期主要集中在2023年，相较于其他已知的开放新闻数据集，具有较高的时效性，有利于提高模型预测的准确性与应对能力。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**数据处理方法**

  

 数据处理方法

**1\. 处理HTML标签：**针对文本中含有HTML标签的部分进行清洗，去除标签并保留文本内容的可读性。

  

**2\. 清洗无效文本：**删除全文无标点的文本和文本长度过短的部分，确保数据集中的文本质量。

  

**3\. 清除特殊字符：**删除文本中的特殊字符，包括emoj表情、特殊符号等，保持文本干净规范。

  

**4\. 处理重复内容：**去除重复的段落，确保每个新闻内容唯一。

  

**5\. 清洗混入的不明文本：**逐行检查处理文本中包含关键词的句子或内容，确保数据集的纯净性。

  

**6\. 删除非法语言部分：**排除非汉语和英语以外的语言内容，确保数据集的语言合法性。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**数据信息**

  

 基本信息

● **数据模态**：纯文本数据

● **主要语言**：中文、英文；（中文占比超过99.9%）

● **数据量**：27GB；880万篇文章

● **数据格式**：以Jsonlines形式存储的语料文本与附加信息

  

  

 统计信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD43yQROvYBOeSZ92icwCyoicP0WZWNEt1dZhvk1d4GiapwJtrGaztrLUXQic6RhF4EFq5j3jmGMiaWVfdw/640?wx_fmt=png&from=appmsg)

（开放新闻库数据集中2023年发布的新闻最多）

###   

  

 数据样例

    {

### （左右滑动查看全部）

  

  

 数据字段格式

以下表格记录了数据各字段的字段名，意义，数据类型和取值说明：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6iagPYutnSRK8QqUSiaeIf8cJdQXu0UwQnmyXEjzOesBic5QCiaHVibdVbvEOTic0AGxTlFYpT6LLNyqvg/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**许可**

**开放新闻库****数据集**整体采用_**CC BY 4.0**_许可协议。您可以自由共享、改编该数据集，唯需遵循以下条件：  

  

**● 署名：**您必须适当地标明作者、提供指向本协议的链接，以及指明是否（对原始数据集）做了修改。您可以以任何合理的方式这样做，但不能以任何方式暗示许可人同意您或您的使用。

  

**● 没有附加限制：**您不得使用法律条款或技术措施来限制他人执行许可证允许的任何操作。完整协议内容，请访问_**CC BY 4.0**_协议全文。

  

===

   **特别注意事项**

请注意，本数据集的某些子集可能受制于其他协议规定。在使用特定子集之前，请务必仔细阅读相关协议，确保合规使用。更为详细的协议信息，请在特定子集的相关文档或元数据中查看。

  

OpenDataLab作为非盈利机构，倡导和谐友好的开源交流环境，若在开源数据集内发现有侵犯您合法权益的内容，可发送邮件至（_OpenDataLab@pjlab.org.cn_），邮件中请写明侵权相关事实的详细描述并向我们提供相关的权属证明资料。我们将于3个工作日内启动调查处理机制，并采取必要的措施进行处置（如下架相关数据）。但您应确保您投诉的真实性，否则采取措施后所产生的不利后果应由您独立承担。

  

* * *

  

开放新闻库数据集已上架OpenDataLab官网

扫码直达↓

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD43yQROvYBOeSZ92icwCyoicPCVtiaxKPRNdspjAAAeOGLB1zRb5IElKTibpXOSsARLUlILicwYibicLKf6w/640?wx_fmt=png&from=appmsg)

阅读原文或浏览器访问：

**https://opendatalab.com/OpenDataLab/OpenNewsArchive**  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言