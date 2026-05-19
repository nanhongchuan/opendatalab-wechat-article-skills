     斩获ACL 2025最佳主题论文奖丨Meta-rater 框架，1% 算力锁定大模型最优数据 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

斩获ACL 2025最佳主题论文奖丨Meta-rater 框架，1% 算力锁定大模型最优数据
==============================================

原创 热爱分享的 OpenDataLab 2025-08-06 19:03 上海

> 原文地址: [https://mp.weixin.qq.com/s/LjBRSryeTbek2H2cx-yFlg](https://mp.weixin.qq.com/s/LjBRSryeTbek2H2cx-yFlg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：
---

第63届国际计算语言学协会年（ACL 2025）于7月27日至8月1日在奥地利维也纳举行。作为NLP领域最具影响力的顶级盛会，今年的ACL依然吸引了全球众多顶尖学者参与，投稿数量与质量再创新高。

在本届大会上，由上海人工智能实验室OpenDataLab团队与华东师范大学团队联合提出的研究成果《Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models》荣获“最佳主题论文奖”（Best Theme Paper Award）。

Meta-rater框架聚焦于提升大语言模型预训练的数据筛选效率，首次提出利用小规模代理模型，在仅约为1B模型训练开销1%的成本下，预测最优数据组合。相比以往依赖大规模试错的“黑箱式”方法，Meta-rater显著降低了算力开销，并通过多维度质量评估体系打破传统筛选标准的局限。

这一方法不仅提高了大模型训练的性价比，也为“什么是高质量语料”提供了全新的理解洞察。其在ACL 2025 获奖，展现了OpenDataLab团队在AI数据领域的深厚积累与创新能力。

**论文链接（已放至文末「阅读原文」):**

https://aclanthology.org/2025.acl-long.533/

**代码与数据集:**

https://github.com/opendatalab/Meta-rater

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUDicAh80d60iaZaddZv87gVqtvVXJAmw9pcJ32RjmggEmedKJ2Gq1cibAgMebciaYDP0O7g0vYAAjh3g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXO1p9hyFugKRoPbgtleLVDTPlXr3UMPKWYXaV98TLyFQicUsyKv9EX8iaTh0dxnYQmJDqKiaCbLZNDw/640?wx_fmt=png&from=appmsg)

01  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xiau6bniaopbDHde76xwriaSibGiaRKS1qqFdOlbeG9oCLVibbkptn0mOX8Ktibnb2cahdj7T4RwXVvbPGlaEF5Q2GRibA/640?from=appmsg)

解密Meta-rater：

如何智能筛选数据？

**Meta-rater**的核心思想是“四两拨千斤”。它通过一个高效的流程，即使用代理模型来训练一个能够预测验证集损失的回归模型，从而学习到最优权重，将这些新维度与现有的质量指标进行整合，最终精准定位出最优的数据组合策略。

1.  **多维质量评分：**研究人员为数据集中的每份文档，从25个不同维度进行打分。其中，首创了**PRRC**四大质量维度，即专业性（Professionalism）、可读性（Readability）、推理深度（Reasoning）和洁净度（Cleanliness），此外还涵盖了文本统计特征与领域重要性等其他方面。
    
      
    
    ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXO1p9hyFugKRoPbgtleLVDZRGtuPpFuahboyGqKA8qvmlT60OUeYC5kLNibp1rXKOCSql4ibFQynYA/640?wx_fmt=png&from=appmsg)
    
    Meta-rater中采集的25个不同维度的评分指标
    
      
    

2.  **训练“代理模型”：**随机生成数百种不同的“评分权重组合”，团队根据每一种权重组合筛选出的数据，训练一个极小规模的“代理模型”（仅18M参数）。
    
3.  **收集“权重-性能”数据**：每个代理模型训练完后，团队在同一个验证集上测试其性能（用损失函数**loss**衡量）并记录下数百个“权重组合”与“模型性能”的对应数据点。
    
4.  **拟合回归模型：**用这些数据点，团队训练一个回归模型**LightGBM**，让其学习“数据权重组合”和“模型最终性能”之间的复杂非线性关系。
    
5.  **预测最优权重组合：**使用训练好的回归模型，即可在不实际训练任何大模型的情况下，快速地在巨大的权重空间中进行搜索，高效地预测出能够使模型性能达到最佳（即验证集**loss**最小）的“黄金权重配比”。
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXO1p9hyFugKRoPbgtleLVDrXbibSrtrzN14RjvLbMNMXOOjyWBMcxv3jGB3ppjkKw3Rz27iarlyN1w/640?wx_fmt=png&from=appmsg)

Meta-rater算法流程

02  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xiau6bniaopbDHde76xwriaSibGiaRKS1qqFdOlbeG9oCLVibbkptn0mOX8Ktibnb2cahdj7T4RwXVvbPGlaEF5Q2GRibA/640?from=appmsg)

从数据到洞见：

实验结果与核心发现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXO1p9hyFugKRoPbgtleLVDglfQ5Eibia3w7yl2MjLmJYYiaOiam4ECZYyictmibrPdjGPoF62ibzUOYIksw/640?wx_fmt=png&from=appmsg)

Meta-rater与随机选择、SOTA基线（QuRating-Educational Value）在1.3B模型预训练上的性能对比

实验结果表明，使用**Meta-rater**筛选的数据进行预训练，**可将1.3B模型的收敛速度直接翻倍，并将下游任务平均性能提升3.23%**，并且这一优势在扩展到7.2B参数的大模型时依然显著。与此同时，Meta-rater筛选方法所需的计算量仅占1.3B模型预训练的0.7%，充分突出了其极高的性价比优势！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXO1p9hyFugKRoPbgtleLVDK9qkhteRTwCLKecLlj0UQjkZDAGlMhicxuaoPb4Y6cExnXtbGJoZqqA/640?wx_fmt=png&from=appmsg)

Meta-rater构建仅占1.3B模型预训练所需计算量的0.7%

值得一提的是，团队通过**Meta-rater****实验**发现，在25个质量维度中，**“教育价值”（EducationalValue）**的权重最高（5.64%），而PRRC指标中的**“推理”（Reasoning）**（4.44%）和**“专业性”（Professionalism）**（4.05%）也贡献显著。相比之下，传统上可能被看重的**“写作风格”（WritingStyle）****的**权重几乎为零（0.05%）。这不仅为我们提供了具有基准意义、经过量化评估的高质量数据，也为研究人员理解何为“高质量数据”提供了全新的、数据驱动的深刻理解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXO1p9hyFugKRoPbgtleLVDRnudIww5mhZgicU2hzLdH4Ia3LMib91Fk0Y8EdZ6pSyiaJyRv8oPuOngQ/640?wx_fmt=png&from=appmsg)

Meta-rater为每一个数据质量评估指标（rater）所分配到的权重

03  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xiau6bniaopbDHde76xwriaSibGiaRKS1qqFdOlbeG9oCLVibbkptn0mOX8Ktibnb2cahdj7T4RwXVvbPGlaEF5Q2GRibA/640?from=appmsg)

理念与实践：**Meta-rater的幕后团队**OpenDataLab

Meta-rater的诞生，并非来自抽象的理论设想，而是源于一个具体且迫切的实际需求——为大语言模型“书生·浦语”（InternLM：https://intern-ai.org.cn/home）构建高质量的预训练数据集。

当时，研究团队面临的核心挑战是：如何在海量原始数据中，依托有限的计算资源和时间，快速筛选出真正能够提升模型性能的高价值数据。传统的数据筛选方式，依赖人工经验或单一维度打分，往往效率低下、效果有限，难以系统性满足大模型的预训练需求。为了突破这一限制瓶颈，Meta-rater框架应运而生。

作为Meta-rater框架的研发团队——上海人工智能实验室OpenDataLab始终聚焦人工智能发展的关键领域——数据，长期专注于AI-Ready数据，致力于提供**高质量、可获取、可信赖**的数据资源，推动AI技术从“可用”走向“好用”。

Meta-rater的提出，正是OpenDataLab以“DataCentric”为理念在大模型时代的集中体现。除本研究外，OpenDataLab还推出了多个具有广泛影响力的开源成果，包括：

*   **OpenDataLab开放数据平台**：集成大量高质量、多模态、多语种的数据集，为全球开发者和研究者提供便捷的数据获取入口；
    
*   **MinerU文档智能解析工具**：具备工业级文档解析能力，可高效从非结构化文档中提取结构化信息，广泛应用于科研、企业与AI模型训练场景。
    

上述成果已获得全球数十万开发者与研究者的广泛关注和持续使用，体现了团队在AI数据领域的深厚积累与创新能力。

未来，OpenDataLab将持续深耕AI-Ready数据，推动Meta-rater等前沿研究成果在更多应用场景中落地，助力全球AI研究者与开发者高效获取优质数据，赋能人工智能技术持续进化。

  

**更多关于Meta-rater的使用方法和结果**

**欢迎访问以下地址**👇

**代码与数据集:**   

https://github.com/opendatalab/Meta-rater

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END  

  

**相关阅读：  
**

  

  

[ACL 2025｜MathFusion题目融合框架出炉，让大模型数学推理能力倍增](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550863&idx=1&sn=806d86d6f06e0b7a50b9d0e41c9d022d&scene=21#wechat_redirect)

2025-07-18

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVr21yk2VRl9Nj7lNCAZSWQSicq1DpHl77Re7WT5iarBEsjytElsDrGb4g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550863&idx=1&sn=806d86d6f06e0b7a50b9d0e41c9d022d&scene=21#wechat_redirect)

[AI“压力面”，DeepSeek性能暴跌近30% | 上海AI Lab&清华&人大](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550887&idx=1&sn=eb0d0ec9253b8e535492edde9e24ef22&scene=21#wechat_redirect)

2025-07-23

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUAVKIAHDXqYr9mZH5rohNPic5pbbgJzNI47WAs39kFibaBkEWH6A62ZYpvhFyQs02cAYKCpPyz0I5A/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550887&idx=1&sn=eb0d0ec9253b8e535492edde9e24ef22&scene=21#wechat_redirect)

[CVPR 2025｜OmniDocBench：PDF解析能力维度的指南针，让文档解析评测更全面、更精细](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550736&idx=1&sn=89f23a808ab98d8d8ee55091a98a75f1&scene=21#wechat_redirect)

2025-06-13

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWiclEgoAjQJYbJxhPGZp2yGhX2QIK3ubxqwSruuhydo9fZBLgUtw1nibvXHzJiblElg7XRARicaoQCuA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550736&idx=1&sn=89f23a808ab98d8d8ee55091a98a75f1&scene=21#wechat_redirect)

[国家数据局点赞！OpenDataLab小语种数据标注方案入选《数据标注优秀案例集》](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550623&idx=1&sn=d0f4750a373ddf37f5976d7c95ad0348&scene=21#wechat_redirect)

2025-05-28

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAX2AvnTTSP4A4f7tXyhh41AibalsauxWPRm71ouL56Viaj1WpneibuyVQzfJn9dTDrGor3Izac7PJ7SA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550623&idx=1&sn=d0f4750a373ddf37f5976d7c95ad0348&scene=21#wechat_redirect)

[官宣！MinerU 正式接入和鲸 ModelWhale，加速科研进程！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550942&idx=1&sn=31c7d439f24820d06769202e90669d84&scene=21#wechat_redirect)

2025-07-25

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7YpdscWAK3N7vriblv9E6RyAgUkoSYzJZliaBzVEvzFX25vDCtPWZ3f5wDHE3OBhtiaJqMzcyc5DicyeyYZxKv1qMA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550942&idx=1&sn=31c7d439f24820d06769202e90669d84&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言