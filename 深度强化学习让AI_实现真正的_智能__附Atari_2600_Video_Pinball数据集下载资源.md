     深度强化学习让AI 实现真正的“智能”，附Atari 2600 Video Pinball数据集下载资源 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

深度强化学习让AI 实现真正的“智能”，附Atari 2600 Video Pinball数据集下载资源
====================================================

原创 专注于AI 数据的 OpenDataLab 2022-04-29 22:15 上海

> 原文地址: [https://mp.weixin.qq.com/s/38jXHUymLqDYlnOMhWg2OQ](https://mp.weixin.qq.com/s/38jXHUymLqDYlnOMhWg2OQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

提到人工智能应用，你会想到什么？

  

人脸识别、无人驾驶、智能推荐……

  

这期咱们就来聊一聊人工智能任务类型和你可能想不到的深度强化学习。

  

  

  

****01****  

**人工智能任务分类**

人工智能任务类型可分为预测型、决策型2个大类。\[1\]

  

**1. 预测型任务**  

预测型任务主要是根据输入的数据预测相应的输出，或者生成一些有价值的数据实例，他们分别对应着机器学习中的有监督学习和无监督学习系统。上述提到的人脸识别属于预测型任务。  

  

**2.决策型任务**  

决策型任务，是在动态的环境中采取行动或决策。

  

与预测型任务不同，决策型任务并不以训练模型（Model）、输出结果为目的，而是通过智能体（Agent）与环境交互，收集外部反馈，改变自身状态，再根据自身状态对下一步的行动进行决策，在行动之后持续收集反馈的循环，不断获取奖励值，从而学习到“完成目标”的最优策略。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6A2pMuRJYQibG7JzXmsogLykf5kvKIjibhzBaEKyBRE2ibJLm9ALc9QPTt7DicVqNJAG5XHVyIdUFRnQ/640?wx_fmt=png)

强化学习系统基本结构（图源：参考资料\[2\]）

  

机器学习领域的一大核心主题是序列决策。该任务是在不确定的环境中根据经验决定所要执行的动作序列。序列决策任务涵盖广泛，有望对很多领域产生影响，比如机器人、医疗保健、智能电网、金融、自动驾驶汽车等等。

  

而序列问题可以用强化学习解决。

  

  

****02****  

**什么是深度强化学习**

深度强化学习（Deep Reinforcement Learning，DRL）是指结合了深度学习的感知能力和强化学习的决策能力的新机器学习算法。

  

其主要利用深度神经网络进行价值函数和策略近似，从而使强化学习算法能够以端到端的方式解决复杂问题。\[3\]

  

为人工智能实现真正的“智能”提供效果良好的实践路径。  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6A2pMuRJYQibG7JzXmsogLypMm4OjKU1Ijr3frCfsAjbyb0nJX1HFZXnfBI9ROXS9Tic5dqaURoO6g/640?wx_fmt=png)

端到端深度强化学习示意（图源：http://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-1.pdf）

  

  

****03****  

**深度强化学习落地场景**

2013年，谷歌DeepMind 团队创造性地提出深度Q网络（Deep Q-Network，DQN）算法，通过深度强化学习，以Atari 2600中2D视频游戏作为实验环境，在大多数游戏中取得了超越人类玩家的成绩。\[2\]

  

自那之后，市面上涌现出了许多优秀的应用，比如颠覆围棋界的AlphaGo，让无数用户沉浸其中的抖音、淘宝等的推荐算法、战胜专业玩家的游戏AI 、通过模仿和强化学习来提高驾驶能力的Wayve自动驾驶平台……

  

深度强化学习使得机器学习效果较传统方法有了“质”的飞跃，打开了人工智能的“潘多拉魔盒”。

  

目前，游戏AI、无人驾驶、交通灯调度、网约车派单、组合优化、推荐搜索系统、数据中心节能优化、对话系统、机器人控制、路由选路、军事场景均有深度强化学习应用。

  

  

****04****  

**深度强化学习带来的关键变化**

深度学习与强化学习各有特点，将二者结合在一起会带来的改变：\[1\]

● 价值函数和策略变成了深度神经网络；

● 相当高维的参数空间；

● 难以稳定地训练；

● 容易过拟合；

● 需要大量的数据；

● 需要高性能计算；

● CPU（用于收集经验数据）和GPU（用于训练神经网络）之间的平衡。

  

  

****05****  

**深度强化学习数据集资源**

OpenDataLab平台已经上架了经典的深度强化学习数据集——Atari 2600 Video Pinball，并提供了整齐的数据集信息、流畅的下载速度，欢迎大家体验。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6A2pMuRJYQibG7JzXmsogLyaq9jbqad3IdrGmJCjOrSQ6M6sr6SJrKavfxoibSpyA3lQaJCXfrKI9Q/640?wx_fmt=png)

Atari 2600 Video Pinball数据集预览（图源：OpenDataLab）

  

Atari 2600是Atari公司于1977年发布的视频游戏。它包含了一系列热门游戏，例如Breakout，Ms. Pacman 和Space Invaders。\[4\]

  

自从2013年 Mnih等人提出了DQN算法后，Atari 2600已成为测试新强化学习算法的标准环境。由于Atari 2600的高清视频输入（尺寸为210 x 160，频率为60 Hz）以及游戏之间的任务差异，它一直是具有挑战性的测试平台。 

  

Atari 2600环境最初是通过Arcade学习环境（ALE）提供的。OpenAI Gym封装了这些环境，以创建更加标准化的界面。OpenAI Gym提供59种Atari 2600游戏作为环境。研究人员普遍认为雅达利 2600 系列游戏是用于评定 RL 表现的一个很好的基准，因为每款游戏都足以代表一个实际的挑战，而整个系列包含非常多品种，提供足够的多样化。

  

可以通过OpenAI Gym框架中的Arcade学习环境来复制Atari 2600游戏环境。

· 开源地址：

https://www.endtoend.ai/envs/gym/atari/

· 数据集地址：

https://opendatalab.com/83
--------------------------

  

  

  

**参考资料：**

\[1\]https://www.bilibili.com/video/BV1mC4y1H75i?spm\_id\_from=333.337.search-card.all.click

\[2\]郭勤. 基于深度强化学习的视频游戏决策模型研究与应用\[D\].江西理工大学,2018.

\[3\]尹舸帆. 深度强化学习中探索问题的研究和实现\[D\].北京邮电大学,2021.

\[4\]http://turingai.ia.ac.cn/app/detail/14  

  

  

\- End -

  

  

**还有哪些你关心的话题？**

**扫码入群,欢迎交流 ![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6qKD9WCiaOd8HjSjiaMeTBNgCrp5PMqHnMAft2j0rj5bfyIzEajecZWhadWjhISZN7EquicHRHReYiaA/640?wx_fmt=png)** 

最新数据集上架动态

最全数据集内容解读

最牛大佬在线答疑

最活跃的同行圈子

……

  

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7NEyym4C8KBFplT20DM2vqAUAysVwzco8icviaYQ6McYIHep7ythBW0oZic97dXnhS6LbnoyibAqCbLQ/640?wx_fmt=jpeg)

添加小助手微信，发送“入群”，等待邀请

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言