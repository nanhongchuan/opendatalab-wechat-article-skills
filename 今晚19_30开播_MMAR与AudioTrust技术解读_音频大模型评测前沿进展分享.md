     今晚19:30开播！MMAR与AudioTrust技术解读，音频大模型评测前沿进展分享 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

今晚19:30开播！MMAR与AudioTrust技术解读，音频大模型评测前沿进展分享
===========================================

原创 OpenDataLab 2025-06-12 18:51 上海

> 原文地址: [https://mp.weixin.qq.com/s/XiwcAhRP3fN5SUKIrPvOng](https://mp.weixin.qq.com/s/XiwcAhRP3fN5SUKIrPvOng)

OpenDataLab联合司南评测体系、 OpenMMLab、2077AI、整数智能、魔搭社区、模速空间、MLNLP、Datawhale、机智流共同发起本期 AI Bench Talk 直播 。  

  

本次直播将**聚焦音频大模型，分享两大创新工作：MMAR，一个评估音频大模型深度推理能力的全新评测基准；AudioTrust，一个针对音频大模型的全方位可信评估框架。同时，本次直播****特设圆桌讨论环节，将深入探讨当前音频大模型在理解、推理和可信赖性方面的关键局限，以及音频大模态如何赋能多模态 AI 未来发展等议题。分享将于 6 月 12 日晚 19:30-21:30 进行，欢迎大家点击下方按钮预约观看。**

  

  

**分享内容  
**

  

**No.1** 

MMAR 分享  

  

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EZ7qLq6RgWA0cw9vPHeb4Bf7qcOEbTcRI3xywibjmqOqaayyIibvrAmKiabZtR8LQ5ouHORnDibpFzPQFXrbiaTibicpQ/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

**马子阳  
**

  

上海交通大学跨媒体语言智能实验室博士在读，他发布的 MMAR 是第一个音频深度推理基准测试，发布的 Audio-CoT 最早探索了音频大模型的思维链推理。曾获 Interspeech 最佳学生论文提名，NCMMSC 最佳学生报告。领导开源的 SLAM-LLM 系列是目前最广泛使用的音频理解大模型框架之一，相关文章被 AAAI、ACL、ICML、ICASSP、Interspeech 等会议接收。  

  

**内容简介：  
**

MMAR 是一个全新评测基准，旨在评估音频大模型的深度推理能力。该基准包含 1,000 个精心构建的音频与问答，并经过多轮纠错与质量校验以确保高标准。与现有局限于特定声音、音乐或语音领域的评测体系不同，MMAR 覆盖现实场景中的混合模态，并采用四级分层分类体系（信号层、感知层、语义层与文化层）。该基准中的每个题目都需要超越表层理解的多层次深度推理，部分问题更要求研究生级别的专业领域知识与感知能力。团队在 MMAR 上评估了多类模型，测试结果表明该基准具有显著挑战性，分析结果进一步揭示了当前模型在理解与推理能力上的关键局限。期待 MMAR 能推动这个重要但尚未充分探索的研究领域的发展。  

  

**文章:** 

https://arxiv.org/abs/2505.13032  

**代码：  
**

https://github.com/ddlBoJack/MMAR  

**数据集：  
**

https://huggingface.co/datasets/BoJack/MMAR  

**Compass hub ：  
**

https://hub.opencompass.org.cn/dataset-detail/MMAR  

  

**No.2** 

AudioTrust 分享  

  

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EZ7qLq6RgWA0cw9vPHeb4Bf7qcOEbTcRuicekZMSPsUuQLib03FBIiau08XIKgMj8cRsBb3qpo6WfRN58IfefUGfQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

**李凯  
**

  

清华大学 TSAIL 实验室博士在读，他致力于多模态与单模态语音分离，当前拓展至音乐分离等通用音频理解任务。曾获中国图象图形学学会优秀硕士论文，NCMMSC 最佳学生报告。曾参加 Sony 组织的分离竞赛获电影分离第一名。以第一作者身份在 NeurIPS、ICLR、ICML、TPAMI 等会议和期刊发表多篇论文，相关研究聚焦语音分离在真实场景中的应用，特别是在神经科学启发下设计轻量化模型，以实现边缘设备的高效部署。相关项目在 GitHub 上累计获得超过 4k stars。  

  

**内容简介：  
**

AudioTrust 是针对音频大模型的全方位可信评估框架，有效揭示音频大模型在公平性、幻觉、安全、隐私、鲁棒性和身份验证六大维度的潜在风险。汇集 4,420+ 条真实场景音频/文本数据，覆盖日常对话、紧急呼叫、语音助手等 18 种实验设置，设计 9 项音频特定评测指标，构建自动化评估流水线。主要发现：闭源模型在鲁棒性和安全防护上表现更佳，开源模型对隐私和公平性仍存盲区；多数音频大模型对性别、口音、年龄等敏感属性存在系统性偏见。期待研究者基于 AudioTrust 继续优化音频大模型，共同推动更安全、可信的 AI 音频生态发展！  

  

**文章:  
**

https://arxiv.org/pdf/2505.16211  

**代码:  
**

https://github.com/JusperLee/AudioTrust  

**数据集：  
**

https://huggingface.co/datasets/JusperLee/AudioTrust  

**Compass hub ：  
**

https://hub.opencompass.org.cn/dataset-detail/AudioTrust  

  

**No.3** 

圆桌讨论                                   

  

**参与嘉宾  
**

*   马子阳，上海交通大学跨媒体语言智能实验室博士在读  
    
*   李凯，清华大学 TSAIL 实验室博士在读  
    
*   袁锐斌，香港科技大学交叉学科研究部博士在读  
    
*   刘明皓，2077AI 核心发起人，整数智能算法工程师  
    

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EZ7qLq6RgWA0cw9vPHeb4Bf7qcOEbTcRTlIbGygOQDU6OKD6g0NS34jx801xE0gicibKCQSdOjweMaALFjJA1vCg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

  

**袁锐斌  
**

  

香港科技大学交叉学科研究部的博士生，硕士毕业于卡耐基梅隆大学。他致力于向通用人工智能注入艺术和创造力，研究方向包括大模型、生成式人工智能、音乐生成与理解基础模型。他在 ICLR / NeurIPS / CVPR / ACL / ISMIR / COLM / INTERSPEECH 等顶级学术会议发表多篇论文，论文总引用量上千次。他联合创办了 AIGC 开源学术社区 Multimodal Art Projection (M-A-P)，参与或领导许多有影响力的开源学术项目，如 MMMU, MERT, YuE, ChatMusician, MAP-NEO, AnyGPT 等。  

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EZ7qLq6RgWA0cw9vPHeb4Bf7qcOEbTcRxvCE0CgskPtaTic8YF9vwbt2vdVNWWvv0KdaopQia9OKXRgT8uVdSia6Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

刘明皓

  

2077AI 核心发起人与重要贡献者，作为一名资深算法工程师，他长期致力于推动人工智能领域的开源创新。作为 2077AI 开源基金会的核心项目参与者，成功开源了多个在行业内具有里程碑意义的项目，其中包括：SuperGPQA，旨在精准评估顶尖 AI 模型极限能力的高难度通用问答基准；PIN-14M，包含千万级图像文本对的多模态数据集；以及 OmniHD-Scenes，一个高分辨率场景数据集。这些项目推动了开源生态的建设与发展。  

  

  

**圆桌议程  
**

*   当前多模态/音频大模型的关键瓶颈与洞察  
    
*   核心技术交锋：模型理解、推理与可信赖性  
    
*   音频模态如何赋能多模态AI未来发展  
    
*   高价值研究成果的开源与生态赋能  
    

  

  

**参与方式  
**

  

观看直播

  

  

参与讨论

  

同时为了方便大家交流沟通，我们建立了相关的交流群，本期分享的大佬也在群里哦，可与大佬进行面对面沟通 ，扫码即可入群~  

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EZ7qLq6RgWA0cw9vPHeb4Bf7qcOEbTcRFu2aRmUic5qGAFZmZTacZfANia1icibrNw7nS8WRwV1Ougk37uibWLEapaA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

  

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EZ7qLq6RgWA0cw9vPHeb4Bf7qcOEbTcRe9cHwoWXucU0M6bfmOtc2Chd9RhNttibOawoItY4ic3sJGnjEicQxr8gA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言