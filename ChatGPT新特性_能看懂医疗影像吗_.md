     ChatGPT新特性，能看懂医疗影像吗？ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

ChatGPT新特性，能看懂医疗影像吗？
====================

原创 OpenDataLab 2023-11-01 20:35 上海

> 原文地址: [https://mp.weixin.qq.com/s/4NjhIavYzU37WASCLVsNJQ](https://mp.weixin.qq.com/s/4NjhIavYzU37WASCLVsNJQ)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

本文授权转自：知乎|通用医疗GMAI

GPT-4V(ision) 是 OpenAI 在 2023 年 9 月 25 日为 ChatGPT 增加的新特性，使得用户可以通过图像与 GPT4 进行交互。这标志着 GPT4 正式成为一个多模态模型，具备对于图像的理解能力。**团队对 GPT-4V 的医疗影像理解能力进行了一系列的测试。**

  

补充一下，GPT4V 主要支持二维图像格式，如JPEG、JPG、PNG、GIF和WEBP。然而，在医疗领域常用的三维图像格式，如 NIFTY 和 DICOM，需转换为二维图像才能供 GPT-4V 分析，这个过程中不可避免地会有信息损失。

  

GPT-4V 目前可以接收图像输入，但是没办法输出图像，意味着无法直接进行医学图像领域常用的分割和检测任务，但是可以通过文本描述来给出一些分析和诊断建议，通过文本来描述一些图像中异常区域的位置。**所以，本文中测试的任务都是能通过文本直接描述的医学影像诊断任务和分类任务。**

**先给结论：**我们认为医疗场景下，GPT-4V 对常见医学图像本身的浅层次信息展示出了足够强的理解能力，但是对于这些信息对应的医学意义缺乏足够认知。因此，GPT-4V 距离实际医疗场景中的准确诊断尚有较远距离，但是辅助医生进行医学图像特征的分析已具有初步的价值。

选取以下5个测试案例说明：

_****案例1****_  

**PET-CT 多模态融合定位肺部肿瘤**

PET与CT 成像是临床上对各种恶性实体肿瘤进行诊断检查的重要手段，两种模态结合能同时提供生物活动和解剖结构的详细信息，从而实现全面和精确的肿瘤定位和诊断。我们将 **AutoPET 数据集**同一病人成对的 PET-CT 3D 图像的某一切片图像上传给 GPT-4V 并提供基本的模态信息，下面是 GPT-4V的分析结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZ8cwWEB5Hkd43yiaHgKvicibF8NHRJ73GDnDvHp6DueH6icWMxY9qCdhCWw/640?wx_fmt=jpeg)

GPT-4V 已经正确的识别到右侧肺存在病变，与如下实际标注一致：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZbTXQBH46FBvBkgtNG4pT1tcyVsvXD5iahoGzLjtibnjicd4ngRj5l9nmQ/640?wx_fmt=png)

###   

_****案例2****_  

**多模态 MR 脑部胶质瘤诊断**

前面已经测试了 PET-CT 的融合诊断，下面测试一个医学影像分析的经典任务，脑部胶质瘤诊断。我们从 **BraTS21 数据集**里随机抽取了一例数据进行测试，模型需要读取4种不同序列的MR影像数据，然后识别到肿瘤的大概位置。这个任务比 PET-CT 的诊断要更加困难一点，因为每种 MR 序列的特征差别很大，需要分别分析并给出综合结论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZOLiajxaDMB3EEtwH9Dib8JibfibOLkIGnjpmDaCuY2PyS6QtrtsrKLM2QA/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZA0tcx96ibZ9hpuWGFY98tibKD2IsAGBnIwAk0kckNl57vsAkMz3qX1BA/640?wx_fmt=png)

GPT-4V 可以结合每一种MR序列单独的特点，为其提供详尽的解读和分析。同时可以结合四种序列的图像，对病变区域进行正确的识别和分析。医生给出的胶质瘤标注如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZs5VtdVpyCibFibWOjbcCJjrdVJWpoa1fTyXB3PPkUEFBaml82lBWLtHw/640?wx_fmt=png)

  

_****案例3****_  

**皮肤瘤良恶性分类**

下面试一个 2D 医学影像模态上的任务，从彩色皮肤镜图片种进行皮肤瘤的分类。这个任务更加接近自然图像场景，GPT-4V应当能展现出更强的理解能力来。我们从 ISIC 2020 数据集选择了 9 例数据，一次性给 GPT4-V 9张图像，只有一张（第二行左边）是恶性，其余都是良性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZOxQxdSuncZWp0QmUfbpeI3aGQELoTKgdciaBuPKyhovO3JHXF4cw36w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZ07evmib0ricQWAfYNTcEiaMGcGKjtibMKn0gxOJulI7HZr9t3eAkeBnicfg/640?wx_fmt=png)

GPT-4V 对皮肤镜图像给出了细致的分析，包括颜色，边缘，色素分布等。对于唯一的一张恶性图像，正确地给出了语气最肯定的诊断。在剩下的8张正常图片中，4 张图像被肯定地认为是正常的，3 张图像认为需要进一步评估，2 张图像给出意见认为可能是恶性。

  

_****案例4****_  

**基础腹部器官的识别**

除了以上的一些肿瘤诊断的案例，我们来考验一下 GPT-4V 对于一些医学常识的认知。首先是解剖结构，看看它能不能从CT片子里认出人体的基本腹部器官。我们选择了 **AbdomenCT-1K** 的一个例子，把窗宽窗位调到腹部常用的\[400,40\]上，然后对其中一个切片用不同的颜色标记出某个器官，红色是肝脏，绿色是肾脏，黄色是胰腺，蓝色是脾脏。这个任务对于图像理解的要求不那么高，很简单就可以看出每个标记对应的器官，但是需要一些医学背景知识来根据切片识别每个器官具体是哪种。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZcE7ILZ1e3c8UEV5ABPbjtic5j1MFFHzicXaXVtq17KWEOYA7ibAAYK4Yg/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZicalJNQLYQ6KllvKwjE4Zlu33k1GENtuLiacx3z6Xsr11YsP4oaUGu7w/640?wx_fmt=png)

识别的正确率很糟糕。。。肝脏和脾脏识别正确。但是胰腺识别成了胃，肾脏识别成了胆囊。

  

_****案例5****_  

**斜视图片的识别**

既然GPT-4V在基础医学知识上存在问题，我们再试试医学知识依赖更少的场景。这里选择了3张人眼的图片，部分图片存在斜视，是否斜视可以直观地从图中看出来，并不需要专业的医学知识，那么GPT-4V的表现如何呢？

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZNLs68d2Mrf6nRIOlszyr3FLhYDrYqOMKiaicoFMGA2Jtj5icJa6ojVCow/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6nkk7vALibFjhsvmRo4UcgZolrMnBwz496Uwz8yutDmbm68Mz7ZNVgDAOuUibn6ykqPGomdKe22IjQ/640?wx_fmt=png)

  

直接被伦理审查ban了。。。看来医学场景测试的prompt设计和案例选用可能需要更仔细一点。

  

总结

尝试了几个常见的医学影像场景，GPT-4V 已经展现了出了对多种模态医学影像惊人的理解能力，能结合不同模态的特点进行分析，并且对一些异常能够精准的识别。但是案例4一些简单的腹部器官的识别错误，又让人对它目前的可靠性有一些 concern。

  

另外我们发现 GPT-4V 存在一些伦理限制，案例5的眼睛图片直接不被允许分析，也许是人脸相关的图片都会比较敏感？个人认为，GPT-4V 的强大能力如果能通过合理的prompt engineering和场景选择来得到合理的发挥，应该能创造出有一定实用价值的医疗应用。期待行业的各位大佬们能够推动这种多模态大模型的实际落地。

\-END-

**更多医疗开源数据集，欢迎访问OpenDataLab官网查看与下载：**

**扫码直达↓**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言