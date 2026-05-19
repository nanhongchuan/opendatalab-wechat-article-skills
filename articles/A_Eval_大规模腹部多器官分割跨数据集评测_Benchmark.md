     A-Eval：大规模腹部多器官分割跨数据集评测 Benchmark \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

A-Eval：大规模腹部多器官分割跨数据集评测 Benchmark
=================================

原创 通用医疗GMAI OpenDataLab 2023-11-14 19:52 上海

> 原文地址: [https://mp.weixin.qq.com/s/L\_qcyzKH5Uge0vJX-ZtbBA](https://mp.weixin.qq.com/s/L_qcyzKH5Uge0vJX-ZtbBA)

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**数据是深度学习模型构建的基石**。在医疗领域，过去由于数据的缺乏，模型往往只能在小规模的特定任务的数据集上训练和验证，这类模型往往很难泛化到其它的数据集上。**而近年来，越来越多的大规模医学图像数据集被构建出来，极大地推动了深度学习模型在医疗领域的发展**。尤其是在腹部多器官分割领域，既有 WORD，FLARE22，AMOS 等专注于腹部多器官分割的大规模数据集，又有 TotalSegmentator 这样覆盖了腹部器官的全身结构分割数据集。在这些数据集上训练出来的模型在自身的验证集和测试集上，都展现了非常优秀的性能。**但是，这些模型是否可以很好地泛化到其它数据集上以及如何进一步提高模型的泛化性却依然是未知的。**

  

**为回答这个问题，GMAI 团队构建了一个大规模的跨数据集腹部多器官分割 Benchmark——A-Eval，并尝试从数据中心和模型规模两个视角来揭示影响模型泛化性的关键因素和最佳实践。**

**![](https://mmbiz.qpic.cn/mmbiz_png/mhIicicHPJQWGPb3pGFN7tEicJrooGnsicYbLNjdDWQro270L7atb4iaNRyFIBBbuYB532RPJK1qfd15EoruknlTekg/640?wx_fmt=png)**

  

**论文:** 

_https://arxiv.org/abs/2309.03906_

**开源代码:**

_https://github.com/uni-medical/A-Eval_

  

![](https://mmbiz.qpic.cn/mmbiz_png/mhIicicHPJQWGPb3pGFN7tEicJrooGnsicYbjKGwwTGMqymAXibyH67icYpcUS3LRTjSxaEU6OsRMuwSvdpicLMWKWeQA/640?wx_fmt=png)

图1：对比传统的评测和 A-Eval benchmark。(a)传统的评测在相同的数据集上划分训练集和测试集来评估模型性能。(b)A-Eval 在不同的数据集上进行训练和测试，提供更全面的模型性能验证以及模型泛化性的评估。

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

******Benchmark的构建******

A-Eval 的构建基于 5 个公开的腹部多器官分割数据(FLARE22, AMOS22, WORD, TotalSegmentator)，其中 4 个大规模数据集的训练集被用来训练模型，这 4 个数据集的验证集以及 BTCV 的训练集一共 5 个数据集被用来测试。由于不同的数据集所涵盖的类别有所不同，为了保证测评的一致性，我们选择了 5 个数据集共有的 8 类腹部器官进行评测。

![](https://mmbiz.qpic.cn/mmbiz_png/mhIicicHPJQWGPb3pGFN7tEicJrooGnsicYbBEB4OnIpcI2zrtdYegDNREiafGJojpkJSU13qHbdO5Gvqiak3icUM4Dkg/640?wx_fmt=png)

图2：A-Eval 使用的数据集介绍，其中使用到了 4 个数据集(FLARE22, AMOS, WORD, TotalSeg)的官方训练集进行训练，使用 4 个数据集的官方验证集以及 BTCV 的官方训练集进行测试。

![](https://mmbiz.qpic.cn/mmbiz_png/mhIicicHPJQWGPb3pGFN7tEicJrooGnsicYbu3YJKwxGxzcTrsvyiaibaFbaXD5RyFTbFHKG5bMa2Tib4RngYclInlxOg/640?wx_fmt=png)

图3：A-Eval 所使用的 5 个数据集包含的类别展示，A-Eval 选择了 5 个数据集都包含的 8 类腹部器官进行测评。（点击查看大图）

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**实验结果**

我们对比了在四个大规模数据集上单独训练模型和在四个数据集上联合训练模型的结果，进行单独训练模型时，我们进一步考虑了以下情况：仅使用FLARE22 数据集的有标注数据和同时使用标注数据和伪标注数据两种情况；仅使用AMOS 的 CT 数据，仅使用 MR 数据和同时使用 CT 和 MR 数据训练三种情况。模型统一使用 STU-Net-L，评测指标使用 DSC 和 NSD。数值结果和可视化结果如下：  

![](https://mmbiz.qpic.cn/mmbiz_png/mhIicicHPJQWGPb3pGFN7tEicJrooGnsicYbWklic37SBlfJEQsTlx0PibiaYYhmLpyrlgvlPLLrDd6uIHqKJkLBicQazw/640?wx_fmt=png)

  

图4：在 A-Eval 上，各种不同的训练数据下，模型的跨数据集泛化性数值结果对比。（点击查看大图）

  

![](https://mmbiz.qpic.cn/mmbiz_png/mhIicicHPJQWGPb3pGFN7tEicJrooGnsicYbeiayUIbdHXzZX6E8fUia4AwAiaC7oJaTrD7qqx18WW5rgfw6P4Prncapw/640?wx_fmt=png)

图5：不同的训练数据集上，跨数据集泛化效果的可视化对比。

  

  

**可以发现以下结论：**

  

1\. 在同一数据集上训练的模型，在该数据集的测试数据上，效果要好于其它数据集上训练的模型，从可视化图中可看到。

2\. 仅对比在有标注的 CT 数据上训练的模型时，它们的跨数据集泛化性有如下规律：FLARE22(50)<WORD(100)<AMOS（200）<TotalSegmentator(1082)。这符合随着数据规模越大，泛化性越好的规律。

3\. 大量伪标签数据的使用，相比仅使用少量的有标注数据，能大幅提高模型的泛化性。

4\. 结合多模态数据训练(CT, MR)，比单一模态训练的模型，具有更好的泛化性。

5\. 联合所有数据集训练的模型，具有最强的泛化性。

**另外我们对比了模型大小对模型泛化性的影响，使用了 4 种不同大小的 STU-Net 模型：**![](https://mmbiz.qpic.cn/mmbiz_png/mhIicicHPJQWGPb3pGFN7tEicJrooGnsicYbNpAAwORHB5cF8rAacwH5UOjicCicWiaVGjQbIbpLrtfVW6SxLjlUAEHzQ/640?wx_fmt=png)

图6：不同大小模型的跨数据集泛化性对比。

  

**可以看到，增加模型大小可以在一定程度上提高模型的泛化性**。但是对于腹部多器官分割任务而言，过大的模型尺寸可能会造成过拟合，反而会降低模型的泛化性。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**总结**

**本文介绍了 A-Eval，一个用于评测腹部多器官分割模型的跨数据集泛化能力的大规模 Benchmark**。基于 A-Eval， 我们以数据为中心，评测了模型在各种不同的训练数据上训练所表现出的跨数据集泛化性，发现使用较大的训练数据集、通过伪标签整合未标记数据、采用多模态学习和跨多个数据集的联合训练都可以显著提高模型的跨数据集泛化能力。**此外，我们的实验结果表明，适当增加模型的大小可以带来更好的性能，从而凸显了大型模型在提高泛化能力方面的潜力。**

来源 | 通用医疗GMAI  

\-END-

**寻星计划火热进行中**

**开源数据集领好礼**

**戳下方了解**  

👇

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6OTUAUZZos5lC2WkZxnic2Ht7tZib7huCibtp3EcJgM7VxxaZJhicXqI7meVrGKwnkuK88xQEnMZko3w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247524116&idx=1&sn=51ac0acca9f8e5834ab24ecff0f0c25c&chksm=c10c0df6f67b84e000840d9b0208b6d379a18bece0c193748b6a3fa6be61355666a59e3aa5bb&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言