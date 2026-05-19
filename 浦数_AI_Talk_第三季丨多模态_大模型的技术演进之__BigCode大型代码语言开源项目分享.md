     浦数 AI Talk 第三季丨多模态、大模型的技术演进之——BigCode大型代码语言开源项目分享 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

浦数 AI Talk 第三季丨多模态、大模型的技术演进之——BigCode大型代码语言开源项目分享
=================================================

原创 热爱学习的 OpenDataLab 2023-04-25 13:20 上海

> 原文地址: [https://mp.weixin.qq.com/s/IXdxEEz5wX3kbZDCYJnT5Q](https://mp.weixin.qq.com/s/IXdxEEz5wX3kbZDCYJnT5Q)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD63NnuiaZCrIQ2ln8hU2exdJanBLvlrAMHABmOow3pzuOoSuhQyxFA9T3a7vGkzVfxibCUicibeZM6OUQ/640?wx_fmt=png)  

**“浦数 AI Talk”****系列直播活动**，由OpenDataLab 浦数 | 人工智能开放数据平台发起，联合各大开源社区，围绕热门 AI 应用场景，选取最受大家关注、最接“地气”的主题，定向邀请垂直领域的 AI 研究员、工程师，为大家带来最前沿的干货分享。

  

我们不局限于单纯的技术讨论，将从更加融合生态、更加注重解决实际问题的角度去启发、探讨，旨在提高场景需求理解能力。

  

从场景定义、数据处理、算法训练，到模型部署；从实用技术教程、高效工具资源、前沿论文解读、科研成果分享，到产业应用经验；从视觉识别、自然语言处理，到决策规划……

  

丰富又多元的内容，总有一“款”适合你。欢迎加入社群，及时掌握最新动态![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/2_06.png)（戳链接回顾：[_AI Talk 第一季（自动驾驶专题）_](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247508750&idx=1&sn=e5c10287bd452a849765fe39f3411b8c&chksm=c10c31ecf67bb8fa64af171679105627bd554670668dc931aa2b541208995028c6a1c15c5395&scene=21#wechat_redirect)、[_AI Talk第二季（数字与内容生成）_](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247516044&idx=1&sn=042e1c45de84027a7e488b586181c09e&chksm=c10c2d6ef67ba478149f25472b722d6be220fe257d088bf76231e5e60c2f4e65514161aaacf6&scene=21#wechat_redirect)）

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****第三季分享主题****

近几年，以Chat-GPT、Stable Diffusion、Copilot等为代表的AI对话、AI绘画、AI代码生成等应用，让我们看到了预训练生成式大模型的魔力，也看到了多模态技术的发展趋势。AIGC（即人工智能内容生成）赛道因此而变得火热，它不仅带来了内容生产方式的全面革新，同时引发了新一代研究浪潮。

  

浦数 AI Talk第三季，我们将围绕“**多模态、大模型的技术演进**”主题，邀请来自最前沿、最一线的算法研究员、工程师等，分享他们在这个赛道上所做的关于算法研究、模型训练、数据处理、产品创新等方面的成果，希望能给同行的小伙伴们启发和帮助。

  

4月26日-5月24日，每周三晚7点，准时在示说网、B站和视频号开播，赶快预约学习~

  

**第一期精彩预告**

4月26日的第一期，将由Hugging Face 组织的BigCode项目的主要贡献者之一，也是Cardiologs的始创人和前CTO的李嘉老师，为我们带来主题为“**The Stack和Big code，大型代码语言模型开源项目经验分享**”。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4G8s7rYictkIYOBWmuvcqw4FDlAdibC4Ilibzpxgy3hlQZQE8qcWluWjTbeWnA8zGerjO2ZLbsmkLBA/640?wx_fmt=png)

扫描上方二维码，添加小助手  

加入交流群，获取完整直播链接  

也可在下方点击或扫码预约

  

**视频号预约：**

  

**示说网平台预约：**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4G8s7rYictkIYOBWmuvcqw4GT1oB2f1N6vsEEtdnXrmcYxps2sU0O4ibuxaT9qScIPCvrFiaBPhib68g/640?wx_fmt=png)

**直播活动****支持：**  

Hugging Face、OpenMMLab、和鲸社区、示说网、bilibili

  

**更多BigCode项目信息获取：**

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****更多精彩内容等你定制****

投票选出你最感兴趣的话题，下季内容由你决定！

  

**还有哪些**你**想学习的知识？**

**加入心动的Talker团，分享你的研究？**

**谁是你最中意的Talker，邀TA分享？**

添加小助手微信，我们来安排~

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7NEyym4C8KBFplT20DM2vqAUAysVwzco8icviaYQ6McYIHep7ythBW0oZic97dXnhS6LbnoyibAqCbLQ/640?wx_fmt=jpeg)

  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****关于我们****

**OpenXLab** **浦源人工智能开源开放体系**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtak0hIoUicBBqNYFf57epBd4M6SwKYT6EJ9v2sVyibzG0y7DNeEDYcDCA/640?wx_fmt=png)

官网链接：https://openxlab.org.cn/home

十年磨一剑，上海人工智能实验室研发的OpenXLab人工智能开源开放体系正在成长为我国人工智能自主原创开放生态的技术基座。

  

OpenXLab包含九大开源项目，覆盖从感知到决策，从平面到立体，从数据到计算，从技术到人文教育的各个方面。它将推动人工智能对产学研各领域全面赋能，为我国构建人工智能自主开放生态，推动人工智能科研与技术突破、交叉创新和产业落地提供全方位的算法与平台支撑。

  

  

**OpenDataLab** 

**浦数丨人工智能开放数据平台**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt8KNmhKXxs80y3ou5nI7L82EQsqcjkhueDRB7NzHdTef67BiaRNHictNA/640?wx_fmt=png)

官网链接：https://opendatalab.org.cn/

作为上海人工智能实验室九大开源项目之一，以统一标准构建开放数据集互通互联网络，是下一代人工智能交叉创新和技术发展的数据底座。

  

平台已集结5400+优质公开数据集、覆盖1,400+任务类型、提供超过80TB大小的数据集资源。

  

平台集数据集智慧检索、智能推荐、高速下载开箱即用、元数据结构化描述、数据可视化预览统计、海量优质多模态全开源、开放共享数据互通优势为一体，致力于打造开放共享的数据生态。

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言