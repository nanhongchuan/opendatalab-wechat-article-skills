     ChatGPT数据集之谜 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

ChatGPT数据集之谜
============

原创 Alan D. Thompson OpenDataLab 2023-02-21 18:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/JWrvy0y\_bpt296bQSUanAw](https://mp.weixin.qq.com/s/JWrvy0y_bpt296bQSUanAw)

![](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlxCb2M0knV8PqghNDoZfdfMDD1xeKQteribSot2f6OBkDDX45bsNhq3Q/640?wx_fmt=jpeg)

半个月以来，ChatGPT这把火越烧越旺。国内很多大厂相继声称要做中文版ChatGPT，还公布了上线时间表，不少科技圈已功成名就的大佬也按捺不住，携巨资下场，要创建“中国版OpenAI“。

  

不过，看看过去半个月在群众眼里稍显窘迫的Meta的Galactica，以及Google紧急发布的Bard，就知道在短期内打造一个比肩甚至超越ChatGPT效果的模型没那么简单。

  

让很多人诧异的是，ChatGPT的核心算法Transformer最初是由Google提出的，并且在大模型技术上的积累可以说不弱于OpenAI，当然他们也不缺算力和数据，但为什么依然会被ChatGPT打的措手不及？

  

Meta首席AI科学家Yann LeCun最近抨击ChatGPT的名言实际上解释了背后的门道。他说，ChatGPT“只是巧妙的组合而已”，这句话恰恰道出了一种无形的技术壁垒。

  

简单来说，即使其他团队的算法、数据、算力都准备的与OpenAI相差无几，但就是没想到以一种精巧的方式把这些元素组装起来，没有OpenAI，全行业不知道还需要去趟多少坑。

  

即使OpenAI给出了算法上的一条路径，后来者想复现ChatGPT，算力、工程、数据，每一个要素都需要非常深的积累。七龙珠之中，算力是自由流通的商品，花钱可以买到，工程上有许多开源项目和团队，因此，对互联网大厂之外的团队来说，剩下最大的挑战在于高质量训练数据集。

  

至今，OpenAI并没有公开训练ChatGPT的相关数据集来源和具体细节，一定程度上也暂时卡了追赶者的脖子，更何况，业界公认中文互联网数据质量堪忧。

  

好在，互联网上总有热心的牛人分析技术的细枝末节，从杂乱的资料中串联起蛛丝马迹，从而归纳出非常有价值的信息。

  

本文作者整理分析了2018年到2022年初从GPT-1到Gopher的相关大型语言模型的所有数据集相关信息，希望帮助有志于开发“类ChatGPT”模型的团队少走一步弯路。

  

同时OpenDataLab上架了包含C4、BookCorpus、The Pile、ANLI、Reddit、TriviaQA、WikiQA、OpenBookQA、MedVidQA、QAConv、Quoref、FewCLUE、SG-NLG、QReCC、Elsevier OA CC-BY等在内的大型语言模型（LLM）相关数据集，欢迎大家查看与下载。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD5XuPsVhCJeYo0b3DpzmhCuq6rx04guEIpOrO5KPYgjACr6QRUtzXgyF0XQK34DN3ZoE23ibj0uBsg/640?wx_fmt=png)

**作者｜Alan D. Thompson**

**OneFlow编译**

**翻译｜杨婷、徐佳渝、贾川**

  

一些研究人员的报告称，通用人工智能（AGI）可能是从我们当前的语言模型技术进行演进\[1\]，预训练Transformer语言模型为AGI的发展铺平了道路。虽然模型训练数据集日渐增大，但缺乏基本指标文档，包括数据集大小、数据集token数量和具体的内容细节。

  

尽管业内提出了数据集组成和整理文档的标准\[2\]，但几乎所有重点研究实验室在揭示模型训练数据集细节这方面都做得不够。这里整合的研究涵盖了2018年到2022年初从GPT-1到Gopher的精选语言模型的所有数据集（包括主要数据集：Wikipedia和Common Crawl）的综合视图。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

********概述********

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlvVDvdQMx9kEp8mzpF1GSQ74ljveS7IENg7FzvYKJia77wst8JUKTr7Q/640?wx_fmt=png)

图 1. 主要数据集大小的可视化汇总。未加权大小，以GB为单位。

2018年以来，大语言模型的开发和生产使用呈现出爆炸式增长。一些重点研究实验室报告称，公众对大语言模型的使用率达到了惊人高度。2021年3月，OpenAI宣布\[3\]其GPT-3语言模型被“超过300个应用程序使用，平均每天能够生成45亿个词”，也就是说仅单个模型每分钟就能生成310万词的新内容。

值得注意的是，这些语言模型甚至还没有被完全理解，斯坦福大学的研究人员\[4\]最近坦言，“目前我们对这些模型还缺乏认知，还不太了解这些模型的运转模式、不知道模型何时会失效，更不知道这些模型的突现性（emergent properties）能产生什么效果”。

随着新型AI技术的快速发展，模型训练数据集的相关文档质量有所下降。模型内部到底有什么秘密？它们又是如何组建的？本文综合整理并分析了现代大型语言模型的训练数据集。

因为这方面的原始文献并不对外公开，所以本文搜集整合了二、三级研究资料，在必要的时候本文会采用假设的方式来推算最终结果。

在本文中，我们会将原始论文中已经明确的特定细节（例如token数量或数据集大小）归类为“公开的（disclosed）”数据，并作加粗处理。

多数情况下，适当地参考二、三级文献，并采用假设的方式来确定最终结果是很有必要的。在这些情况下，token数量和数据集大小等细节是“确定的（determined）”，并以斜体标记。

模型数据集可分为六类，分别是：维基百科、书籍、期刊、Reddit链接、Common Crawl和其他数据集。

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlL9Rx7ueJrR9mFyQKo9VWLDmlBKyJibZhjts17UwYcjicmmLxajQL7e0w/640?wx_fmt=png)

表1. 主要数据集大小汇总。以GB为单位。公开的数据以粗体表示。确定的数据以斜体表示。仅原始训练数据集大小。

**_****1.1****_**  ****维基百科****

维基百科是一个免费的多语言协作在线百科全书，由超过300,000名志愿者组成的社区编写和维护。截至2022年4月，英文版维基百科中有超过640万篇文章，包含超40亿个词\[5\]。维基百科中的文本很有价值，因为它被严格引用，以说明性文字形式写成，并且跨越多种语言和领域。一般来说，重点研究实验室会首先选取它的纯英文过滤版作为数据集。

**_****1.2****_**  ****书籍****

故事型书籍由小说和非小说两大类组成，主要用于训练模型的故事讲述能力和反应能力，数据集包括Project Gutenberg和Smashwords (Toronto BookCorpus/BookCorpus)等。

**_****1.3****_**  ****杂志期刊****

预印本和已发表期刊中的论文为数据集提供了坚实而严谨的基础，因为学术写作通常来说更有条理、理性和细致。这类数据集包括ArXiv和美国国家卫生研究院等。

  

**_****1.4****_**  ******Reddit链接******

WebText是一个大型数据集，它的数据是从社交媒体平台Reddit所有出站链接网络中爬取的，每个链接至少有三个赞，代表了流行内容的风向标，对输出优质链接和后续文本数据具有指导作用。

  

**_****1.5****_**  ********Common Crawl********

Common Crawl是2008年至今的一个网站抓取的大型数据集，数据包含原始网页、元数据和文本提取，它的文本来自不同语言、不同领域。重点研究实验室一般会首先选取它的纯英文过滤版（C4）作为数据集。

  

**_****1.6****_**  ******Common Crawl**其他数据集********

不同于上述类别，这类数据集由GitHub等代码数据集、StackExchange 等对话论坛和视频字幕数据集组成。

  

### 

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**常用数据集**

2019年以来，大多数基于Transformer的大型语言模型 (LLM) 都依赖于英文维基百科和Common Crawl的大型数据集。在本节中，我们参考了Jesse Dodge和AllenAI（AI2）\[8\]团队的综合分析，按类别对英文维基百科作了高级概述，并在Common Crawl数据集\[7\]的基础上，用谷歌C4\[6\] (Colossal Clean Crawled Corpus)在Common Crawl中提供了顶级域（domains）。

  

****_****2.1****_**  **********维基百科（英文版）分析************

下面按类别\[9\]列出了维基百科的详细信息，涵盖了2015年抽样的1001篇随机文章，研究人员注意到随时间推移文章传播的稳定性。假设一个11.4GB、经过清理和过滤的维基百科英文版有30亿token，我们就可以确定类别大小和token。

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlqRCp8ylIUDl3wv7Fpy3IurrkjMSPWxzNdZjClupg63ZzzxEibacia1uA/640?wx_fmt=png)

表2. 英文维基百科数据集类别。公开的数据以粗体表示。确定的数据以斜体表示。

****_****2.2****_**  ************Common Crawl分析**************

基于AllenAI (AI2)的C4论文，我们可以确定，过滤后的英文C4数据集的每个域的token数和总体百分比，该数据集为305GB，其中token数为1560亿。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlOeibcRPaWwiajy2HNT5E11ILVhBWQWUnCzrqUNcUfyRdqXl8Af5gicIaw/640?wx_fmt=jpeg)

表3. C4：前23个域（不包括维基百科）。公开的数据以粗体表示，确定的数据以斜体表示。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**GPT-1数据集**

2018年，OpenAI发布了1.17亿参数的GPT-1。在论文中，OpenAI并没有公布模型训练数据集的来源和内容\[10\]，另外，论文误将‘BookCorpus’拼写成了‘BooksCorpus’。BookCorpus以作家未出版的免费书籍为基础，这些书籍来自于Smashwords，这是一个自称为“世界上最大的独立电子书分销商” 的电子书网站。这个数据集也被称为Toronto BookCorpus。经过几次重构之后，BookCorpus数据集的最终大小确定为4.6GB\[11\]。

  

2021年，经过全面的回顾性分析，BookCorpus数据集对按流派分组的书籍数量和各类书籍百分比进行了更正\[12\]。数据集中有关书籍类型的更多详细信息如下：

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nl9YHWNoD2zVb7tERmhjtBFgZ00otRnNKghMLTPQtPPuQxMA7KKpUia5A/640?wx_fmt=jpeg)

表4. BookCorpus书籍类型。公开的数据以粗体表示，确定的数据以斜体表示。

在随后的数据集重构中，BookCorpus数据集进一步过滤掉了书籍中的“吸血鬼”类别、降低了言情类书籍的百分比、增加了“历史”类书籍，增加了收集的书籍数量。

  

**_****3.1****_**  ********GPT-1数据集总结********

GPT-1最终的数据集总结分析如下：

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nlsu1VkpNlmqvtcen0jpic2GlzagqICRIgEf9KScAQVDpKD0cBGcEibMgw/640?wx_fmt=png)

表5.GPT-1数据集总结。以GB为单位。公开的数据以粗体表示，确定的数据以斜体表示。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**GPT-2数据集**

2019年，OpenAI发布了拥有15亿参数的语言模型GPT-2。GPT-2论文阐明了所用训练数据集的大小\[13\]，不过并未说明其内容。而GPT-2模型卡（model card）（在GPT-2 GitHub仓库中）说明了模型内容\[14\]。

我们可以从GPT-3论文中得到token数量，该论文使用了WebText扩展版本来表示190亿token。据推测，2020年推出的WebText扩展版本拥有12个月的额外数据（additional data），因此它可能比2019年推出的GPT-2版本大25%左右\[15\]。GPT-2最终的token数量确定为150亿左右。

如GPT-2论文所述，假设模型卡显示链接数时，每个链接都可以被4500万链接总数所除，那WebText的内容在数据集中所占的百分比的详细信息就可以确定。

然后可以使用确定的150亿token数量来查找每个域的token数量。请注意，在可用的前1,000个域中，此处仅显示前50个域。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlayFUdB3qRrBhfibXo6tTGuCcK9XZiahdfBPCjRMhe5Cudqic8WibSuZJyA/640?wx_fmt=jpeg)

表6. WebText: 前50个域。 公开的数据以粗体表示，确定的数据以斜体表示。

  

**_****4.1****_**  ******GPT-2数据集总结******

GPT-2模型最终的数据集总结分析如下：

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nl5gBetu4jKkeicoWMTTbxJZlY5O2IJXgHyIXicz7yu6DPhQkoR7bBEOpw/640?wx_fmt=png)

表7. GPT-2数据集总结。 公开的数据以粗体表示，确定的数据以斜体表示。  

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

**GPT-3数据集**

GPT-3模型由OpenAI于2020年发布。论文阐明了所用训练数据集的token数量\[16\]，但训练数据集的内容和大小尚不清楚（Common Crawl的数据集大小除外\[17\]）

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlX18Eh5gdibZicc82sXNt2ewkQzDkGaMKEjup5nqoftp34bkf0TthFwUA/640?wx_fmt=png)

表8. GPT-3数据集。 公开的数据以粗体表示，确定的数据以斜体表示。

****_****5.1****_****  ********GPT-3：关于Books1和Books2数据集的分析********

特别值得关注的是，在OpenAI的GPT-3论文中，并未公开Books1数据集（120亿token）和Books2数据集（550亿token）的大小和来源。关于这两个数据集的来源人们提出了几个假设，包括来自LibGen18和Sci-Hub的类似数据集，不过这两个数据集常以TB为计，大到无法匹配。

  

******_****5.2****_****  **********GPT-3：Books1************

GPT-3使用的Books1数据集不可能与GPT-1使用的BookCorpus数据集相同，原因在于Books1的数据集更大，达120亿token。在一篇引用的论文\[19\]中就提及GPT-1使用的BookCorpus数据集拥有9.848亿个词，但这可能只相当于13亿token（984.8字x 1.3字的token乘数）。

  

该数据集由两部分构成：训练集、测试集。训练集中一共有300幅图像，通过随机抽样的形式从原始数据集中抽取出来。余下的200幅图像构成测试集。

通过标准化项目古腾堡语料库（SPGC），Books1有可能与古腾堡项目保持一致性。SPGC是一种开放式科学方法，被用于古腾堡项目完整的PG数据的精选（curated）版本。SPGC包含120亿个token\[20\]，大约为21GB\[21\]。

  

******_****5.3****_****  **********GPT-3：Books2************

Books2（550亿token）可能与Bibliotik保持一致，并由EleutherA收集该来源的数据，组成数据集，使其成为The Pile v1的一部分。Bibliotik版本为100.96GB\[22\]，其确定的token数仅为250亿，低于Books2公开的550亿。然而，使用SPGC的‘每字节token数’比率（大约为1:1.75），Bibliotik的token数和大小将更接近于Books2。

  

******_****5.4****_****  **********GPT-3数据集总结************

附录A概述了使用Wikipedia + CommonCrawl + WebText数据集的顶级资源列表。GPT-3模型的最终数据集总结分析如下：

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlR5xichic3CdwjcSeiaND3pRJD0meHRHKbWqdnGKs4yy30AhTra05wgoJA/640?wx_fmt=png)

表9.GPT-3数据集总结。公开的数据以粗体表示，确定的数据以斜体表示。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtyHJJpqJIq57a7pOL1tj9uccwf8Ahoe4CzlrjJKlmYUYDGsLxq47vpg/640?wx_fmt=png)

**The Pile v1（GPT-J和GPT-NeoX-20B）数据集**

The Pile v1数据集由EleutherAI于2021年发布，该数据集已被用于训练包括GPT-J、GPT-NeoX-20B在内的多种模型，并作为包括MT-NLG在内的其他模型的部分数据集。The Pile v1论文阐明了所用训练数据集的来源和大小。随着token数量的增加，The Pile v1论文应被用作未来数据集文档的黄金标准。

有关token数量的更多详情，可以使用本文提供的信息来确定，参见表1（大小以GB为单位）和表7（token/每字节）\[23\]。

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlPIpOmxxib01biataN9ibORARRx2OuUGRaIJNxxicIibQjjuJlVCuBJGIEDw/640?wx_fmt=png)

表10. The Pile v1数据集。公开的数据以粗体表示，确定的数据以斜体表示。

********_****6.1****_****  ************The Pile v1分组数据集（Grouped Datasets）****************

 为了确定如‘Books’、‘Journals’和‘CC’这类数据集的大小，笔者对数据集进行了分组，如下表所示。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlEJzKe0ic4J4Wo5vKAuNpxd2vkkkojJbWmSyZiaicpH17QppVgKEr5o5aA/640?wx_fmt=jpeg)

表11. The Pile v1分组数据集（不包括Wikipedia、CC 和 WebText）。公开的数据以粗体表示，确定的以斜体表示。

  

**********_****6.2****_****  ************The Pile v1数据集总结******************

The Pile v1数据集与GPT-J和GPT-NeoX-20B模型的最终数据集总结分析如下：

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nl6jHtIxRuANyTKQRfeqX67CnaNskMmGTWZ4zTuCVwfpsektW8icUJ4vg/640?wx_fmt=png)

表 12. Pile v1 数据集总结。 公开的数据以粗体表示，确定的数据以斜体表示。

### 

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtztdZX0DDicrmiaDAjwXpPEQ1D5wZ28Amq9L7527bEEehbbPCKoEBfiaKQ/640?wx_fmt=png)

**Megatron-11B和RoBERTa数据集**

2019年，Meta AI(当时称之为Facebook AI)和华盛顿大学联合发布了拥有1.25亿参数的RoBERTa模型。次年，Meta AI发布了拥有110亿参数的Megatron-11B模型。Megatron-11B使用的训练数据集与RoBERTa相同。RoBERTa\[24\]论文阐明了所用训练数据集的内容，不过必须参考引用的论文(BERT\[25\]和toryes\[26\])来确定最终的数据集大小。

**BookCorpus**： 确定的数据集为4.6GB，如上面的GPT-1部分所示。

维基百科：公开的数据集为“16GB（BookCorpus加上英文维基百科）”。在减去BookCorpus数据集（4.6GB，如上面的GPT-1部分所述）后，维基百科数据集确定为11.4GB。

**CC-News**：（经过滤后）公开的数据集为76GB。

**OpenWebText**: 公开的数据集为38GB。

**Stories**: 公开的数据集为31GB。请注意，此数据集是“基于常识推理任务问题”的Common Crawl内容，不属于本文的‘Books’类别。相反，将Stories与CC-News数据集（76GB）相结合，Common Crawl的总数据集则为107GB。

************_****7.1****_****  **************Megatron-11B和RoBERTa的数据集总结**********************

Megatron-11B和RoBERTa最终的数据集总结分析如下：

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlV6O8icD0yzQokOpYx5jiaMEDkmO40XLVLTbzjUs3vZb6gJf2iboZhcmoQ/640?wx_fmt=png)

表13. Megatron-11B和RoBERTa的数据集总结。 公示的数据以粗体表示，确定的数据以斜体表示。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtOqM8xpgl1IcC4IwpA3n65eZUP09eAucn3eRDcJSHGT9WRHm6ByD05w/640?wx_fmt=png)

**MT-NLG数据集**

2021年，英伟达和微软发布了拥有5300亿参数的语言模型MT-NLG。MT-NLG是微软Turing NLG（拥有170亿参数）和英伟达Megatron-LM（拥有83亿参数）的“继任者”。MT-NLG论文阐明了所用训练数据集的来源和token数量，不过没有明确指出数据集的大小。

如前所述，有关数据集大小的更多详情，可以使用The Pile v1论文中提供的信息来确定。虽然使用的组件相同，但注意的是，MT-NLG和The Pile v1中报告的组件大小却各不相同，这是由于来自Eleuther AI (The Pile v1数据集)和Microsoft/NVIDIA (MT-NLG模型)的研究人员采用了不同的数据过滤和去重方法。

  

************_****8.1****_****  ****************MT-NLG中的Common Crawl数据集************************

**Pile-CC**：公开的数据集为498亿token，确定的数据为227.12GB左右，参见上述Pile v1部分。

**CC-2020-50**: 公开的数据集为687亿token，假设token的每字节率（per byte rate）为0.25 TpB=274.8GB。

**CC-2021-04**：公开的数据集为826亿token，假设token的每字节率为0.25 TpB=330.4GB

**RealNews**（来自RoBERTa/Megatron-11B）：显示为219亿token。根据RealNews论文\[27\]，数据集确定为120GB。

  

**CC-Stories**(来自RoBERTa/Megatron-11B)：公开的数据集为53亿token，如上述RoBERTa部分所示，数据集确定为31GB。

根据以上来源，可确认Common Crawl的总数据量为983.32GB，共计2283亿token。

**************_****8.2****_****  ******************MT-NLG分组数据集（Grouped Datasets）****************************

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nl1ib5UjCjwrAWv0oNhRGPewsOZr0bXX66jo76f421q1bLXicNiaHfNSkiaw/640?wx_fmt=png)

表14. MT-NLG 分组数据集。公开的数据以粗体表示，确定的数据以斜体表示。

**************_****8.3****_****  ******************MT-NLG数据集总结****************************

MT-NLG模型最终的数据集总结分析如下：

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nl3zpTCNDd7x0qN5LGVECibCjicx7jZcTunxPtcSXkZJIEbl7dFh81JYsw/640?wx_fmt=png)

表15. MT-NLG数据集总结。 公示的数据以粗体表示，确定的数据以斜体表示。

### 

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt4KCGXlXBiac4QPDq4ZMr7On0lboCp4JaL6Q5Yroticg3TtGOG5143OQg/640?wx_fmt=png)

**MT-NLG 数据集Gopher数据集**

Gopher模型由DeepMind于2021年发布，有2800亿参数。该论文清楚地说明了所使用训练数据集所包含的高级token数量和大小\[28\]，但没有说明详细内容。

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nlle9iby9XvvEpH7KOCgJcRGlRY1dgb2LnhwpIVVDFicVAPOAcOOqUaQHA/640?wx_fmt=png)

表16. 公开的Gopher数据集 (MassiveText)。公开的数据以粗体表述，确定的数据以斜体表示。

有趣的是，据Gopher论文披露：其Books数据集中包含一些超过500年历史（1500-2008）的书籍。

  

****************_****9.1****_****  ********************MassiveWeb数据集分析********************************

DeepMind于2014年被谷歌收购，并在创建MassiveText时获得了海量数据。虽然Gopher论文中没有进一步详细描述MassiveWeb，但第44页附录中的表A3b注明了MassiveWeb中出现的前20个域\[29\]。根据披露的每个域所占的百分比，我们可以使用MassiveWeb的总token数（5060亿token）和总原始大小（1900GB）来确定每个域的token数量和大小。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NlHkUzvUeI1xQGwNHM5mcUibCLTafWvBYpSRFSRNiclQ5n28mMsuYztLrw/640?wx_fmt=jpeg)

表17. MassiveWeb：前20个域。公开的数据以粗体表示，确定的数据以斜体表示。

******************_****9.2****_****  **********************Gopher：关于维基百科数据集的分析************************************

维基百科数据集的总规模很难确定。在Gopher论文中，研究人员指出维基百科没有进行数据去重\[30\]。然而，论文中列出的不同大小数据集（12.5GB MassiveWeb Wikipedia与1GB MassiveText Wikipedia）可能是由于失误而造成的，误将“10GB”写成了“1GB”。无论如何，本文仅使用MassiveWeb数据集版本 (12.5GB)。

********************_****9.3****_****  ************************Gopher:不包括WebText****************************************

Gopher数据集的组成部分不包括Reddit外链的WebText数据集。为了清楚起见，尽管Reddit是MassiveWeb中的顶级域，但该数据集仅抓取Reddit域内的Reddit链接。根据定义，WebText\[31\]由“所有Reddit的外链”组成（即指向Reddit域外的链接）。

  

**********************_****9.4****_****  **************************Gopher分组数据集********************************************

MassiveWeb被认为是MassiveText的子组件，并被集成到Gopher的数据集汇总中，其分组基于以下列出的可用信息：

  

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nlfpp53g6HWofbWKLGicaUK4EvPSqAIfRh8O7hKEibg0fkDvhE2LnfGj0Q/640?wx_fmt=png)

表18. Gopher分组数据集。公开的数据以粗体表示，确定的数据以斜体表示。

************************_****9.5****_****  **************************Gopher数据集总结**********************************************

Gopher是本文中最大的数据集，大小为10.5TB。Gopher模型的最终数据集总结分析为：

![](https://mmbiz.qpic.cn/mmbiz_png/lBhAE42wKWq8vNMMhx7UalPsfL7gT1Nl9OfRYtMdvEY1En2RkW7iaEEDsPgibZdIuEa2bIRZ9AyHfEcnSdicWo6pQ/640?wx_fmt=png)

表19. Gopher数据集总结。公开的数据以粗体表示，确定的数据以斜体表示。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtPGADgFqf6qZfYhhMv8QEOtJwowc0S2xYdu8MCfbs205tvjfHibianlicQ/640?wx_fmt=png)

**结论**

对于训练当代Transformer大型语言模型的数据集而言，这可能是最全面的整合分析内容（截止2022年初）。在主要数据源不透明的情况下，本次研究主要从二级和三级来源收集数据，并经常需要假定来确定最终估计值。随着研究人员要处理千万亿个token（1,000万亿）和数千TB的数据（1,000TB），确保详细披露数据集组成的文档变得越来越重要。

特别值得关注的是，基于大型语言模型的强大AI系统产生的冗长而匿名的输出正在迅速发展，其中许多数据集的细节内容几乎没有文档说明。

强烈建议研究人员使用突出显示的“数据集的数据表（Datasheet for Datasets）”论文中提供的模板，并在记录数据集时使用最佳实践论文（即Pile v1论文，包括token数量）。数据集大小（GB）、token数量（B）、来源、分组和其他详细信息指标均应完整记录和发布。

随着语言模型不断发展并更广泛地渗透到人们的生活中，确保数据集的详细信息公开透明、所有人都可访问且易于理解是有用、紧迫和必要的。

### 

**扩展阅读及脚注**（请上下滑动） 

考虑到简洁和可读性，本文使用了脚注而非文本/括弧式引文。主要参考文献如下，或者参见http://lifearchitect.ai/papers/，获取大语言模型领域的主要基础论文。以下论文按本文顺序显示。

  

1.  Datasheets for Datasets Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J., Wallach, H., Daumé III, H., & Crawford, K. (2018). Datasheets for Datasets. https://arxiv.org/abs/1803.09010
    
2.  GPT-1 paper Radford, A., & Narasimhan, K. (2018). Improving Language Understanding by Generative Pre-Training. OpenAI. https://cdn.openai.com/research-covers/language-unsupervised/language\_understan ding\_paper.pdf
    
3.  GPT-2 paper Radford, A., Wu, J., Child, R., Luan, D., Amodei, D. & Sutskever, I. (2019). Language Models are Unsupervised Multitask Learners. OpenAI. https://cdn.openai.com/better-language-models/language\_models\_are\_unsupervised \_multitask\_learners.pdf
    
4.  GPT-3 paper Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., & Dhariwal, P. et al. (2020). OpenAI. Language Models are Few-Shot Learners. https://arxiv.org/abs/2005.14165
    
5.  The Pile v1 paper Gao, L., Biderman, S., Black, S., Golding, L., Hoppe, T., & Foster, C. et al. (2021). The Pile: An 800GB Dataset of Diverse Text for Language Modeling.
    
6.  EleutherAI. https://arxiv.org/abs/2101.00027
    
7.  GPT-J announcement Komatsuzak, A., Wang, B. (2021). GPT-J-6B: 6B JAX-Based Transformer. https://arankomatsuzaki.wordpress.com/2021/06/04/gpt-j/
    
8.  GPT-NeoX-20B paper Black, S., Biderman, S., Hallahan, E. et al. (2022). EleutherAI. GPT-NeoX-20B: An Open-Source Autoregressive Language Model. http://eaidata.bmk.sh/data/GPT\_NeoX\_20B.pdf
    
9.  RoBERTa paper Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., & Chen, D. et al. (2019). RoBERTa: A Robustly Optimized BERT Pretraining Approach. Meta AI. https://arxiv.org/abs/1907.11692
    
10.  MT-NLG paper Smith, S., Patwary, M., Norick, B., LeGresley, P., Rajbhandari, S., & Casper, J. et al. (2021). Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B, A Large-Scale Generative Language Model. Microsoft/NVIDIA. https://arxiv.org/abs/2201.11990
     
11.  Gopher paper Rae, J., Borgeaud, S., Cai, T., Millican, K., Hoffmann, J., & Song, F. et al. (2021). Scaling Language Models: Methods, Analysis & Insights from Training Gopher. DeepMind. https://arxiv.org/abs/2112.11446
     
12.  Appendix A: Top 50 Resources: Wikipedia + CC + WebText (i.e. GPT-3)
     

  

附录 A：前50个资源：Wikipedia + CC + WebText（即 GPT-3）

基于本文内容，尤其是每个数据集中每个资源的token数量，我们可以对将Wikipedia + Common Crawl + WebText数据集的组合，作为其整体训练数据集的一部分模型进行资源或域的排序。为清楚起见，这包括以下模型：OpenAI GPT-3、EleutherAI GPT-J、EleutherAI GPT-NeoX-20B、Meta AI Megatron-11B和RoBERTA，以及 Microsoft/NVIDIA MT-NLG等。

请注意，展示的排名基于数据集中可用的未加权总token，每个数据集的主观权重由研究人员在模型预训练之前计算得出。其中有一些重复（例如，《纽约时报》既出现在有1.11亿token的WebText中，也出现在过滤后有1亿token的Common Crawl中）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/lBhAE42wKWq8vNMMhx7UalPsfL7gT1NltL259bHUSzxWwtJBHXQrAicjvx24I6TuaVyOiaBBVPicsQIxGtg1TbkhQ/640?wx_fmt=jpeg)  

  

脚注

1. GPT-NeoX-20B paper: pp11, section 6 http://eaidata.bmk.sh/data/GPT\_NeoX\_20B.pdf

2. Datasheet for Datasets paper: https://arxiv.org/abs/1803.09010

3. OpenAI blog: https://openai.com/blog/gpt-3-apps/

4. On the Opportunities and Risks of Foundation Models: https://arxiv.org/abs/2108.07258

5. Size of Wikipedia: https://en.wikipedia.org/wiki/Wikipedia:Size\_of\_Wikipedia

6. C4 dataset: https://www.tensorflow.org/datasets/catalog/c4

7. Common Crawl website: https://commoncrawl.org/

8. C4 paper: https://arxiv.org/abs/2104.08758 pp2, Figure 1 right

9\. Wikipedia categories: https://en.wikipedia.org/wiki/User:Smallbones/1000\_random\_results: “维基百科涵盖哪些主题？覆盖范围是否随时间变化？使用2015年12月抽取的1001篇随机文章对这些问题和类似问题进行了查验...随着时间推移，这些比例相当稳定...传记（27.8%），地理（17.7%），文化和艺术（15.8%），历史（9.9%），生物学、健康和医学（7.8%），体育（6.5%），商业（4.8%），其他社会（4.4%），科学与数学（3.5%），教育（1.8%）。”

10. GPT-1 paper: pp4 “We use the BooksCorpus dataset for training the language model.”

11. https://huggingface.co/datasets/bookcorpus: “Size of the generated dataset: 4629.00 MB”

12. BookCorpus Retrospective Datasheet paper: pp9 https://arxiv.org/abs/2105.05241

13\. GPT-2 paper: pp3 “我们从社交媒体平台Reddit中抓取了至少有3个karma的所有出站链接。这可以被认为是一个启发式指标，用于判断其他用户是否觉得该链接有趣、有教育意义或只是有趣……WebText包含这4500万个链接的文本子集……其中不包括2017年12月之后创建的链接。经过去重和一些基于启发式的清理后，其中包含大约超过800万个文档，总共40GB文本。我们从WebText中移除了所有维基百科文档...”

14\. GPT-2 model card: https://github.com/openai/gpt-2/blob/master/model\_card.md: “我们已经发布了WebText中出现的前1,000个域及其频率的列表。WebText中排名前15位的域是：Google、Archive、Blogspot、GitHub、纽约时报、Wordpress、华盛顿邮报、维基亚、BBC、卫报、eBay、Pastebin、CNN、雅虎和赫芬顿邮报。”

15\. GPT-3 paper: “WebText2：190亿token。\[Alan：WebText2是从WebText稍微扩展而来，所以我们可以减去20%，得到150亿token\]”

16. GPT-2 paper: pp3 “GPT-3: pp9, Table 2.2 “CC: 4100亿token. WebText2: 190亿token. Books1: 120亿token. Books2: 550亿token. Wiki: 30亿token”

17. GPT-3 paper: pp8

18\. BookCorpus repo: soskek/bookcorpus#27: “books3.tar.gz似乎类似于OpenAI在他们的论文中引用的神秘“books2”数据集。不幸的是，OpenAI不会提供细节，所以我们对其差异知之甚少。人们怀疑它是“libgen的全部”，但这纯粹是猜测。尽管如此，books3仍是“所有的bibliotik”......”

19\. BookCorpus paper: https://arxiv.org/abs/1506.06724: “# of words: 984,846,357 \[Alan: BookCorpus有13亿token。我们想要有120-550亿token\]”

20\. Gutenberg paper: https://arxiv.org/abs/1812.08092: “我们介绍了标准化项目古腾堡语料库（SPGC），这是一种开放的科学方法，用于处理完整PG数据的精选版本，其中包含超过50,000本书和3×109word-token\[Alan：相当于大约120亿BPE token，见下文 \]”

21\. Gutenberg repo: https://zenodo.org/record/2422561 “未压缩大小：3GB（count）+ 18GB（token）\[总计21GB\]”

22\. The Pile v1 paper: “Books3（Bibliotik tracker）：100.96GB” \[Alan：乘以每字节token数0.2477 = 250亿token\]

23. The Pile v1 paper: pp3, Table 1 for datasets. pp28, Table 7 for Tokens per byte.

24\. RoBERTa paper: https://arxiv.org/abs/1907.11692 “BOOKCORPUS加上英文WIKIPEDIA。这是用来训练 BERT的原始数据。（16GB）。”

25\. BERT paper: https://arxiv.org/abs/1810.04805 “BERT在BooksCorpus（8亿字）和维基百科（25亿字）上进行训练。”

26. Stories paper: https://arxiv.org/abs/1806.02847 pp5-6

27\. RealNews paper: https://arxiv.org/abs/1905.12616v3 “去重后，RealNews在没有压缩的情况下为120GB。”

28. Gopher paper: https://arxiv.org/abs/2112.11446 pp 7: list of sizes and tokens.

29. Gopher paper: https://arxiv.org/abs/2112.11446 pp 44, Figure A3b.

30. Gopher paper: pp41n14 “请注意，我们将文档去重应用于除Wikipedia和GitHub之外的所有MassiveText子集“

31. GPT-2 paper, pp3.

  

**关于作者**

Alan D. Thompson博士是人工智能专家、顾问。在2021年8月的世界人才大会（World Gifted Conference）上，Alan与Leta（由GPT-3提供支持的AI）共同举办了一场名为“The new irrelevance of intelligence”的研讨会。他的应用型人工智能研究和可视化成果受到了国际主要媒体的报道，同时还在2021年12月牛津大学有关AI伦理的辩论中被引用。他曾担任门萨国际（Mensa International）主席、通用电气（GE）和华纳兄弟（Warner Bros）顾问，也曾是电气与电子工程师协会（IEEE）和英国工程技术学会（IET）会员。

  

（本文经授权后由OneFlow编译发布，译文转载请联系OneFlow获得授权。原文：https://lifearchitect.ai/whats-in-my-ai/）

  

\-END-

更多顶会数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言