     多模态抢鲜看！OmniMedVQA：大规模医学VQA评测数据集 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

多模态抢鲜看！OmniMedVQA：大规模医学VQA评测数据集
===============================

原创 OpenGVLab OpenDataLab 2024-05-07 18:40 上海

> 原文地址: [https://mp.weixin.qq.com/s/1na1XGxIPMA3n73mEz5uFA](https://mp.weixin.qq.com/s/1na1XGxIPMA3n73mEz5uFA)

在过去的两年里，计算机视觉领域涌现出了多种不同的多模态大模型（LVLM），如BLIP2, MiniGPT4等。这些大模型在多种不同的视觉任务上取得了亮眼的效果。为了准确评估多模态大模型的能力，许多研究人员从不同角度对模型进行了评测\[1，2\]。结果显示，LVLM在各种多模态任务中展示了卓越的能力。但是，这些评测工作大多只关注LVLM在通用视觉任务中的效果，它们在医学领域的潜力尚未被充分探索。这些多模态大模型能否较好地解决医学领域的问题，如何准确评估多模态大模型在医学领域的能力，仍然是一个未知的问题。  

  

要准确评估多模态大模型在医学领域的效果，就需要构建全面的、涉及多种不同模态、覆盖人体多种不同位置的医学评测数据集。同时，对于多模态大模型而言，视觉问答能力（VQA）是其最基础且关键的能力之一。因此，要想准确评测医学大模型的能力，就需要一个全面的医学VQA数据集做支撑。但是，如图1所示。由于高质量医学数据的稀缺性，现有的医学VQA数据集不论是规模还是全面性都有所欠缺。因此，为了准确评估多模态大模型在医学领域的能力，构建一个大规模、全面的医学评测数据集十分重要。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzlsfib7NpYdztUwEIXfYvgCjqOZT3sxicHqXrFnzln6ia4C6tFNdoTkiaQmHWAbyzNloYRD1ARVJh4lDw/640?wx_fmt=png)

图 1 不同医学VQA数据集比较

  

**论文地址：**

__https://arxiv.org/pdf/2402.09181__  

  

**Github：**

__https://github.com/OpenGVLab/Multi-Modality-Arena__  

  

**下载地址：（点击阅读原文直达）**

_https://opendatalab.com/GMAI/OmniMedVQA_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****数据集构建****

由于高质量医学数据的稀缺性，加之普通标注员很难处理医学数据，因此，构建高质量的医学VQA数据集是一个十分有挑战性的任务。为了解决这个问题，我们从医学分类数据集入手，基于数据集中的类别属性和其他延伸知识，构建VQA问题。

  

比如，对于一个肺结核患者拍摄的胸腔X-Ray影像。我们可以设计如下QA模版对：

Q：该图像是通过什么模态采集得到的  A：X-Ray

Q：该图像显示了什么部位的信息  A：胸部

Q：该图像呈现出何种疾病  A：肺结核

  

根据上述思路，我们以**73**个不同分类数据集为基础，拓展出了多种QA模版。我们基于这些QA对进行采样，得到了**12,7995**个不同的VQA条目。为了拓展OmniMedVQA数据集的多样性，我们通过GPT-4对QA模版进行复写。同时，为了便于评测，我们让GPT-4为每个条目配置错误答案，将其构造成选择题的形式。通过这种方式，在确保语义不变的前提下，使不同VQA条目的问答形式更多样。最终，我们的OmniMedVQA数据集包含**118,010**种不同图片，拥有**12**种不同模态，涉及超过**20**个人体不同的器官、部位。

  

数据集概览如图2所示。图2右侧展示了OmniMedVQA的五种问题类型。图3反映了数据集包含的不同模态的影像和涉及的相关器官。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzlsfib7NpYdztUwEIXfYvgCjjaPMlqLhxQMQMiaURs9ibLAbxQUvCNIV6UR2MmsexFNTY6AfqwXfgiamA/640?wx_fmt=jpeg&from=appmsg)

图 2 OmniMedVQA数据集概览

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzlsfib7NpYdztUwEIXfYvgCjMOXsL25dkE9FrUUUn3MqTVSdBnfq1tBnAqDUzn4k7jpd8FTZEd7Jdw/640?wx_fmt=jpeg&from=appmsg)图 3 OmniMedVQA涉及的模态和器官

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****评测方法****

为了准确评测多模态大模型在医学领域的能力，我们设计了两种评测指标：**Question-answering score**和**Prefix-based score**。它们各自的流程如图4所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzlsfib7NpYdztUwEIXfYvgCjjic2iaAHicHHyicPCjZ6KSib6odia0CDic8dPC7XFGK4RWwPUUEfbjBwM9Nkw/640?wx_fmt=jpeg&from=appmsg)

图4 Question-answering score和Prefix-based score评测流程示意图

  

**Question-answering score**以选择题的形式进行评测。我们将问题和选项作为文本输入，让多模态大模型结合图像进行回答，进而根据模型的输出结果判断是否回答正确。

  

**Prefix-based score**则更关注模型内在的知识。具体来说，在多项选择问答任务中，给定输入图像和文本句子，我们首先分别提取视觉特征和question的文本特征。然后，将视觉特征与文本特征一起输入大语言模型，计算大语言模型输出各选项的可能性得分。这个得分被视为该图像-文本对的Prefix-based score，反映了模型生成相应文本内容的概率。对于每个测试条目中的所有选项，我们都通过此方式计算Prefix-based score。得分最高的选项意味着它是这个问题最可能的答案，我们将该选项与真实答案进行比较判断模型回答是否正确。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****实验****

我们利用OmniMedVQA数据集，测试了8个通用多模态大模型：BILP2, MiniGPT-4, InstructBLIP, mPLUGOwl, Otter, LLaVA, LLama adapter v2, 和VPGTrans。以及四个医学多模态模型：Med-Flamingo, RadFM, MedVInT 和 LLaVA-Med。实验结果如图5和图6所示，它们分别按5种不同任务类型和12种不同模态体现了各模型的评测结果。表格中“/”左侧和右侧的数值分别是Question-answering Score 和Prefix-based Score。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzlsfib7NpYdztUwEIXfYvgCjU4GqjVkJpHrKzXbDA1yXQK82skyLFQpLqjPpFTJqgWbKmdNtKQaV0g/640?wx_fmt=jpeg&from=appmsg)

图 5按照5种不同问题类型分别计算的评测结果

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzlsfib7NpYdztUwEIXfYvgCjUTrTDFrDriadpMuOvpliaouFomTb26cot1Uh1UxTszaiadYfbZARQibiaFQ/640?wx_fmt=jpeg&from=appmsg)图 6按照12种不同模态分别计算的评测结果  

  

### **从实验结果我们可以得到如下结论：**

● 让我们非常惊讶的是，在所有LVLM中，BLIP-2和InstructBLIP取得了最好的表现，远远超过许多医学LVLM。这说明现有医学LVLM并没有得到充分的训练，它们的表现还有很大的进步空间。

  

● 医学领域迫切需要一个强大的模型来对齐图像-文本对，从而产生更多高质量数据用于训练LVLM。BLIP在通用数据集和我们的OmniMedQA中都展现出了较好的表现，因为它是使用各种视觉领域的大量高质量图像-文本对进行训练的。因此，开发通用医学LVLM的关键在于使用来自不同医学领域的大量高质量“图像-文本”数据对模型进行训练。由于医学数据的稀缺性和标注难度，如果有一个强大的图像-文本对齐模型，可以更好地由医学影像生成文本描述，为医学领域带来更多高质量数据。

  

● MedVInT和Med-Flamingo在所有医学LVLM中取得了最优的表现，并且还超过了除BLIP2和InstructBLIP之外的许多通用LVLM。这种成功可能是因为他们在训练中接受了大量专门的医学知识。Med-Flamingo学习了超过4000本医学教科书，而MedVInT基于381K图像-标题对生成的QA数据进行训练。这表明，为了获得更好的性能，应该向LVLM注入更多的医学领域知识。

  

● 从图6中我们可以发现，对于CT、MRI这种分布和自然图像有明显区别的影像，医学LVLM展现出了更好的表现。这是因为医学LVLM在训练中接触过更多CT、MRI数据，这些数据和自然图像有明显不同。因此，医学LVLM在这些数据上展现出了更好的表现。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

****结论****

医疗是关系国计民生的大事，建立鲁棒的医学多模态大模型可以大大促进医疗人工智能的水平，带来重要的社会价值。但是，由于医疗安全的重要性，在现实医疗场景应用多模态大模型前，需要谨慎测评各模型的能力，确保鲁棒性和安全性。

  

为此，我们建立了**OmniMedVQA**数据集，并对现有主流多模态大模型进行了全面评测。评测结果显示，**现有主流多模态大模型面对很多医学问题仍然无法很好结果**。同时，**医学大模型的效果并没有明显优于通用大模型**。为了训练更为鲁棒的医学LVLM，需要一个**强大的图像-文本对齐模型**提供更多高质量医学数据。同时，由于不同医学影像模态间的多样性和不同器官间的差异性，现阶段想直接建立一个通用的医学LVLM十分不易。因此，我们认为可以尝试**从某一个器官的部分模态入手，建立一个针对某个科室或某几种疾病的专门化的医学LVLM**。我们希望该数据集可以为未来医学多模态大模型的发展提供评测基准。

  

**论文地址：**

__https://arxiv.org/pdf/2402.09181__  

  

**Github：**

__https://github.com/OpenGVLab/Multi-Modality-Arena__  

  

**下载地址：（点击阅读原文直达）**

_https://opendatalab.com/GMAI/OmniMedVQA_

  

  

**参考文献**

\[1\] Wenqi Shao, Yutao Hu, Peng Gao, Meng Lei, Kaipeng Zhang, Fanqing Meng, Peng Xu, Siyuan Huang, Hongsheng Li, Yu Qiao, et al. Tiny lvlm-ehub: Early multimodal experiments with bard. arXiv preprint arXiv:2308.03729, 2023.

\[2\] Peng Xu, Wenqi Shao, Kaipeng Zhang, Peng Gao, Shuo Liu, Meng Lei, Fanqing Meng, Siyuan Huang, Yu Qiao, and Ping Luo. Lvlm-ehub: A comprehensive evaluation benchmark for large vision-language models. arXiv preprint arXiv:2306.09265, 2023.

  

* * *

  

更多大模型评测数据集，请访问OpenDataLab官网

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言