     小小视频-文本标注，LabelU轻松拿下！ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

小小视频-文本标注，LabelU轻松拿下！
=====================

原创 LabelU OpenDataLab 2024-04-02 15:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/u1k2qRP2LiB3HjAdsv2bIA](https://mp.weixin.qq.com/s/u1k2qRP2LiB3HjAdsv2bIA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

最近因为 Sora 模型大火，带动了文生视频任务研究。有小伙伴“吭哧吭哧”上手后，到人工精标数据时迷茫了，不知道选什么视频-文本标注工具为好。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7yjDpC9UfD7e5eSUeat8ZxSmTrkZOv6L1sV9IGHSB83JmaBJ6y9KtkqTO2GD6nEzYQqwBB6Of8aYs3STZZb0lQ/640?wx_fmt=gif&from=appmsg)

小编听了也急的发愁，远在天边，近在眼前，这么好用的视频标注工具——**LabelU**就在OpenDataLab网站明晃晃地挂着，可恶，竟然没人知道？！今天可得给你好好说道说道。

当然，你内心肯定会想：

> _LabelU是啥？听都没听过吧？_
> 
> _为什么要用LabelU？_
> 
> _别的标注工具不是也能标吗？_
> 
> _图片、音频标注，LabelU真的行吗？_

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD48YIXJzOwOwibpAWMHsKWGicq6iauY2X40Qa62X5MjcLw3uiclpFKOddYYUTzWOJMn2QNOia9Lu1ATgLQ/640?wx_fmt=jpeg)

首先，得承认，LabelU可能不是专业数据标注团队的首选，毕竟它没有那些花里胡哨的协同标注、团队管理功能。但是，对于那些算法工程师、开发者、大学生，特别是那些想要自己动手丰衣足食的朋友们，LabelU简直就是个宝藏工具！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7e5eSUeat8ZxSmTrkZOv6LYhCg4kpqv3yTzPgncGZ1PVHr7OoBbIUWvmiczhicEb5nyw1icAjLXFzSg/640?wx_fmt=png&from=appmsg)

视频、图片、音频都能标，支持80+主流标注场景

  

LabelU提供了多种标注工具和功能，可广泛适用于文生视频、文生图片、文生音频、目标检测、分类、分割、关键点、折线、OCR等算法场景，具体有哪些呢：

**● 基于视频，**具备强大视频处理能力，可实现**视频分割**、**视频分类**、**视频时间戳**等功能，为模型训练提供高质量标注数据。

**● 基于图像，**提供多功能图像处理工具，涵盖**2D框**、**语义分割**、**多段线**、**关键点**等多种标注工具，协助你轻松完成图像的标识、注释和分析。

**● 基于音频，**提供高效精准的音频分析工具，能够进行**音频分割**、**音频分类**、**音频时间戳**等，更好地注释复杂的声音信息。

光看介绍可能觉得没什么特别的，但要知道，**免费开源的标注项目中能提供这么多工具，并且体验足够丝滑的，全网很难找到第二个**，足以说明LabelU的地位了。

（要是找到了，请告诉小编，俺也很想知道![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/Yellowdog.png)）

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7yjDpC9UfD48YIXJzOwOwibpAWMHsKWGicjgCvdPgA4k6IdQ8y9CWy7rqqFGciaSmjg3CIwOE7NXudZDnfNRlK02Q/640?wx_fmt=gif&from=appmsg)

（视频片段分割标注示意）

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7yjDpC9UfD48YIXJzOwOwibpAWMHsKWGic1viaSeJTPgg8n4Esia4t7Sbtxa5IaibPI7ogeQXftQYpwXZZDyKVZuTAw/640?wx_fmt=gif&from=appmsg)

（图片立体框标注示意）

  

简单易用，轻松标记，快速输出标注结果

LabelU另一个特点是简单，没有眼花缭乱的菜单栏内容（没说眼花缭乱不好的意思😆），要用什么标注工具，页面上自由选择、灵活搭配，提前配置好，进入标注界面就能随心所欲地标注了。标注结果支持JSON、COCO、MASK等多种格式快捷导出，相当方便。

关键还有一点，LabelU支持导入预标注 JSONL 文件进行二次修改，这意味着什么？（划重点！）**用大模型自动标注，如果结果不准确，可以导入LabelU进行人工批量审核、二次修改，相当实用的功能！**用来制作视频生成大模型常用的微调数据，也能轻松搞定。真的很不错，你就说是不是！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7e5eSUeat8ZxSmTrkZOv6LFyFNYr6lpfian6ZdNLh1nFchu4RMxgbJWU6iaxsicZR0Clb91r5EGw4Kw/640?wx_fmt=png&from=appmsg)

（LabelU简洁的标注界面）

  

部署简单，保证数据安全，源码开放可“魔改”

LabelU提供了安装包，本地部署使用，数据无需上传，在岸标注，保证数据的安全性和隐私性。尤其对于数据分布在多处，或者数据下发独立标注的场景，用它标注再合适不过了。

同时，LabelU代码完全开放，支持二次开发、集成，“魔改”更多玩法，“炼丹”大神听了都忍不住拍手叫好。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5oQLeGkR6qj73ERWxY19G56zHq3Gp3rPf7zoDiafqibEnKadRaAuW1w8ApGSW59hNmArPAjtCaDc6hCpOeGo7F4w/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

使用指南

这么强大的LabelU，相信不少朋友已经跃跃欲试了。但对于刚接触这个工具的小伙伴来说，可能会对提供的丰富的标注工具名称有点陌生，不知道怎么选择。为了方便大家快速上手，小编简要介绍一下，其实很简单，

1.  不管标注对象是什么，只要记住LabelU根据交互方式，将标注工具分**2大类，**一类是“**全局**”，另一类是“**标记**”：
    

1.  **“全局”**标注工具：对标注对象进行整体内容概括、总结，不与细节做交互，比如常见的“天气”、“场景”标签等；
    
2.  **“标记”**标注工具：对具体的内容细节、局部标记，根据不同数据类型有不同的特异性交互方式，比如视频/音频有片段分割、时间戳，图片有标点、标线、拉框、多边形等；
    

3.  不管哪种工具、哪种交互方式，打标签都有**2种形式**，分别是**选项**、**文本描述，**（选项包含单选、多选2种形式）**。**可以形象地理解为交互标记之后，填入标签内容时是做**选择题，还是填空题**。
    

1.  **单选或多选**：在“分类”属性中设置，特点是，需要提前配置好具体选项内容，标注时下拉勾选。
    
2.  **文本描述**：在“文本”属性中设置，特点是，无预设内容，在标注时按需填写即可。
    

了解上面2个维度之后，你就可以自由组合标注工具了，既能给全局打文本标签、选项标签，也能给视频分割/时间戳、图片的描点/拉框/多边形等打文本标签、选项标签，以此类推，只要按需选择即可。

当然，还有其他配置内容，比如标签颜色、标签中英文ID、标签参数（比如标点工具的点数范围、多边形线条类型/闭合点数范围设置）、便捷的通用标签（多种交互方式都可能用到的重复标签，可配置为通用标签）、画布外标注等，配置比较简单，就不多介绍了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7e5eSUeat8ZxSmTrkZOv6L3l6ScI7TXpC5L3Lmwqxrul1uF97dD5OJPg5vFFj2QbGkxRMZdA29ww/640?wx_fmt=png&from=appmsg)

（LabelU视频全局、标记类工具配置示意）

配置好标注工具，就可以进入工作台，愉快地标注了。LabelU还提供了诸如快捷键、可视化任务管理等功能，帮助大家提升标注效率，快来试试吧。

**LabelU本地部署与开发文档：**

_https://github.com/opendatalab/labelU/blob/main/README\_zh-CN.md_

**OpenDataLab提供了在线版LabelU供大家体验、使用，传送门：**

**● Demo体验**：

_https://opendatalab.github.io/labelU-Kit/#/image_

**● 在线使用**：

_https://labelu.shlab.tech/tasks_

（注意：在线版，每日凌晨数据将自动清空，请及时备份重要数据。如需完整使用，建议本地部署）

如果想使用JSONL预标注导入，进行视频-文本场景人工审核、修改，小编为你准备了一份最简单的全局文本描述标注的案例，快导入同名“视频1.mp4”的视频和下方JSONL进行体验吧：

`{"sample_name":"视频1.mp4","config":{"textTool":[{"key":"全局文本描述","value":"text-label-1","required":true,"type":"string","maxLength":1000,"stringType":"text","defaultValue":""}]},"meta_data":{"duration":122},"annotations":{"textTool":{"toolName":"textTool","result":[{"id":"js6htkz785h","type":"text","value":{"text-label-1":"这是大模型对视频1的自动标注的文本描述值，可进行人工二次审核与修改"}}]}}}`

（滑动查看全部）

  

当然，JSONL预标注文件玩法还有很多，如果想了解更多字段配置及格式参考，详见LabelU说明文档，统统都有：

_https://opendatalab.github.io/labelU/#/schema/pre-annotation/video_  

  

精彩预告

LabelU即将上线**大语言模型常用的文本标注**工具，快来关注LabelU Github 主页，提 pr 给开发小哥哥催更吧 ![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/newemoji/2_06.png) 要是觉得不错，请不要吝啬你的star~ 你的鼓励是我们前进的最大动力！

**LabelU 主页：**  

_https://github.com/opendatalab/labelU_

**更多数据处理宝藏工具，尽在 OpenDataLab GitHub仓库：**  

_https://github.com/opendatalab_

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7yjDpC9UfD48YIXJzOwOwibpAWMHsKWGic8xAmZ4Lj2o6peV9LpCHaxnZTraG4cS1YiaPLYJf3GGFRrhTzxe1BK6w/640?wx_fmt=gif&from=appmsg)

* * *

  

还有很多精彩开源数据集资源，欢迎访问OpenDataLab官网

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言