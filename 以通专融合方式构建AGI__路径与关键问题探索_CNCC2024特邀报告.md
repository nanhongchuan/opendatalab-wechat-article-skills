     以通专融合方式构建AGI——路径与关键问题探索｜CNCC2024特邀报告 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

以通专融合方式构建AGI——路径与关键问题探索｜CNCC2024特邀报告
====================================

原创 OpenDataLab 2024-12-03 17:45 上海

> 原文地址: [https://mp.weixin.qq.com/s/rFz2WB1vvrqTlKp0OvN9Nw](https://mp.weixin.qq.com/s/rFz2WB1vvrqTlKp0OvN9Nw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

2024年10月25日，上海人工智能实验室主任、首席科学家周伯文教授在CNCC2024大会发表特邀报告，分享了以通专融合方式构建AGI的路径与关键问题探索。

  

自2016年以来，周伯文教授及其团队持续深入研究AGI的实现路径（2024年7月，周教授曾在世界人工智能大会暨人工智能全球治理高级别会议上做[**“通专融合是通往AGI的战略路径”**](https://mp.weixin.qq.com/s?__biz=MzkzNzIyNDg4MQ==&mid=2247557862&idx=3&sn=50ce34cd2b6b4c56c15b42b7d6d4747d&scene=21#wechat_redirect)报告）；当前，面对大语言模型在Scaling Law与架构等方面的技术瓶颈，周教授及其团队不仅提出了完整的AGI实现路径，更创新性地从应用价值出发，探索更高效发挥AGI潜力的场景与方法。

  

本文详细介绍了这一原创性路径及其技术研究，为AGI的未来发展提供新的纵深视角与实践参考。

  

**人工智能突破从哪里来，未来向何处发展？**

前沿学者们对大语言模型的能力边界进行了持续讨论。例如，图灵奖得主Yann LeCun常提及，机器学习目前存在诸多短板，他的研究偏重泛化性，关注如何尽量达到人类的智能。而DeepMind强化学习团队负责人David Silver提到，要做到Superhuman Intelligence（超人类人工智能）以及发现更多新知，大语言模型尚且存在局限，仍有许多工作有待完成。在这里，他强调的是如何在一些专业领域实现Superhuman Intelligence，并不是具备更强的通用能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQWqjJ401RO8ASyibYApaG4FiaOQ8h2vFcf7wQquK3TWZHQ8vaAV5cw1jA/640?wx_fmt=png&from=appmsg)

因此，在当下这一时间节点，探讨AGI的实现方向及其关键问题，具有重要的意义。

我最早对AGI发展路径的思考作公开分享是在2016年，当时我正担任IBM总部的人工智能基础研究院负责人。在那一年的Town Hall Meeting上，我提出人工智能的发展会经历三个阶段，分别为**狭义人工智能（ANI）、广义人工智能（ABI），以及通用人工智能（AGI）**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQIPw17LWfUaZrBb72HBn9LHdQhmoRZGx5O6LxyVTA9W9pFrmp1qDyhA/640?wx_fmt=png&from=appmsg)

周伯文教授在2016年提出，人工智能的发展会经过ANI、ABI、AGI三个阶段

当时我的判断是，基于深度学习的监督算法仅能实现狭义人工智能，因其在任务间的迁移和泛化能力极为有限，并且需要大量标注数据。另一方面，2016年，AGI还是非常模糊的愿景，全世界只有极少数研究者谈论，我个人当时给出AGI的定义是比人类更聪明，会独立自主学习，并且一定需要更好地治理和监管——这点非常明确。但怎样从狭义人工智能走向AGI，我判断中间有一个必经阶段，并将其称之为ABI，即广义人工智能。

这应该是ABI概念被首次提出，因此我也给出了三个必备要素的定义：即自监督学习能力、端到端能力，以及从判别式走向生成式。尽管2016年时狭义人工智能进展明显，但因为判断其能力存在上限，我当时呼吁AI研究者尽快从狭义人工智能，转向探索广义人工智能。

回过头看2022年底出现的ChatGPT，以上三个要素基本都已具备，所以可以认为基于Scaling Law的大模型较好地实现了广义人工智能。但当时我本人未曾预料其具备如此强大的涌现与零样本学习能力，尽管我曾提到ABI应该具备优秀的小样本学习能力。

认知决定行动，行动取得结果，有了上述判断，我的团队在2016年转向广义人工智能研究，开始思考如何让模型更好地泛化，随后在2016年底提出了**多头自注意力机制的原型**（A Structured Self-attentive Sentence Embedding, https://arxiv.org/abs/1703.03130），并首先应用在与下游任务无关的自然语言表征预训练中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQKLs2ydNQicUIs75kib29rQicz8faXPfv19hIWII6yr2vpJ0gB1t9Uhxqw/640?wx_fmt=png&from=appmsg)

研究团队认为，模型在思考过程中能更灵活、多样、有效地使用元动作，是模型在推理阶段能够利用更多思考时间解决更复杂任务的重要原因。

Transformer完善了多头自注意力架构，但其价值的放大，来自于OpenAI的研判。OpenAI发现并认为，基于多头自注意力架构用于预测下一个词，由此训练出来的大语言模型是目前最好的世界知识压缩器。站在2019-2022年的视角,这个认知非常前沿，是实现压缩智能的基础。我们可以认为Transformer和GPT代表的压缩智能是AGI的重要里程碑。

但毫无疑问，仅靠压缩智能远远不能实现AGI。Google DeepMind发表于2023年的论文（Levels of AGI: Operationalizing Progress on the Path to AGI. 2023），将AGI进行了分级。一方面借用了我们提出的从狭义人工智能到通用人工智能对比的概念，另外一方面在专业性上将人工智能分成了6个级别，从不具备AI能力即纯粹编程，到Superhuman Level（“超人类”水平）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQN0YKDJtT6E9WOZoZT5W6YchD4vuPicFAadhSBjm17JnWVwC9fy5mcIA/640?wx_fmt=png&from=appmsg)

Google DeepMind把AGI分为6个等级

可以看出，ChatGPT虽然有很好的泛化性，但在智力水平只属于第一级Emerging Level（“初现”），还达不到第二级Competent Level（“和人类相当”）——后者的定义是超过50%的人类。再往上为Expert（专家级），是指超过90%人类的水平；Virtuoso（魔术师级）是指超过99%人类；而所谓Superhuman（超人类）是指在该领域可以超越所有人类——如同最新版的AlphaFold一样，人类无法在蛋白质折叠这个领域再击败AI了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQlicaBWNZmqceG5cic1lia6056vXc9jVhyVEp1g2HMJUxnnvSpuhYCQYvA/640?wx_fmt=png&from=appmsg)

但类似AlphaFold这种专业性极强的AI，其泛化性往往较为有限。若将泛化性与专业性结合考虑，可以形成一个二维概念框架。我们注意到，ChatGPT和Sora在泛化性方面取得了显著进展，但在专业性方面仅达到人类15%-20%的水平。即便运用Scaling Law（规模律）进一步增加模型参数，其专业性的提升效果并不显著，而成本却显著增加。专业性不足不仅限制了创新，还会导致大量事实错误的出现。

回顾人工智能七十余年的发展历程，我认为实现通用人工智能的路径可被视为一张二维路线图：横轴代表专业性，从IBM的深蓝到DeepMind的AlphaGo，在横轴方向（专业性）上取得了显著进展；但这些工作的泛化性一直较为薄弱，限制了AI技术的进一步普及。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQHKqVIXXoh7bYANsibmt8ic2Rk0LP1uIkWcibgpj8Ebg7xIiaHAGGSMPwjA/640?wx_fmt=png&from=appmsg)

而从2016年多头自注意力，到Transformer、ChatGPT出现，压缩智能代表的是泛化性狂飙。但可以看出，它在专业性上的水平进展极其缓慢，Scaling Law很明显不足以延伸它的专业性，能力长期停留在level 1的左侧。

未来人工智能应当如何发展，并推动更大的价值创造？从2022年底，我在多个场合讲过，存在一个高价值区域，这个区域在横轴应达到或超过90%以上专业人士的水平。同时又具备能达到广义人工智能级以上的泛化能力，以极低成本在不同任务之间进行迁移。这个区域，即是AGI路线图中的“高价值区域”。

这个区域离这张路线图出发最近的点，我称之为**通专融合引爆点**。是否存在一种路线，从当前技术出发，能更快地接近通专融合引爆点？我认为存在这样的路线，并将其称为**通专融合技术路线**。

虽然我们看到此前OpenAI一直都是在Scaling Law的泛化性上持续推动，但今年也开始朝专业性方向迭代。从GPT-4o之后，将很多精力投入“草莓”系统的研究，开始沿着与通专融合相似的方向发展。

关于通专融合的目标，一方面，随着合成数据飞轮效应的加速，过去一年基础模型获取通用能力的难度显著降低；另一方面，在世界知识的压缩能力上，开源模型的性能已无限逼近闭源模型。然而，不管是开源还是闭源模型，在专业化能力方面仍存在显著瓶颈。例如，在实际的软件工程环境中，GPT-4仅能解决GitHub中1.74%的人类提出的问题。即便通过引入大量工具、结合基础模型与工具型Agent的方式，这一比例也仅提升至13.85%。

可以看到，目前对于世界知识进行压缩的智能发展路径正在自然演进，但我们认为在这之上的专业能力，才是现阶段AGI皇冠上的明珠。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQWbyDxgwhibvNsYCsgg9rs8nV7mS2dG17GtQLLA52CumN0hgZ0bf4fmA/640?wx_fmt=png&from=appmsg)

  

**通专融合AGI实现路径**

我们提出的通专融合，不仅需要同时具备专业性和通用泛化性，还必须解决任务可持续性的问题，来让人工智能能高效地可持续发展，它们形成了通专融合技术挑战的三个顶点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQg6AouoUucBmDjUEicGccjImiaqZjftbl2V597wqo8Ywsd1smbnb1j0OQ/640?wx_fmt=png&from=appmsg)

“通专融合”必须实现“通用泛化性”“高度专业性”“任务可持续性”三者兼得

自2023年初以来，我们提出了具体的**通专融合实现路径**（Towards Building Specialized Generalist AI with System 1 and System 2 Fusion，https://arxiv.org/abs/2407.08642），该路径需要三个层次相互依赖，而非仅依靠单一模型或算法。对每一层我们都有整体规划与具体技术进展，不过由于时间关系不能一一展开，下面简要描述每一层的核心思想，以此完成对通专融合技术体系的拆解。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQPXsn9OOLJcOgjFia8gmibLGgSe946cke53OsY7Nn0lRa5U2qZrpliaqmA/640?wx_fmt=png&from=appmsg)**

路径的第一层是“基础模型层”，这一层需要大量工作来改变现有架构。其中，最重要的是如何实现知识与推理的有效解耦与组合，同时实现高智力密度的监督信号，并在架构方面实现长期记忆——目前Transformer难以实现长期记忆，通过改变现有架构，AI能够获得强大的泛化性和迁移能力。

在基础模型的能力之上，具备通用的架构和学习能力，还需要高效的学习方法，才能更好地实现通专融合，这便进入了第二层“融合协同层”。自2017年以来，我们提出“系统1”和“系统2”（即“快思考”和“慢思考”）的动态融合，以解决更多问题。

两种思考方式的动态融合最接近人类大脑的思考方式，也是从能耗和泛化角度而言最佳的方法。这里可以进一步延伸至多智能体协同，它不仅仅是单个系统1或系统2，多个智能体的协同在群体层面产生智能涌现，必须具备复杂任务的规划能力。在融合协同层，需要脱离目前基于统计相关性的推断，转向因果推断，这是避免大模型能力瓶颈的有效方法。

我们已经认识到，“压缩智能”并不代表所有智能。正如人类看再多的书和视频也无法学会游泳一样，要获得关于游泳的智能，就必须与物理世界互动，让物理世界的反馈影响肌肉记忆，直至大脑皮层。这种反馈自主学习与发现，就是我们所说的第三层“探索进化层”，这层的关键在于高效地获取反馈和奖励，即从真实环境中获得可持续、高置信的反馈信号。同时，我们还需要跨媒介可交互的世界模型来对物理环境进行建模。

  

**通专融合关键技术**

**1、基础模型层的进化方向**

高密度监督信号是专业化知识注入的关键。在基础模型层，必须高效引入高智力密度监督信号。在压缩智能学习方式下，容易让人误以为只需给出下一个词作为监督，模型就能高效学习。然而，这种学习方式在很多情况下只能让模型学会一种“快捷方式”（Shortcut），它知道如何找到最佳答案，但对于“为什么这是最佳答案”，则缺乏系统化的思考。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQQUXMQsUBuQPlao7cUYjWvJOicj8T7sGqAAkvy8hJPofibjzXnqdeYtwA/640?wx_fmt=png&from=appmsg)**

基于这一原因，在直接偏好优化阶段，我们提出了带有观测、批评、修改循环流程的树状偏好数据构建方法。在每个推理阶段，给模型提供多个选择并给出优先级，通过更高密度的监督，使模型在推理过程中学会更多可替代性的比较（Advancing LLM Reasoning Generalists with Preference Trees，https://arxiv.org/abs/2404.02078）。该方法在OpenAI o1亮相前已公布，仔细研究会发现它采用了类似的高智力密度监督推理过程。这是为模型注入专业化知识的关键。

何为“专业”与“不专业”？前者意味着始终能在多个选择中找出最佳答案；而后者则仅能做出“最佳猜测”，常被其他待选项所混淆。（11月25日，上海AI实验室推出了能够自主生成高智力密度数据、具备元动作思考能力的[**强推理模型书生InternThinker**](https://mp.weixin.qq.com/s?__biz=MzkzNzIyNDg4MQ==&mid=2247559051&idx=1&sn=f189f750895fc8ce197f739ea81d7656&scene=21#wechat_redirect)。该模型能在推理过程中进行自我反思和纠正，从而在数学、代码、推理谜题等多种复杂推理任务上取得更优结果。）

除了当前的主流结构外，高效的知识推理可组合可分离的架构更有利于构建可信赖、泛化、扩展的大模型。布罗德曼分区（Brodmann area）是神经科学里面公认对大脑不同区域承担不同专业功能的分区架构。我们寻找的架构，应具备知识应用可信赖、推理过程可泛化、知识内容可拓展三种性质，同时能够有效地进行组合。Transformer的一个优点在于，可实现推理与知识的高度融合，拥有很大的提升空间。但缺点也在于当知识和推理高度融合之后，一旦模型产生幻觉，将很难溯源。所以寻找一种新的架构极其重要。

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQ3G6c6JXibkghiaWHgvmKqsJLdXh0B8vh7t0MIYcIibhUvc4WIMyfLUwXw/640?wx_fmt=png&from=appmsg)****

长期记忆机制是通专融合的中间桥梁，需要这样的机制在通用与专业能力之间架起一座兼容桥梁。目前，这种长期记忆机制在Transformer架构中的表现并不充分，这方面我们有一系列工作（如我2015年的研究https://arxiv.org/abs/1510.03931，以及近期的工作https://arxiv.org/html/2408.01970）。

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQibYQjVusRV5vLkyZriagfToB5iaSBQvw0x2bUC8rSFgDccsx7eq5l8u0Q/640?wx_fmt=png&from=appmsg)****

**2、融合协同层**

通专融合路径的第二层是融合协同层，特别强调快速处理和深度推理结合。在CVPR 2024收录的论文中，我们探索了这一领域（Interactive continual learning: Fast and slow thinking）。我们构建了一个高效识别图像的快系统（专用系统），当其遇到不确定的情况时，会将信息传递给一个更强大的慢系统（通用推理系统）。慢系统基于输入信息进行深度分析，并将结果反馈给快系统并在快系统中完成了一个结构化长期存储的更新。这种结合不仅降低了能耗，还提升了处理速度和准确率。

这种结合在处理速度和能耗上优于单独使用慢系统。许多问题快系统可自行回答，无需调用慢系统。此外，我们发现这种结合的准确度高于单独使用快系统或慢系统，这一发现颇具启发性。其潜力在于，快系统缺乏深度思考，易犯错；而慢系统对具体情况的判断不如快系统，许多细节不了解。通过快系统的输入，慢系统可排除不可能情况，做出更好判断。

快系统好比前线侦察员，提供具体输入信息；慢系统则相当于后方指挥官，具有更好的思考深度和判断能力。两者结合，可做出更准确高效的决策。这种结合不仅是简单叠加，而是深刻互动和理解。快系统从慢系统的输出中学习，并形成长期记忆；慢系统从快系统的输入中获得专业判断和背景。

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQDQll4uOLuKMpyE4mFYzPyn3BHwmF8p5yLapmrrqxCxCHSLxxvyCYicw/640?wx_fmt=png&from=appmsg)****

上述系统不仅适用于图像识别，我们还尝试把将其应用于自然语言生成，让这样一个通专融合架构生成非常专业化的描述文字，例如某种疾病治疗方法、具体商品的营销策略等。我们发现，专业模型承担了大部分任务。如下图所示，蓝色部分是专业模型生成的，红色部分则是专业模型“求助”通用模型进行泛化推理之后产生的。80%的内容由专业模型独立完成，而20%的慢推理对提升专业模型的泛化性有非常大的帮助（CoGenesis: A Framework Collaborating Large and Small Language Models for Secure Context-Aware Instruction Following. 2024）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQjmt0OZL1tR81C5ObjKdk16vE4hE10H6neqWr2MOSb810WibVl2CV3Ug/640?wx_fmt=png&from=appmsg)

针对专业化个性内容生成任务，通用大模型仅对其中约20%的内容有贡献（纲要内容/推理能力，红色token），剩下80%内容则主要依赖专业化小模型生成（蓝色token）

**3、探索进化层**

正如前面提到，人类学会游泳必须与真实物理世界互动，AI也是如此。在这一层，我们尝试进行模型与环境长期实时交互，并进行具身自主探索与世界模型构建。比如上海人工智能实验室提出了开源且通用的[**自动驾驶视频预测模型GenAD**](https://mp.weixin.qq.com/s?__biz=MzkzNzIyNDg4MQ==&mid=2247555169&idx=1&sn=87058efccb357ac663080d391e595f24&scene=21#wechat_redirect)，类似于自动驾驶领域的“SORA”，能够根据一张照片的输入，生成后续高质量、连续、多样化、符合物理世界规律的未来世界预测，并可泛化到任意驾驶场景，被多种驾驶行为操控。

在与物理世界的互动探索中，一方面我们深入物理世界，另一方面则在虚拟世界中通过模拟进一步提升效率。如具身智能训练，我们实现了在单卡上模拟训练一小时，相当于在真实物理世界训练380天的效率。这些成果通过[**首个城市级具身智能仿真训练场浦源·桃源**](https://mp.weixin.qq.com/s?__biz=MzkzNzIyNDg4MQ==&mid=2247558068&idx=1&sn=1e1f82f332fe35c204cd01bf2e3052c8&scene=21#wechat_redirect)进行了开放，欢迎大家在这个平台上训练专属的具身智能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQ6l4PN5qZHTUzyEGAoNnavBWJacIGZgk7Y7k3smLYtHd8iclR8GVMbSQ/640?wx_fmt=png&from=appmsg)

**通专融合实践：科学发现**

2023年1月5日《Nature》发表的封面文章《Papers and patents are becoming less disruptive over time》，文章提到，过去70年来论文数越来越多，专利数越来越多，但单篇论文的影响力却逐年下降，这不仅仅出现在计算机领域，也适用于生物、物理、化学等领域。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQp1ydTvRibSeatTlqptian9UuAl9ERdPjmQV6CEzzmdeyOHg4Qv7SFtvg/640?wx_fmt=png&from=appmsg)**

这篇论文只做了数据分析，没有追溯原因。对此我的个人思考是，该现象与科学发展规律密切相关。科学经过100余年的建设，已建成趋于完美的大厦，在大厦内部，每门子学科形成了非常强大的信息茧房，茧房间壁垒高，茧房内信息过载，所以导致论文与以前相比很难产生更广泛的影响力。

解决这一问题，还需要对科研的组织方式和适配性进行适当调整。与此同时，也需要科研工作者与时俱进，用好AI新工具。

我们有没有可能通过人工智能在技术层面帮助科学家获得更多突破？例如，人工智能的通用能力可以帮助人类解决信息壁垒太高的问题——因为人类的信息容量是有天花板的。茧房的信息过载的问题，则可以通过人工智能系统深度思考突破。所以，**通专融合是解决科学创新，开创下一代科学创新范式必须具备的能力**。

关于使用大模型开展科学创新，目前存在诸多问题，例如不确定性和幻觉。不过原OpenAI联合创始人Andrej Karpathy认为，这种不确定和幻觉一方面可以被认为是大模型目前的不足，但另一方面则更像一个特性而非缺陷，这种幻觉与创造性相关，模型的幻觉可以与人类做梦类比。

在科学历史上，德国有机化学家August Kekul梦见衔尾蛇，进而发现苯环结构。这种发现的过程，从某种意义上讲，与大模型的幻觉具有很强的相似性，关键在于如何把幻觉的创造性用好，利用大模型的这种特点发挥价值。

基于这些思路，我们过去几年来开展了一系列的工作，比如我们认为大语言模型是非常有效的零样本（Zero-shot）科学假设的提出者。所谓零样本就是大模型可以提出全新、原创的科学假设。不一定像牛顿三大运动定律那样具有划时代意义，但模型确实能提出一些科学家没有发现和观察到的现象（如我们2023年的工作Large language models are zero shot hypothesis proposers以及近期工作UltraMedical: Building Specialized Generalists in Biomedicine）。例如，我们构建的全自动蛋白质组学知识发现系统Proteus能结合真实的蛋白质组学数据，独立发现了191条经过专家评估的、具有自洽性、逻辑性和创新性的科学假设（https://arxiv.org/abs/2411.03743）。

在相关的工作中，我们验证了通专融合大模型能够提出有效的科学假设。如果把通专融合再进一步延伸至多智能体，我们发现，具备通专融合的系统，可以在科学研究的全生命周期过程中发挥不同的作用，并可与人类科学家进行配合。

我们进而提出了“人在环路大模型多智能体与工具协同”概念框架，用以模仿人类科研过程。通过构建AI分析师、工程师、科学家和批判家等多种角色，同时接入工具调用能力来协同提出新的假设，并进一步将人类专家纳入其中，借助“人在环路”挖掘人机协同的潜力。实验结果表明，这一框架能够显著提升假设发现的新颖性与相关性等多个维度指标（Large Language Models are Zero Shot Hypothesis Proposers. NeurIPS 2023，https://arxiv.org/abs/2311.05965）。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQ4HM5GgTStlmONzcCcA7DQUVHzH3icrficibvDHbHt5DZficDrzPVYph1NQ/640?wx_fmt=png&from=appmsg)**

早在1900年，德国数学家大卫·希尔伯特（David Hilbert）提出了著名的“23个问题”，引领了数学多个子领域数百年的发展。无论是希尔伯特还是爱因斯坦，他们都谈到过，提出科学问题，远比解决问题更重要。我们希望通专融合的AI系统，能帮助各个领域出现更多希尔伯特。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQIm7hI8VTbX91NUmPw454YibMFO0IjelUpfaWkoWHq77O6zlGm5sVR6Q/640?wx_fmt=png&from=appmsg)**

**展望：AGI的中心法则？**

分子生物学中，有一个被称为“中心法则”的概念，1958年由诺贝尔奖得主佛朗西斯·克里克（Francis Crick）首次提出，明确了遗传信息从DNA传递到RNA，再从RNA传递到蛋白质的过程。这一法则不仅深刻揭示了生命现象的本质，也为之后的生物技术发展提供了方向指导。随着科学研究的深入，中心法则经历了多次修正和完善，逐渐成为分子生物学的核心理论之一。

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQt2fvc4nhSa07ko9oLIL91t8qlbWL3SkCrRaSOyR12yJulibK2OmuStQ/640?wx_fmt=png&from=appmsg)**

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJF3vg2DX2MxPGxalXiaQBjlQWUoZKAHrWX5UYzOyjiaSjynl5xLDQ1FRpd0M1oGjDJIBvl99iaJfyIpg/640?wx_fmt=png&from=appmsg)****

这一法则令我印象深刻。因为它非常有洞察地揭示和影响着生物领域的各个方面。这进一步引发了我的联想：关于AGI如何实现，此前还未形成一条指导实践的完整路径，我们能否找到一种AGI的“中心法则”？

我在报告中提出的“通专融合”路径，是对这一问题的探索。生物学的中心法则是在几十年研究中不断地迭代更新，很多优秀科学家一同共创，做出了杰出贡献。同理，AGI可能也需要这样来自人工智能研究与其他交叉学科社区的共创。希望本文介绍的思路与相关工作，能为各位读者带来启发。

**感谢姚期智、陈纯、鄂维南、高文、张亚勤教授对本文初稿的审阅与建议。**

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUjQ75AV2KSWpWBNDnOvWkuI2PWW6v7WzBrCcvYPyq27F8SicMPJnLicOA/640?wx_fmt=png)

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言