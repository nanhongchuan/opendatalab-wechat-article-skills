     有点意思！腾讯 ARC Lab 最新发布的MiraData数据集，用于长视频生成，从这些方面做了clip分层描述…… \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

有点意思！腾讯 ARC Lab 最新发布的MiraData数据集，用于长视频生成，从这些方面做了clip分层描述……
==========================================================

原创 虹桥北北 OpenDataLab 2024-04-11 19:23 上海

> 原文地址: [https://mp.weixin.qq.com/s/I276Hp-8Y4ljXfug7X8wpg](https://mp.weixin.qq.com/s/I276Hp-8Y4ljXfug7X8wpg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

最近小编网上冲浪时，被腾讯 PCG ARC Lab 新开源的文本-视频数据集——**MiraData** 吸引了目光。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7yjDpC9UfD7vkkDvHm0SibX8smKaTCMxaJWP2DCKUMDcoBDZBqMCF6dywicicOFiaTmWFGCS8HqeWEORVeBb0dyQicA/640?wx_fmt=gif&from=appmsg)

  

这个数据集有多新？Readme在一天前刚更新完的那种，而且数据集有一大特点，是**专门为长视频生成任务设计的大规模视频数据集**，不仅提供了**时长更长**的数据，还从视频主体、背景、风格等不同维度进行了非常详细的**文本“分层”描述**，关注视频生成的小伙伴不容错过！相信一定能给你启发，赶紧和小编一睹为快。

  

**MiraData项目地址：**

_https://github.com/mira-space/MiraData_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****数据集概览****

视频数据集在sora等视频生成大模型中发挥着至关重要的作用。然而，现有的文本-视频数据集在**处理长视频序列**和**捕获镜头过渡**方面往往存在不足。为了解决这些限制，腾讯 PCG ARC Lab 研究人员引入了**MiraData**（**Mi** ni-So **ra** Data），这是一个专门为长视频生成任务设计的大规模视频数据集。

（MiraData 官方Demo Video，来源：Youtube）

  

  

 MiraData 的主要特点

**1\. 长视频时长：**与以前的数据集不同，以前的数据集视频剪辑通常非常短（通常小于 6 秒），MiraData 专注于时长从 **1 到 2 分钟不等**的**未剪辑视频片段**。这种延长的持续时间允许对视频内容进行更全面的建模。

  

**2\. 结构化描述：**MiraData 中的每个视频都附有**结构化描述**。这些标题从不同角度提供了详细描述，增强了数据集的丰富性。描述平均长度为**349字**，保证了视频内容的全面呈现。

  

  

 数据集构成

在这次初始发布的版本中，MiraData 包含 **57,803** 个视频片段，总时长 **1,754** 小时，主要提供**游戏**和**城市/风景探索**两个场景。clip数量和视频时长如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7vkkDvHm0SibX8smKaTCMxa4HXhA0yzpAPF70TKVZqL9twxWsfZkx5lCaJaDWVrh0CFCSv67pQ9Eg/640?wx_fmt=png&from=appmsg)

**2种场景内容**

**● 游戏场景**：包含了丰富的游戏体验相关视频；

**● 城市或自然景观场景**：通过视频捕捉了多样的城市风貌和自然美景。

  

**6种类型的描述**

MiraData 中的每个视频都附有结构化描述，从以下6种不同角度进行了详细地描述，增强了数据集的丰富性：

● **主体描述**（Main Object Description）：描述视频中的主要目标或主体，包括它们在整个视频中的属性、动作、位置和运动。

● **背景**（Background）：提供有关环境或场景的信息，包括物体、地点、天气和时间。

● **风格**（Style）：涵盖艺术风格、视觉和摄影方面，如写实、赛博朋克、电影风格。

● **摄像机运动**（Camera Movement）：详细说明摄像机的平移、变焦或其他运动。

● **简短描述**（Short Caption）：一段简洁的摘要，描述视频的精髓，使用Panda-70M字幕模型生成。

● **密集描述**（Dense Caption）：一个更详尽和详细的、总结了上述五种类型的描述。

  

**举个“栗子”**

看1个官方提供的例子，就明白了，比如这个游戏视频

（开头画面冲击力较强，注意谨慎观看）

  

**描述内容有：**

> **主体描述**
> 
> 从玩家的视角出发，最初与一个对手搏斗，这一点可以从机械部件和玩家手部的特写镜头中得到证实。随后，焦点转移到一位老年女性身上，她最初表现出攻击性或防御性，高举着铲子，好像随时准备出击。接着她转身，带领玩家绕到一个木制结构的侧面，那可能是她的家。随着时间的推移，她的态度变得柔和，看起来像是在和玩家交谈，因为她放下了手中的铲子，姿态变得更加放松。
> 
>   
> 
> **背景描述**
> 
> 背景描绘了郁郁葱葱的乡村环境，有一座木屋或棚屋，周围环绕着绿色植物、岩石和红色花朵。环境具有自然主义的感觉，晴朗的天空和日光表明这是白天的环境。背景中没有可见的其他人物或移动元素，这表明这是一个虽然与世隔绝但平静的地点。
> 
>   
> 
> **风格描述**
> 
> 视觉风格是现实主义的，具有详细的角色模型、自然光照以及高度的环境细节，共同营造出一个沉浸式且令人信服的乡村环境，适合于电子游戏的背景设定。
> 
>   
> 
> **镜头描述**
> 
> 相机视角在整个序列中始终与第一人称视点保持一致。初始画面表明了一场动态的斗争，伴随着快速的动作，而随后的画面则显示了玩家与女性互动时更为稳定的相机。镜头跟随女人移动，将她保持为焦点，并且拍摄角度会随着玩家视角的变化而变化，以保持女人在视野中，特别是当她移动和转身时。
> 
>   
> 
> **简短描述**
> 
> 一个电子游戏角色站在房子前面。
> 
>   
> 
> **密集描述**
> 
> 该视频序列展示了视频游戏角色在乡村环境中与不可玩角色 (NPC) 互动的第一人称视角。最初，玩家角色似乎正在与敌人或生物搏斗，如特写斗争和火花或余烬的存在所示。场景切换到玩家角色站在一位老年妇女面前，她以防御或威胁的姿势挥舞着铲子。该女子的表情和姿势表明她对玩家持警惕或对抗态度。随着视频的进展，这名女子似乎稍微放松了一点，放下了铲子并与玩家交谈，这一点从她不断变化的面部表情和肢体语言可以看出。

  

===

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****数据采集与标注****

为了收集MiraData，研究团队首先手动选择不同场景下的YouTube频道。然后，使用**PySceneDetect**下载并分割相应频道中的所有视频。之后，选择了时长在1到2分钟之间的视频片段。对于超过2分钟的视频片段，他们将其分成多个2分钟的片段。最后，使用 GPT-4V 为视频剪辑添加描述。

  

  

 GPT-4V 描述

研究团队测试了现有的开源视觉LLM方法和GPT-4V，发现**GPT-4V**的描述在时间序列方面的语义理解上表现出更好的准确性和连贯性。它还可以更准确地描述主要主体和背景物体，减少物体遗漏和幻觉问题。因此，他们使用GPT-4V来生成**密集描述**、**主体描述**、**背景描述**、**镜头描述**和**风格描述**。

  

  

 Panda-70M 描述

为了平衡标注成本和描述准确性，他们为每个视频统一采样 8 帧，并将它们排列成一张大图像的 2x4 网格。然后，使用Panda-70M的描述模型为每个视频添加一句话描述，作为主要内容的提示，并将其输入到他们的微调 prompt 中。

  

通过将微调的提示和 2x4 大图像输入 GPT-4V，他们可以在一轮对话中高效地输出多个维度的描述。具体提示内容可以在_caption\_gpt4v.py_中找到，欢迎大家贡献更多优质的文字-视频数据。

  

**caption\_gpt4v.py链接：**

_https://github.com/mira-space/MiraData/blob/main/caption\_gpt4v.py_

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****统计****

数据集信息统计如下：  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7vkkDvHm0SibX8smKaTCMxaUwrxCvRmI7yKadeKLFicUvmHxZ0qZ1YFYJ0zbR3nc3YAP7rwV5zhCAQ/640?wx_fmt=png&from=appmsg)

密集字幕的总文本长度统计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7vkkDvHm0SibX8smKaTCMxaKXzmCiag9KwVz7G6tibibIVp3FbEFTTSEotOGcZf0sqVpUM6EgGicXLTkw/640?wx_fmt=png&from=appmsg)

六种类型字幕的总文本长度统计

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7vkkDvHm0SibX8smKaTCMxa8gS9QPKm1UiaSI9H6p4hZCIFC6yABIWBI3zNibejkXicj0ShRnJcicRlDA/640?wx_fmt=png&from=appmsg)

简短描述词云

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7vkkDvHm0SibX8smKaTCMxaPCAh78TwdkoBv1v32GiaE4Ec58TCXeRT5gJvMYhH6QDwPGRUraExT2g/640?wx_fmt=png&from=appmsg)

密集描述的词云

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

****数据集下载****

作者提供的描述元文件，除了上述6种维度描述外，还提供了YouTube视频ID等相关信息：

**● 元文件字段：**

> **· index** : 视频片段索引，由以下部分组成{download\_idx}\_{video\_id}-{clip\_id}
> 
> **· video\_id** : YouTube 视频 ID
> 
> **· start\_frame** : YouTube 视频的剪辑开始帧
> 
> **· end\_frame** : YouTube 视频的剪辑结束帧
> 
> **· main\_object\_caption**：视频中主体描述
> 
> **· background\_caption** : 视频背景描述
> 
> **· style\_caption**：视频风格描述
> 
> **· camera\_caption** : 镜头描述
> 
> **· Short\_caption**：简短描述
> 
> **· dend\_caption**：密集描述
> 
> **· fps**：用于提取帧的视频帧率

  

_\*你可以使用 start\_frame/fps 或 end\_frame/fps 获取开始和结束时间戳_

  

另外，作者提供了视频下载并分割的脚本：

    python download_data.py --meta_csv miradata_v0.csv --video_start_id 0 --video_end_id 10631 --raw_video_save_dir miradata/raw_video --clip_video_save_dir miradata/clip_video

  

其中_\--video\_start\_id_和表示要下载的元文件的_\--video\_end\_id_开始值和结束值。游戏场景范围为0至7416，城市/风景探索范围为7417至10631。_download\_idxindex_

  

以上就是本次分享

你对MiraData数据集怎么看？

欢迎添加小助手，进交流群讨论

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7NEyym4C8KBFplT20DM2vqAUAysVwzco8icviaYQ6McYIHep7ythBW0oZic97dXnhS6LbnoyibAqCbLQ/640?wx_fmt=jpeg)

* * *

  

更多数据集，请访问OpenDataLab

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言