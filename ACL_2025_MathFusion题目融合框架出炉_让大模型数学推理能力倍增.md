     ACL 2025｜MathFusion题目融合框架出炉，让大模型数学推理能力倍增 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

ACL 2025｜MathFusion题目融合框架出炉，让大模型数学推理能力倍增
========================================

原创 热爱分享的 OpenDataLab 2025-07-18 17:17 上海

> 原文地址: [https://mp.weixin.qq.com/s/RjpZvAnL4EQXZQx4nZ\_saw](https://mp.weixin.qq.com/s/RjpZvAnL4EQXZQx4nZ_saw)

  

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：

当前大模型的数学数据合成方法常常局限于对单个问题进行改写或变换，好比是让学生反复做同一道题的变种，却忽略了数学题目之间内在的关联性。 这种“单点式”的训练让大模型在面对由多个子问题组成的复杂场景时捉襟见肘，难以有效利用不同知识点之间的内在联系。 就像一个学生可能做独立的填空题可以做得很好，但是做包含多个有关联子问题的应用题时却很困难。

为了打破这种局限，让大模型学会“串联”与“并联”知识，我们提出了MathFusion，通过指令融合增强大模型解决数学问题的能力。受到人类学习过程中系统性接触关联的概念来提升能力的启发，MathFusion通过融合不同的数学问题来增强模型的数学推理能力。 仅使用45K的合成指令，MathFusion在多个基准测试中平均准确率提升了18.0个百分点，展现了卓越的数据效率和性能。

本研究成果《MathFusion: Enhancing Mathematical Problem-solving of LLM through Instruction Fusion》由OpenDataLab和人大高瓴等高校学院、研究结构联合提出，已被计算语言学和自然语言处理领域的顶级会议ACL 2025接收，欢迎关注。

  

论文链接（已放至文末「阅读原文」）：  

https://arxiv.org/pdf/2503.16212

代码：

https://github.com/QizhiPei/MathFusion

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVxcDstIYNx2rwIVzHs5kRGWzuSL6Q8ATCXaUCiccVJ9hgzic3IVRxnNbg/640?wx_fmt=jpeg&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**MathFusion方法介绍**

MathFusion是一种通过融合不同数学问题来增强大模型数学推理能力的全新框架，其核心思想在于以互补性数学指令的策略性组合来释放模型更深层次的推理能力。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVoMtAqx4kNmHicicUibcIDSpkbLcLQic33LlJxI2wpHB28PibgwBM5ibJ1mGg/640?wx_fmt=png&from=appmsg)

具体而言，通过三种“融合策略”，将不同的数学问题巧妙地结合起来，生成封装了二者关系和结构的新问题：

*   **顺序融合 (Sequential Fusion)**：将两个问题串联起来，前一个问题的答案作为后一个问题的某个输入条件。这就像解决一个多步骤问题，模型需要先解出第一步，才能进行第二步，从而学会处理问题间的依赖关系。
    

*   **并列****融合 (Parallel Fusion)**：将两个相似的问题融合在一起，对它们的数学概念进行识别和融合，在原来问题的基础上提出一道新的问题。
    

*   **条件融合 (Conditional Fusion)**：创造一个需要对两个问题的解进行比较和选择的问题场景。
    

通过这三种策略，我们生成了一个全新的融合数据集MathFusionQA。 首先从现有数据集（GSM8K、MATH）中识别出适合融合的问题对（主要通过embedding search），然后应用融合策略生成新问题，并利用GPT-4o-mini来生成解答。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**融合实例**
--------

通过整合两个现有问题，MathFusion 会合成一个新的数学问题，该问题涵盖了原始两个问题的关系性与组合性特征。  

为了更直观地理解这三种融合策略，我们来看基于以上融合策略生成的新数学问题的具体例子：

**原始问题**

![](https://mmbiz.qpic.cn/mmbiz_png/HdGgWugCMaseIKAsf07ibOhib3oax8PpH1BPOAkpXGebH7L2WoLlAhN1fTrPO6gpNG1NrKP9cicWTSqfcCibhyamkA/640?from=appmsg)

  

问题 A：一天内，一艘船在湖中航行4次，每次最多可载12人。请问在2天内，这艘船可以运送多少人？  

问题 B：学校组织去博物馆。他们租了4辆巴士来接送孩子和老师。第二辆巴士的人数是第一辆的两倍，第三辆比第二辆少6人，第四辆比第一辆多9人。如果第一辆巴士上有12人，请问总共有多少人去了博物馆？

**顺序融合后的新数学问题：  
**

![](https://mmbiz.qpic.cn/mmbiz_png/HdGgWugCMaseIKAsf07ibOhib3oax8PpH1BPOAkpXGebH7L2WoLlAhN1fTrPO6gpNG1NrKP9cicWTSqfcCibhyamkA/640?from=appmsg)

  

学校组织一次去博物馆的旅行，需要运送学生和老师。首先，请计算一艘船在2天内的载客量，这艘船每天航行4次，每次最多可载12人。然后，将这个总载客量作为第一辆巴士的人数。 已知第二辆巴士的人数是第一辆的两倍，第三辆比第二辆少6人，第四辆比第一辆多9人。请问总共有多少人去了博物馆？  

如上所示，顺序融合后，问题A中船的总载客量作为问题B中的输入条件，即第一辆巴士的人数。

  

**并列融合后的新数学问题：**

![](https://mmbiz.qpic.cn/mmbiz_png/HdGgWugCMaseIKAsf07ibOhib3oax8PpH1BPOAkpXGebH7L2WoLlAhN1fTrPO6gpNG1NrKP9cicWTSqfcCibhyamkA/640?from=appmsg)

  

一所学校组织一次到博物馆的实地考察，并租用了4辆巴士和一艘船。这艘船一天航行2次，每次载客12人。每辆巴士的人数不同：第一辆巴士有12人，...，第四辆比第一辆多9人。请计算在2天内，船和所有巴士总共可以运送多少人？  

可以看到，并列融合后，生成了一道新的符合问题A和B原始语境的问题：计算运送的总人数。实际情况中，融合出来的新问题多种多样，这里以其中一个最简单的问题作为示例。

  

**条件融合后的新数学问题：**

![](https://mmbiz.qpic.cn/mmbiz_png/HdGgWugCMaseIKAsf07ibOhib3oax8PpH1BPOAkpXGebH7L2WoLlAhN1fTrPO6gpNG1NrKP9cicWTSqfcCibhyamkA/640?from=appmsg)

  

一个社区正在组织两种不同的郊游活动。对于湖上游览，一艘船每天运营4次，载客量为12人，他们计划让这艘船服务2天。与此同时，一所学校正在安排一次有4辆巴士的博物馆之旅。 第一辆巴士有12人，第二辆是第一辆的两倍，第三辆比第二辆少6人，第四辆比第一辆多9人。考虑到这些安排，哪种交通方式的载客能力更强？  

如上所示，条件融合后，新的问题要求模型结合语境，对问题A和B的结果进行比较和选择。

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**实验设置与结果**
-----------

**实验设置：**

为了更好验证MathFution对于模型解决数学能力的增强作用，我们做了一系列的实验：

1\. 从7B数学专用基础大模型DeepSeekMath-7B和7-8B通用基础大模型（Mistral-7B、Llama3-8B）出发进行训练。

2\. 每个基础模型均通过三种融合策略（顺序、并行、条件）进行微调。每种策略的微调数据集（30K样本）由 GSM8K、MATH 的原始数据集（15K样本）及对应融合策略生成的增强数据（15K样本）合并而成。MathFusionQA 数据集（60K样本）由所有子数据集合并构成。为验证 MathFusion 的Scaling能力，我们通过纳入Top-2至Top-4近邻样本扩大数据集，最终形成15K+4×(3×15K)=195K样本。所有模型均训练3轮完整训练。

3\. 我们在两个领域内（In-Domain）基准测试GSM8K和MATH上评估模型。领域外（Out-of-Domain）评估采用CollegeMath、DeepMind-Mathematics、OlympiadBench-Math和TheoremQA基准。

4\. 基线对比：我们主要将 MathFusion 模型与基于数学指令的模型进行比较，这些模型分为三类：

*   过往表现最优的方法：DART-Math、RefAug、MMIQC等  
    
*   在GSM8K和MATH数据集上指令微调的模型（Standardard，15K样本）  
    
*   基线方法的下采样版本（60K样本），以进一步评估不同数学数据增强方法的数据效率
    

**实验结果：**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVAm1tib5oSZFm0cicHHyCvNC3M2QIj8ybiaT4F3OXzJMPZWlLaPkjZicDZg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtV7qe5m2ia3SZPrlNUudW9LIicfIQIuvj9TH9L8xr5qL7VKmUL5icLG90rA/640?wx_fmt=png&from=appmsg)

越靠左上角，模型表现越好且数据效率越高

**显著提升模型性能与效率**：与标准训练方法（只在GSM8K数据集和MATH数据集上训练）相比，MathFusion在多个基础模型（包括DeepSeekMath-7B、Llama3-8B、Mistral-7B）上都取得了稳定的性能提升。 更重要的是，MathFusion在大幅提升性能的同时，保持了极高的数据效率，用远少于其他方法的数据量就达到了良好的效果。

**策略之间优势互补**：由于三种融合策略捕捉了问题融合的不同方面，组合融合策略优于每种单一融合策略，表明三种策略的结合可进一步增强模型的数学能力。

**强大的泛化与扩展能力**：MathFusion不仅在in-domain测试中表现优异，在更具挑战性的out-of-domain基准测试中同样超越了标准模型。

我们做了进一步的分析，有如下几点发现：

*   融合之后的问题的指令遵循难度（IFD）更高，说明融合之后的问题对于模型来说更加困难。
    
*   随着融合数据量的增加，MathFusion模型的性能呈现出近似对数形式的增长。
    
*   当把MathFusionQA数据集与DART-Math数据集结合使用时，模型的性能可以得到进一步的提升，甚至超过了单独使用任何一个数据集时的表现。这表明MathFusion的“问题融合”思路与DART-Math的“挖掘难题”思路是互补的。
    
*   通过t-SNE可视化分析，我们发现MathFusion得到的问题在特征空间中的分布比原始问题更均匀和广泛。
    
*   通过对teacher model的消融分析，证明了MathFusion带来的提升源自于问题融合本身，而非teacher model的好坏。
    

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVWIu8RR9lvo1ribDGqMl3v6zbyyaprL0xqlQQ3vIvoAJX43vQ6GPlXwQ/640?wx_fmt=png&from=appmsg)

  

GSM8K和MATH数据集上原始数据与融合数据的无条件和条件困惑度 (PPL)

  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtV01Jy9ncjuLTcpibtvwnC8yRXaDb71wt3j9mQWXK8AevybJRvXZq91NA/640?wx_fmt=png&from=appmsg)

  

GSM8K和MATH 数据集上原始数据与融合数据的 IFD（指令遵循难度）

  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVuLlQDPDqRuernfI2aku3tTorbn2cVjyExIRheicwRPjNU6smbYYSlzA/640?wx_fmt=png&from=appmsg)

  

Llama3-8B模型在不同规模增强数据上的性能缩放表现 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVyriaCOM3iayfkaVs0S3iaibqoFuVhXbwBSLC2QewBKYmH6wYcqp4Fhs4DA/640?wx_fmt=png&from=appmsg)

  

在MathFusionQA与DART-Math-Hard组合数据集上，使用不同规模采样数据微调Llama3-8B模型的平均性能

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtVwwPEIOx8dPKkOGiaUFrEcNQQ93ZEW7Cr0ywICV2dejiaXt1I4eFcasQQ/640?wx_fmt=png&from=appmsg)

  

通过t-SNE对GSM8K数据集的问题嵌入进行可视化

  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAW2dlUkZUxEtqiacq6H5icKtV7Aj3sicMwDnxaGMeqP5Su4yREwEBbfmNknUjnVNwbBv5CicHQeIiaS7Sw/640?wx_fmt=png&from=appmsg)

  

通过t-SNE对MATH数据集的问题嵌入进行可视化

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**总结**
------

MathFusion提出了一种全新的数学数据增强范式，从“融合问题”而非“改造问题”的角度出发，为提升大模型的复杂推理能力开辟了一条新路径。通过生成结构更多样、逻辑更复杂的合成问题，MathFusion有效地增强了模型捕捉问题间深层联系的能力。但目前MathFusion还只在GSM8K、MATH这种比较简单的数学问题，以及short cot solution的数据集上进行了验证，有待进一步扩展到更难的数学问题、long cot solution以及其他领域的数据上。

  

**更多关于MathFusion的使用方法和结果**

**欢迎访问以下地址**

👇

代码：  

https://github.com/QizhiPei/MathFusion

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

END  

  

**相关阅读：  
**

  

  

[2025《“人工智能+”行业发展蓝皮书》: AI数据，驱动智能时代的核心引擎](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550776&idx=1&sn=a5859ed3b0c4e813676f2466230486d6&scene=21#wechat_redirect)

2025-06-19

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUCKDo5xrUMfUOkaS66I8XHibamXwAg0bZayibHWaibVVl82S13PHkdsia3Hic7mQZymesG5C2QWqeD1RQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550776&idx=1&sn=a5859ed3b0c4e813676f2466230486d6&scene=21#wechat_redirect)

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