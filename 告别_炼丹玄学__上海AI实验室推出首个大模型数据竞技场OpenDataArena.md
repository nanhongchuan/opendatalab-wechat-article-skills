     告别“炼丹玄学”：上海AI实验室推出首个大模型数据竞技场OpenDataArena \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

告别“炼丹玄学”：上海AI实验室推出首个大模型数据竞技场OpenDataArena
=========================================

原创 OpenDataLab 2025-08-25 17:39 上海

> 原文地址: [https://mp.weixin.qq.com/s/PBwMFvZkmHf8LuDbgoIeTA](https://mp.weixin.qq.com/s/PBwMFvZkmHf8LuDbgoIeTA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

数据在AI时代的重要性已经不言而喻，但悬而未决的是——

如何精确量化这些数据的价值、辨别其优劣？

为此，上海人工智能实验室OpenDataLab团队在数据领域持续深耕，正式推出了**开放数据竞技场OpenDataArena**。

地址：https://opendataarena.github.io/index.html  
工具：https://github.com/OpenDataArena/OpenDataArena-Tool  
数据：https://huggingface.co/OpenDataArena

![](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtClKP8yVMIx7lU7Vu7wUVaYlVXMFRzljy2NXumIGTHLcEoTc5wtZk6libPia0KKcyOO2OPbbVu8cNjg/640?wx_fmt=png&from=appmsg&watermark=1)

展开来说，在海量的SFT_（监督式微调）_后训练数据面前，研究者们常常陷入“黑盒式”的困境：不清楚哪些数据真正有用，也难以系统性地评估和比较不同的数据集。

而OpenDataArena，正是一个为数据价值而生的“竞技场”，致力于将数据质量的评估从“玄学”变为“科学”。

团队希望通过一个**公平、公开、透明**的平台，首次正式尝试回答“如何验证数据价值”这一核心问题。

它不仅提供了一个直观的**数据评测榜单**，更构建了一套完整可复现的数据价值验证体系——

通过一套训评一体化的开源工具，让不同数据集在同等条件下公平“竞技”，用模型效果作为衡量数据价值的最终标准。

同时，通过开发多维度评分工具，对数据进行精细化“体检”，让数据价值不再是模糊的“黑盒”。

下面详细来看。

OpenDataArena：数据价值的首次全面验证
-------------------------

OpenDataArena首次系统性地探究**“如何评价数据质量”**这个难题。

为此，该项目构建了“开放数据竞技场”，并配套开发了一整套数据价值验证工具。

该平台的核心成果包括：

*   OpenDataArena平台：一个公平、公开、透明的SFT后训练数据价值评测平台，涵盖一个多领域、可视化的数据竞技榜单。
    
*   多维度数据打分：平台从几十种维度对已有数据进行精细化打分，并已开源了部分评分数据，便于研究员们后续直接下载使用，避免重复API调用。
    
*   训评一体化工具：团队开源了整套数据训练、评估以及数据打分工具，让价值验证过程可复现、可扩展。
    

OpenDataArena为以下几类核心需求提供了实际的解决方案：

1、**对数据质量的评估与筛选：**帮助**模型训练者**和**数据研究者**快速识别并筛选出高质量数据集，摆脱盲目试错，高效赋能模型训练与应用。

2、**对数据生成的指导与优化：**为**数据合成的研究者**提供多维度的评分数据和工具，助力他们寻找高价值的“种子数据”，为生成更优质的合成数据提供指导。

3、**对数据价值的深入洞察：**赋能**学术研究人员**探索数据特征与模型效果的内在关联，为数据选择、数据生成等前沿研究提供坚实的数据支持和客观的评估依据。

平台目前已覆盖4+领域、20+基准测试、20+数据评分维度，处理了100+数据集，超过20M+数据样本，并完成了600+次模型训练、10K+次模型评估，这些指标都在不断增长。

![](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtClKP8yVMIx7lU7Vu7wUVaYMg6vP2DxibVqlsJMsaNtPfSZwUYeR4Y5W5jkIJMLO3D34hpmUNFicTew/640?wx_fmt=png&from=appmsg&watermark=1)

数据竞技场：让数据在实战中一较高下
-----------------

OpenDataArena的核心理念，就是让数据价值在实战中得到验证。

该平台通过一套公平、公开、可复现的大模型训练与评测机制，来比较不同训练数据集的优劣。

那么，OpenDataArena具体是如何运作的呢？

**1、数据集选择**

平台覆盖了来自通用、数学、代码、科学等多个领域的后训练数据集。这些数据来自于HuggingFace并且有一定的下载和关注度，不仅具有代表性，而且具备时效性，确保了评测的现实意义。

**2、模型选择**

平台采用了社区中最常用、最具代表性的**Llama3.1**和**Qwen 2.5**的**7B版本**作为基准模型，它们代表了真实的学术和工业应用场景，同时尽可能反映了最多场景中实际使用的模型大小的数据性能。

**3、训练与评估**

平台采用标准化训练配置，训练环节采用广受认可的**LLaMA-Factory**框架，并且严格采用最常见的训练参数。

测试环节使用**OpenCompass**进行全面评估，在测试环节的参数设置上，团队进行了大量预实验，确保推理模板和评估器等细节都经过了精心的优化，排除外部干扰，让测试结果能更公平、公正地反映训练数据集的真实质量。

**4、评测集全面覆盖**

平台选择了通用、数学、代码、长链推理等多维度基准测试集，力求全面、客观地反映单领域数据质量，以及混合领域的数据综合质量。

最终，OpenDataArena数据竞技场诞生，通过**数据评测榜单**直观的给出数据“优秀”程度。

平台希望能够帮助模型训练者和数据研究者快速识别并挑选高质量数据集，降低试错成本，赋能模型训练与应用。

![](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtClKP8yVMIx7lU7Vu7wUVaYtvhawfHWm3z8G9xurQgXjj4K8iaMEleSIgSSrXC5Ev9VcPvHhHdUqGg/640?wx_fmt=png&from=appmsg&watermark=1)

数据多维度评价：打开数据质量的“黑匣子”
--------------------

除了通过训练模型得到下游任务的表现来直接反应数据的质量之外，OpenDataArena还通过多维度的客观评分工具，来对数据本身进行细致的“体检”，这些客观评分指标得到了学界和业界的广泛认可。

**1、20+维度，精准画像**

平台对代表性的数据集整体，以及数据集中的每一条数据，都进行了细致的多维度打分。

不论是直接选用整个数据集，还是用于挑选优质子数据，都方便操作。同时，无论是指令数据，还是指令-响应对数据，平台都从不同方面提供了相应的评分。

**2、多源评分，深度剖析**

平台的评分工具整合了多种维度评估方法，包括基于模型的评估（Model-based Evaluation，如IFD）、大模型作为评委（LLM-as-a-Judge，如准确性、复杂度）和启发式方法（Heuristic，如回复响应长度）。

这些维度涵盖了数据的常见评价指标，为数据的价值提供了丰富的量化视角。

**3、开源评分数据**

团队已完成对超过15M+数据的多维度评分，并已开源这些数据评分结果。

对于需要依赖常见评价指标开展数据筛选、种子数据生成等任务的科研用户而言，这不仅极大降低了打分成本，还有效避免了重复的API调用，从而节省了实际开销，可谓一项极其宝贵的资源。

通过上述努力，平台为数据合成、数据筛选的研究者提供了多维度的评分数据和工具，助力他们寻找高价值的“种子数据”，最终为生成更优质、更高价值的数据提供了直接的帮助。

![](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtClKP8yVMIx7lU7Vu7wUVaYITtKAgpYGtGbKEzqlltJicibnj6KiaQgfkiaibBRo7zQicsC3jXicHricMn3fg/640?wx_fmt=png&from=appmsg&watermark=1)

开源工具：让数据价值验证触手可及
----------------

为了“公平、公正、公开”的OpenDataArena平台的设计原则，同时也为了让更多人能参与到数据价值验证中来，真实地评价数据的质量，OpenDataArena团队将整个平台的核心工具都进行了开源。

包括基于模型的训练评测工具，以及客观的多维度数据评价打分工具，所有的细节能在完整的OpenDataArena-Tool中找到说明。

![](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtClKP8yVMIx7lU7Vu7wUVaYicRWMSV0zgah5EBxCZwBUeiaEBKbNpZzPZNVdR7JPbxIFdZsvdmZvLYg/640?wx_fmt=png&from=appmsg&watermark=1)

*   训评一体化工具
    

平台基于主流的LLaMA-Factory训练框架，以及评测端知名的OpenCompass框架，打造了一套端到端的训练与评测工具，给出了所有的配置和流程复现脚本，确保了评估实验的结果可复现性与公平性。

相关的设置都尽可能与当前的主流研究工作、以及其余开源工具进行了对齐，保证了结果的公平公正可比。

具体的说明可以在配置详情和工具说明中，找到所有细节。

*   多维度数据打分工具
    

平台对于数据评价的打分工具也在持续完善中。

目前已实现的大部分评估维度打分工具均已开源，并提供了详细的使用教程。不管是单个维度的数据评估，还是所有已支持的数据评估维度，用户都可以在官方wiki文档中了解到如何使用这些工具，并为自己的数据进行“体检”。

同时，团队还在持续优化支持更多的数据打分维度，为用户提供更多维度的数据打分选择。

通过上述的工具开源，OpenDataArena团队希望提供一个开放共享的数据价值评估平台，让所有用户都能参与到数据评估中来，并为产生真正的高价值数据共同努力。

![](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtClKP8yVMIx7lU7Vu7wUVaYhibiatR41y5xGbGicRheoVXgaFCKjia4lEUDJgE21T3ibNEpRssyNw2o6tA/640?wx_fmt=png&from=appmsg&watermark=1)

未来展望：数据价值的星辰大海
--------------

据团队介绍，目前OpenDataArena已经完成的仅仅只是冰山一角，也只是对数据价值验证的开始。

项目未来也有更多的计划，例如下面这些：

*   扩展验证范围： 逐步支持多模态等更复杂的数据类型；
    
*   深化应用场景： 扩展至医疗、金融、科学等更多专业领域；
    
*   保持新鲜度： 每月更新数据竞技场，确保数据排行榜的及时性。
    

团队认为，数据价值的验证需要社区的共同努力，上述计划也非常需要科研社区的力量来共同参与。

感兴趣可以进一步关注。

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END  

  

**相关阅读：  
**

  

  

[MinerU又双叒更新了！化学解析×多模式翻译等多种功能上线！文档解析处理爽到飞起！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

2025-08-08

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTyWAumU6Y7sdbgsxLgByGO8XbrzT7AOhs8LlQhV1ph0m76jjMmKVkhA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

[上海AI实验室发布MinerU2：通专融合路线如何补齐AI-Ready数据的最后一公里](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550992&idx=1&sn=5f53580545f1f6070e5242ab35cae86d&scene=21#wechat_redirect)

2025-08-07

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWBNkx3esjVNr2VtRgpf9vlV5iaGkUiaXPhgnb94tv1wfx2ahMq2icbHz0Bxkt7Y4NmONUJWYo57Fibibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550992&idx=1&sn=5f53580545f1f6070e5242ab35cae86d&scene=21#wechat_redirect)

[新工具开源！Vis3大模型数据可视化利器：填 AK/SK 直接预览 S3 数据，JSON/视频/图片秒开！本地文件也可用](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550861&idx=1&sn=f7057a62647e879a194cce5938cc76ac&scene=21#wechat_redirect)

2025-07-04

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUn8yYtug9M9iaemDlEomWBrcUrHQ5KAguBYe2jqOz84Q8IsoY3G5pAERnnJTGOqWAIupGwRxibgFDA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550861&idx=1&sn=f7057a62647e879a194cce5938cc76ac&scene=21#wechat_redirect)

[Dify、n8n、扣子、Fastgpt、Ragflow到底该怎么选？超详细指南来了【好文推荐，附MinerU实用教程】](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550805&idx=1&sn=4b73bf0c9f9cc85ab3ed4cf36a22acd9&scene=21#wechat_redirect)

2025-06-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUniaALHa5jYSxXR991CavbDvPXicgJSx3AmxRq7DY4ZRXq5RMczgD9H9fZLfgRqjkKXkrgmr3uRSibg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550805&idx=1&sn=4b73bf0c9f9cc85ab3ed4cf36a22acd9&scene=21#wechat_redirect)

[MinerU × Cherry Studio：知识库再添动力！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550749&idx=1&sn=8e8668431c3d41c81b5071d0d37064c4&scene=21#wechat_redirect)

2025-06-17

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAV3ojk5ZyrEnaWN2SN1WCrUZ4z3BAvHsyficZwGUAMHiao25HvyMn5JNVpnUTiaicHqHnTNre2IPueNTQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550749&idx=1&sn=8e8668431c3d41c81b5071d0d37064c4&scene=21#wechat_redirect)

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言