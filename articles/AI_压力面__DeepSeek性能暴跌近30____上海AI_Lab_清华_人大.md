     AI“压力面”，DeepSeek性能暴跌近30% | 上海AI Lab&清华&人大 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI“压力面”，DeepSeek性能暴跌近30% | 上海AI Lab&清华&人大
=========================================

原创 热爱分享的 OpenDataLab 2025-07-23 18:50 上海

> 原文地址: [https://mp.weixin.qq.com/s/UgRqvvrwsi69SEY78l16GQ](https://mp.weixin.qq.com/s/UgRqvvrwsi69SEY78l16GQ)

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：

给AI一场压力测试，结果性能暴跌近30%。

来自上海人工智能实验室OpenDataLab、清华大学和中国人民大学的研究团队设计了一个全新的“压力测试”框架——**REST (Reasoning Evaluation through Simultaneous Testing)**。

该框架在一个prompt里同时抛给模型多个问题，模拟真实世界中复杂的、多任务并行的推理场景。

结果发现，即便是像DeepSeek-R1这样的顶级模型，在“高压”之下的表现也大幅缩水，例如，**在AIME24测试集上的准确率骤降29.1%**。

  

论文链接（已放至文末「阅读原文」）：  

https://arxiv.org/abs/2507.10541

项目地址：

https://opendatalab.github.io/REST

代码：

https://github.com/opendatalab/REST

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNPJVA5ia8Y2r2F9e9WUXIIpdIkBKD16sHmz4prI2zcRkS8zLYI1ib84vSg/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**给大模型来一场“压力测试”**

如今的大模型在各种推理能力测试中动辄拿下接近满分的成绩。

如果让模型一次做好几道题，它还会那么“神”吗？

团队认为，当前大模型的评测模式普遍存在三大痛点：

1. 区分度低：在许多基准测试中，顶尖模型的得分已趋于饱和，难以分出高下。例如，7B参数的DeepSeek-R1-Distill-Qwen-7B和671B参数的DeepSeek-R1在MATH500上的准确率分别为93.0%和97.0%，看似相差不大，但推理能力仍有显著区别。

**2. 成本高昂**：由于现有的数学题几乎已经被纳入了大模型的训练数据。为了有效评估，社区不得不持续投入大量人力物力去开发更新、更难的测试题。但设计这样的测试题需要极高水平的人类专家，一年也出不了几个题。例如，AIME24和AIME25都只有30道题。

**3. 脱离现实**：一次只答一道题的模式，无法考察模型在真实世界中处理交叉信息，完成多重任务的综合能力。

为了解决这些问题，团队设计REST框架——改造现有基准，如GSM8K、MATH500、AIME24等7个代表性推理任务，不再逐题测试，而是**把多个问题拼接成一个长prompt，一次性让模型在一次输出中逐一回答**。

研究团队基于GSM8K、MATH500、AIME24等7个主流推理基准，构建了REST评测集，并对超过30个参数从1.5B到671B的主流推理模型进行了全面测试。

这种“压力测试”不仅考察模型基础的推理能力，更深入评估了以往被忽视的几项关键能力：

*   **上下文预算分配**：模型得聪明地决定怎么在多个题目中分配思考Token。
    
*   **跨问题干扰抵抗**：避免一道题的错误“传染”到其他题。
    
*   **动态认知负载管理**：在高压下保持高效推理，别在一道题上陷入“过度思考”的陷阱。
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNP2dyrkZ4YCpo0uHFHFjglWytx9r6icNxKamvp4bJUbYYzksMODPUsTuQ/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**SOTA模型也“扛不住”，REST拉开差距**
-------------------------

1. 最强模型，在多题高压下也顶不住：LRMs可以在单个推理过程中处理多个相对简单的问题，但在REST下，性能皆下降。

比如DeepSeek-R1，在AIME24基准上，单题模式下效果拔群，但“压力测试”下准确率直降29.1%！其他模型也类似，整体性能大打折扣。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNPU5g4qtc5dMU2knTTQZqYmxL1ULkGyMQXaAKe5sIeKQ7ibaHRn7CEapA/640?wx_fmt=png&from=appmsg)

**2.** **拉开区分度，撕开“伪高分”面纱**：传统单题测试中，不同大小模型得分都接近天花板，看不出谁更牛。但REST一上，差距立现！如下图所示，7B参数的小模型在高压下崩得更快！而更大的32B参数的模型性能虽有下降但仍保持优势。不同压力水平下，模型性能拉开明显梯度——这让REST成为更强的“分辨器”，帮我们精准比较模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNPVFyX6icvH86YK4J9IpOCBhIfCmPSw4RvWuxdJiabibhP9R06UFDeHiaVMQ/640?wx_fmt=png&from=appmsg)

**3.****“过度思考”成大坑，long2short技术救场**：为什么模型在REST下变差？分析显示，关键是陷入了过度思考的陷阱。就像学生考试，在一道难题上思考太久，没时间做后面的题目了。

但用“long2short”技术（鼓励模型缩短推理过程）训练的模型，就能更好地保留单题性能，在REST下领先。如L1Qwen-1.5B-Exact和L1-Qwen-1.5B-Max，在高压力水平下表现出显著的性能优势。如下图所示，L1-Qwen-1.5B-Max在MATH500上压力水平s=9时，准确率比R1-1.5B高出44.71%的显著差距。7B模型中也观察到类似的趋势。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNPiaia67icibY4eBZ8HG9zYUFqOoGYeRWb7m6VGf6x7zj6iaKdysYwr4yicOMw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNPUJOIic27CTJJfUABkS3CXWlcklc8iaUFycC9dwZZBaUTnfxAzsz3ffBQ/640?wx_fmt=png&from=appmsg)

4. **动态分配token，有的模型更“聪明”**：REST下，一些聪明的模型（如Nemotron-nano-7B和DeepSeek-R1）会动态调整推理预算：当压力增大时，它们为第一道题分配更少的推理token，留力后续。但低性能模型（如DeepS-eek-R1-Distill-Qwen-7B）往往在前面的题上用掉太多token，导致整体崩盘。

这一观察表明，在REST中表现优异的LRM模型在压力下倾向于对早期问题进行更简洁的推理，从而为后续问题留出足够的空间。团队将这种能力称为“自适应推理努力分配”，认为这是在REST下实现稳健性能的关键因素。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNP93FdhrDcvLPeVSJTK8dzSlwxcW0bmBKYYEwEQUjeqLA6Pqu8VOKPKQ/640?wx_fmt=png&from=appmsg)

此外，REST还揭示了一些推理不良行为，如问题遗漏和对推理过程总结错误，这些问题在单问题评估中未被发现。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**总结**
------

总而言之，REST不是简单加题，而是给大模型来场“压力测试”，挑战了“LLMs是多问题解决者”的普遍假设，揭示了当前评测方法的局限性，提供了一种更低成本、更贴近真实的评测数据构建新范式，为未来开发更健壮和强大的LRMs提供了更加深刻的见解。

  

**更多关于REST的内容和实验结果**

**欢迎访问以下地址**

👇

项目地址：https://opendatalab.github.io/REST 

代码仓库：https://github.com/opendatalab/REST

  

![](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

END  

  

**相关阅读：  
**

  

  

[ACL 2025｜MathFusion题目融合框架出炉，让大模型数学推理能力倍增](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550863&idx=1&sn=806d86d6f06e0b7a50b9d0e41c9d022d&scene=21#wechat_redirect)

2025-07-18

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVr21yk2VRl9Nj7lNCAZSWQSicq1DpHl77Re7WT5iarBEsjytElsDrGb4g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550863&idx=1&sn=806d86d6f06e0b7a50b9d0e41c9d022d&scene=21#wechat_redirect)

[CVPR 2025｜OmniDocBench：PDF解析能力维度的指南针，让文档解析评测更全面、更精细](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550736&idx=1&sn=89f23a808ab98d8d8ee55091a98a75f1&scene=21#wechat_redirect)

2025-06-13

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yGhX2QIK3ubxqwSruuhydo9fZBLgUtw1nibvXHzJiblElg7XRARicaoQCuA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550736&idx=1&sn=89f23a808ab98d8d8ee55091a98a75f1&scene=21#wechat_redirect)

[CVPR 2025｜公式识别评测新指标CDM：视觉元素buff加成，让大模型公式识别评价更准确、更客观](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550674&idx=1&sn=a270d72ea7b75fefd90c07eece467e16&scene=21#wechat_redirect)

2025-06-11

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXZ51dpXQ09VWmgID7PImUzeAbMLfx9qNTbhD4MGkm377dlWVXibZ0CTYuxtLtTjO8mZ7t8ttkwHEw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550674&idx=1&sn=a270d72ea7b75fefd90c07eece467e16&scene=21#wechat_redirect)

[全自动调整数据配比，解放LLM工程师丨上海AI Lab&上海交大联合团队提出创新数据均衡方法，让大语言模型不“偏科”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550657&idx=1&sn=cd586a6c25e19337a70be8f2fed1992d&scene=21#wechat_redirect)

2025-06-10

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVOTWa1icqFo4x6Ighsl2g7HVIGbn4j2TibmswBqcNsl5rXNGash2MfbH9KpjR3btvOIpuhUbvBXUbw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550657&idx=1&sn=cd586a6c25e19337a70be8f2fed1992d&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言