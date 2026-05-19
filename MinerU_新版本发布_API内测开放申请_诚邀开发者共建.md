     MinerU 新版本发布，API内测开放申请，诚邀开发者共建 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU 新版本发布，API内测开放申请，诚邀开发者共建
==============================

原创 MinerU OpenDataLab 2024-11-08 16:46 上海

> 原文地址: [https://mp.weixin.qq.com/s/\_DXuYAXBvUnzfFIvFztk5A](https://mp.weixin.qq.com/s/_DXuYAXBvUnzfFIvFztk5A)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

AI结构化数据提取开源工具 MinerU 最新版本发布。本次更新进行了大量代码重构，降低了硬件需求，数据提取性能及易用性“双提升”。（点击查看MinerU介绍→[登顶GitHub Trending，开源工具MinerU助力复杂PDF高效解析提取](http://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544657&idx=1&sn=0772359cc3df0033866cada0021f34fd&chksm=c124b24ef6533b58357e67d0f3a774d0fa2d73ad710073935ae5472cefe75881df4aeee989cc&scene=21#wechat_redirect)）

  

全新版本 MinerU 接入了新的表格模型 StructTable-InternVL2-1B，表格解析选择更丰富。同时优化了线上Demo使用体验，开放API内测申请，参与“探索者”计划，加入MinerU开源共建，将有机会赢得精美周边及算力支持等丰富奖励。

  

**MinerU项目地址：**（点击文末“阅读原文”直达）

_https://github.com/opendatalab/MinerU_

  

**MinerU Demo 地址：**

_https://opendatalab.com/OpenSourceTools/Extractor/PDF_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

****MinerU最新版特点****

  

 重构文档处理模块：提升排版适应性与识别精度

● 重构**排序**模块代码，使用 _layoutreader_ 进行阅读顺序排序，确保在各种排版下都能实现极高准确率；

● 重构**段落拼接**模块，在跨栏、跨页、跨图、跨表情况下均能实现良好的段落拼接效果；

● 重构**列表和目录识别**功能，极大提升列表块和目录块识别的准确率及对应文本段落的解析效果；

● 重构**图、表**与**描述性文本**的匹配逻辑，大幅提升图注和脚注与图表的匹配准确率，并将描述性文本的丢失率降至接近0；

  

  

 模型能力全面升级：多语言、布局、公式、表格解析效率倍增

● 增加 **OCR 的多语言支持**，支持繁/简中文在内的全球 84 种语言的检测与识别，OCR 语言支持列表清单：  

_https://paddlepaddle.github.io/PaddleOCR/latest/ppocr/blog/multi\_languages.html#5_

● 集成最新 _**PDF-Extract-Kit 1.0**_ 版本，文档布局检测、公式识别、表格识别准确度、速度更上一层楼。PDF-Extract-Kit 1.0模型包括：

    - 加入自研的 _doclayout\_yolo_ 模型，在相近解析效果情况下比原方案提速10倍以上，可通过配置文件与 _layoutlmv3_ 自由切换；

    - 公式解析升级至 _unimernet 0.2.1_ ，在提升公式解析准确率的同时，大幅降低显存需求；

   - 正式接入 _StructTable-InternVL2-1B_ 表格模型，支持HTML输出格式；可通过配置文件与 _tablemaster_ 自由切换；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVuXMyVazKmLrGcNStfULPDDg3YpVUK5kicicmWlLcYHLSiaPWSpDUPlGiaZsM7amJpet8LSaHlknSSSA/640?wx_fmt=png&from=appmsg)

（doclayout\_yolo布局检测模型效果示意）

  

  

 显存优化，降低资源需求，大力提升处理速度

● 优化配置文件的功能开关，除已有的表格检测开关外，MinerU 0.9.2版本新增了独立的**公式检测**开关，无需公式检测时可大幅提升速度和解析效果；

● 增加显存回收逻辑及其他显存优化措施，大幅降低显存使用需求。开启除表格加速外的全部加速功能(layout/公式/OCR)的显存需求从16GB降至8GB，开启全部加速功能的显存需求从24GB降至10GB；

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****Demo使用体验升级，API开放内测申请****

  

 支持多种文档格式，可解析在线PDF

MinerU 线上Demo新增支持 doc\\docx\\ppt\\pptx 4种格式文档提取；支持输入PDF文件url链接自动解析（url需要以.pdf结尾）；此外，文件可以**批量上传**，在文件列表统一管理所有任务，查看、筛选、删除提取记录更方便。

  

**MinerU Demo 地址：**

_https://opendatalab.com/OpenSourceTools/Extractor/PDF_

  

**划重点！！！**大家呼声很高的MinerU API初版已推出，正在小范围体验和试用，有需要的朋友可添加小助手报名，获取密钥口令。

![](https://mmbiz.qpic.cn/mmbiz_gif/dTxkmqQ6SznicxdpxUKbBLoJzSlpvNfyfeGn8PIB1Wx5kSbhECECnibDwEYfQrkyyjQibSo1zMUX5sJo4KzcibF9GQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD73YXswn0XWT4bLm7ClibnIcHJtZnNo5k8ZZlJYQ0S7knjYKHXILd6amZAO3UTULPiardEya7yrCJ5g/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****“探索者”开发激励计划****

  

OpenDataLab社区卧虎藏龙，很多小伙伴凭借高超的代码、算法能力，轻松“玩”转 MinerU 项目，并且衍生出了不少有意思的应用。

  

为了感谢大家的支持，激励更多伙伴参与共建热门开源项目——MinerU，同时给予贡献者正式荣誉认证，我们启动了**“探索者”开发激励计划**，完成以下任一项内容，即可以获得奖励：

**● 发布MinerU **原创技术文档或视频** 1个以上**

**● 提交高质量Github pr 并**成功合入**3次以上**

**● 创作MinerU 衍生项目或应用 1个以上**

  

**探索者奖励包括但不限于：**

● 价值300元的阿北精美周边大礼包  

● 认证证书

● 顶级项目支持（算力、宣传等资源）

● 技术直播讲师邀约

  

**同时会评选出** **3 位****年度最有实力的贡献者，提供****岗位招聘****、****学术合作****、****项目赞助****等绝对超值的专享权益。**

  

**快点击下方链接提交你的成果吧：**

_https://aicarrier.feishu.cn/share/base/form/shrcneaKr8tecz3agwNa90Xqh0g_

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAX1OakmNeZfESnKeicwibbx4b0IsHOvX7ibfrPzRLRO6Y5RMicNxkG5bVotp0qHmVm6p9ibCG3Njy4NUibQ/640?wx_fmt=png&from=appmsg)

  

**相关阅读：**

  

[

谁才是你最爱的 AI 数据平台？在线等，急！（有奖调研）

2024-10-22

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXKI92aL5FN2vKAnaRfdovBmN4j9Fsqd37rYiaxOGVzls4CMGNowDPkuWPAfuNn4HVibQgL6VPWN9LA/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247547121&idx=1&sn=dc215a4f50f9a9bb79bd5c4fd815d982&chksm=c124a5eef6532cf805a0ecd0864fbbd53c5147bbc57291bc6824f1f2dafe8429ecea0d076a09&scene=21#wechat_redirect)

[

🎉复杂PDF提取开源工具MinerU Github star突破10k!

2024-08-27

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD4w3aXKibBlOOhOGpXtudB0M30ibLSRU0lmp6AsptEpmLCCQaVyA3mePfHj9T0njoAA0nKDaXogAibEg/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544662&idx=1&sn=ca57a60ff921687c6afccbbbb78af575&chksm=c124b249f6533b5fc7bae815c424482b6a54eefe49605786437e2995c741b97823a9324fcc1f&scene=21#wechat_redirect)

[

不是吧？这么好用的开源标注工具，竟然还有人不知道…

2024-08-22

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6jsZJmjym44k1KnuBibIibwV47VtuvqyerwKmT7UnBgAp4eL1Uqic7ulsE0NcPnlKtRNSGyGjiasYDiaw/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

[

赌你一定想要！OpenDataLab首款大模型多模态标注平台Label-LLM正式开源

2024-06-06

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD7kMmQsy4kYAm3oP4iaX5wQTUBloGx5Qm1Rtxq8ibUh0oFnyF2TD8ib6883KMKOSf6j3odOhibVHSGTuQ/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247535978&idx=1&sn=e0ac60cf8b43d21637d18e3d45afd89e&chksm=c10cdf88f67b569e67c6d2e0f3d62fa8e6f4ed81feb656a84fa0ad56ebc537e34e23c2894a28&scene=21#wechat_redirect)

[小小视频-文本标注，LabelU轻松拿下！](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247533524&idx=1&sn=41ef0eb7c80443449b0c966fbc007ee3&chksm=c10cd136f67b5820b59a3789b5d3e64c9e1de47d0fa75395e100b30157915d6b41091493eeb3&scene=21#wechat_redirect)

[2024-04-02](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247533524&idx=1&sn=41ef0eb7c80443449b0c966fbc007ee3&chksm=c10cd136f67b5820b59a3789b5d3e64c9e1de47d0fa75395e100b30157915d6b41091493eeb3&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD48YIXJzOwOwibpAWMHsKWGicbjFwFIqiaKC1icK51laHF4e7yU5JDly3tmLWaKib4BZ4FMF2C8JibtIlQQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247533524&idx=1&sn=41ef0eb7c80443449b0c966fbc007ee3&chksm=c10cd136f67b5820b59a3789b5d3e64c9e1de47d0fa75395e100b30157915d6b41091493eeb3&scene=21#wechat_redirect)

  

  

  

  

  

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言