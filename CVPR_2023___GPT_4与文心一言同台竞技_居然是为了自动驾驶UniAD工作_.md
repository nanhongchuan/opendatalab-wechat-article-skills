     CVPR 2023 | GPT-4与文心一言同台竞技，居然是为了自动驾驶UniAD工作！ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

CVPR 2023 | GPT-4与文心一言同台竞技，居然是为了自动驾驶UniAD工作！
============================================

原创 OpenDriveLab OpenDataLab 2023-03-24 20:00 上海

> 原文地址: [https://mp.weixin.qq.com/s/lCYG04SyBANMzS7RW8Gs3Q](https://mp.weixin.qq.com/s/lCYG04SyBANMzS7RW8Gs3Q)

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWf4yXPEd9r21t5bNL0C57drch8grgY7OMd55Pc6F9vibfHJhRv05Yolg/640?wx_fmt=png)

**前言**

  

都说 ChatGPT 是自然语言处理中技术大魔王，国内百度的文心一言是国内技术一霸，那自动驾驶中的技术魔王，你听过说吗？另外，ChatGPT 和文心一言都好评的自动驾驶端到端模型，大家不好奇吗？

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWL9lmEOqTNCK8Iu5beJ0gPKC0Ts8EBqBSia2dqvxibuYHgwY5ce8jJhDA/640?wx_fmt=png)

图源：文心一言；关键词：技术大魔王

  

ChatGPT 的横空出世解决了自然语言中绝大多数的任务：包括语言生成、文本分类、机器翻译、文本摘要和对话生成。ChatGPT 对自然语言处理任务表现出强大的“统治能力”，已经一统语言处理的江湖。国内百度的文心一言也统筹解决了聚集中文环境中的自然语言处理的任务。看着这些自然语言处理的技术大魔王，再看看OpenDriveLab自己的研究领域——自动驾驶。不禁发问：一个大的任务只需要一个模型就足够了吗？会存在自动驾驶领域的大魔王吗？

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWb7wU4HUUicqhutkonILgicFvEvicVLwEfrsmnNdF5ZIuOT8muQrtwjXmg/640?wx_fmt=png)

  

自动驾驶是一项高度复杂的技术，需要多个学科领域的知识和技能，包括传感器技术、机器学习、路径规划等方面。自动驾驶还需要适应不同的道路规则和交通文化，与其他车辆和行人进行良好的交互，以实现高度可靠和安全的自动驾驶系统。面对这种复杂的场景，大部分自动驾驶相关的工作都聚焦在具体的某个模块，关于框架性的研讨则相对匮乏。

  

自动驾驶是个相对困难的任务，但是**上海人工智能实验室 OpenDriveLab 自动驾驶团队**迎难而上，勇攀高峰的精神让我们团队的精神小伙们探索出自动驾驶中魔王级别的算法框架——**Unified Autonomous Driving（UniAD）**！

  

从任务看，UniAD 首次将检测，跟踪，建图，轨迹预测，占据栅格预测以及规划整合到一个基于 Transformer 的端到端网络框架下。从性能看，UniAD 在 nuScenes 数据集下的所有相关任务都达到 SOTA 性能，尤其是预测和规划效果远超其他模型。目前论文已被 CVPR 2023 接收。UniAD 完美契合了大魔王“多任务”和“高性能”的特点，可称为自动驾驶中的技术大魔王。同时 UniAD 也获得了 ChatGPT 和文心一言的认可，可谓是通过了技术魔王的“同行评议”：

  

  

 ChatGPT 版本：

  

我们把论文中的文字部分输入给ChatGPT，让他来理解 UniAD。文中其他的回答也都基于在模型理解完论文之后给出的答复。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6lDHiaibgyOv5bSvWFNwoNaGurlxNWgp9PxZLicDj5GiaqjCm49cqonO2y4iaHQlUh0SvJyt0qeib4ETbg/640?wx_fmt=png)

  

  

  

  

  文心一言版本： 

  

  

同样，我们把论文的文字部分输入到文心一言中，让他来理解 UniAD。文中其他的回答也都基于在模型理解完论文之后给出的答复。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6lDHiaibgyOv5bSvWFNwoNaGjiaPMCk1UWCzVX8AbOzYHpcccuONLzTO9MrokicmgO4YRUzpic9A3Lmuw/640?wx_fmt=png)

  
**想知道的更多 UniAD 的细节，下面的两个链接会给你答案。****1\. 项目地址：**https://github.com/OpenDriveLab/UniAD**2\. 论文地址：**https://arxiv.org/abs/2212.10156

![](https://mmbiz.qpic.cn/mmbiz_jpg/SLE456SxnMKndImjj3G5kjzrIxFD0GWWxHvFZKKgoJlaDUlJXKfAk90XibsWonKmLCuWicOicsJZ2Husenuf3mdqQ/640?wx_fmt=jpeg)

  

  

**01**

**魔王诞生**

  

  

**有关 UniAD 的诞生，要不先听听技术大佬们：青年研究员陈立、ChatGPT 和文心一言怎么说？**

  

  

 ****“ UniAD为什么会诞生？”****

  

  

可以先听听我们团队青年才俊、**自动驾驶研究员****陈立**的看法：

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6lDHiaibgyOv5bSvWFNwoNaGq1L7zpGV4wwOicsGpBbDFnax39UjyWMKHtxrbibWeb1GIHXSmfWFicicHw/640?wx_fmt=png)

  

  

  

  

 ChatGPT 是这样认为的：

  

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWuJlcZx42AnK1vPjOksl94KJiaV6iaKA5iaTz2NQUbvG0nmHBbFwFrTs9A/640?wx_fmt=png)

  

  

  

  

 文心一言也分析得头头是道：

  

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWXoqibxGjLnSdYUtNvlkBYibhneAFgKmzEryeib7ffq2aFibBHASHsy2jaQ/640?wx_fmt=png)

  

通过我们的青年研究员和两个技术大魔王的分析，相信大家肯定有所了解。接下来给大家详细阐述为什么 UniAD 会诞生，这必然会回到一个问题：“**为什么之前的模型没有同时做到这么多的任务呢**？”或许还要从自动驾驶的框架开始分析：

‍‍‍‍‍‍‍

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWW61dNEsJicBMI4n1nzKa3rdUp0vIbayKl6wVdHNocaPgoNWhHkibelmjQ/640?wx_fmt=png)自动驾驶UniAD框架对比 （a）传统模块化（b）多任务模块（c）端到端自动驾驶模块

  

**如上图所示，现有自动驾驶系统可大致归为三类：**

01

**传统模块化**

每个模型负责单独的子任务，优势在于易于调试迭代，但是解耦就会丢失最优性，各个模块的优化目标并不是以驾驶为最终目标，并且每个模块的误差会传递到之后的模块。

  

02

**多任务模块**

多任务范式利用一个共享的特征提取器来完成多个子任务，好处是节省计算成本，缺点在于不同任务之间可能会存在负面影响。

03

**端到端模块**

**端到端（End-to-end， E2E）**范式以最终的驾驶性能为目标，具体又可以细分为两种范式：隐式的端到端和显式的端到端。其中隐式端到端是以传感器数据作为输入，直接输出规划或者控制指令。这种范式的好处是较为简洁，缺点是缺乏可解释性，难以调式及迭代。显式端到端则是将多个模块囊括在端到端模型之中，每个模块有各自的输出，并且会将提取到的特征传递到下游任务。  

**我们对目前显式端到端自动驾驶工作进行了比较：**

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWNAgIJvqLRibiaEgicIEu72mVVZ3XfTNfljMRHbgkQYb2Be9vjr6m6gbtA/640?wx_fmt=png)

端到端自动驾驶工作对比

  

可以发现，大多数工作都关注了感知、决策和规划三部分，但具体任务存在差异，且没有框架融合所有的任务。那为什么会出现这种情况呢？一方面受限于对自动驾驶的认识，研究者们没有对任务之间的关联和构建方式研究清楚；另一方面受限于模型的最终效果，或许有人曾经尝试过把全部任务融合，但是效果不佳。

  

为了探讨这一问题，UniAD 首次将所有检测，跟踪，建图，轨迹预测，占据栅格预测与规划都包含进来，从实现方面解决了这一难点。另一方面，通过严格的消融实验发现，在正确的融合方式下，所有的任务对最终的驾驶性能都是有收益的。至此，自动驾驶方面的技术魔王为了解决实际问题而来。

  

**02**

**魔王登基**

  

  

那为什么我们的模型可以解决不同任务的融合难的问题，从而实现多任务和高性能呢？让我们开始揭晓自动驾驶技术大魔王的真身：

  

整体而言，UniAD 利用多组 query 实现了全栈 Transformer 的端到端模型。如图所示，UniAD 由 2 个感知模块，2 个预测模块以及一个规划模块组成。其中感知和预测模块是通过 transformer 架构进行预测，每个模块输出的特征会传递到之后的模块来辅助下游任务。

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWW8QwmLKuVz8vwC1x1XIJR45Wk4XicyNG6nkwBE3O9BicvIO187RmxZE6g/640?wx_fmt=png)

UniAD整体框架图

  

  

 秘密武器1：

多组 query 的全 Transformer 模型

UniAD 利用多组 query 实现了全栈 Transformer 的端到端模型，我们可以从具体 Transformer 的输入输出感受到信息融合。在 TrackFormer 中，Track query 通过与 BEV 特征通过 attention 的方式进行交互，对特征进行输出。类似的，Map query 经过 MapFormer 的更新后，得到相应的特征。MotionFormer 使用 Motion query 与 BEV 特征进行交互，得到未来轨迹。

  

OccFormer 以密集的 BEV 特征和稀疏的特征对应的位置信息来构建实例级别的占据栅格。

  

  

 秘密武器2：

基于最终“规划”为目标

在 TrackFormer 中，Track query 中包含一个特定的 ego-vehicle  query 用来表示自车属性。规划模块 (Planner) 将 MotionFormer 更新后的 ego-vehicle  query 与 BEV 特征进行交互，此时 ego-vehicle query 包含对整个环境的感知与预测信息，因此能更好的学习 planning 任务。为了减少碰撞，我们还利用占据栅格预测模块 OccFormer 的输出对自车路径进行优化，避免行驶到未来可能有物体占用的区域。在这个过程中，全部的模块通过输出特定的特征来帮助实现最终的目标“规划”。

  

**03**

**魔王雄风**

  

  

UniAD 在 nuScenes 数据集中的所有任务都达到了 **SOTA**，尤其是预测和规划部分，具体的定量指标我们不多赘述。下面给出 UniAD 在不同场景的可视化结果。在技术大魔王的框架之下，如果我们能有机会坐在实车中，一定会享受整个驾驶过程。ChatGPT 和文心一言也抱有相同的看法呢：

  

  

 ChatGPT 版本：

  

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWW0xroibxkUHL0HzIxHW7czIYNx4szk8dhn1fG9hCiaRH6Y06lrj6xeh7w/640?wx_fmt=png)

  

  

  

  

  文心一言版本： 

  

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWzy46AicdXLicLdRSOicqcPUHeZziavribTicohbiaMG0U6uQLHJujWSXW28yg/640?wx_fmt=png)

  

  

  

01

晴天直行

![](https://mmbiz.qpic.cn/mmbiz_gif/SLE456SxnMKndImjj3G5kjzrIxFD0GWW2CFibwICyCgXlZammxAtdfe6AQKibKasVOpEwAibbbCMMEpSHM6jNmiaMQ/640?wx_fmt=gif)  

UniAD 可以感知左前方等待的黑色车辆，预测其未来轨迹（即将左转驶入自车的车道），并立即减速以进行避让，待黑色驶离后再恢复正常速度直行。

  

02

晴天转弯

  

![](https://mmbiz.qpic.cn/mmbiz_gif/SLE456SxnMKndImjj3G5kjzrIxFD0GWWUJqOSkNibibUyha5wiaII2oXP1OSicic7zQXjWgBBk4jQkaRP1aPNaWAicibg/640?wx_fmt=gif)

得益于UniAD的地图分割模块，其可以沿着分割得到的道路结构适时地转弯。

  

03

雨天直行

![](https://mmbiz.qpic.cn/mmbiz_gif/SLE456SxnMKndImjj3G5kjzrIxFD0GWWhqFnnaiabwV02cTWHh3wILU5ibGhC03LSGvYK75RiaaEB6rwLWuiccs9gw/640?wx_fmt=gif)

在视野干扰较大的雨天环境中，UniAD 也能感知到周围车辆进行正常行驶。

  

04

雨天转弯

  

![](https://mmbiz.qpic.cn/mmbiz_gif/SLE456SxnMKndImjj3G5kjzrIxFD0GWWZVz2OB13sFPq7cnnwrrh12rnxvV7xMib9wVoC4iatxDSWmbPLJ4nVEAA/640?wx_fmt=gif)

在视野干扰较大且场景复杂的十字路口，UniAD 能通过分割模块生成十字路口的整体道路结构（如右侧 BEV 图中的绿色分割结果所示），并完成大幅度的左转。

  

05

夜晚直行

![](https://mmbiz.qpic.cn/mmbiz_gif/SLE456SxnMKndImjj3G5kjzrIxFD0GWWdrwIv6Ev10LQoA3Wxp1dNX9BLjR3gmCrqVYLR7sSP6Clzlq2JRy6ibA/640?wx_fmt=gif)

在夜晚视野变暗的情况下，UniAD 仍然能感知到前方以及右侧的车辆（双车道场景），确保自车行驶。

  

06

夜晚转弯

![](https://mmbiz.qpic.cn/mmbiz_gif/SLE456SxnMKndImjj3G5kjzrIxFD0GWWOkoyUJExsjhln83lqwhTQsh4tXaRWYgt8leCSeOj5mARjHRcVldIcg/640?wx_fmt=gif)

在夜晚视野变暗的情况下，UniAD 能感知到前车并完成先静止，后左转的规划。

  

  

  

**04**

**未来展望**

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/SLE456SxnMKndImjj3G5kjzrIxFD0GWWE2URsy82Z9XO3QHUk1NLoU2UITxCyNEn8r2thRiaVPibh1t4BE6NTdSw/640?wx_fmt=jpeg)

图源：文心一言；关键词：自动驾驶

  

UniAD 的发展还在如火如荼的进行，那他的未来会是什么样呢？让我们一起来听听ChatGPT 和文心一言怎么说，毕竟同行最了解同样，技术魔王最懂技术魔王呀！  

  

  

 ChatGPT 版本：

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWWu765Mxj2uHj8OByicuRWPoFBStdpXRBlbPp256FgtCJneMl7KTueszw/640?wx_fmt=png)

  

  

  

  文心一言版本： 

![](https://mmbiz.qpic.cn/mmbiz_png/SLE456SxnMKndImjj3G5kjzrIxFD0GWW5H7qUwPdwZUX7BLU6QL0Q0o2K8HgqFBEiaia40JzsWiagkcOMYe0mMUKw/640?wx_fmt=png)

  

总的来说，UniAD 作为一项极具创新性的自动驾驶技术，具有很大的潜力和应用价值。尽管该技术目前仍处于发展初期，但其已经引起了人们的广泛兴趣和关注，未来的发展前景非常值得期待。

  

后续我们将会持续推出更多技术类干货，带领大家了解更多自动驾驶领域的前沿技术与发展路线，欢迎大家多多关注**上海人工智能实验室 OpenDriveLab 自动驾驶团队**工作及最新动态！

  

[![](https://mmbiz.qpic.cn/mmbiz_jpg/SLE456SxnMKndImjj3G5kjzrIxFD0GWW7vmnmTdBy34F2csLTpQcJWr3zQp4ibYemosvg9iaiaXJXcuKCsKqHogNg/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247516721&idx=1&sn=48a897db42f8f6df5183cbd3a89a6441&chksm=c10c10d3f67b99c59bfb9ce89bfe4a5c838f4c99b510e81c7923e5bf9ed419e9e979cfdf5e1d&scene=21#wechat_redirect)  

  

  

\-END-

  

更多自动驾驶数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言