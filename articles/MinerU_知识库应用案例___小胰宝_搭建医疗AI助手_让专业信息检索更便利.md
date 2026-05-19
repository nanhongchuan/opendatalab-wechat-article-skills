     MinerU 知识库应用案例 | 小胰宝：搭建医疗AI助手，让专业信息检索更便利 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU 知识库应用案例 | 小胰宝：搭建医疗AI助手，让专业信息检索更便利
========================================

原创 OpenDataLab 2025-03-11 20:01 上海

> 原文地址: [https://mp.weixin.qq.com/s/jHLU74CLCGRX55hT5UFcgA](https://mp.weixin.qq.com/s/jHLU74CLCGRX55hT5UFcgA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

经常逛 MinerU 社区的朋友会发现，里面卧虎藏龙，总是充满惊喜。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUBB9h4qa4JeYnUsUwwGLSTQYOq286qUg42KxJMTbzAGJkeEsicNPj3R1melxrO8cGUNJtVAD8k4Tg/640?wx_fmt=jpeg&from=appmsg)

最近，小编就发现了一个很不错的项目——**小胰宝**，它基于MinerU、大模型、知识库系统等，构建了一个专为胰腺癌患者提供诊疗、护理等知识服务的**AI智能助手**，这不仅是一个造福患者的公益应用，也是RAG技术在垂直场景应用的代表案例，快来看看它是怎么做的吧，相信一定能给你带来启发。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Wow.png)

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

****产品框架及文档解析引擎介绍****

小胰宝基于**MinerU**，二次构建了深度优化的文档解析引擎 **Mineru-xyb**，实现医疗文档的多模态解析与知识萃取，形成标准化知识库；然后依托多种大模型，结合混合RAG框架（集成检索增强、医疗专用插件及API网关）实现知识库的高效检索、智能推理，最终构建跨平台服务矩阵，支持微信公众号、社群机器人、小程序等多样化终端接入，为胰腺癌疾病诊疗提供便捷的知识服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUBB9h4qa4JeYnUsUwwGLSTNDS1ibGjQA1jjbmYxzCZBx9MJp7SznyQ4xq6oFRpozHuNdtXyfn6lcA/640?wx_fmt=png&from=appmsg)

  

 文档解析引擎 Mineru-xyb，打破RAG中医疗相关文档的"次元壁"

在知识库文件准备环节，小胰宝团队总结了3个主要痛点：

**⚠️ 传统解析方法让30%关键数据流失**

**⚠️ PDF文档的图片/公式成"信息黑洞"**  

**⚠️ 单文档转化效率太低**

  

在对比多个工具后，他们选择 **MinerU 文档提取工具**用于知识库文件准备，并在文档解析引擎构建中，提出3个关键要点：

**1\. 提升文档处理效率：**解决传统 RAG 工具在处理 PDF 等格式文档时的信息损耗问题，努力保持保留文档中的图片、公式等关键信息的完整性；

**2\. 降低部署成本：**适配云端免费服务资源（腾讯Cloudstudio/魔搭社区等），一键部署，低成本转化；

**3\. 提供企业级存储方案：**结合 Sealos 和 Minio，支持 S3 配置，确保图片链接的长期可用；

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVVTKnCq5DTNRFwWbORU8EcbGzA7mh3LoSuh0dddYsvVah3N1KlwPITibR9YiaNZpWcIos2cY3IIhlg/640?wx_fmt=jpeg)

小胰宝图文混排效果

最后，他们打造了这样一个文档解析引擎：  

**1\. 智能解析层**

• 支持多种知识库文档格式，高质量转换为markdown格式

• 完整保留表格/分子式/关键示例图片/指南图片

**2\. 云端架构**

• 基于Sealos+Minio的弹性架构

• 高质量连续批量处理混排文档

**3\. 评估体系**

• 首推RAGAS医疗专项测评

• AI自评估准确率校准系统

**新的架构，使小胰宝项目文档能力较传统方法，实现了多方面的突破：**

40%33%27%技术突破成本控制图文还原度处理速度

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****体验入口与项目介绍****

目前他们已将自己优化后的文档解析引擎 Mineru-xyb做了开源，需要的朋友可以自取，GitHub地址：

_https://github.com/PancrePal-xiaoyibao/MinerU-xyb_

  

**小胰宝项目介绍**

据创始人介绍，小胰宝是一个病友自助开始的项目，2023年创立，2024年中开源发展，于当年年底捐献给天工开物基金会，2025年升级为社区化，由基金会和社区管理委员会CMC管理，成为纯血版的AI类公益开源项目——小X宝社区。

  

社区目的是推动AI技术和RAG应用的普及化，集合力量助力25+癌种患者，立足患者公益服务，有效减少医患信息差。目前已经推出了小胰宝助手，小肺宝助手，小萌宝助手，小粉宝助手，小胃宝，小妍宝助手等项目。

![图片](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****MinerU探索者计划****

MinerU 开源项目提供了丰富的产品形态，包括本地部署的模型代码、批量调用的API、桌面客户端、在线体验的网页入口等，提供了丰厚的创新“沃土”，欢迎大家探索、开发更多有意思的衍生研究与应用。可点击下方链接提交、分享您的成果，让更多人了解、使用。

  

**MinerU 官网：**

_https://mineru.net/_

  

**MinerU 衍生****成果提交**（或浏览器复制网址打开填写）

_https://aicarrier.feishu.cn/share/base/form/shrcneaKr8tecz3agwNa90Xqh0g_

  

![](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png)

END

  

  

**相关阅读：**

  

  

[

MinerU大上新！桌面客户端、新版API、国产化适配版全都有，更多功能等你解锁

2025-01-21

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUKVun2ZibS4hY5pJBgBL1SwjZwQnCpZGXK3S5NjReNlpg01xwpV4rvW676SChOO9uSwTzzQRWdhGA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549851&idx=1&sn=0c3208dfa19356b9044d2ff7d6fa6b93&scene=21#wechat_redirect)

[

免费下载 | 百万机器人真机数据 AgiBot World 上架OpenDataLab

2025-01-20

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVxCL9HyEOiandKBYBarhialJnjOw4jBdNbZZYQHqLIZfnPOno1NKH1Bw0WR5A6Aq41QT78npbHukEQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549824&idx=1&sn=fd59d9092bbea81dc73b34407923dce2&scene=21#wechat_redirect)

[

多语言语料库“万卷·丝路”发布，AI赋能共建“一带一路”

2025-01-09

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXk2oA4FMPVDMdcDVCU27qrcoZJcm8XvX9zEvQMy5Nico74zGOeIyvq1Doc1Zr5ly2RYm8TavQR3rg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[

上海人工智能实验室大模型中心 | 全球招聘

2024-11-12

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXnHSa53PEJIj7ibXib1kJnduh9icBX5VGrvjCIAV1Yib3ZdXWnh8p8zC3oPibdlPH1yvMnhI9nicegxL2w/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247548246&idx=1&sn=43e054a06b4f3db074ac8d369b26b616&chksm=c124a049f653295fbaaed9541aa8d351efdade89efdb7b3431ec47b3fc28f906fb3c5c0cea3a&scene=21#wechat_redirect)

[不是吧？这么好用的开源标注工具，竟然还有人不知道…](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

[2024-08-22](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6jsZJmjym44k1KnuBibIibwV47VtuvqyerwKmT7UnBgAp4eL1Uqic7ulsE0NcPnlKtRNSGyGjiasYDiaw/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言