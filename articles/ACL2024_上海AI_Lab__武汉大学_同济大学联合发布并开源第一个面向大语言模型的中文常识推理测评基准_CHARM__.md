     ACL2024|上海AI Lab, 武汉大学，同济大学联合发布并开源第一个面向大语言模型的中文常识推理测评基准 CHARM ! \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

ACL2024|上海AI Lab, 武汉大学，同济大学联合发布并开源第一个面向大语言模型的中文常识推理测评基准 CHARM !
===============================================================

原创 热爱学习的 OpenDataLab 2024-06-14 19:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/LoMiN\_jD8AXUXMMMwmjOqQ](https://mp.weixin.qq.com/s/LoMiN_jD8AXUXMMMwmjOqQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

  

上海人工智能实验室OpenDataLab, 武汉大学，同济大学合作推出了**第一个中文常识推理测评基****准：CHARM**。该工作已经被 “**第62届国际计算语言学年会 ACL 2024 主会录用**”！快来看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD58iaT1btuUFtsGmkkBq8NwV4TLvdcaEFsCXBGqnOIYyq1O5ukjmeHur2WbMVEM22mMxJNaCqb2Fhg/640?wx_fmt=png&from=appmsg)

  

**论文地址：**

__https://arxiv.org/abs/2403.14112__

  

**Github：**

__https://github.com/opendatalab/CHARM__

  

**排行榜：**

__https://opendatalab.github.io/CHARM/leaderboard.html__

**项目主页：**

____https://opendatalab.github.io/CHARM/findings.html____

  

**下载地址：**

_https://opendatalab.com/OpenDataLab/CHARM_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW9eTjLLqxpUfLut1vCOtNPKxx6ZgZVJcmluhHPquATmEaQI013ibncfnA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**研究概述**

**CHARM 是首个对大型语言模型 (LLMs) 的中文常识推理能力进行全面且深入评估的测试基**，并且涵盖了世界各地广为人知的常识和独具中国特色的常识。我们在此基准上，对7种英文和12种以中文为主的LLMs进行了评估，同时采用了五种具代表性的提示策略（如CoT），来提升LLMs的推理能力。

  

我们发现，LLMs的**语言取向**和**任务领域**均会影响**提示策略的有效性**，这进一步丰富了之前的研究结果。我们构建了紧密关联的**推理和记忆****任务**，在此过程中发现，部分LLMs在**记忆中文常识**方面存在困难，这直接影响了他们的**推理能力**。然而，还有一些LLMs在记忆表现相似的情况下，他们的推理能力却存在差异。进一步地，我们评估了LLMs**独立于记忆的推理能力**，并针对典型错误进行了分析。

  

我们的研究精确地突显了LLMs的优势和弱点，从而为其优化提供了明确的方向。此外，这项研究也可为其他领域的相关研究提供参考。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD58iaT1btuUFtsGmkkBq8NwV8fdHibWOt7Mibc7jjSicFLMfaqUcRDPicXY4XTtWqXXKJEh378eqtuTrlA/640?wx_fmt=png&from=appmsg)

（CHARM评测基准构建示意）  

###   

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**CHARM基准构成**

CHARM 是首个全面深入评估大型语言模型（LLMs）在中文常识推理能力的基准测试，它覆盖了国际普遍认知的常识以及独特的中国文化常识。此外，CHARM 还可以评估 LLMs 独立于记忆的推理能力，并分析其典型错误。

  

  

 常识领域

**全球常识领域:** 

全球常识领域包含了具有普遍理解性的常识，覆盖了现代生活中的各种对象和方面，是个体应当了解的知识。这些内容包括基础教育期望个体所掌握的基本知识。涉及到人物时，这些都是在全球范围内广为认可的人物。

  

**中国常识领域:** 

中国常识领域包含了特定于中国的元素，我们将其分为以下七个方面：

> **● 历史 (H)** ：包括中国历史上的重要事件和人物、中国的朝代以及关于中国历史的其他基础事实和共享知识。
> 
> **● 传统文化与艺术 (CA)** ：囊括中国的传统文化艺术、文学作品和传统生活方式。
> 
> **● 日常生活和习俗 (LC)** ：包括现代中国的日常生活、服装、食品、住房、交通、节日等。
> 
> **● 娱乐 (E)** : 包括现代中国日常生活中的电影、电视节目、音乐和其他娱乐活动。
> 
> **● 公众人物 (F)** ：涵盖在中国社会广为人知的公众人物。
> 
> **● 地理 (G)** ：包括中国的地理分布、自然景观和特色地区文化。
> 
> **● 汉语语言 (L)**：包括中国语言的基本知识，如汉字、成语等。

  

  

 任务列表

**推理任务 :** CHARM 由7个推理任务组成，包括：时代错误判断（AJ）、时间理解（TU）、序列理解（SqU）、电影和音乐推荐（MMR）、体育理解（SpU）、自然语言推断（NLI）以及阅读理解（RC）。

  

**记忆任务:** 我们选择了AJ（时代错误判断）、TU（时间理解）、MMR（电影和音乐推荐）以及 SpU（体育理解） ，这些被称为记忆-推理-互联（MRI）的任务，我们构建了与这些推理任务相关的记忆任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD58iaT1btuUFtsGmkkBq8NwVjjkr7cYTF3IWoyhwWnWriat89xbWB86LSHWQibLm2eCHwPsbibtrl0W6g/640?wx_fmt=png&from=appmsg)

（评测任务构成）  

###   

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**评测结果**

  

 LLM在CHARM上的整体表现

我们使用5种常用的prompt strategies，评估了19种LLMs在CHARM推理任务上的表现，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD58iaT1btuUFtsGmkkBq8NwV94MhqoaKkuKwaooDwMpuUGT4icR0icFneLZBOL9iaiau5eUibL3GPjs6aHg/640?wx_fmt=png&from=appmsg)

（点击放大查看19个热门LLM在CHARM任务上的表现）

####   

  

 LLM综合推理与记忆能力的对比

我们评估了LLM在CHARM的MRI任务上，综合推理与记忆能力之间的相关性。下面是 LLMs 在 4 个 MRI 任务上的平均表现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD58iaT1btuUFtsGmkkBq8NwVvOr89zMN8VTtef8xYFaSEmWNaQ7QashP8icGG87LXHskKIwk0h63oCg/640?wx_fmt=png&from=appmsg)

  

如图所示，这19个 LLMs 大致可以被分为三种类型：

**● 类型 I：低记忆能力和低综合推理能力**。我们发现，除了 OpenAI 的 GPT 系列外，所有其他的英文 LLMs 都属于这个类型。

**● 类型 II：高记忆能力和中等综合推理能力**。GPT3.5 和所有规模在 30B 以下的面向中文的 LLMs 都属于这个类型。值得注意的是，一些 LLMs 具有高度的记忆性能，但相对较差的综合推理能力。

**● 类型 III：超高记忆能力和高综合推理能力**。个类别包括 GPT4 和三个规模超过 30B 的面向中文的 LLMs。

  

上述结果为精准优化LLM的记忆能力和推理能力指明了方向。

  

  

 LLM使用不同prompt策略在CHARM不同知识域上的表现

#### LLM使用不同prompt策略在CHARM不同知识域上的表现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD58iaT1btuUFtsGmkkBq8NwVsVZrHoLUSV0J1WYVqulBtoCGibTmcXYIu45cllZwWveUXA3mI9hBEMQ/640?wx_fmt=png&from=appmsg)

  

结果显示，LLMs的语言取向和任务的知识领域会影响提示策略的表现，这进一步丰富了先前的研究发现。

**● 从 LLM 维度来看**, 不同的 LLMs 显然偏好不同的提示策略：在5种策略中，XLT 对于英文 LLMs 始终表现优秀，而对于面向中文的 LLMs，尽管存在一些复杂性，但 ZH-CoT 通常表现最好。

**● 从常识领域维度来看**, 使用英文进行推理的策略（如 XLT、Translate-EN 等）适用于全球常识领域；然而，ZH-CoT 在中国常识领域中的表现通常更好。

  

这里的结论与前面的研究有所不同 (Huang et al., 2023a, Zhang et al., 2023a, Shi et al., 2022),之前的研究提出，在处理非英文的推理任务时，使用英文比使用题目本身的语言更为有效。

  

**更多详细结果及分析请见：**

_https://opendatalab.github.io/CHARM/leaderboard.html_

_https://opendatalab.github.io/CHARM/findings.html_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**总结**

### **我们这项工作的主要贡献：**

**1、CHARM是中文常识推理领域的开创性工作:** 包含Chinese-specific commonsense domain和global commonsense domain，从而实现对LLM中文常识推理能力进行完整全面的评估，填补了中文常识推理领域的空白。

  

**2、CHARM拥有评估LLM的记忆能力和memorization-independent reasoning能力。**可以便于准确定位LLM的推理和记忆能力的长处和不足，为精准优化LLM指明清晰的方向。

  

**3、基于CHARM我们在LLM的prompt strategies方面得到的新的研究结论。**LLMs的语言取向和任务的知识领域会影响提示策略的表现，这进一步丰富了先前的研究发现。

  

**更多细节请访问：**

**论文地址：**

__https://arxiv.org/abs/2403.14112__

  

**Github：**

__https://github.com/opendatalab/CHARM__

  

**排行榜：**

__https://opendatalab.github.io/CHARM/leaderboard.html__

**项目主页：**

___https://opendatalab.github.io/CHARM/findings.html___

  

**下载地址：**

_https://opendatalab.com/OpenDataLab/CHARM_

本项工作引文：

> @misc{sun2024benchmarking,  
>           title={Benchmarking Chinese Commonsense Reasoning of LLMs: From Chinese-Specifics to Reasoning-Memorization Correlations},   
>           author={Jiaxing Sun and Weiquan Huang and Jiang Wu and Chenya Gu and Wei Li and Songyang Zhang and Hang Yan and Conghui He},  
>           year={2024},  
>           eprint={2403.14112},  
>           archivePrefix={arXiv},  
>           primaryClass={cs.CL}  
>     }

  

* * *

  

CHARM数据集已上架OpenDataLab

扫码直达↓

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD58iaT1btuUFtsGmkkBq8NwV4FkxB1YHR4GvGhKuaRy25V51rKAU04r7bpSHnxJe5BXmwFRzVQOEJg/640?wx_fmt=png&from=appmsg)

阅读原文或浏览器访问：

**https://opendatalab.com/OpenDataLab/CHARM**

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言