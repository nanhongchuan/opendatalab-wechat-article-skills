     详解 MinerU 在线 API 深度调用 | MinerU实战训练营第三课上线，直播答疑预约，速来 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

详解 MinerU 在线 API 深度调用 | MinerU实战训练营第三课上线，直播答疑预约，速来
==================================================

原创 OpenDataLab 2026-04-08 23:27 上海

> 原文地址: [https://mp.weixin.qq.com/s/x95k9ODxXaNq5xggQa-ZVw](https://mp.weixin.qq.com/s/x95k9ODxXaNq5xggQa-ZVw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

 MinerU实战训练营是什么？

[2026 MinerU 数据智能与前沿语料挑战赛已启动](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)！作为大赛官方配套的实战赋能项目，[MinerU 实战训练营](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551728&idx=1&sn=938bbae1c68af433f85ba95267aac517&scene=21#wechat_redirect)同步开启。

  

本课程旨在通过体系化教学，手把手带你掌握 MinerU 全系列产品，从基础部署、模型微调，到 Skills 开发、AI Agent 搭建……

  

MinerU 实战训练营为你准备了全套免费课程视频、学习文档与实战资料，更有算力支持、专业导师直播答疑，以及结营证书认证，助你快速补齐从 MinerU “会用”到“实战”的关键技能，真正完成从“工具使用者”到“AI 应用构建者”的跃迁。

  

立即报名：

https://mineru.net/MDIC2026

（点击“立即报名”按钮，注册账号后进入比赛专区，选择“MinerU实战训练营”填写详细信息，完成报名、学习）

[![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAYibrCNZLcSOriaV0iaeicqicb2TISxaDKVoYhgvryW8M1aibmkhLANnYic7r9DJwoxdQkc5KeFCHj93T5pBtictzDOib4nCaOTnTdjuY7k/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551728&idx=1&sn=938bbae1c68af433f85ba95267aac517&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAbXxGy3iaSIIH0OraJ8wD7vITjc4CwicXtJQ8cxNRRaQ9FCMsiadIxRrkKalTZ3a3b0aSafmyPgKGfu5jjkLJG1hnfaIBEvx2QD3c/640?wx_fmt=png&from=appmsg)

**MinerU 实战训练营 · 第三课上线！**

  

上一周，第二课2位讲师给大家详解了 MinerU 及 MinerU-HTML 模型本地部署的操作，并且分享了如何进行本地、多任务高效文档处理，干货满满。（点击阅读原文，获取课程资料）

  

这次，MinerU 实战训练营第三课——《MinerU 在线 API 深度调用》将由MinerU SaaS产品架构师、后端工程师亲自讲解、示范，带你掌握 MinerU API 认证与调用逻辑；编写脚本实现批量 PDF 文档的异步并行解析与状态监控（包含HTML提取），并且在本周四为大家带来集中的线上直播答疑。欢迎大家先学课程、做作业，带着问题来直播间交流。

  

📚 课程获取方式

1️⃣ 官网报名：

大赛官网注册，进入比赛专区，选择「MinerU 实战训练营」报名：  

https://mineru.net/MDIC2026

（或者点击阅读原文获取）

2️⃣ 课程学习：  

在「课程内容」页面，即可查看课程安排、往期及最新课程文档与视频

3️⃣ 作业提交：

完成学习后，在「提交」板块提交对应课程任务，完成作业打卡

  

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAbWQzzlYq469QNxJRbBoWRq8uX5icKN4IhhvboNibapqNz23OrPSArFMpNQicicB7LdrC6DtXB4vMxBEU99xTHmM6Rl43E67koLRSs/640?wx_fmt=png&from=appmsg)

（课程及作业入口示意）

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAZhicDMkRQSVCAGLrticNTJ1bQ8bPV6mALibNcHGfg5RSykjlJh5jHNQ5bLHLMxgO7QUu8bdSUicm9V6d45G2l9eM3lhmiaiaiaMgLqLQ/640?wx_fmt=png&from=appmsg)

**⏰第三课直播答疑预约**

**时间**：4月9日19:00

**主题**：《MinerU 在线 API 深度调用》课程答疑

**讲师**：MinerU SaaS产品架构师 吴倩倩、MinerU 后端工程师 杨起

  

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAbXSfNal2CtibjUwSGb59DeLo8XlhEF0mEBs8k2B8I36AmNjjohRMYqWXO2QFV54owdEPcAZZGIzkSv3IkUxk1jSsR1yeCedCIM/640?wx_fmt=png&from=appmsg)

  

**更多信息，加入MinerU 实战训练营交流群获取：**

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAZ3dRmPgzFZIKVyZqeDBibvouWribr6cKltMLml7mKKTxMUxExfrI16FdS06wq7ziaM2bhkTpClAGKXRicESneXia9Uwa4Uzw27icVb4/640?wx_fmt=png&from=appmsg)

  

本次 MinerU 实战训练营的顺利开展，离不开各界合作伙伴在技术、算力以及社区生态方面的大力支持。

![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)在此特别感谢：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAYoby138ibFEAMV33lw6MiadfTAEUaia7MsAaprCnw1f9OnpgMvvkfIQA7hdRLY8iaWAETC4oXv7GtKuAPMWPH9QQehF0FPtK0KVn0/640?from=appmsg)

  

  

END  

  

**相关阅读：  
**

  

  

[科学智能数据库 Sciverse 正式发布：让科学数据成为 Agent 可调用的资源](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551767&idx=1&sn=bdfbcd3ed3510bfd4713edb8443f6836&scene=21#wechat_redirect)

2026-03-30

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAapvYr5D6hpAm9MytDtiaEnBkDb8Qsnq8DLtc7ibVoYtvZ0otIW5wQcKhMAZWQvhJaE5iaKTIwrTpxAOKmcpse1SkkTTMWgOr9BibA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551767&idx=1&sn=bdfbcd3ed3510bfd4713edb8443f6836&scene=21#wechat_redirect)

[MinerU-Diffusion发布：我们想重新回答，文档 OCR 到底该怎么做](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551745&idx=1&sn=32f28edfba35c37043d66f28dc254890&scene=21#wechat_redirect)

2026-03-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAanjOc0Y7utkLlOWLzhzOIaib1rNGia9egfP05ib0RiaAgQ2eUrSDibh79ssibicAGprFFsUmyeIeH9HuUsuzgb4aWBLFTbQ0upszBh1M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551745&idx=1&sn=32f28edfba35c37043d66f28dc254890&scene=21#wechat_redirect)

[一句话，让你的🦞看懂PDF，MinerU 官方 Skill 来了！附赠开发者“全家桶”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

2026-03-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbZZOF5ZU4633TUhZvib1DtcPjUoonLTDianYHpSU7f41y5eMfmkHsZJ5rvLLa95chfTKAw2iaI4OgZVsJZVBNfXkszm2iaPsxyF2M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

[领跑 AI-Ready 数据赛道：MinerU 全面深度适配主流国产算力，持续扩容生态版图](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551531&idx=1&sn=6d13d9fd5561fba5ae62a2af83d3ff1f&scene=21#wechat_redirect)

2026-02-10

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbAiatjCgctictxTmgAoyqBaE1ZiatJLib065zr3icTFKOweUUqUdobmvWu8s7NKeE4l2ZMU7wPbKycoVT4icDRB4TkNWEH3SEJAAPO8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551531&idx=1&sn=6d13d9fd5561fba5ae62a2af83d3ff1f&scene=21#wechat_redirect)

* * *

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言