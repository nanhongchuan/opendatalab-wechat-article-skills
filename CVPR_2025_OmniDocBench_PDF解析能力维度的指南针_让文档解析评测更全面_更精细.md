     CVPR 2025｜OmniDocBench：PDF解析能力维度的指南针，让文档解析评测更全面、更精细 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

CVPR 2025｜OmniDocBench：PDF解析能力维度的指南针，让文档解析评测更全面、更精细
===================================================

原创 OpenDataLab OpenDataLab 2025-06-13 17:11 上海

> 原文地址: [https://mp.weixin.qq.com/s/ELqzS2jrXQLpYe16fkYBVw](https://mp.weixin.qq.com/s/ELqzS2jrXQLpYe16fkYBVw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：

  

PDF等文档的内容提取与解析是计算机视觉领域的一个基础任务，它支撑着大模型和检索增强生成（RAG）技术对高质量数据的需求。相关的技术和工具正在蓬勃发展，引起了较多的关注，但是现有的文档解析方法在多样性和评测全面性上还存在较多局限性。

  

为此我们提出一个自动化文档内容提取的多元类型基准OmniDocBench，覆盖了9种文档类型，涵盖19种文档布局和15个属性标签，可以更全面地评估文档内容提取的准确性。

  

本研究成果《OmniDocBench:Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations》已被计算机视觉顶级会议CVPR 2025接收，作者团队来自上海人工智能实验室，Abaka AI，2077AI，欢迎关注。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yGkvvsK4QtSM6vjd1tGIokWxeqhXxjwlTQNrkpN1InJeec8Fen0qsAnw/640?wx_fmt=jpeg&from=appmsg)

  

论文链接：  

https://arxiv.org/pdf/2412.07626

代码：  

https://github.com/opendatalab/OmniDocBench

下载链接：

https://opendatalab.com/OpenDataLab/OmniDocBench

🔎PDF解析指的是将PDF的内容解析成机器可读的格式，比如Markdown、HTML等。PDF解析从2024年上半年开始引起众多关注，一方面是模型训练端需要提取PDF高质量图文数据训练，另一方面是检索增强生成（RAG）成为大模型时代的热门应用，需要提取大量PDF信息建立数据库。

  

🔧目前PDF解析工具如雨后春笋一般蓬勃发展，前期主要发展的是Pipeline工具（MinerU、Marker等）、专用模型（Nougat、GOT-OCR等），后期通用视觉语言大模型（GPT4o、Gemini）和AI Agent（LandingAI）也开始在PDF解析上持续发力。

  

📚然而，目前已有的评测PDF解析工具能力的benchmark大部分集中在一些单模块的评测上（公式识别、表格识别、OCR），端到端的文档解析评测集较少（比如Fox，Nougat等），且覆盖的文档类型较少，页面数量也较少。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**现有的PDF解析能力Benchmark**

现有的PDF解析能力评测基准，主要分为单模块和端到端两类：

*   单模块的评测包括PubLayNet、TableBank、M6Doc等，这类Benchmark主要是评估单模块的识别能力，例如公式、表格、OCR、版面分析、阅读顺序等功能的检测和识别能力。
    
      
    
*   还有一种是端到端的评测，端到端评测主要是评估页面或者文件级别整体的识别能力，例如Fox、Nogout、GOT-OCR等。
    
      
    

目前已开源的端到端评测集较少，且存在一定的局限性：

*   较少的文档类型：目前大部分评测集包含的文档类型主要是学术文献，缺乏较为多样化的文档类型。
    
      
    
*   评测方法上的局限性：大部分评测还是采用MD2MD直接全文计算Edit Distance指标的方法，这种文本的指标计算，没有办法公平的评估公式及表格，还有阅读顺序的精度，并且这几个因素也会使得文本的精度评估受到影响。
    
      
    
*   缺乏更加细粒度的评测结果：大部分评测结果只是给一个总分，一个模型到底在哪个方面做得不好，哪个方面做得好，这个问题没有得到解答。
    

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yG3REZLBX4dXVQ4XkJxm4LPia11uAM4aeZtSChEmibascn0CQrPDA1K4fg/640?wx_fmt=jpeg&from=appmsg)

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

**OmniDocBench的优势**
-------------------

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yGyMnG7OhG5N3pfxK9TcvZHP1bqp5kYvictWtBU935yoMq2JB4HH6ADJA/640?wx_fmt=png&from=appmsg)

  

OmniDocBench涵盖9种文档类型，具有丰富的密集标注，并开发了配套的评测方法，使其既具备单模块的评测能力（包括布局检测，公式识别，表格识别，文本识别），又具备端到端的评测能力，能够从文本、表格、公式、阅读顺序这几大维度分别评估，具体来说体现在以下几个方面：

  

**数据多样性：**OmniDocBench从多个来源搜集了近20万个PDF，在这批数据中做了采样和聚类，筛选了6000张PDF页面，对这批数据做了页面级别的类别标签标注（包括PDF类型、布局、语种、页面特殊情况等），然后在这个标注基础上做了一个均衡采样，并且人工检查去除了敏感数据，最终筛选出了981张多样化的PDF页面，覆盖了9类文档来源的高质量标注数据，包括学术论文、教材等基础类型，以及手写笔记、密排报纸等高挑战性样本。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yGXDWb02HHEj7n3KdCL0icZpb5ia7tSBia9RibPhgeo4X9qGGqGM3O8Vx0ZA/640?wx_fmt=png&from=appmsg)

  

**标注的多样性：**OmniDocBench制定了严格的标注规则和流程，由高质量标注团队及专家质检员进行标注和质检，验证集涵盖了19种布局类别（包括了Block级别和Span级别的标注），以及15项属性标签（页面标签6项，文本属性3项，表格属性6项），还有block间的关系标签（比如表格和表格标题的归属关系、分栏截断的段落之间的连接关系），因此能够提供各个类别下的细粒度评测结果。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yGeOVZA69WhAPI3ahnFn30vvVyKEz76w7aqvZeQIVEqAfdicoicQTeJVlA/640?wx_fmt=png&from=appmsg)

  

**评测方法合理性：**OmniDocBench开发了一套基于文档组件拆分和匹配的评测方法，优化了匹配合并的算法，这一套评测方法能够针对不同的元素（比如公式、表格）使用更加合适的评测指标（CDM、TEDS），提供了分页面以及分属性的精细化评测结果，精准定位模型文档解析的痛点问题。

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

**PDF解析工具与OmniDocBench**
------------------------

OmniDocBench为文档内容提取提供了一套更加全面、精细的评估基准，旨在在提升各类智能文档处理工具在文档内容提取与解析等任务下的能力。我们使用OmniDocBench对目前主流的PDF解析工具展开评测，结果如下：

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yGunP5iaCRpibibT6DI21ad1YEMLcicxcsuc6UeGicR1ebEia5B5hYsYfZibZNQ/640?wx_fmt=png&from=appmsg)

  

**更多关于OmniDocBench评测集的使用方法和结果**

**欢迎访问以下地址：**

👇

仓库地址：

https://github.com/opendatalab/OmniDocBench

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

END  

  

**相关阅读：  
**

  

  

[MinerU 偷偷放大招！3大新功能上线、模型重磅升级，解析效率超级加倍……](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

2025-04-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUBlUJUFkG3acE1KjtVb7X1jUoqEZqSTu6b1NHzoPYiaicQjBaQ6NCG78GYurSgtzE1ITE3Q4WCux1Q/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[MinerU 教程第三弹：零基础使用 n8n 调用 MinerU MCP 搭建文档处理自动化系统](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550718&idx=1&sn=4fbf1dbec848be4af80cb8fbf5ebf4dd&scene=21#wechat_redirect)

2025-06-12

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXWsUJ0kaxZIBDPAJMTuh7nWke27IPxyhdsybajr2niaAZiaaJkZhwia9bQF2Zqmy5uqqicm6nxiafibvxw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550718&idx=1&sn=4fbf1dbec848be4af80cb8fbf5ebf4dd&scene=21#wechat_redirect)

[MinerU 知识库应用案例 | 小胰宝：搭建医疗AI助手，让专业信息检索更便利](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550080&idx=1&sn=a29d6d2ce665bb450b188a2e4ebf1e93&scene=21#wechat_redirect)

2025-03-11

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVVTKnCq5DTNRFwWbORU8Ec0tjKeNcLwUJxbZl6NnaiaUE4lBaCAibIgsLvZlDb8S2xPzkkloWdFvsA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550080&idx=1&sn=a29d6d2ce665bb450b188a2e4ebf1e93&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言