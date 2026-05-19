     浦数 AI Talk 第五季 | 直击前沿：探索多模态AI的无限可能①——详解InternVL，开源多模态大模型“黑马” \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

浦数 AI Talk 第五季 | 直击前沿：探索多模态AI的无限可能①——详解InternVL，开源多模态大模型“黑马”
============================================================

原创 热爱学习的 OpenDataLab 2024-06-04 19:10 上海

> 原文地址: [https://mp.weixin.qq.com/s/Zs7nf4s8L5svvc\_xp7\_HdA](https://mp.weixin.qq.com/s/Zs7nf4s8L5svvc_xp7_HdA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD792UchicU2skfHCOibeISIXfasWeJvWEWCjUnxkwg8nxcZHWibiba1fW3toADMzibRVXgzSAA33kpfwHA/640?wx_fmt=jpeg&from=appmsg)

**“浦数 AI Talk”****系列直播活动**，由OpenDataLab 浦数 | 人工智能开放数据平台发起，联合各大开源社区，围绕热门 AI 应用场景，选取最受关注、最接“地气”的主题，定向邀请垂直领域的 AI 研究员、工程师，为大家带来最前沿的干货分享。

  

我们不局限于单纯的技术讨论，将从更加融合生态、更加注重解决实际问题的角度去启发、探讨，旨在提高场景需求理解能力。

  

从场景定义、数据处理、算法训练，到模型部署；从实用技术教程、高效工具资源、前沿论文解读、科研成果分享，到产业应用经验；从视觉识别、自然语言处理，到决策规划……

  

丰富又多元的内容，总有一“款”适合你。欢迎加入社群，及时掌握最新动态![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/2_06.png) 点击查看，往季回顾：

[_AI Talk 第一季（自动驾驶专题）_](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247508750&idx=1&sn=e5c10287bd452a849765fe39f3411b8c&chksm=c10c31ecf67bb8fa64af171679105627bd554670668dc931aa2b541208995028c6a1c15c5395&scene=21#wechat_redirect)

[_AI Talk 第二季（数字与内容生成）_](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247516044&idx=1&sn=042e1c45de84027a7e488b586181c09e&chksm=c10c2d6ef67ba478149f25472b722d6be220fe257d088bf76231e5e60c2f4e65514161aaacf6&scene=21#wechat_redirect)

[_AI Talk 第三季（大模型专题）_](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247520995&idx=1&sn=3efcf04cca3bb9fc6f1793ce2de85ec5&chksm=c10c0001f67b89179f4816e4fb0410c8a0bd0ffbff53c5367517174623c0082f574e94912026&scene=21#wechat_redirect)

[_AI Talk 第四季（多模态专题）_](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247528363&idx=1&sn=fbac57951198cc91b810eeac7e9e84a1&chksm=c10cfd49f67b745f55a45ab5e2ab08dc4673aa52d68cb4bc390560cea201136b7356ded83808&scene=21#wechat_redirect)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****第五季分享主题****

在人工智能的演进历程中，多模态大模型正逐渐揭开AI系统“理解”世界的全新篇章。随着Gemini、GPT-4o等创新模型不断突破界限，我们正处于一个多模态能力爆发的临界点。面对着开源模型的海量涌现，研究者们急需一个筛选和深入理解这些模型的高效途径。

  

浦数“ AI Talk”系列直播第五季，将以“**直击前沿，探索多模态AI的无限可能**”为主题，带您深入多模态大模型的世界，从模型训练、微调、评测，到数据处理清洗、标注……我们将精选那些在关键领域具有突破性应用的模型，提供专业的讲解和实际的应用案例分享，努力为AI研究者提供一个清晰的“导航”。

  

无论你是AI初学者还是行业专业人士，这都将是一次宝贵的学习与交流机会。期待与你探索多模态大模型的无限可能！6月5日-7月3日，每周三晚7点，准时在视频号、B站和示说网开播，赶快预约学习~

**第一期精彩预告**

6月5日19:00，将由南京大学在读博士生 陈喆带来《详解InternVL：开源多模态大模型“黑马”》的主题分享，更多精彩内容见海报：

  

**InternVL在线试用**：

_http://internvl.opengvlab.com_

  

**InternVL模型开源地址：**

_https://github.com/OpenGVLab/InternVL_

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD792UchicU2skfHCOibeISIXfaFwVF9kG74bujWV5RM8Qw84xSquIDxe4zTflGMDzaDCQ9sxGsq9Fibw/640?wx_fmt=png&from=appmsg)

扫描上方二维码，添加小助手  

加入交流群，获取完整直播链接  

也可在下方点击或扫码预约

  

**视频号预约：**

**直播活动****支持：**

OpenGVLab、bilibili、示说网

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****更多精彩内容等你定制****

投票选出你最感兴趣的话题，下季内容由你决定！

  

  

  

欢迎联系小助手，加入交流群  

获取更多精彩内容  

  

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7NEyym4C8KBFplT20DM2vqAUAysVwzco8icviaYQ6McYIHep7ythBW0oZic97dXnhS6LbnoyibAqCbLQ/640?wx_fmt=jpeg)

  

  

相关阅读

[

微调数据最新开源！ChemData: 为化学语言模型提供全面数据支持

2024-05-24

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD5SicSb4Dj2PZsVJ4AVVur08D6VFg8ZiaTeoyqvDXOD6wk93l2RalpLAeGJibr4sWyqgdVbcltVEaKqA/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247535445&idx=1&sn=8c63f6f446d6f52c49bd9b1a30d9d8e2&chksm=c10cd9b7f67b50a1c06ea43315a513d0f269b842695a83de623fccf3cebfe643f1d84afa74d0&scene=21#wechat_redirect)

[

高质量新闻数据集OpenNewsArchive：880万篇主流新闻报道，国产大模型开源数据又添猛料

2024-05-15

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6iagPYutnSRK8QqUSiaeIf8cVEcHegsE53SWPWQ5OHShFchPvN2icFf8wXSAibNdrS1Dw0lvn1GS8hiag/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247534906&idx=1&sn=a4e9941e8e64a3fc68747784e7df3f21&chksm=c10cdbd8f67b52cef5c1bf51dfd0132fc40d2eb8f3fa61b11e022a38a3871c332c182c87dc79&scene=21#wechat_redirect)

[

百里挑一“萃取”数据精华，上海AI实验室开源发布高质量语料“万卷CC”

2024-03-07

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD7bZp5uyPBITbFuziceXvjvSAmLPrAdtICXnKj3nJbdkPytvZsAq2jibGBGW6LC3ibXwksmnTKFmicCaA/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247532709&idx=1&sn=2c7e5ddbadc917b5f3c22db31cd0f95d&chksm=c10cd247f67b5b51c61e9415a6a8a02ec4b13f9ca3c640865ba1bfe073aab4c5c597de64bd89&scene=21#wechat_redirect)

[

12家新成员单位加入、3个专业数据集发布……中国大模型语料数据联盟开放日活动成功举办，凝聚各方资源，推动大模型语料数据高水平供给

2023-11-27

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD4QJZdpliaHhcZKH9pvok9k2CQF2ROA8ic5yPFkU5jUBrRef1n6TC2kOMxXOPDOEV1Q8asVQuj6iapSQ/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247525545&idx=1&sn=a0e16e942dd947b88aa4a8fccc807ca9&chksm=c10cf64bf67b7f5dd25427498bda4bfe767ec24c0e5e8972613318e7b36b317d1abc4046329d&scene=21#wechat_redirect)

[中国大模型语料数据联盟迎来9家新成员，开源第二批语料数据](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247523597&idx=1&sn=73f603251f534573afc31208ab9f6231&chksm=c10c0feff67b86f9a8d011b22427a282f5cfec9fef1ee9e963218b5062c8ffab4162dca0f11f&scene=21#wechat_redirect)

[2023-09-08](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247523597&idx=1&sn=73f603251f534573afc31208ab9f6231&chksm=c10c0feff67b86f9a8d011b22427a282f5cfec9fef1ee9e963218b5062c8ffab4162dca0f11f&scene=21#wechat_redirect)

  
[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD7zod4eOw2jKyWtUOGQfTDFqf1tHqwCLCGI8Bdezkqo2zFYbfBzuibgk3ibrr1kgHfyriaMzNbMRD7lA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247523597&idx=1&sn=73f603251f534573afc31208ab9f6231&chksm=c10c0feff67b86f9a8d011b22427a282f5cfec9fef1ee9e963218b5062c8ffab4162dca0f11f&scene=21#wechat_redirect)  
  
  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言