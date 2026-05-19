     上海AI实验室无人机视觉语言导航最新基准！OpenFly：空中VLN的全能工具链与大规模测试基准 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

上海AI实验室无人机视觉语言导航最新基准！OpenFly：空中VLN的全能工具链与大规模测试基准
================================================

原创 视觉语言导航 OpenDataLab 2025-05-23 21:45 上海

> 原文地址: [https://mp.weixin.qq.com/s/UrVwqpaxmmYSRvsW00eSYA](https://mp.weixin.qq.com/s/UrVwqpaxmmYSRvsW00eSYA)

*   论文标题：OpenFly: A Versatile Toolchain and Large-scale Benchmark for Aerial Vision-Language Navigation
    
*   作者：Yunpeng Gao, Chenhui Li, Zhongrui You, Junli Liu, Zhen Li, Pengan CHEN, Qizhi Chen, Zhonghan TangLiansheng Wang, Penghui Yang, Yiwen Tang, Yuhang Tang, Shuai Liang, Songyi Zhu, Ziqin Xiong, Yifei Su, Xinyi Ye, Jianan Li, Yan Ding, Dong Wang, Zhigang Wang, Bin Zhao, Xuelong Li
    

*   论文链接：https://arxiv.org/pdf/2502.18041
    

*   项目主页：https://shailab-ipec.github.io/openfly/
    
*   数据集下载链接：https://opendatalab.com/liujunli\_1/OpenFly
    

主要贡献
----

  

*   论文开发了**自动化工具链OpenFly**，用于生成空中视觉语言导航的数据，集成了多种渲染引擎，能够高效地生成多样化和高质量的数据。
    
*   构建了包含10万个轨迹的大规模**空中视觉语言导航数据集**，覆盖了18个不同的场景，提供了丰富的环境多样性。
    
*   提出了**基于关键帧感知**的空中视觉语言导航模型OpenFly-Agent，能够有效地处理视觉冗余并提高导航性能。
    
*   通过**广泛的实验**，验证了所提方法和数据集的有效性，并建立了空中视觉语言导航任务的基准，展示了其在多个任务上的优越性能。
    

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIV1TjTEA392v4spGTXeZwxCMiarXLxC5ibr8S0XTkS4znnAZiaV2L5YjqA/640?wx_fmt=gif&from=appmsg)

研究背景
----

### **研究问题**

室内视觉语言导航（VLN）已经被广泛研究，而室外空中VLN仍然是一个未被充分探索的领域。

主要原因在于室外空中视野覆盖范围广，数据收集更具挑战性，导致缺乏基准数据集。

因此，论文主要解决的问题是如何在室外空中环境中进行VLN。

### **研究难点**

该问题的研究难点包括：

*   数据多样性不足、数据收集效率低、数据规模小；
    
*   现有的方法依赖于AirSim和Unreal Engine（UE），限制了数据的多样性；
    
*   数据收集过程依赖飞行员操作无人机并在模拟器中进行手动标注，效率低下且难以扩展；
    
*   当前的数据集规模较小，仅有约10k条轨迹，远不及其他领域的数据集。
    

### **相关工作**

*   **模拟器用于具身AI**：
    

*   介绍了多种用于具身AI研究的模拟器，如MuJoCo、Habitat、PyBullet、Matterport3D、OpenAI Gym和Isaac Gym。
    
*   这些模拟器主要用于室内机器人操作和导航，而不适合空中视觉语言导航（VLN）任务。
    
*   Gazebo和AirSim是常用的无人机模拟器，但存在兼容性和维护问题。
    

*   **视觉语言导航数据集**：
    

*   回顾了多个VLN数据集，包括R2R、RxR、TouchDown、REVERIE、CVDN等，这些数据集主要用于室内或地面导航。
    
*   最近的研究开始关注空中VLN，如ANDH和CityNav，它们分别使用鸟瞰图像和地理信息来辅助导航。
    

*   **视觉语言导航方法**：
    

*   讨论了VLN方法的进展，包括基于图的方法和LLM驱动的方法。
    
*   这些方法在连续环境中进行导航时面临挑战，特别是在空中VLN任务中，研究者提出了前瞻性引导和空间推理技术来应对这些问题。
    

OPENFLY数据生成平台
-------------

该平台通过集成多个模拟器和设计工具链来实现自动化的数据生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIUKkyqWHOkks5sjWKrpaVLiaN2RVGicIAdM7uDD9SkzPm9CbJgwxAYPMA/640?wx_fmt=png&from=appmsg)

### **模拟器和数据资源**

为了收集高质量和现实的模拟数据，平台从多个渲染引擎和模拟器中获取数据。具体包括：

*   **Unreal Engine + AirSim/UnrealCV**：
    

*   Unreal Engine（UE）提供高度真实的交互式虚拟环境。
    
*   平台使用UE5和UE4中的多个场景，涵盖多种城市景观和建筑风格。
    
*   AirSim是一个开源的无人机模拟器，通过UnrealCV插件与UE4集成，用于从无人机视角获取图像数据。
    

*   **GTA V + Script Hook V**：
    

*   GTA V是一个开放世界的游戏，提供高度真实和动态的虚拟环境。
    
*   通过Script Hook V库，平台能够控制虚拟代理以收集所需的数据。
    

*   **Google Earth**：
    

*   Google Earth软件结合卫星图像、航空照片和GIS数据，提供四个城市场景。
    
*   Google Earth Studio用于创建自定义视频，自动绘制飞行轨迹。
    

*   **3D Gaussian Splatting**：
    

*   3D GS是一种高度真实的重建方法，适用于渲染大规模区域。
    
*   平台使用该方法重建五个大学校园的场景，并通过SIBR viewers进行可视化。
    

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIrt1bWGB9QIVcIBg08j1pp5DhxyKRDdq6q3DJ0R5EAmgZWBLIqnib4LQ/640?wx_fmt=gif&from=appmsg)

  

### **自动数据收集工具链**

为了实现自动化数据生成，平台设计了三个统一的接口和一个工具链，包括：

*   **统一接口**：
    

*   **Agent Movement Interface**：设计了一个坐标转换模块，统一所有模拟器的坐标系统。
    
*   **Lidar Data Acquisition Interface**：集成不同的点云数据获取方法，确保数据对齐。
    
*   **Image Acquisition Interface**：整合HTTP RESTful和TCP/IP协议，允许从任意位置获取图像数据。
    

*   **3D点云获取**：提供两种方法来重建整个场景的点云地图，包括栅格化采样重建和基于图像的稀疏重建。
    
*   **场景语义分割**：对四种类型的模拟场景进行语义分割，使用3D场景理解、点云投影和轮廓提取等方法。
    
*   **自动轨迹生成**：利用点云图和分割工具生成无碰撞的轨迹，采用A\*路径搜索算法和基于网格的路径搜索方法。
    
*   **自动指令生成**：提出了一种基于大模型（VLM）的高度自动化的语言指令生成方法，减少手动标注的成本并提高数据集的可扩展性。
    

  

### **质量控制**

平台还包括数据过滤和指令优化步骤，以确保数据质量和一致性：

*   **数据过滤**：移除损坏或低质量的图像，排除无人机穿过树木模型的轨迹，以及去除过短或过长的轨迹。
    
*   **指令优化**：使用NLTK库简化指令，检测并合并相似描述，减少冗余信息。
    

数据集分析
-----

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uItCZGcicym6uz6rthd9icW90UCq0GTIoGmNSMgpEiaUo3cU1eIaNnET8Dg/640?wx_fmt=jpeg&from=appmsg)

### **概述**

OpenFly数据集通过工具链收集了10万个轨迹，每个轨迹都配有相应的图像序列和语言指令。数据生成过程中设定了最小运动步长为3米，以产生更细粒度的轨迹。数据集的特点包括：

*   **轨迹数量**：显著多于现有的VLN数据集。
    
*   **词汇量**：拥有更大的词汇量，提供了更丰富的指令描述。
    
*   **环境多样性**：涵盖了多种不同的场景和环境。
    
*   **轨迹长度和指令长度**：平均轨迹长度和指令长度相对较短，旨在符合人类用户的实际使用习惯。
    

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIiaIN01kOKCH1aMoH8rBNOIOEswEgV6IjibbeSsEtJXaFA75jtmfta1Ig/640?wx_fmt=jpeg&from=appmsg)

### **轨迹分析**

除了丰富的场景多样性，数据集还努力在轨迹的难度级别、长度和高度上实现多样化：

*   **难度级别**：根据轨迹中的动作数量将轨迹分类为“简单”、“中等”和“困难”。例如，少于30个动作的轨迹被归类为“简单”。
    
*   **轨迹长度和高度**：轨迹长度范围从0到300米，飞行高度从0到150米不等。这种广泛的分布有助于训练模型应对不同复杂度的任务。
    
*   **动作分布**：在大型户外场景中，前进动作的比例自然较高。为了缓解模型对主导动作的过度拟合，将“前进”动作分为三种粒度（3米、6米和9米），并在轨迹中合并连续的“前进”动作。
    

OPENFLY-AGENT
-------------

介绍了OpenFly-Agent的设计、架构及其在视觉语言导航（VLN）任务中的应用。

### **数据集划分**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIVs2rbIwrjOCXHzzmSyYzuITqFDicmKib3TFCYIIWxjddkvR5U7Zib82zA/640?wx_fmt=jpeg&from=appmsg)

数据集被划分为三个部分，以便在不同的数据子集上评估模型的性能：

*   **训练集（Train）**：
    

*   主要用于模型的训练。训练集包含来自多个场景的轨迹，其中大部分来自Unreal Engine，因为它提供了最多的场景。
    
*   具体的轨迹数量根据场景的面积进行采样，以确保数据集的平衡性。
    

*   **测试可见集（Test-seen）**：
    

*   用于评估模型在已知场景中的表现。测试可见集包含从训练集中未使用的场景中均匀采样的轨迹。
    
*   这样可以确保模型在未见过的场景中进行测试时，仍能表现出色。
    

*   **测试不可见集（Test-unseen）**：
    

*   用于评估模型的泛化能力。测试不可见集包含从未在训练集中出现过的场景中的轨迹。
    
*   这有助于验证模型在新场景中的适应性和鲁棒性。
    

### **问题定义**

*   在视觉语言导航任务中，无人机的初始位置和姿态被随机设定在一个3D环境中。
    
*   无人机通过其自带的摄像头感知周围环境，并根据自然语言指令进行导航。
    
*   任务的目标是预测下一个导航动作，这些动作可以是前进、转向、上升、下降或停止。
    

### **模型架构**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIzDiaEPynS0CZTSo1wevN8to5hFwBuLXb2nbakVIgzUc37OUSoX5lQlw/640?wx_fmt=png&from=appmsg)

OpenFly-Agent基于OpenVLA模型进行扩展和改进，采用了端到端的架构。主要特点包括：

*   **关键帧选择**：
    

*   为了减少视觉冗余并保持关键信息，模型采用关键帧选择策略。
    
*   通过检测无人机的运动变化点来识别关键帧，确保包含关键地标的信息。
    
*   具体来说，模型通过绘制无人机的轨迹曲线，并在波峰附近选择帧作为候选关键帧。
    
*   然后，使用场景分割图来检测关键地标，确保选定的帧包含重要的导航信息。
    

*   **视觉token合并**：
    

*   为了减少计算负担，模型采用视觉token合并策略。
    
*   通过计算参考图像和后续图像之间的相似性，合并相似的视觉token。
    
*   具体来说，模型在每个关键帧集合中选择一个参考帧，并计算其与后续帧之间的余弦相似性。
    
*   相似的视觉token通过平均处理进行合并，以减少冗余信息。
    

*   **动作预测**：
    

*   模型定义了六种无人机动作：前进、左转、右转、上升、下降和停止。
    
*   每种动作被离散化为多个区间，模型输出映射到每个动作类型的区间，以预测飞行动作。
    
*   具体来说，“前进”动作有三个不同的单位（3米、6米和9米），而“左转”和“右转”的单位是30度，“上升”和“下降”的单位是3米。
    

实验与分析
-----

### **实现和训练细节**

*   **模型组成**：
    

*   OpenFly-Agent由Dino-SigCLIP（224 x 224像素）作为视觉编码器和预训练的Llama-2（7B）作为语言模型组成。
    
*   视觉token通过投影层与文本嵌入对齐后输入到Llama-2模型中。
    

*   **视觉token处理**：
    

*   当前帧保留256个视觉token，所有历史关键帧压缩为一个token。
    
*   历史记忆库的容量设置为2。
    

*   **动作预测**：使用词汇表中最后256个特殊token表示动作，每个动作类型被离散化为多个区间，用于预测。
    

### **评估指标**

*   **导航误差（NE）**：测量无人机最终停止点与目标位置之间的平均偏差。
    
*   **成功率（SR）**：成功任务的比率，定义为无人机在目标20米范围内停止的任务比例。
    
*   **Oracle成功率（OSR）**：如果轨迹上的任何点在目标20米范围内，则认为任务成功。
    
*   **路径加权成功率（SPL）**：根据实际执行路径长度与目标路径长度的比例加权的成功率。
    

### **结果分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIsNOmqJVnzC3pWdfEKaD3TIcqqA3sxlo57Avu6fcfqyPp0xQCygbZWQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uILe8UvsOgVPrbQ1CUs6CcKc9DzSHQ6ofPwYYRJicOM4xur1nAAgDgiaXA/640?wx_fmt=jpeg&from=appmsg)

*   **定量结果**：在测试可见集和测试不可见集上测试OpenFly-Agent，并区分容易、中等和困难的样本。与其他VLN方法相比，OpenFly-Agent在所有难度级别上均表现出最佳性能。
    

*   **Test-seen**：OpenFly-Agent在各个难度级别上均优于其他方法，显示出强大的视觉语言导航能力。
    
*   **Test-unseen**：尽管所有方法的性能都有所下降，但OpenFly-Agent仍然表现出一定的泛化能力。
    

*   **定性结果**：
    

*   展示了OpenFly-Agent的成功导航案例和失败案例。
    
*   成功案例中，模型能够根据指令成功导航至目的地；
    
*   失败案例中，模型可能未能正确识别地标或输出错误的动作。
    

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIaxSsx3TRl9NOAt9XbKuhqgBhiaBCxzgeyGnoun94ASPlz1V8KQyes3w/640?wx_fmt=jpeg&from=appmsg)

### **消融研究**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWk7Hxe4dSlRKdicwMG3H7uIuPmZ9kKDd2rxuicFHSpLYPYOw8m11tnEn0ibUqOT7oMlRL9QicLNbkZOA/640?wx_fmt=jpeg&from=appmsg)

  

*   评估关键帧选择和视觉token合并对模型性能的影响。
    
*   结果表明，关键帧选择和视觉token合并策略显著提高了模型的成功率。
    

总结
--

*   论文提出了OpenFly平台，用于大规模数据收集和室外空中VLN任务。
    
*   OpenFly集成了多种渲染引擎，生成了多样且高质量的数据。
    
*   提出的OpenFly-Agent模型在多个评估指标上表现优异，验证了其有效性，并为未来的空中导航研究提供了一个全面的基准。
    

本文仅做学术分享

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END

  

**相关阅读：**

  

  

[MinerU教程第二弹丨MinerU 本地部署保姆级“喂饭”教程](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

[2025-05-16](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUUOH1ib8viafCJ0mFGr96SWphia1CXYlB7PYcd0mOyDymiaPiboxic4YrUJMsYFiaqZ4mJWtY8VxpqumSuQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[2025-05-09](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2DfiaWj7tD6u36J9MUptoIn8mjrdEE46UKxxIePWjHAujAAXkRVZR4rA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[用“万卷·丝路”数据集打造阿拉伯语版DeepSeek（附免费算力与教程）](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[2025-05-07](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVVE4CUaZgloMDBwxJp0ZKlqtIEr8eYASLlgX0y2BK3sIyyrE5SErdqfyR4wCyo1Sng8m0ibNA46Qw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[MinerU 偷偷放大招！3大新功能上线、模型重磅升级，解析效率超级加倍……](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[2025-04-14](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUBlUJUFkG3acE1KjtVb7X1jUoqEZqSTu6b1NHzoPYiaicQjBaQ6NCG78GYurSgtzE1ITE3Q4WCux1Q/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[多语言语料库“万卷·丝路”发布，AI赋能共建“一带一路”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[2025-01-09](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXk2oA4FMPVDMdcDVCU27qrcoZJcm8XvX9zEvQMy5Nico74zGOeIyvq1Doc1Zr5ly2RYm8TavQR3rg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言