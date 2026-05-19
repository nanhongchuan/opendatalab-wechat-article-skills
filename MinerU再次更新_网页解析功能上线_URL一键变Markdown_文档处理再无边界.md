     MinerU再次更新，网页解析功能上线！URL一键变Markdown，文档处理再无边界 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU再次更新，网页解析功能上线！URL一键变Markdown，文档处理再无边界
===========================================

原创 爱学习的 OpenDataLab 2026-01-21 18:36 上海

> 原文地址: [https://mp.weixin.qq.com/s/h2R\_nkMJZEj4jXqVUeQZLg](https://mp.weixin.qq.com/s/h2R_nkMJZEj4jXqVUeQZLg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：  

各位 MinerU 的铁粉们，你们的“生产力神兵”又进化了！还在为DeepResearch获取网页信息、网页知识库构建、复杂网页内容提取、网页文章复制乱码等场景感到头疼吗？

  

（MinerU.HTML介绍，点击查看）

  

在 AI 数据处理领域，以 **Jina AI** 和 **Firecrawl** 为代表的行业先行者已经为我们展示了“网页转 LLM 友好格式”的巨大潜力，**但 MinerU 决定再往前走一步。** 这次我们直接把深度优化的“网页解析”功能装进了 MinerU 网页端与桌面端，凭借在公式、表格识别上的深厚积淀，让整个互联网都成为你的 AI-Ready 语料库！

  

今天，我们边上手边拆解，带你玩转 MinerU 的“网页解析”功能

● 在线体验（直接进入网页解析功能）：https://mineru.net/OpenSourceTools/Extractor

● 技术报告链接：  

https://arxiv.org/pdf/2511.16397v1

● 模型链接：  

https://huggingface.co/opendatalab/MinerU-HTML

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

网页解析“统一入口”：动态网页秒变AI-Ready语料

  

这次更新的核心利器——“MinerU HTML”**网页解析系统**，正式上线网页端与桌面客户端。大家可以在 MinerU 网页端和桌面客户端通过简单的 URL 输入，实现网页到 Markdown 的完美转换。解析成功后，你会看到超酷的**左右分栏视图，**左边是网页快照，右边是清晰的 Markdown 或 JSON。支持高质量缩放，对照查看，所见即所得！

**核心亮点：**

**1\. 极致转化，秒变 Markdown。**无需复杂操作，在统一输入框内粘贴网址，无论是图文并茂的深度长文，还是结构复杂的动态页面，MinerU 都能将其精准转化为逻辑严密、结构清晰的 Markdown 文档。

**2\. 深度解析，继承技术优势。**该功能**充分继承了 MinerU 在公式、表格识别领域的领先优势**。网页中嵌入的复杂科学公式、嵌套表格均能被精准还原，确保解析后的文档具备极高的可读性与专业性，完美适配学术研究与专业分析场景。

**3\. 韧性解析，自带“重试”机制。如果动态加载出现问题，系统会自动切换重试。无论是复杂的交互页面还是难以提取信息的站点，在 MinerU 面前统统都要乖乖变回结构化的数据。**

**4\. 无惧动态渲染，深度兼容。**针对现代网页常见的 React、Vue 等框架生成的动态内容，MinerU 展现了强大的解析能力。告别乱码与格式错位，让“所见即所得”成为现实。

**5\. 纯净体验，去冗留精。**系统会自动识别并过滤广告干扰、侧边栏杂讯及无关链接，剔除冗余信息，只为您提取最核心、最纯净的高价值内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVetPrwHQ2AaqicYicsIpeRruvNhrHwTFHkzpPFPaaQgv4Y7X80RFa3rkqLSo54X4l0OsnQEe9KNk4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVetPrwHQ2AaqicYicsIpeRrughWJuwyMMoyiav3HZGnAem7qGNzr50Gm32haBeAGhhnOczT81TURObg/640?wx_fmt=png)

  
目前，网页端与桌面客户端我们提供了每人每日 100次的免费配额，助您轻松提取网页，让网页信息的获取与利用效率实现指数级飞跃！

💡 小贴士：如果遇到无法直接访问的“深网”内容怎么办？

别担心！MinerU 除了支持 URL 链接解析，还支持本地 HTML 文件上传解析。你可以通过以下简单的手动步骤获取动态网页的 HTML，再交给 MinerU 处理：

1\. 打开开发者工具：在页面上点击鼠标右键，选择“检查”（Inspect），或者按快捷键 F12（Mac 为 Cmd + Option + I）。

2\. 定位到根节点：在弹出的面板中切换到 “Elements”（元素）标签页。

3\. 定位并复制HTML：滚动至顶部，找到 <html> 标签，点击右键选择 “Copy” -> “Copy outerHTML”。

4\. 保存为本地文件：将内容粘贴至文本编辑器（如记事本、VS Code），保存为 .html 文件即可上传至 MinerU 进行解析。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/hkUN8E95VAVetPrwHQ2AaqicYicsIpeRruE7Kib6Gb3RYqeAdroEwZsPAoaPgicSCEiaP5PKhPMUiaPetF5sFuzGlgTQ/640?wx_fmt=gif&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**开发者福利：API 侧的“逻辑大一统”**

  

如果你是开发者或研究员，面对海量的资讯采集、竞品追踪或学术文献收集任务，手动操作显然不是长久之计。这时候，MinerU 的 API 接口便是为你量身定制的“自动化利器”。

  

为了让开发者的逻辑更简洁，我们重构了输入流程，**多源输入，一个接口搞定** 。不同于网页端与桌面客户端注重即时交互的体验，API 侧更强调**逻辑的整合性**：我们特意将 HTTP 文件上传与 URL 上传接口进行了“大统一”。无论你输入的是 PDF 文件还是网页链接，一个接口即可完成所有分发，极大降低了代码维护成本。

  

在 API 侧，我们赋予了数据解析前所未有的“透明度”，**透明化解析，进度尽在掌握** 。响应包中新增的 `fetch_status` 字段，让你能实时洞察每一个网页的抓取状态。无论是复杂的动态渲染过程，还是特殊的请求反馈，后台数据一目了然，让你的程序逻辑更加稳健可靠。

  

配合系统自带的“智能路由”功能，不管是混合了 PDF、网页还是截图的复杂任务，MinerU 都能在后台自动并行处理，最后为你吐出整齐划一的高质量数据。

  

你可以试着将它接入 Dify 或 Notion 等工具。只需简单配置一下 API 密钥，MinerU 就能化身为你的自动化“知识中枢”，在后台静默而高效地收割全网干货。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVetPrwHQ2AaqicYicsIpeRrua0ZYWoxMZZ8rQV8Dx82ltYgev9KicorhF50Nr9ZSJBl17MCzyXlus3w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVetPrwHQ2AaqicYicsIpeRruOA7hpRTvFqMqHHV2vB8Ak8tBJKG6icvJck6gbGFkhrqFNOfKAq6rRsw/640?wx_fmt=png&from=appmsg)

（API调用方法，详细内容可查看 MinerU 官网 API 文档）

  

**结语：**MinerU 正在努力打破文档、网页与大模型之间的信息围墙，致力于成为您工作流中不可或缺的“信息获取中枢”。无论是为 RAG 知识库提供不失真的 Markdown 语料，还是为 Agent 工具链输送结构化的业务字段，MinerU 始终坚持 **“AI-Ready”** 的核心目标。

  

现在就去登录网页端或更新桌面端，让互联网碎片秒变高质量 AI 资产！ 如果您在使用中发现解析不准，请直接“点踩”反馈。您的每一条意见，都是我们打磨“数据神兵”的动力！

  

![](https://mmbiz.qpic.cn/mmbiz_gif/vRlf8RwCJiarFwxlxOCGI8L2cBdfyibibiby1FADAgJNibUvl4HfnavdWx2XfDTLbqm7ibYOeSjaxCtQTyic7exDXo5Aw/640?from=appmsg)

点击 阅读原文 ，立即体验 MinerU 网页解析新功能！或者浏览器访问：

https://mineru.net/OpenSourceTools/Extractor

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/G0ExkYMwshQa9fq3RIR5aQJOGPtMUFT7kVgADhEOok0TqMEp7GOY8x7uPN6JBDwibczs5iccH7nARdtuL5jVicQlQ/640?from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END  

  

**相关阅读：  
**

  

  

[强强联手！MinerU携手沐曦完成适配，曦云C500推理性能加速60%](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551297&idx=1&sn=3b6a50dd0cb7570f8d26a093d8bb4e8b&scene=21#wechat_redirect)

2025-12-24

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUErF25RmMkX9p2nREV80RribvGPYw6MmAX2ibXhlcibtYRwN5PXZRib6cNCnNBRiaH16eSxgWxYsZnx0g/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551297&idx=1&sn=3b6a50dd0cb7570f8d26a093d8bb4e8b&scene=21#wechat_redirect)

[超实用！MinerU新增3个新功能，支持文档逐块修正](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551268&idx=1&sn=d972ba5b345812a8203cd08118fba64f&scene=21#wechat_redirect)

2025-12-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVc92v8qoKfwcZoINhJ6eSHOajibSH3cMjOlmhMo7Gv32hXiaOO2wQmofxia1kXDP5FvmwOib0BgLicZDQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551268&idx=1&sn=d972ba5b345812a8203cd08118fba64f&scene=21#wechat_redirect)

[打破桎梏！MinerU-HTML重构网页提取范式，开源超大规模高质量多语言语料AICC](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551242&idx=1&sn=ec6d3a0ef6b0cacbd6c020cd5bf96cc0&scene=21#wechat_redirect)

2025-11-26

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAW3rrHt9Q1sAxTkMttibnTqlCzSUPj4rBjYG74G5mX45ZMEGeERNI97ibMGOmvvKkWGMvEKtEkPhMdA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551242&idx=1&sn=ec6d3a0ef6b0cacbd6c020cd5bf96cc0&scene=21#wechat_redirect)

[MinerU又双叒更新了！化学解析×多模式翻译等多种功能上线！文档解析处理爽到飞起！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

2025-08-08

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXjL2XwkNOQoBBNjT5kzEgTyWAumU6Y7sdbgsxLgByGO8XbrzT7AOhs8LlQhV1ph0m76jjMmKVkhA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550993&idx=1&sn=7dcaaebd9cec296ccf2548d6257bf411&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言