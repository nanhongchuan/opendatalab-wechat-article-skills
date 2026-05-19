     干货满满丨MinerU 3.0 系列更新：一次不止于模型的全面进化 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

干货满满丨MinerU 3.0 系列更新：一次不止于模型的全面进化
=================================

原创 MinerU OpenDataLab 2026-04-20 19:53 上海

> 原文地址: [https://mp.weixin.qq.com/s/l9MUQXDwcYxhjalwyxMtWg](https://mp.weixin.qq.com/s/l9MUQXDwcYxhjalwyxMtWg)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

  

随着 MinerU2.5-Pro 模型在 OmniDocBench 1.6 上取得 SOTA 成绩的发布，大家都在询问我们：MinerU 开源项目什么时候能真正把这个超强模型接进来，跑在实际的文档解析项目里？

  

好消息：**最新发布的 MinerU 3.1.0 开源项目已经完成了对 MinerU2.5-Pro 模型的适配，正式发布！![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Party.png)**

**● MinerU 开源模型获取地址：**

**https://github.com/opendatalab/MinerU**

**● HuggingFace demo 体验入口：**

**https://huggingface.co/spaces/opendatalab/MinerU**

**● ModelScope demo 体验入口：**

**https://modelscope.cn/models/OpenDataLab/MinerU2.5-Pro-2604-1.2B**

**\* MinerU线上服务正在快马加鞭适配中，敬请期待！**

**这次更新并不只是简单“接入一个新模型”，而是围绕解析能力、系统架构和工程可用性，带来了一整套更底层的重构和升级。如果把这次更新说透，那便是：****MinerU 3 系列开源项目，不是“多加了几个功能”，而是从一个文档解析工具，往大规模、可部署的工业化文档解析基础设施又推进了一步。**

过去很多人理解 MinerU开源项目，更多还是从“PDF 转 Markdown”“公式转 LaTeX”“表格转 HTML”这样的能力层面看它；但 3系列之后，它明显不只是解决“能不能解析”的问题，而是在解决“能不能稳定跑、能不能大规模跑、能不能在真实业务里跑”的问题。我们在README 对这次升级讲的也很直白：**这是围绕解析能力、系统架构和工程可用性的系统升级，而不是一次零散补丁。**

目前，开源项目版本与模型版本彻底解耦。模型可以持续演进，从 2.5 Pro 走向更高版本，但 MinerU 开源项目本身作为解析系统，不需要随着模型变化反复重构，而是可以稳定承接新的能力。这种分层，使它不再只是依赖模型的工具，而开始具备基础设施的特征。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAaqR2uWYYH2B7gw6oXhwrX5hPXjA3CarV9fPxDp4vlRyecgGibhF0BSibpoB14qbiaDIDow9sCAUG3ojXDudjJEcvqibgTlhf0Bkak/640?wx_fmt=png&from=appmsg)

配图来源：NanaDraw流程图生成器：https://shannon.science/nanadraw

  

在这个前提之下，再看 MinerU 3.1.0 的其他变化，就会发现它的整体方向已经发生了明显转向：

  

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAYrWefNvQjnGCYSJAzYq5xzaqO9AOzNGgQy9Iq7fzKUY0PQU49P7KGpPbUlSdibKFFibDl7qWOyibicwQx2A1742XPw42YwB9fHUnc/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**开源协议更新，商业用途限制放宽  
**

  

首先是协议从 AGPLv3 切换到了基于 Apache 2.0 的 MinerU 开源许可证。表面上看，这只是一次许可证调整，但对开源社区、开发者以及中小企业来说，它带来的实际利好非常直接——接入门槛更低了。

  

该开源许可证现在为开源使用、二次开发以及一般商业集成释放了更大的空间。**对于绝大多数开发者、创业团队和中小企业来说，只要在合规前提下，可直接用于商业用途，无需取得我们授权，可以更放心地把 MinerU 用到自己的产品和业务里，**而不需要一开始就被复杂的授权问题拦住，让更多人先用起来、接进去、跑起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAaEZs868YSiczZVmPZ3Ggu9KT5lxI7wjb8CVl1dP576YeuBTWy2BRdIvDLCJiaU89HA2JUBKz7m7EIYKtpAkxiaFQj8BMs1el2AFU/640?wx_fmt=png&from=appmsg)

配图来源：NanaDraw流程图生成器：https://shannon.science/nanadraw

  

当然，这里也需要说明，MinerU 当前采用的并不是标准 Apache 2.0，而是一个基于 Apache 2.0 并附带少量额外条款的项目许可证。它的整体方向是放宽，而不是收紧。只有在少数超大规模商业化场景下，项目方才保留了进一步的授权要求。比如，月活跃用户超过 1 亿、或月总收入超过 2000 万美元的大型商业主体，通常需要另行取得商业许可；如果是基于 MinerU 向第三方提供在线服务，也需要在产品界面或公开文档的显著位置明确标注使用了 MinerU。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAYCzic3LhLDK5fRX5Uxvk2zzSkPZRuR4Gq8wiaYKdz0ZtibuFw7uiciaSzWAafxaerovrK6UDGq6eaQzgmBOAWyNshCXIv2dqDXUTbg/640?wx_fmt=png&from=appmsg)

**向 AI 标准件进发：支持多种文档格式原生解析  
**

  

===

与此同时，从系统视角来看，MinerU 的角色也已经发生了变化。它不再只是一个前处理工具，而是开始成为 AI 系统中的标准组件——一个可以被稳定调用、持续存在的能力节点。这种变化在“数据入口”这一层体现得尤为明显。

  

**MinerU 3 系列开源项目正式补齐了对 DOCX、PPTX、XLSX 的原生解析能力，而且是在无幻觉前提下完成结构还原。**过去，很多文档处理流程其实都绕了一大圈：Word 往往要先转成 PDF 再解析，PPT 往往要先转图片再做 OCR，表格文件也常常要经过额外格式转换后才能进入后续链路。这样做的问题并不只是精度受损，链路本身也会变长、变重，过程中还会丢失不少原始结构信息。

  

而原生解析把这条路径大幅缩短了。除了精度更高、结构还原更完整、能够避免大模型式“幻觉”之外，它在工程上也更轻：一方面，相比“先转 PDF / 图片再解析”的传统方案，整体处理速度可以实现数十倍提升；另一方面，这条链路本身几乎不占用 GPU 资源，资源消耗更低，也更适合高频、批量、在线化的文档处理场景。换句话说，MinerU 现在解决的已经不只是“能不能解析”的问题，而是“能不能以更低成本、更高吞吐地稳定解析”。

![](https://mmbiz.qpic.cn/mmbiz_png/uo0n2KqOLAb2FyaHCAP3683sZKWHSfJV409goiaY8gHkCdIvibibf9D8oEwsnfpX2rbhmxuriaNWxgguibYOEJBibXBOMiaSc4VicTXSx9nfyvz2RFw/640?wx_fmt=png&from=appmsg)

配图来源：NanaDraw流程图生成器：https://shannon.science/nanadraw

  

这背后带来的变化，其实是数据进入 AI 系统方式的改变。文档不再需要经过多轮中转和格式牺牲，才能勉强变成可处理对象；现在，它可以直接进入解析系统，并直接输出结构化、可用的数据结果。这种变化正在把文档从静态文件重新变回系统里的数据源，正在重塑 AI 系统的数据入口。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAbZnVLSN8XSsia1aBqxFlVGS9kr2tkuZUKt9sq4nfjse2mZTVSOkNuQj2hibBmicIaOqiaLRJhHMP7UcRukaiaVTbLJ8x2mjMUQaoIk/640?wx_fmt=png&from=appmsg)

**大规模任务问题，逐个击破：降显存、多机多卡、高并发  
**

  

===

如果说前面的变化更多体现在解析能力上，那么 MinerU 3 系列开源项目更深一层的升级，其实发生在工程侧。这次更新明显在回应一个长期存在、但过去常被忽视的问题：一个开源解析系统，怎样才能真正跑进生产环境，并且稳定地跑下去。

  

围绕这一点，MinerU 3.0 在部署形态和运行链路上都做了系统性增强。**它不仅支持单机多卡，也进一步具备了面向多机多卡场景的扩展能力，配合自动****负载均衡****，可以更从容地应对高并发请求和大规模任务处理，把整体吞吐能力拉到一个新的水平。**与此同时，通过对推理链路的持续优化，系统整体速度也获得了数量级提升。这样的变化不只是“更快了”，而是意味着 MinerU 开始具备了承接真实业务流量的工程基础。

  

另一个关键变化发生在长文档处理上。相比 MinerU 2 系列主要依赖高内存机器来支撑超长文档解析，例如在 128GB 内存环境下完成约 3000 页长文档处理， MinerU 3 系列更核心的突破是把问题转向了内存使用方式本身的优化。通过滑动窗口机制与流式落盘配合，长文档解析不再需要一次性将全部中间状态压进内存，而是以更平滑的方式持续推进任务执行。部署后，单个 worker 在 8GB 内存条件下，也可以稳定处理上万页级别的长文档。这不仅显著降低了部署门槛，也让系统在长时间运行时更稳定、更可控。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uo0n2KqOLAYPeMCZibKI6mb1oxiaYR8990yWtT45DQhTdibBnEwpoKKvCiaYH4OXXtlibQiar62ibMKsJ44Jyq3VnwK53UK8IlqDQkeuP5dlFI7o8M/640?wx_fmt=jpeg)

配图来源：NanaDraw流程图生成器：https://shannon.science/nanadraw

  

这些能力组合在一起，使得 MinerU 开源项目已经具备了承载大规模文档处理任务的工程基础。它不再只是一个“解析工具”，而是在向“Agent 时代的数据解析基础设施”演进。一方面，它提供了更轻量的调用方式，使解析能力可以更自然地嵌入到 Agent 和 workflow 中；另一方面，它的稳定性和扩展能力，使其可以作为系统中的长期组件存在。当模型能力与系统能力叠加之后，文档不再只是被读取，而是可以被结构化、被计算，并直接参与到 AI 系统的运行中。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uo0n2KqOLAZq5FcRWA8Ldr5PfQWWSjMK3Dic9CdpdYOSCfAKYHU9OaBta9Cs7NibzrHtUiapjX7n5HoNJpJEIpGZFFzhAUDuTm67TbvQfMrlJk/640?wx_fmt=png&from=appmsg)

**总结  
**

  

===

**如果需要对这次 MinerU 3 系列开源项目的升级做一个总结，可以说它完成的不是一次简单的版本升级，而是一次从工具到工业级方案的跨越。**它不仅提升了解析能力的上限，也解决了规模化运行的下限问题，使文档解析从“能用”走向“可用且可规模化使用”。在这样的基础之上，企业级系统的RAG 的效果会更加稳定，Agent 的执行会更加可靠，而数据处理的成本也会被重新压缩。更重要的是，数据终于开始以正确的结构进入系统，成为真正可以被模型理解和调用的资源。

  

目前，MinerU 的生态边界正在被快速拉宽。它不再局限于“文档解析”这一单点能力，而是开始完整覆盖 skills、RAG、workflow 以及 OpenAPI 的整条应用链路。这意味着解析结果可以更自然地进入后续的数据处理、调用和应用流程中，而不需要额外的适配层。与此同时，**基于开源项目演进的 MinerU 在线产品，也正在持续跟进这些最新能力，并加快完成相关适配与产品化落地**。如果大家希望感受 MinerU2.5-Pro 模型的强悍转化能力，欢迎访问在线demo进行体验：

● MinerU 开源模型获取地址：

https://github.com/opendatalab/MinerU

  

● HuggingFace demo 体验入口：

https://huggingface.co/spaces/opendatalab/MinerU

  

● ModelScope demo 体验入口：

https://modelscope.cn/models/OpenDataLab/MinerU2.5-Pro-2604-1.2B

\* MinerU线上服务正在快马加鞭适配中，敬请期待！

  

在大模型持续演进的当下，很多人把注意力放在参数规模和推理能力上，但真正决定系统效果的，往往是数据链路是否完整。MinerU 3.0 开源项目所做的，正是补上这条链路中最容易被忽略、却最关键的一环。

  

  

END  

  

**相关阅读：  
**

  

  

[MinerU-Diffusion发布：我们想重新回答，文档 OCR 到底该怎么做](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551745&idx=1&sn=32f28edfba35c37043d66f28dc254890&scene=21#wechat_redirect)

2026-03-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAanjOc0Y7utkLlOWLzhzOIaib1rNGia9egfP05ib0RiaAgQ2eUrSDibh79ssibicAGprFFsUmyeIeH9HuUsuzgb4aWBLFTbQ0upszBh1M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551745&idx=1&sn=32f28edfba35c37043d66f28dc254890&scene=21#wechat_redirect)

[总激励200万！2026 MinerU数据智能与前沿语料挑战赛正式启幕，筑基 AGI4S 高质量语料新高地！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

2026-02-06

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbgD2vP9QPR0XKXLQTSUt6ledgMJyDU6v5WQXrCSpFS4CHCKTChAANic5J0mG9aDyYJZ1icuQ3BflZELSOUP8HDyy1iasz49ianpYo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

[MinerU 实战训练营来了！免费学 MinerU 部署、微调、Agent 搭建](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551728&idx=1&sn=938bbae1c68af433f85ba95267aac517&scene=21#wechat_redirect)

2026-03-24

[![](https://mmbiz.qpic.cn/mmbiz_jpg/uo0n2KqOLAYlsICsvsibibQia2K54IvK5euJhnguRE8JPkLJBHphIVibqZJJCKmFVficcYVMVtrqTibHRB1ENRSMBwFw9iaNn5fwNp4KCrUJmnq3r8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551728&idx=1&sn=938bbae1c68af433f85ba95267aac517&scene=21#wechat_redirect)

[一句话，让你的🦞看懂PDF，MinerU 官方 Skill 来了！附赠开发者“全家桶”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

2026-03-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbZZOF5ZU4633TUhZvib1DtcPjUoonLTDianYHpSU7f41y5eMfmkHsZJ5rvLLa95chfTKAw2iaI4OgZVsJZVBNfXkszm2iaPsxyF2M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言