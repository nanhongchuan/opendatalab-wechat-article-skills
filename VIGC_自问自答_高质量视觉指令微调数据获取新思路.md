     VIGC：自问自答，高质量视觉指令微调数据获取新思路 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

VIGC：自问自答，高质量视觉指令微调数据获取新思路
==========================

原创 热爱学习的 OpenDataLab 2023-09-13 18:10 上海

> 原文地址: [https://mp.weixin.qq.com/s/noBZO-LKQGRiZzH\_NKSzgw](https://mp.weixin.qq.com/s/noBZO-LKQGRiZzH_NKSzgw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

  

从今年四月份开始，随着MiniGPT-4, LLaVA, InstructBLIP等多模态大模型项目的开源，大模型的火从NLP领域烧到了计算机视觉及多模态领域。

  

多模态大模型需要高质量的图文对话数据进行指令微调，而当前多模态指令微调数据多基于纯文本GPT-4构建，其数据质量及多样性相对受限。为此，我们提出了**视觉指令生成及修正模型VIGC**，可以基于多模态模型自动生成多样性的指令数据，并基于指令修正模块减少幻觉，保证数据质量。这些指令数据加入模型微调，可以进一步提升模型性能。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5mzQ5ba0aNPRcEAZTIUJ9Q1eYVVpy0ZFKgX68ZywymiaImywfP1b6ohW0ouqTBE7KFOp0vX4Ihk9A/640?wx_fmt=png)

  

VIGC能做什么？

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5mzQ5ba0aNPRcEAZTIUJ9Q82bsvf140ruSaAXGIm3kLdJNE00LmcyySNS4p28m5vRxBTm5TPo0xA/640?wx_fmt=png)  

图1. VIGC示例：输入图像，模型自动生成相关问题及对应答案

  

如图所示，用户提供（1）任意图像；（2）所需数据类型，VIGC可以生成该图像对应的问题和答案。相比于当前图文多模态大模型给定图像和问题，获取对应问题的答案，VIGC可以实现自问自答，而这些问答对本身可以作为高质量的指令微调数据，用于多模态大模型的训练，进一步提升模型性能。

  

VIGC有什么优势？

要回答这个问题，我们首先看一下当前指令微调数据的获取方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD5mzQ5ba0aNPRcEAZTIUJ9QhtmxAu2rYmxaGLp5Z8luBSsoUrzPJ7JhQicAa7gcz5iaPico88RYUicaxQ/640?wx_fmt=jpeg)

图2：纯文本GPT-4用于指令微调数据生成

  

当前获取图文指令微调数据多基于Language-only GPT-4，结合提供的图像、图像相关标注及人工标注问题，由GPT-4来生成对应的答案。这种方式存在两个缺陷：

  

**● 标注成本高：**由于GPT-4无法看到真实图像，需要人工标注对应的图像信息（如图像中的目标类别，定位信息，描述信息）基于跟图像相关的问题。

**● 答案质量受限于标注：**一张图像中包含的信息量远远大于标注信息，所以GPT-4在回答问题时，直接依赖于受限的标注信息，容易丢失图像中的细节信息。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5mzQ5ba0aNPRcEAZTIUJ9QDiayc0bNCErWL6UXy9zvhicBTIoyYST89lDs40VhYiaEHcaTveK14M1yw/640?wx_fmt=png)

  

相比之下，VIGC通过初始的指令微调数据训练模型，引导模型基于图像自动生成合适的问题及回答。这种方式相比于纯文本GPT-4生成指令微调数据的优势在于：

  

**● 包含更多细节内容：**VIGC生成的答案是模型真正看到图像内容进行回答，包含了更多的细节信息；

**● 无需额外表述：**VIGC能够针对没见过的图像内容依然生成高质量的问答数据，得益于VIGC模型能够通过视觉模型提取到图像的视觉信息，并依赖于后续的语言模型自动生成答案。**这里的关键点在于：视觉模型和大语言模型本身就看过海量的图文、纯文本数据，本身集成了大量的知识，VIGC更像是从这些大模型中蒸馏出跟图像相关的知识。**

  

  

如何训练和使用VIGC？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5mzQ5ba0aNPRcEAZTIUJ9Q625HNTofFXsTD16PNIg5mKn8EMJibhcWnMaMxDlDAs0TRABibVLgSgrA/640?wx_fmt=png)

图3. VIGC框架图。左侧对应VIGC训练流程，右侧对应VIGC推理流程。

###   

01

**训练流程**

为了获取给定图像，自动生成图文的内容，需构造初始的指令微调数据，包含图像、问题类型，对应图像相关的问题及正确答案。视觉指令生成VIG训练阶段的

  

**● 输入信息：**图像及对应的问题类型（如对话类型、详细描述类型、逻辑推理类型）

**● 输出信息：**该类型的问题和答案。

  

然而仅利用上述的方式，模型在输出详细描述类信息时，经常会出现严重的幻觉问题，这一现象在当前主流多模态大模型中普遍存在，本质上**是当训练数据存在某些重复的模式时，生成模型很容易过拟合到这种数据分布**。例如在训练图像中，问答对中出现人和桌子的描述时，后续经常会出现椅子的描述。推理阶段，模型会倾向于看到人和桌子，就提及椅子（即便推理图像中没有椅子）。

  

为此，**VIGC通过使用迭代Q-Former的方式及时更新输入到模型的特征信息，让模型在回答问题时结合问题本文关注的内容以及当前已有部分回答，完成后续的回答**。所以在训练阶段，我们同时加入视觉指令修正模块VIC，该阶段的：

  

**● 输入信息：**图像、对应问题类型、问题

**● 输出信息：**答案

  

02

**推理阶段**

为了获取高质量的指令微调数据，推理阶段的流程如下：

**a.** 给定图像及问题类型，VIG生成对应问题和答案；

**b.** 将图像及VIG生成问题输入VIC，经Q-Former提取问题相关的图像特征后生成新的答案  ；

**c.** 将上述答案拆分，将第一句回答和图像、问题再次输入VIC，生成更新后的第二句答案 A2；

**d.** 整个过程迭代执行，直到模型遇到结束符。

  

VIGC数据对模型帮助？

基于VIGC生成的数据，重新加入模型训练后，我们发现模型的性能可以进一步提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5mzQ5ba0aNPRcEAZTIUJ9Q3upXgNMhbOcJ6tootp00QicFdoIb5BhwM6LRhxAgrwsCe1WT9ic53Sww/640?wx_fmt=png)

表1. 加入VIGC数据模型性能提升

  

如上表所示，在基于MMBench的评测上，加入VIGC生成的额外数据，**指标可以从24.4%提升至27.5%。在LLaVA评测集上，指标从84.7%提升到87%**。

  

总结

**VIGC提出了一种新的多模态指令数据构造方式，**可以基于无标注的图像自动生成多样性的高质量数据，且基于生成数据可以进一步提升当前模型的性能，可以作为指令数据获取及模型性能提升的新思路。

  

****VIGC相关资料****

**论文地址：**

__https://arxiv.org/pdf/2308.12714.pdf__

**代码：**

__https://github.com/opendatalab/VIGC__

  

**Demo：**

__https://opendatalab.github.io/VIGC__

  

\-END-

VIGC项目已开源，欢迎star!

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD5mzQ5ba0aNPRcEAZTIUJ9QGVtXP2pGJKtaOPmkibfn49jfrmF1abOKn769Uz3zY98LacBPXmxUuhQ/640?wx_fmt=png)

更多精彩内容，请访问 OpenDataLab：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7vkz4XTP9dNyQZNeGmJjySBjg4HBylYbHw7reqRwJDNDic5LwnqpS1dNXGcb5Ws3o99JcocU9oFOg/640?wx_fmt=png)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言