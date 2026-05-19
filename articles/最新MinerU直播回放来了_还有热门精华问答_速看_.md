     最新MinerU直播回放来了，还有热门精华问答，速看！ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

最新MinerU直播回放来了，还有热门精华问答，速看！
===========================

原创 MinerU OpenDataLab 2024-11-25 12:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/OH1OtGyZgwBuuG7nKUBDxQ](https://mp.weixin.qq.com/s/OH1OtGyZgwBuuG7nKUBDxQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

11月20日，AI数据超能学院第3期直播，我们邀请了上海人工智能实验室 OpenDataLab数据提取工程师 MinerU核心开发者赵小蒙在线详细讲解了MinerU的项目构成及最新模型效果，以及如何更好地基于MinerU进行二次开发和扩展应用。

  

很多小伙伴意犹未尽，提了很多问题，我们整理了大家比较关心的内容，统一进行回复；另外附上了直播回放，以供参考。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVnSwT2DFTJicSwKduNibp7Bt12SbMbgEdC8cy41Hicgwjkel3tQYnyOgGh4uXRUvrFoNLibrJGXQrsibw/640?wx_fmt=png&from=appmsg)

  

**首先，提问比较多的是，关于MinerU目录与标题的检测识别原理及优化方法：**

**Q**

文档目录是如何检测的？

按我们目前的理解，列表是文本的子集，目录是列表的子集，目前的layout模型只能识别出文本块，我们后面通过line和block的关系，根据一些常见的规则将text块分类为list块和index块，形成了现在的列表和目录，在输出排版的时候会增加额外的换行，让文本不再“坨”在一起，起到优化输出格式的效果。

  

‍‍‍‍

目前的列表/目录识别能力我们基本满意，能够覆盖日常遇到的绝大多数场景，我们也会针对bad case 增加目录识别的规则。MinerU完整的目录规则主函数可以在这里查看：

_https://github.com/opendatalab/MinerU/blob/master/magic\_pdf/para/para\_split\_v3.py_

**Q**

标题只能获取一级吗？有什么办法获取多级标题？

目前标题只能获取一级，比如明显加粗、加大的文本，模型会提取为标题。因为是靠视觉特征进行区分的，不同文档标题特征不同，目前没有通配的方案，获取多层级标题还是比较困难的。

  

我们后续也会考虑增加2到3级的标题提取，大致思路是：获取整篇文档的标题，把所有标题的line收集起来，做个聚类，估计会分到两级或三级，这是个比较折中的方案。

**另外，大家对布局检测相关内容也比较感兴趣：**

**Q**

Layoutreader是用什么方法做的？

Layoutreader是由微软实验室开源的一个项目，最早基于单词来预测顺序，后有研究员改为基于“行”去排序，我们将其改为了基于“块”去排序，大家感兴趣可以去看Layoutreader仓库和论文：

_https://github.com/ppaanngggg/layoutreader_

另外对我们布局检测模型 DocLayout-YOLO感兴趣的，可以查看具体的代码和论文，训练方法和数据集也已经开源，支持微调：  

_https://github.com/opendatalab/DocLayout-YOLO_

**Q**

色块分割怎么判断顺序，是根据语义吗？

MinerU没有采用语义进行拼接，而是纯模型输出的顺序，没做其他处理。其实阅读顺序无非是左到右，或者上到下，是有一些细节特征的，比如前后顺序的色块距离会更近一些，类似这样的特征模型进行自动学习，给出判断。

**Q**

图片caption如何与图片进行关联？

图片与caption关联这个功能我们已经支持了。在MinerU生成的middle.json中间态文档中，会把图片和对应的caption放在一个内容里，可在content list.json中查看。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVBSJ9c3GUZ8eKkxUicI1QvZ47E8f7PWOxehibfkozaFLfBDGZ0uqL5CHNREWoSWwZaOQn7IxiczB5eA/640?wx_fmt=jpeg&from=appmsg)

  

**还有朋友问了提取的文本回溯及样式还原相关问题：**

  

**Q**

文本可以回溯到PDF的具体位置吗？

可以的，在middle.json里每个块都是一个元素，是一个dict，有相应的页码数据和分类，另外还有其在页面中的宽度、高度、坐标等具体位置信息（page\_info字段里能看）。  

  

大家可以通过这个去定位和回溯元素的位置，当前markdown里不支持直接定位，需要自行通过middle.json进行定制。不过这个功能我们也有在考虑，后续会通过不同方式尽力满足大家需求，争取提供定位、二次编辑，如果发现识别有错误，支持标注修改；敬请期待。

  

另外如果你想将提取的数据还原为原来的样式，也能根据middle.json提供的元素坐标、位置参数进行还原。这个是根据内容区块位置来的，不需要考虑分栏因素。

**如何基于MinerU二次开发，也是问得比较多的问题：**

  

**Q**

二次开发，直接把MinerU当作工具调用还是可以自己修改模型？

都是可以的，不过想修改模型的话，需要先在 PDF-Extract-Kit 模型库里查看哪些模型可以改，哪些不可以改。能修改或微调的模型一般都会提供训练、微调代码，比如Doclayout-YOLO可以，LayoutLMv3就不行。

  

另外你也可以直接调用模型或者MinerU输出的中间态文件（分别是model.json、middle.json），调用相关函数，修改pipline，添加自己的逻辑等。其中model.json是 PDF-Extract-Kit 模型输出的文件，主要是进行元素画框分类，包含属性、页码等；middle.json则是MinerU工作流输出的带具体文本、内容、坐标、block\\line\\span等详细信息的文件。

  

同时MinerU提供API供大家直接调用，demo前端代码也开源了，大家可以按需使用。

  

API申请，请关注OpenDataLab公众号，后台回复“API”关键词，即可获取。

  

如果你有MinerU相关衍生应用、项目，或者相关技术文章、功能pr贡献，都可以参加“探索者计划”，提交你的成果，领取奖励：（点击原文直达）

_https://aicarrier.feishu.cn/share/base/form/shrcneaKr8tecz3agwNa90Xqh0g_

**表格\\OCR模型以及magic-doc、magic-html也受到大家的关注：**

  

**Q**

旋转表格能提取吗？跨页表格能合并吗？

旋转表格可以提取，比较简单，识别出旋转之后再旋转过来就可以了。我们也在考虑出这个功能，不过目前团队人力有限，还是更聚焦在提升解析效率和效果上。

  

跨页表合并MinerU不支持，因为特异性比较大，需要根据内容去判断，我们目前不考虑。

**Q**

支持“文本+OCR”混合识别吗？手写体有什么好的识别方案？

在即将发布的0.10.x版本，我们将默认的文本识别能力升级到了文本+ocr混合识别，在文本类型的PDF上效果提升很大，可以期待一下  

**Q**

doc转PDF用magic\_pdf效果好？还是直接用magic\_doc效果好？后续会把magic\_doc和magic\_pdf合在一起吗？magic\_html会更新吗？

doc和docx直接用magic-doc提取会好一点，文本的格式和顺序基本都能保留，但是没有图片的提取能力，目前magic-doc已经处于停止维护状态了，如果有多模态的提取需求，可以试着用liboffice将doc文档转成pdf再使用magic-pdf提取。magic-html功能基本完善了，短时间内不会再有更新。

  

以上就是本次分享的热门问答摘录，完整内容可查看回放

👇

  

  

****传送门：****

**● MinerU Github主页**

_https://github.com/opendatalab/MinerU_

  

**● MinerU线上demo**

_https://opendatalab.com/OpenSourceTools/Extractor/PDF_

**● “探索者计划”成果提交**

_https://aicarrier.feishu.cn/share/base/form/shrcneaKr8tecz3agwNa90Xqh0g_

  

  

**相关阅读：**

[

上海人工智能实验室大模型中心 | 全球招聘

2024-11-12

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXnHSa53PEJIj7ibXib1kJnduh9icBX5VGrvjCIAV1Yib3ZdXWnh8p8zC3oPibdlPH1yvMnhI9nicegxL2w/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247548246&idx=1&sn=43e054a06b4f3db074ac8d369b26b616&chksm=c124a049f653295fbaaed9541aa8d351efdade89efdb7b3431ec47b3fc28f906fb3c5c0cea3a&scene=21#wechat_redirect)

[

MinerU 新版本发布，API内测开放申请，诚邀开发者共建

2024-11-08

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAX1OakmNeZfESnKeicwibbx4bW315QyhQVVXFM8CPTicGJUQbZpInKh30N8sjC0n20QFnCpD6qTia6Tsg/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247548230&idx=1&sn=3b46b188bbcddd1bb65054c9dd46b1ff&chksm=c124a059f653294fe3c6f3e57865f4991c3c3761642bf0a99f38399a60ad3fa87244f988cd04&scene=21#wechat_redirect)

[

DocLayout-YOLO，让多样性文档布局检测更快、更准、更强

2024-10-29

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXTzCbOYD7l9ialGdVwJmBugRJBcUicz7Q1ibwUeC2TCJBmicfvKzrqg8T3MkjRumdozg6ibEhTg7AaSAw/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247547791&idx=1&sn=c72c41bb5e26e6f5ff9987e901dc00eb&chksm=c124a690f6532f867c0326941cea3f4903563ab3efed67cab74b2fb0cc5944fc86ce37c6c14b&scene=21#wechat_redirect)

[

不是吧？这么好用的开源标注工具，竟然还有人不知道…

2024-08-22

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6jsZJmjym44k1KnuBibIibwV47VtuvqyerwKmT7UnBgAp4eL1Uqic7ulsE0NcPnlKtRNSGyGjiasYDiaw/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544661&idx=1&sn=462724e0b95801d0bfefdaa858806985&chksm=c124b24af6533b5c25f55e54d9047a6b423d2c723b2d678ee50d19d86132861eac39a9c569d1&scene=21#wechat_redirect)

[

登顶GitHub Trending，开源工具MinerU助力复杂PDF高效解析提取

2024-07-30

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6GL7SVSu4b9OLicVrR9A07M6PcibrISFpdrwLInzliaZ9kibQ2ylNourdoT9wVpstBuFGOTuwrsqHtVA/640?wx_fmt=jpeg)

](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247544657&idx=1&sn=0772359cc3df0033866cada0021f34fd&chksm=c124b24ef6533b58357e67d0f3a774d0fa2d73ad710073935ae5472cefe75881df4aeee989cc&scene=21#wechat_redirect)

[赌你一定想要！OpenDataLab首款大模型多模态标注平台Label-LLM正式开源](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247535978&idx=1&sn=e0ac60cf8b43d21637d18e3d45afd89e&chksm=c10cdf88f67b569e67c6d2e0f3d62fa8e6f4ed81feb656a84fa0ad56ebc537e34e23c2894a28&scene=21#wechat_redirect)

[2024-06-06](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247535978&idx=1&sn=e0ac60cf8b43d21637d18e3d45afd89e&chksm=c10cdf88f67b569e67c6d2e0f3d62fa8e6f4ed81feb656a84fa0ad56ebc537e34e23c2894a28&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD7kMmQsy4kYAm3oP4iaX5wQTUBloGx5Qm1Rtxq8ibUh0oFnyF2TD8ib6883KMKOSf6j3odOhibVHSGTuQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247535978&idx=1&sn=e0ac60cf8b43d21637d18e3d45afd89e&chksm=c10cdf88f67b569e67c6d2e0f3d62fa8e6f4ed81feb656a84fa0ad56ebc537e34e23c2894a28&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言