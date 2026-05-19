     CVPR 2025｜公式识别评测新指标CDM：视觉元素buff加成，让大模型公式识别评价更准确、更客观 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

CVPR 2025｜公式识别评测新指标CDM：视觉元素buff加成，让大模型公式识别评价更准确、更客观
===================================================

原创 OpenDataLab OpenDataLab 2025-06-11 20:24 上海

> 原文地址: [https://mp.weixin.qq.com/s/MQEKkHpgU7uUNo0j6\_UfEw](https://mp.weixin.qq.com/s/MQEKkHpgU7uUNo0j6_UfEw)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

导言：

  

大模型时代，基于个人文档库的 RAG 应用迅速崛起，而文档解析作为关键首步，直接决定了大模型对文档内容的理解程度与回答准确性。在面对科学类文档中大量的公式时，准确解析公式显得尤为关键。而评价一个模型是否准确的前提是有一个准确、公平的指标。然而，熟悉公式识别领域的人员会发现使用BLEU、EditDistance等纯文本指标无法准确地衡量公式识别的性能，原因是同一个公式存在多种Latex书写方式。

  

为此我们提出一套基于视觉元素匹配的评价指标CDM，与人工查看公式方式类似，能更准确的评价公式识别的效果，从而促进公式识别领域的发展。

  

本研究成果《Image Over Text: Transforming Formula Recognition Evaluation with Character Detection Matching》已被计算机视觉顶级会议CVPR 2025接收，作者团队来自上海人工智能实验室OpenDataLab团队与上海交通大学，欢迎关注。

  

论文链接：  

https://arxiv.org/pdf/2409.03643

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXZ51dpXQ09VWmgID7PImUzZlCOTydAUgrgZzZdlsLricUHDkynLEClCZgOQDnHh9Onz4JJANUNI9A/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**什么是CDM**

CDM（Character Detection Matching），顾名思义，是从字符检测和匹配的角度来考虑公式的评测问题，首先来看下官方Demo给的简单案例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXZ51dpXQ09VWmgID7PImUzRsibjA6pT33NkOoQn91icEElnibgvaiayKHkFvKdhzo9H9ktbmakDZcOqQ/640?wx_fmt=png&from=appmsg)

Demo界面中，左侧是两个文本框，用来键入公式的真值和预测值（Latex格式），右侧是计算的结果指标，以及可视化的匹配结果，可视化结果里，清楚的用绿色框来定位预测正确的字符，同时用红色框来定位预测错误的字符。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**CDM和传统指标的对比**
---------------

**1\. CDM和纯文本指标（BLEU，Edit Distance等）的对比**

下图展示了CDM和BLEU、EditDisttance ExpRate等纯文本指标相比的优点，其中，case1，预测和真值的公式是相同的，但是由于书写风格不一致，纯文本的指标都不能正确的评价这种情况；case2和case3同样都是将"z"识别成"2"，但是错误个数不一样，纯文本指标都不能正确的根据错误个数来衡量错误程度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXZ51dpXQ09VWmgID7PImUzqbnutBP3csEDPe6JwM5wDJ97Ng8WuersVEMliaWzBLCKpaeXxYRWYMw/640?wx_fmt=png&from=appmsg)

为了验证CDM在更大范围优于纯文本类指标，作者做了两组实验。其一是人工投票实验，作者随机挑选了1000组case，并计算它们的CDM指标和BLEU指标，然后让志愿者筛选哪个指标更合理，下图(a)显示投票结果中，64%的case，CDM要优于BLEU，剩下的情况里，32%的case两者同样合理，3%的case BLUE要优于CDM，还有1%的case两者都不合理，可以看见CDM在大多数情况下都是合理且要优于BLEU的；下图(b)显示的是按分数分层的case里，CDM和BLEU更优的数量，可见在公式的预测质量越高，CDM约显示出绝对的准确性，在公式预测的分数较低的情况下，才有一些CDM不够合理的case出现。

  

除了人工投票实验，作者还设计了一个模拟实验，让ChatGPT对一组公式进行重写，重写的过程不能改变公式的渲染效果，这种情况下按理来说评测指标不应该产生变化，但是实际上，只有CDM的结果始终保持为1，BLEU和ExpRate指标都受到了很大程度的扰动，如图(c)所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXZ51dpXQ09VWmgID7PImUz8r0r4vDg5iaWfMfjnnp2UToJMshAxZUu1kBu5snEvRzMuUCBnGCzwJg/640?wx_fmt=png&from=appmsg)

**2.** **CDM和纯图像指标（image diff，MSE等）的对比**

除了BLEU等纯文本的指标，也有一些纯图像层面的指标，用来衡量公式识别效果，这些指标相对比较冷门，作者在附录中也把CDM和它们进行了对比。

如下图所示，直接对图片进行作差或者在作差的基础上计算MSE都有一个很大的缺点，即收到渲染布局的扰动非常明显，这类指标，只有在图像差或者MSE为0的情况下，能说明预测的结果是正确的，但是反过来指标不为0的时候却不能保证预测结果是错误的，也无法区分错误的不同程度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXZ51dpXQ09VWmgID7PImUzicxaU4rGIqzybKOXH64AzrhKITichP1IibUX6RuicX87dkGH7iaZib1ro43Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**CDM是如何实现的**
-------------

看了这么多CDM的case，可以说CDM在公式评测领域对传统的评测指标是降维打击，那么CDM到底是怎么实现的呢？

下图是论文中给出的流程图:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXZ51dpXQ09VWmgID7PImUzaSOG9p0ibwQ5gEJibic1WzWs0rcT9on4Remdh7k0ZjngYnPFbRLXYZnyQ/640?wx_fmt=png&from=appmsg)

图中，CDM一共有**4个步骤**：

1.  **元素定位**：这一步首先给公式里的不同字符渲染上不同的颜色，然后用图像处理的方法，根据这些不同的颜色，得到不同字符的定位，也就是边界框，这一步是整个CDM的基础，如果这一步失败，CDM也就无法计算了；
    
      
    
2.  **元素匹配**：在得到真值和预测结果的全部元素及其定位后，在这一步进行匹配，将每一个真值的元素和预测结果的元素一一匹配，这里匹配的算法采用的是匈牙利算法；
    
      
    
3.  **匹配检查**：由于匈牙利匹配是完全匹配，所以在匹配完之后，需要进行检查，把不合理的匹配去掉，这里检查的角度包括字符一致性和位置关系一致性，即匹配双方不是相同的字符，或者匹配双方的位置关系和整体不一致，则都会认为错误匹配；
    
      
    
4.  **指标计算**：根据最终得到的正确匹配和错误匹配的个数，计算F1score等指标。
    

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**总结**
------

CDM是一种新型的公式识别评测指标，它利用字符定位和匹配对公式进行评测，对比传统纯文本的指标，在准确性上有压倒性的优势。不过，CDM目前也有一些缺陷，从官方仓库的安装教程来看，它的环境安装较为复杂，如果能进一步优化的话，应该能够获得更广泛的应用。

  

**更多内容：**

👇

代码：  

https://github.com/opendatalab/UniMERNet/tree/main/cdm

Demo:  

https://huggingface.co/spaces/opendatalab/CDM-Dem

  

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

END  

  

**相关阅读：  
**

  

  

[MinerU 偷偷放大招！3大新功能上线、模型重磅升级，解析效率超级加倍……](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

2025-04-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUBlUJUFkG3acE1KjtVb7X1jUoqEZqSTu6b1NHzoPYiaicQjBaQ6NCG78GYurSgtzE1ITE3Q4WCux1Q/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[【MinerU × LazyLLM】PDF无损拆包，让RAG更懂你的文章！附PDF解析组件选型与RAG案例分享](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550423&idx=1&sn=aae4f098fd607829e3df9fef37814fe8&scene=21#wechat_redirect)

2025-04-08

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUk7Csn0E5A7R5kcqCt7p1btpsj2Oqmus7IGicuxnkZSWEddwcDeMrFO8eicLszAj8RqIBF1icL29Sqg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550423&idx=1&sn=aae4f098fd607829e3df9fef37814fe8&scene=21#wechat_redirect)

[全自动调整数据配比，解放LLM工程师丨上海AI Lab&上海交大联合团队提出创新数据均衡方法，让大语言模型不“偏科”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550657&idx=1&sn=cd586a6c25e19337a70be8f2fed1992d&scene=21#wechat_redirect)

2025-06-10

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVOTWa1icqFo4x6Ighsl2g7HVIGbn4j2TibmswBqcNsl5rXNGash2MfbH9KpjR3btvOIpuhUbvBXUbw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550657&idx=1&sn=cd586a6c25e19337a70be8f2fed1992d&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言