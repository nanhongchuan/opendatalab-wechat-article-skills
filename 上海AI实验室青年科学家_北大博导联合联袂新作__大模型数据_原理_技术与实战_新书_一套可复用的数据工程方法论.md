     上海AI实验室青年科学家、北大博导联合联袂新作：《大模型数据：原理、技术与实战》新书，一套可复用的数据工程方法论 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

上海AI实验室青年科学家、北大博导联合联袂新作：《大模型数据：原理、技术与实战》新书，一套可复用的数据工程方法论
========================================================

原创 OpenDataLab 2026-04-20 19:53 上海

> 原文地址: [https://mp.weixin.qq.com/s/dLfWg67HD\_\_WaL7pQtevwQ](https://mp.weixin.qq.com/s/dLfWg67HD__WaL7pQtevwQ)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

  

过去两年，大模型技术的发展呈现出一个清晰的演进脉络：模型架构的创新节奏趋缓，而数据工程的重要性正在被重新评估。

  

这种转变并非偶然。当Token成为大模型交互与计价的统一单位时，一个技术事实值得被重新审视：Token是模型理解与表达的最小单元，但它本身并不蕴含智能。每一个Token的生成，本质上都是模型对训练数据中所习得的概率分布的一次采样。换句话说，Token是智能的“计量单位”和“输出载体”，而决定输出质量的，始终是其上游的数据供给系统。模型的能力边界，在训练数据被确定的那一刻，就已经被大体框定。

  

然而在实际落地过程中，一个普遍的困境正在浮现：尽管通用大模型的能力已得到广泛验证，但将其应用到垂直业务场景时，效果往往难以达到预期——Demo表现优异，上线后波动显著，且问题的根因难以定位。调Prompt、换模型、加RAG、上Agent，这些手段往往只能带来局部的、暂时的改善。

  

问题的本质在于，数据链路——从采集、清洗、配比、合成、增强到反馈优化——这条隐形的供给线，在多数项目中并未被当作一个严肃的工程系统来对待。

  

那么，一条稳定、可复用的数据链路究竟该如何构建？这正是《大模型数据：原理、技术与实战》一书试图回答的问题。

  

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAZ7lpg6vuO1DRuY4N5xEtqePqichgpVxB9To7TXibib1Tdvu7iamJcibQ3FLJ5DYgOjWPdfkKX4SzcTfLnGx7obB2XcXRmzcEhKgdibA/640?wx_fmt=png&from=appmsg)

  

===

  

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAa7Skr7W4iaQGkGa0tV94VS3NYc0okDFUhuMlynnBXa4axb7LVE72OT5nTtMu6oQs5DmuUYewe3ialOiasysX29Gf925ElniaL4Ybs/640?wx_fmt=png&from=appmsg)

**作者介绍  
**

本书由上海人工智能实验室青年科学家、OpenDataLab发起人何聪辉，上海人工智能实验室青年科学家、OpenDataLab前沿研究引领人之一吴郦军，携手北京大学博士生导师张文涛共同打造。
==============================================================================================

[OpenDataLab](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549458&idx=1&sn=296de8cace3047a9a2faebb6f61695e3&scene=21#wechat_redirect)已成为国内大模型数据领域最具影响力的开源社区之一，服务了数以万计的AI开发者和研究机构。团队自研的[MinerU高精度文档解析引擎](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551394&idx=1&sn=b099a4e76c33bed6eab755a0a63c2841&scene=21#wechat_redirect)与[“万卷”语料库](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544627&idx=1&sn=b42ca5c64486dd69fcc069d6dd395bca&scene=21#wechat_redirect)，均已成为各自领域广泛采用的标杆性成果；面向科学智能提出的[Sciverse数据基座](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551767&idx=1&sn=bdfbcd3ed3510bfd4713edb8443f6836&scene=21#wechat_redirect)构想，代表了团队在AI4S方向的前沿探索——这些工作既是其学术洞察力的工程印证，也为本书提供了扎实的实践注脚。

  

三位作者长期深耕大模型数据方向，在数据采集、清洗、配比、合成、增强与反馈优化等关键环节积累了深厚的理论功底与实战经验。书中系统梳理了一套从原始数据到高质量模型输入的完整方法论，其中大量洞见来自作者们在OpenDataLab、MinerU等一线数据项目中的真实沉淀。

  

无论是被模型效果不稳所困的工程师，还是希望建立数据处理与评估体系的数据从业者，抑或是正在打通AI落地最后一公里的开发者，都能从中获得可落地的认知框架与实践指引。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uo0n2KqOLAbeIySqFgseicTOVBGknWYTzOavnplrfhZ1Q7RjPfibjIAgghuo62RcBibf3Lw1XicD3Ylmo9XYpib4ACLC7Y3weOZzfrGSjCO5pxB8/640?wx_fmt=jpeg)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAYCzic3LhLDK5fRX5Uxvk2zzSkPZRuR4Gq8wiaYKdz0ZtibuFw7uiciaSzWAafxaerovrK6UDGq6eaQzgmBOAWyNshCXIv2dqDXUTbg/640?wx_fmt=png&from=appmsg)

**这本书关注什么**

本书特色主要体现在三个层面：

● 前沿：聚焦大模型时代最稀缺的数据能力，探讨如何用合成数据打破真实数据的瓶颈。

● 实操：提供从PDF文档到可训练数据的完整案例复现，而非停留在理论推演。

● 系统：沉淀一套可复用的数据工程方法论，覆盖数据产生、清洗、组织、合成、增强到反馈优化的完整链路。

###   

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAbZnVLSN8XSsia1aBqxFlVGS9kr2tkuZUKt9sq4nfjse2mZTVSOkNuQj2hibBmicIaOqiaLRJhHMP7UcRukaiaVTbLJ8x2mjMUQaoIk/640?wx_fmt=png&from=appmsg)

**适合哪些读者**

本书主要面向以下人群：

![大模型数据海报-05.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/uo0n2KqOLAYmm7OKCNOIzXcsowf2ZSyhvhuaibM8s11ibTJ3iaDkrsZnvicxjqRtIPcYVn1dWsj7IzA9U5uFwM4dcsZrUO7F69iawCaWxYNb3oMg/640?wx_fmt=jpeg)

###   

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAZq5FcRWA8Ldr5PfQWWSjMK3Dic9CdpdYOSCfAKYHU9OaBta9Cs7NibzrHtUiapjX7n5HoNJpJEIpGZFFzhAUDuTm67TbvQfMrlJk/640?wx_fmt=png&from=appmsg)

**学界推荐**

本书获得了北京大学讲席教授、中国科学院院士鄂维南与香港中文大学教授林达华的推荐。

  

鄂维南院士认为：“对于渴望在Data-Centric AI时代掌握核心竞争力的研究人员与算法工程师来说，这是一本不可多得的案头指南。”

  

林达华教授指出：“如果你正在为AI在垂直领域的落地而困扰，这本书将为你提供一套清晰、可落地的操作范本。”

  

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAbdCF7Pes6picjsbibAk0dMQx9u4QPHJvjlia8DJjGB1sxicOaicV5kKe6OM2Lnupe6D3PoY2JficcSicjwicVlr1TcjADap8cqgHE33Gk/640?wx_fmt=png&from=appmsg)

**互动赠书**

《大模型数据：原理、技术与实战》现已正式出版。为感谢社区长期以来的支持，OpenDataLab将向评论区读者赠送五本纸质书。

  

欢迎在评论区留言，分享你在AI项目实践中遇到的数据相关问题——可以是一个棘手的处理细节，也可以是对Data-Centric AI的思考。

  

截止本周五中午12:00，评论区点赞数排名前五的读者，将各获赠书一本。

  

* * *

_在词元经济时代，Token是输出的计量单位，而数据是决定输出质量的供给系统。理解这一点，或许比追逐任何一个新模型都更重要。_

  

END  

  

**相关阅读：  
**

  

  

[跳出 SOTA 内卷，我们发了个“好用至上”的文档解析模型](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551853&idx=1&sn=7a5737aced92eb9986958a2fc0cc9c29&scene=21#wechat_redirect)

2026-04-10

[![](https://mmbiz.qpic.cn/mmbiz_jpg/uo0n2KqOLAZFBcbw20Oh5TuOpComwHCMQdibgTRQS1E6GBCG8luOezoanibezKn3Ju3wvic64SsvvODaWfykfn1kNZtxCXwkWwes8Djs0QZp6g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551853&idx=1&sn=7a5737aced92eb9986958a2fc0cc9c29&scene=21#wechat_redirect)

[科学智能数据库 Sciverse 正式发布：让科学数据成为 Agent 可调用的资源](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551767&idx=1&sn=bdfbcd3ed3510bfd4713edb8443f6836&scene=21#wechat_redirect)

2026-03-30

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAapvYr5D6hpAm9MytDtiaEnBkDb8Qsnq8DLtc7ibVoYtvZ0otIW5wQcKhMAZWQvhJaE5iaKTIwrTpxAOKmcpse1SkkTTMWgOr9BibA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551767&idx=1&sn=bdfbcd3ed3510bfd4713edb8443f6836&scene=21#wechat_redirect)

[文档OCR 3.2倍提速！上海AI实验室&北大新作MinerU-Diffusion，用扩散模型重构文档OCR](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551767&idx=3&sn=b0d088ae5eae66c57b3dd9a4ed075968&scene=21#wechat_redirect)

2026-03-30

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAZnkOUnQp7sdqGGvCJY18s0KIIMTXnbicRq7CYzxwtpclEp444tO2VibetZqbNhunMDib8q0LwLlscL4yngjDMRMV9GYoWVs61zG8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551767&idx=3&sn=b0d088ae5eae66c57b3dd9a4ed075968&scene=21#wechat_redirect)

[一句话，让你的🦞看懂PDF，MinerU 官方 Skill 来了！附赠开发者“全家桶”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

2026-03-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbZZOF5ZU4633TUhZvib1DtcPjUoonLTDianYHpSU7f41y5eMfmkHsZJ5rvLLa95chfTKAw2iaI4OgZVsJZVBNfXkszm2iaPsxyF2M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言