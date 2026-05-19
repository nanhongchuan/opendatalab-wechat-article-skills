     规范使用开源数据集，一定要看License \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

规范使用开源数据集，一定要看License
=====================

原创 专注于AI 数据的 OpenDataLab 2022-06-29 18:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/MpmHvCL2-F\_wdMenczyaDA](https://mp.weixin.qq.com/s/MpmHvCL2-F_wdMenczyaDA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD7DYzsibeib72U1ZfgFhMIWsXqvt2ILN8Lniarq1Wnf1GqU1BO5IDnZ2xJicSLchAmZWNkWM1aFyPXzkg/640?wx_fmt=gif)

  

为了共享科研成果，许多AI 研究员选择开源自己的项目和数据集。但开源不等于毫无限制，不代表使用者可以为所欲为。不正确的使用方式，会带来许多法律风险。  

  

本文介绍数据集 License 的基本知识，教你看懂和正确使用它们。

  

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png)

**IBM论文被曝抄袭开源项目**

这两天，接连2篇入选的论文被曝抄袭，让原本就备受关注的CVPR 2022 站到了风口浪尖。

  

一篇是来自韩国首尔大学 AI 研究团队的论文，入选了 CVPR Oral（口头报告），被曝出涉嫌抄袭10篇论文，甚至出现原句照抄的内容。

  

另外，IBM 一篇入选的论文也被举报涉嫌抄袭，来自平安科技的研究员向CVPR 2022 program chairs 举证，指出 IBM 的 TableFormer 从方法论、预处理、后期处理、文字行检测与识别等9个方面抄袭了自己团队2021年的开源项目 TableMASTER。爆料者表示，很多痕迹都可以看出，IBM 基于他们开源的预训练模型训练，只是改了一些细节。\[1\]\[2\]

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7VHe6fck36kJEsapsoCXZkiaVJpwZLTiczJTiaDGW6HkbA79Mf9PdRclQvPSsNOPT0RmdMkg2AM8mew/640?wx_fmt=png)

IBM 相关 TableFormer论文被指抄袭（图源：参考资料\[7\]）

  

这引发了国内外 AI 研究员的热烈讨论。有网友调侃，抄袭的论文都能拿Oral，而认认真真做实验的论文却因为各种理由被拒，得好好研究一下这是如何做到的。

  

其背后透露出的是科研人的苦楚、对论文审查结果的不满，还有对开源项目不规范使用的担忧。

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvA07ENaR6ibO8U9JpC13Ckb5QS4Jtx80dfzfibCnZESwOWZp1h7ia982Nw/640?wx_fmt=png)

**数据集开放协议****介绍**

在倡导开源共享的今天，开源不仅仅是一种热爱分享的极客精神，而是已经成为一种分布式可信的开发模式。许可协议（License）则是规范知识产权保护与作品使用权限的有力载体。

  

不管是算法、模型、数据集，从创造之初就和其他创意作品一样默认享有著作权。许可协议则是基于著作权法，为了实现作品的自由分发以及自由修改，而提出的一系列标准化的公共许可合同，便于作品拥有人授权给其他人使用。

  

软件与其他类型的创意作品有较大不同，常用“开源协议”来规范开源软件的使用。比如，常见的Apache v2、BSD、MIT、GPL、LGPL等，有的数据集也会采用这类开源协议，经常接触开源项目的朋友比较熟悉，就不做过多展开。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7S2eJBYbNbTOIo3ZQiaSEmW5G6icnRXr9lEWIibrY0PpImpav0J5pDe8OTbGibk1lnk3tgJgWNQz1pJg/640?wx_fmt=png)

代码托管平台的开源协议示意（图源：Github）

  

而常用的数据集许可协议有3种来源：

● 知识共享 (CC)

● 开放数据共享 (ODC)

● 社区数据许可协议 (CDLA)

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvXS8PPBkwZE6mNz2Q5ib40MYJNaPayjz34c0wHtFExtzkIOcTmQp8KSQ/640?wx_fmt=png)

**知识共享许可协议**

知识共享这一非营利性组织于2001年成立。知识共享组织提供了6种非独占的、不可撤销的标准化著作权许可协议，每个许可协议都有自己的使用条款，便于作品的作者放弃自己的部分著作权，从而有助于作品的共享。\[3\]

  

知识共享许可协议（Creative Commons license），即CC许可协议，是目前全球最受欢迎的数据集许可证，主要涉及4项权利，署名（BY）权，继承（SA）权，非盈利（NC）权，禁止演绎（ND）权。

  

（需要注意的是，CC许可协议是著作权许可协议，因此只涉及著作权及相关的邻接权，而不涉及专利、商标等其他知识产权，也不涉及肖像权、隐私权、形象权等其他权利。\[4\]）

  

**1\. 六种CC许可协议**

**● CC BY**

**（****Attribution 署名）**

保留原作者姓名，允许基于商业目的传播、改编或者二次创作。  

  

**● CC BY-SA** 

**(Attribution-ShareAlike 署名-相同方式共享)‍** 

保留原作者姓名，并且新作品也使用相同的许可协议，才能对原作进行基于商业目的的改编和二次创作。  

  

**●** **CC BY-ND** 

**(Attribution-NoDerivs 署名-禁止演绎)‍** 

保留原作者姓名，允许商用，但是不能改编原作与他人分享。

  

**●** **CC BY-NC**

**（Attribution-Noncommercial 署名-非商业性）**

保留原作者姓名，允许非商业目的重新编排、改编或者再创作，但是不能商用。基于原作的演绎作品无需使用相同的许可协议。

  

**●** **CC BY-NC-SA** 

**(Attribution-NonCommercial-ShareAlike 署名-非商业性使用-相同方式共享)** 

需保留原作者姓名，并在基于原作创作的新作品适用同类型的许可协议，即可基于非商业目的对原作重新编排、改编或者再创作。

  

**● CC BY-NC-ND**

**(Attribution-****NonCommercial-NoDerivs 署名-非商业使用-禁止演绎)** 

这是六种主要许可协议中限制最为严格的，保留原作者姓名，允许下载和分享，但是不能对原作进行任何形式的修改和商用。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7S2eJBYbNbTOIo3ZQiaSEmWE85Wu84Sveicoj3O7PvHFmVoqmLNI607D88rvbukgjFb8ePPNOsG5ng/640?wx_fmt=png)

CC许可协议示意（图源：参考资料\[5\]）  

  

**2\. 公共领域许可协议**

**● CC0**

知识共享组织于2009年发布了一种放弃著作权的便捷方式，即CC0。严格来讲CC0并非双方的许可合同，而是一种单方的声明。选择CC0作为许可协议，则说明作者将数据集捐赠给公众使用，此数据集完全公有，使用时无需署名，也无其他限制。

  

  

  

‍‍‍‍‍![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvc28Cv4ibH4X6RglOEbl7oFEM2UYZiaufmILLCAH3MwDjnPicPwqjnr9Pg/640?wx_fmt=png)

********开放数据共享****许可证************  

开放数据共享 (ODC) 为开放数据提供合法工具。他们提供三种许可类型，每种都有自己的使用条款！
================================================

  

**● ODC-PDDL**

这是开放数据共享公共领域专用许可证，版权所有者永久删除所有版权，不保留任何权利。这对应于CC0 许可协议。

  

**● ODC-BY**

这是开放数据共享署名许可。你可以自由分享和改编，但需要注明出处，允许商业用途。这对应于CC BY（署名）许可。  

  

**● ODC-ODbL**

这是开放数据共享开放数据库许可证。你可以自由分享和改编，并在基于原作创作的新作品适用同类型的许可协议。允许商业用途。这对应于CC BY-SA (署名-相同方式共享)许可协议。

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlv9P8ZCtKWJtP379LbKF8mlhw1CPKuyKOSVa6ztadfIfRjFFvTiaia91BQ/640?wx_fmt=png)

********社区数据许可协议********

2017年，Linux 基金会提出了社区数据许可协议 (CDLA) 为社区提供了开放的数据共享选项。他们提供两种许可类型，每种都有自己的使用条款。\[5\]
==============================================================================

  

===

**● CDLA-Permissive-2.0**
=========================

这是社区数据许可协议的第二个版本。对开放数据的贡献者和使用者不作要求。你可以使用、修改和共享，许可协议不对结果的使用、修改或共享施加任何限制或义务。
==========================================================================

  

===

**● CDLA-Sharing-1.0**
======================

这属于copyleft（强制共享）许可类别，你可以使用、修改和共享，但无论是否修改，基于原作创作的新作品必须与原始版本有相同的许可协议。
====================================================================

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7S2eJBYbNbTOIo3ZQiaSEmWZKrYkfuicJaCAe8f058dWLlGs2JgWL0L0Vm94jGP53ZS2Gq6Q2iaj2BQ/640?wx_fmt=png)

社区数据许可协议 (CDLA)官网（图源：参考资料\[6\]）
===============================

  

  

以上就是常见的数据集的许可协议类型，也即是我们常说的数据集License 的含义。你学会解读了吗？

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5ObGqmYR1ibg6mKt4icpIzlvicHXaibBqlsWve4HconrGGRFwKHTtVJebYqS8ConcN6UPgA4XqUrGeQg/640?wx_fmt=png)

********License结构化描述与审核********

在OpenDataHub，我们贴心地帮大家整理好了各个数据集的License信息，并且从Permission, Limitations, Condition三个方面进行结构化梳理，使之更加完善，方便大家自主查询。

  

同时，平台也建立了严格的安全审核机制，核实了每个数据集的分发依据，确保每个可获得的数据集都是符合授权的，使大家能够快速、便捷、安全无忧地使用。

  

还等什么，快来试试吧。

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD7S2eJBYbNbTOIo3ZQiaSEmWaz4u916JBCKVcHxGSq28ENiaoWN5icuRyFYyAQWf7ibPyG3cBkZ6foQbQ/640?wx_fmt=gif)

OpenDataHub数据集License示意 
========================

（图源：https://opendatalab.com/）
=============================

  

  

  

**参考资料**  

\[1\]https://zhuanlan.zhihu.com/p/115911178

\[2\]https://www.youtube.com/watch?v=UCmkpLduptU

\[3\]https://wiki.creativecommons.org/wiki/Considerations\_for\_licensors\_and\_licensees#Make\_sure\_the\_material\_is\_appropriate\_for\_CC\_licensing.

\[4\]https://www.reddit.com/r/MachineLearning/comments/vlpnuw/d\_ibm\_zurich\_research\_plagiarised\_our\_paper\_and/

\[5\]https://creativecommons.org/

\[6\]https://cdla.dev/sharing-1-0/

\[7\]https://www.reddit.com/r/MachineLearning/comments/vlpnuw/d\_ibm\_zurich\_research\_plagiarised\_our\_paper\_and/  

  

  

  

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