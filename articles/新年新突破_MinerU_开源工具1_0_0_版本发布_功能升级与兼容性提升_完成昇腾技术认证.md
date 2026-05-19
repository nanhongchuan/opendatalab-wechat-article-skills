     新年新突破：MinerU 开源工具1.0.0 版本发布，功能升级与兼容性提升，完成昇腾技术认证 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

新年新突破：MinerU 开源工具1.0.0 版本发布，功能升级与兼容性提升，完成昇腾技术认证
===============================================

原创 MinerU OpenDataLab 2025-01-10 22:56 上海

> 原文地址: [https://mp.weixin.qq.com/s/BuHTAcBeRc-3kIFTtL\_\_FA](https://mp.weixin.qq.com/s/BuHTAcBeRc-3kIFTtL__FA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

一元复始，万象更新。2025年伊始，MinerU以扎实的技术成果揭开新一年的篇章：  

● MinerU最新开源工具1.0.0 正式版发布，全新API接口方便灵活调取，更广泛且全面的兼容性适配；

● 与此同时，MinerU项目已经通过昇腾相互兼容性技术认证，切实为行业打造出可信可靠的文档提取转化方案。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****MinerU推出最新正式版本，功能升级并完成Linux系统兼容性适配****

经过团队的不断努力与开发者社区的积极参与，MinerU推出1.0.0开源版本，标志着本项目达到了一个重要的里程碑。

这一版本中，我们加入全新API接口：

*   对于数据侧API，我们引入了Dataset类，旨在提供一个强大而灵活的数据处理框架。该框架当前支持包括图像（.jpg及.png）、PDF、Word（.doc及.docx）、以及PowerPoint（.ppt及.pptx）在内的多种文档格式，确保了从简单到复杂的数据处理任务都能得到有效的支持。
    
*   针对用户侧API，我们将MinerU的处理流程精心设计为一系列可组合的Stage阶段。每个Stage代表了一个特定的处理步骤，用户可以根据自身需求自由地定义新的Stage，并通过创造性地组合这些阶段来定制专属的数据处理流程。
    

同时，我们还增加了自动语言识别功能：

*   通过引入全新的语言识别模型， 在文档解析中将lang配置为auto，即可自动选择合适的OCR语言模型，提升扫描类文档解析的准确性。
    

此外，我们还进行了更全面的兼容性适配：

*   通过优化依赖环境和配置项，确保在ARM架构的Linux系统上能够稳定高效运行。
    
*   深度适配昇腾NPU加速，积极响应信创要求，以安全可靠的技术助力科研、政企用户迈向文档数字化新高度。
    

为了更加高效地满足特定场景的需求，我们在1.0.0版本的基础上，开发了一个经过深度优化的高性能版本，主要面向重要的科研合作用户进行提供。

**MinerU 国产化开源可用版本代码仓库：**

_https://github.com/opendatalab/mineru_

**MinerU 国产化高性能版本申请入口：**

_https://aicarrier.feishu.cn/share/base/form/shrcnb10VaoNQB8kQPA8DEfZC6d_

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****MinerU 通过昇腾相互兼容性技术认证****

日前，MinerU通过昇腾相互兼容性技术认证，取得昇腾技术认证书，标志着其在国产化适配和性能优化方面迈出了重要一步，为充分发挥国产基础软硬件协同的综合优势，以及为开发者提供更安全可靠的文档转化能力奠定了坚实的技术保障。

  

目前，MinerU已在昇腾平台上实现高效运行，其性能表现与Nvidia平台相当，可为机器学习、自然语言处理、大模型训练、知识检索等领域提供自主可控的文档数据解析引擎，高效解决多源异构数据清洗与处理的技术难题。

  

这一认证彰显了MinerU在数据解析技术领域的领先地位，同时深度挖掘了国产软硬件协同的潜力，以安全可靠的技术，助力科研、政企用户迈向文档数字化新高度。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****“探索者”开发激励计划****

  

为进一步提升MinerU在社区开发者中的影响力，并激励更多优秀开发者参与其中，我们特推出**MinerU“探索者”开发激励计划**：

**● 发布MinerU**原创技术文档或视频** 1个以上**

**● 提交高质量Github pr 并**成功合入**3次以上**

**● 创作MinerU 衍生项目或应用 1个以上**

  

**探索者奖励包括但不限于：**

● 价值300元的阿北精美周边大礼包  

● MinerU贡献者认证证书

● 顶级项目支持（算力、宣传等资源）

● 技术直播讲师邀约

  

**同时会评选出****3 位****年度最有实力的贡献者，提供****岗位招聘****、****学术合作****、****项目赞助****等绝对超值的专享权益。**

  

**快点击下方链接提交你的成果吧：**

_https://aicarrier.feishu.cn/share/base/form/shrcneaKr8tecz3agwNa90Xqh0g_

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAX1cSzzcgqgekdnQgcmm4oiauZRoa13xtXib4rM3F21HfYw8qCXHDXkG1jiav56ibvKBp6LMqZCbKfLlQ/640?wx_fmt=png&from=appmsg)

  

**相关阅读：**

[

多语言语料库“万卷·丝路”发布，AI赋能共建“一带一路”

2025-01-09

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXk2oA4FMPVDMdcDVCU27qrcoZJcm8XvX9zEvQMy5Nico74zGOeIyvq1Doc1Zr5ly2RYm8TavQR3rg/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[

小工具如何影响大模型？MinerU四个月获2万星标！OpenDataLab用户破10万

2024-12-05

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaV4aNQ1sKoNTsNwZibpiadkONfsyUmpricMMNWIf9V6QIcEf9leq6giaJ9xA/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549458&idx=1&sn=296de8cace3047a9a2faebb6f61695e3&scene=21#wechat_redirect)

[

上海人工智能实验室大模型中心 | 全球招聘

2024-11-12

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXnHSa53PEJIj7ibXib1kJnduh9icBX5VGrvjCIAV1Yib3ZdXWnh8p8zC3oPibdlPH1yvMnhI9nicegxL2w/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247548246&idx=1&sn=43e054a06b4f3db074ac8d369b26b616&chksm=c124a049f653295fbaaed9541aa8d351efdade89efdb7b3431ec47b3fc28f906fb3c5c0cea3a&scene=21#wechat_redirect)

[

不是吧？这么好用的开源标注工具，竟然还有人不知道…

2024-08-22

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6jsZJmjym44k1KnuBibIibwV47VtuvqyerwKmT7UnBgAp4eL1Uqic7ulsE0NcPnlKtRNSGyGjiasYDiaw/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

  

  

  

  

  

  

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言