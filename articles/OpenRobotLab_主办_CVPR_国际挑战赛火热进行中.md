     OpenRobotLab 主办 CVPR 国际挑战赛火热进行中 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

OpenRobotLab 主办 CVPR 国际挑战赛火热进行中
===============================

原创 OpenDataLab 2024-05-07 18:40 上海

> 原文地址: [https://mp.weixin.qq.com/s/umfZk7I8CP89RiEhqsB5ww](https://mp.weixin.qq.com/s/umfZk7I8CP89RiEhqsB5ww)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/se9VmVQqhGOnjFH9dqx5cU99PH7bWhibpv9cavqBkun0zcnnjPvKhCpPPHHCLnPWWLMkz6ib2w0JhW9ialp553T8g/640?wx_fmt=png&from=appmsg)

计算机视觉顶级会议 CVPR 2024 即将在 6 月于美国西雅图举办。上海人工智能实验室 OpenRobotLab 浦器团队聚焦具身智能和计算机视觉的核心问题，联合多家国内外机构，主办了两项挑战赛的两个主要赛道：EmbodiedScan 竞赛暨多视角三维视觉定位挑战赛和 OV-PARTS 竞赛暨开放域部件分割挑战赛。获胜者有机会获得多达数千美金奖励，在研讨会上做突出展示和亮点报告，还有机会被邀请在国际顶级期刊进行投稿。我们为每个赛道准备了详细的参赛指引及基准模型，点击每个赛道对应链接即可访问。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/se9VmVQqhGOnjFH9dqx5cU99PH7bWhibpDfpjTD4gLhpvwWNPK3kvu0vnlu7tMialRNDGzeSDEyEGDU4Iia50GxjQ/640?wx_fmt=png&from=appmsg)

  

_**1**_

**【赛道一】EmbodiedScan Challenge: Multi-View 3D Visual Grounding**

  

@Autonomous Grand Challenge & Foundation Models for Autonomous Systems Workshop, with OpenDriveLab 

  

室内环境下的具身三维感知系统面临着与驾驶场景截然不同的挑战。它需要处理包含语言指令的多模态输入，理解复杂的语义，识别多样的物体类别和朝向，以及适应差异化的感知空间。为此，我们构建了首个基于第一视角的多模态全场景三维感知工具包 EmbodiedScan 。这项挑战的目标是：在给定特定物体的语言描述后，能够准确检测出目标物体的类别及其带朝向的三维框。

  

**赛道信息：**

  

https://opendrivelab.com/challenge2024/#multiview\_3d\_visual\_grounding

  

**测试服务器：**

  

https://huggingface.co/spaces/AGC2024/visual-grounding-2024

  

**数据集概况：**

  

原始传感器数据：2T+。需从 ScanNet / 3RScan / Matterport3D 官方下载相关原始数据。

  

比赛相关数据：约 300 G。根据 EmbodiedScan 官方指导预处理和准备相关数据，只需要保留第一视角 RGB-D 图像数据即可。

  

标注数据：约 300 M。请填写数据集申请表，我们会尽快回复邮件提供数据下载链接。标注文件包括整体 pkl 文件，occupancy 标注和视觉定位语言标注，拿到标注数据后按照官方指导放在相应目录下即可。

  

**评测指标：**

  

阈值为 0.25 和 0.5 的基于 3D IoU 的平均精度 (AP)。此次竞赛将根据 AP@0.25 由高到低对提交结果进行排名。  

  

**参赛方式：**

  

注册：所有参赛队伍需填写表格注册信息，更多详细规则见官方网站说明。

  

提交结果：我们在 Github 仓库提供了测试集上推理的脚本，以及将推理结果打包成提交结果的脚本，参赛者需根据个人队伍情况修改脚本中相应信息。准备好提交结果后，提交到 Huggingface 的测试服务器上，评测一般需 10 分钟左右，因提交结果内容可能会有所浮动，请耐心等待。提交格式、其他说明及 FAQ 详见 Huggingface 网站上说明。

  

**时间线：**

  

  

  

即日起-

2024年6月1日

**01**

**参赛报名**

  

  

2024年3月1日

**02**

**比赛正式开始**

  

  

2024年3月底

  

**03**

**测试服务器开放**

**基准方法开源**

  

  

2024年6月1日

**04**

**测试服务器关闭**

  

  

2024年6月18日

**05**

**比赛结果公布**  

  

  

  

**基准方法：**

  

EmbodiedScan 中 Multi-View 3D Visual Grounding Baseline，参考 benchmark 见 github。

  

**参考训练时间：**

  

样本数据 8 卡 A100 0.5 天，全量数据 8 卡 A100 2 天

  

**联系方式：**

  

Email: taiwang.me@gmail.com, openrobotlab.contact@pjlab.org.cn

Slack channel: #visual-grounding-2024

  

**附相关表格链接：**

  

数据集申请表格：

https://docs.google.com/forms/d/e/1FAIpQLScUXEDTksGiqHZp31j7Zp7zlCNV7p\_08uViwP\_Nbzfn3g6hhw/viewform

  

参赛注册表格：

https://docs.google.com/forms/d/e/1FAIpQLSctm2iipw5r1\_wY-kVt7X-4RRynnt3ZzYMzaBVzEpNStoc-rQ/viewform

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/se9VmVQqhGOnjFH9dqx5cU99PH7bWhibphwaLFQv9yKdcf0wbbsKZfXH5qVGANINR5ScbTBJBkFVmTq8jpgSibJA/640?wx_fmt=png&from=appmsg)

  

_**2**_

**【赛道二】OV-PARTS Challenge: Open-Vocabulary Part Segmentation**

@Visual Perception via Learning in an Open World Workshop

  

开放域的 part 级别分割挑战（OV-PARTS）旨在基于自然语言对物体的细粒度组成进行语义分割，以推动视觉和机器人领域的多种应用。目前大部分的研究工作关注于开放域的物体分割，对于 part 级别的相关研究仍需深入探讨。主要的挑战在于 part 的语义定义相对模糊，且通常具有开放的粒度。现有的基础多模态大模型如 CLIP 在 part 识别能力上还有所欠缺。因此，本次挑战鼓励参与者研究如何有效利用现有的大模型来解决 OV-PARTS 问题。

  

**赛道信息：**

  

https://ov-parts.github.io/

  

**测试服务器：**

  

https://eval.ai/web/challenges/challenge-page/2283/overview

  

**数据集概况：**

  

本次挑战用了两个公开数据集的 part 标签, 并对其进行了数据清洗和整理：

Pascal-Part-118：包含 16 个物体的 118 个 part 的标注。

ADE20K-Part-234：包含 44 个物体的 234 个 part 的标注。

  

**评测指标：**

  

OV-PARTS 评测模型两方面的能力：

hIoU ：针对训练时不可见的物体 part 的泛化能力，计算训练和未训练类别的 mIoU ，然后计算调和平均hIoU。

mIoU ：主要针对不同词汇和粒度的 part 的泛化能力，计算跨数据集验证（ADE20K-Part-234--> Pascal-Part-118)的 mIoU 。

  

**参赛方式：**

  

通过 EvalAI 注册并提交结果至测试服务器。

  

**时间线：**

  

  

  

即日起-

2024年6月9日

**01**

**参赛报名**

  

  

2024年4月5日

**02**

**比赛正式开始**

  

  

2024年4月18日

**03**

**测试服务器开放，**

**基准方法开源**

  

  

2024年6月9日

**04**

**测试服务器关闭**

  

  

2024年6月12日

**05**

**比赛结果公布**  

  

  

  

**基准方法：**

  

微调物体级别开放域分割的方法 ClipSeg 其中的少部分参数，将其迁移到 part 级别的开放域分割，详见 github 。

  

**联系方式：**

  

Email:kellymeng0427@gmail.com, openrobotlab.contact@pjlab.org.cn

竞赛正在火热进行中，欢迎大家踊跃参赛！

  

**微信公众号**

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/se9VmVQqhGOnjFH9dqx5cU99PH7bWhibpybPVArawzJbpnjcCqHuJS9ExN226z9GBYibIQjjFMzGeoiaRtrhjicy7A/640?wx_fmt=jpeg&from=appmsg)

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言