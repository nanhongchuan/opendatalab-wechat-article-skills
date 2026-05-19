     WanJuan-CC数据集：为大型语言模型训练提供高质量Webtext资源 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

WanJuan-CC数据集：为大型语言模型训练提供高质量Webtext资源
=====================================

原创 虹桥北北 OpenDataLab 2024-03-20 18:40 上海

> 原文地址: [https://mp.weixin.qq.com/s/myO1bsy7K2ZsJXUH95ihhQ](https://mp.weixin.qq.com/s/myO1bsy7K2ZsJXUH95ihhQ)

 Datawhale干货 

**作者：**虹桥北北****

**如何在参差不齐的海量网页数据中提炼高质量内容？如何保证模型训练数据的质量和安全性，如何构建高效的处理策略？上海人工智能实验室的这篇论文提供了一种不错的参考方案。**

众多大语言模型成果表明，基于大规模数据预训练，即使在无需标注数据微调的情况下，也能在各类NLP任务中展现出优异的性能。

根据大模型的训练过程中，最优模型参数量、训练数据量和总计算开销之间所存在的 **规模定律(Scaling Law)** 来看，要训练出更强大的模型，需要更多的模型参数量和更大的预训练数据。有研究显示，训练一个拥有175B参数量的语言模型大约需要3.7TTokens的高质量预训练数据。然而，传统的从特定数据源收集并进行定制清洗的数据方案已经无法满足这种规模的数据需求，这对预训练数据集的构建工作提出了新的挑战。

为此，上海人工智能实验室OpenDataLab团队设计了一套针对CommonCrawl网页数据的处理流程，包括数据提取、启发式规则过滤、模糊去重、内容安全过滤以及数据质量过滤等多个步骤，可实现高效生产 **内容安全** 与 **高质量数据** 两大核心目标。

通过这一流程，他们从CommonCrawl中高效获取了一个1.0T Tokens的高质量英文网络文本数据集——WanJuan-CC。结果显示，与各类开源英文CC语料在PerspectiveAPI不同维度的评估上，WanJuan-CC都表现出更高的安全性。此外，通过在4个验证集上的困惑度（PPL）和6个下游任务的准确率，也展示了WanJuan-CC的实用性。

WanJuan-CC在各种验证集上的PPL表现出竞争力，特别是在要求更高语言流畅性的tiny-storys等数据集上。通过与同类型数据集进行1B模型训练对比，使用验证数据集的困惑度（perplexity）和下游任务的准确率作为评估指标，实验证明，WanJuan-CC显著提升了英文文本补全和通用英文能力任务的性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWadJx8YZPGLZlwyxKdgGOOicicowBOAibtQrUMatw7YRZhAFXZKFrsUiaa4Q/640?wx_fmt=png&from=appmsg)

论文链接：https://arxiv.org/abs/2402.19282

数据集下载链接：https://opendatalab.com/OpenDataLab/WanJuanCC

根据论文显示，日前作者从WanJuan-CC中抽取了100B Tokens的开源数据，为其他大型模型的训练提供了宝贵的数据资源，节省了数据成本。与此同时，他们也在数据集中加入了包含数据质量的统计信息，并发布了一篇详细介绍数据处理方法的相关论文，以便开发者可以根据自身需求选择恰当的数据和处理策略。这为大模型的数据处理提供了实用的参考方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWacH5gicX6iblibqiaHMWZUgaiaiaDSia4EOBElTE2MLcrvFHzfsIicJSho0JqibA/640?wx_fmt=png&from=appmsg)

1\. 背景知识
--------

CommonCrawl(CC)作为一个开放的互联网网页的超大规模数据库，收录自2008年以来的历史公开数据，是目前主流大模型预训练数据的重要来源，但由于其原始数据规模庞大、格式复杂、存在大量低质量数据以及可能含有色情、毒性、个人隐私等不安全内容，在数据抽取、清洗过滤、质量提升和价值观对齐等方面存在诸多挑战。

以往的公开数据集中，有些直接使用了CommonCrawl数据库，或者采用了基于CommonCrawl的OSCAR数据集，例如RefinedWeb、Redpajama以及Dolma等。从**数据集大小**、**CC dumps数量**，以及**数据集的安全性**、**个人隐私保护**和**数据质量筛选方法**等多个维度来看，WanJuan-CC与其他基于CommonCrawl处理的数据集相比，具有以下特点：

1.  与RefinedWeb是唯二覆盖了超过90个CC dumps的数据；
    
2.  除了常用的基于关键词和URL的屏蔽之外，还使用了基于模型的方法来排除含有**毒性（toxic）**和**色情（prongraphy）**内容的数据，并利用正则表达式来遮蔽**个人隐私信息（PII）**；
    
3.  特别采用了**基于模型的质量筛选方法**，筛选出了相对高质量的数据；
    
4.  是唯一一个能够完全覆盖**毒性**、**色情**和**个人隐私**三个方面的内容安全措施的公开数据集。
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWasYOc5yQ8u05Az4ojUEVo1hvFARNjib89EqlStrgicN0diazLPLtFQDFmQ/640?wx_fmt=png&from=appmsg)

WanJuan-CC与开源英文CC语料多维度对比

2\. 高性能分布式数据处理框架
----------------

OpenDataLab团队搭建的数据处理流程如图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWaEDzFpw4VWaqXkI9HGCPnxZAdcqVDTUic2uTtVkgTFofRu7iaTxyGTMZQ/640?wx_fmt=png&from=appmsg)WanJuan-CC数据处理工作流

有以下5个核心步骤：

1.  从CommonCrawl的WARC格式数据中提取文本，得到**"原始数据"**（Rawdata）。
    
2.  通过启发式规则对原始数据进行过滤，生成**"清洗数据"**（Cleandata）。
    
3.  利用基于LSH的去重方法对清洗数据进行处理，得到**"无重复数据"**（Dedupdata）。
    
4.  使用基于关键词和域名列表的过滤方法，以及基于Bert的有害内容分类器和淫秽内容分类器对无重复数据进行过滤，产生**"安全数据"**（Safedata）。
    
5.  采用基于Bert的广告分类器和流畅性分类器对安全数据进行进一步过滤，得到**"高质量数据"**（High-Qualitydata）。
    

详细每一步的具体实现可见论文：https://arxiv.org/abs/2402.19282

3\. WanJuan-CC数据处理结果
--------------------

#### 3.1 文档留存率

在CommonCrawl中抽取了约1,300亿份原始数据文档，基于高性能数据处理工作流得到了9.71TB（35.8亿个文档）安全数据，并根据质量排序精选出4.45TB（17.8亿个文档）最高质量的数据作为**WanJuan-CC数据集**，占原始数据的**1.38%**。

如下图所示的是WanJuan-CC处理中，以处理的文档数（即CommonCrawl的网页数）为维度统计的每个阶段相对上一阶段的去除率，以及相对初始网页数的保留率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWaaon8Ria11R2gYaoMeYTlGV7fmRgkh2HWWYHojn0xp66OeX9DyibdtmBQ/640?wx_fmt=png&from=appmsg)

各清洗阶段的文档保留率和去除率（注意：使用的是对数坐标轴）

#### 3.2 不同指标的分布

参考了Redpajama-v2中的一些数据质量指标对WanJuan-CC进行了统计。统计了数据集的文档长度，行数，token长度，非字母字符占比，唯一词占比，平均词长，句子数，停用词占比，符号占词比。每个指标的分布如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWa791lAeeke7yYW63l1Cv5EspDr8aSgdBltMzIw1pX1JzOL2G7aud4iaw/640?wx_fmt=png&from=appmsg)

WanJuan-CC上各指标百分比统计图。为了绘制出分布的主要区域，部分指标的统计范围被截断由于存在长尾分布。

#### 3.3 数据毒性检测

对Wanjuan-CC、Redpajama和RefinedWeb数据集分别抽样100K条数据，使用PerspectiveAPI对7个安全维度进行评分，并根据得分绘制不安全性分布曲线，通过计算曲线下面积作为不安全性的度量指标。由下表结果可看出，Wanjuan-CC在各个维度上的不安全性最低，表明其具有更高的安全性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWakcUIiaQpFXWZZiblribCZneApeztibVaaq1dKG9ycLJssjS5bT5p4NcqaQ/640?wx_fmt=png&from=appmsg)

WanJuan-CC与开源英文CC语料安全性对比

#### 3.4 模型评测结果

为了进一步验证数据的质量，作者使用相同的自回归decoder-onlyTransformer模型，分别使用WanJuan-CC和RefinedWeb从零开始训练。分别在1B参数和3B参数的水平上进行了实验，其中1B模型使用了100Btokens而3B模型使用了200Btokens。

对于1B模型采用计算验证数据集上平均PPL作为评价指标。这是由于小参数量模型很难观测到下游任务的指标变化，因此采用使用验证集的ppl指标会更容易度量小模型的训练效果。作者使用了来自Pile的三个子集pile-books3,pile-openwebtext2,pile-wikipedia-en，以及来自Tiny-stroys的tiny-storys共四个验证集。

实验结果如下表所示，WanJuan-CC在pile-books3，pile-openwebtext2以及pile-wikipedia-en上的ppl都比RefinedWeb略低，而在tiny-storys上的ppl则比RefinedWeb显著低。表明WanJuan-CC的数据质量略优于RefinedWeb，尤其在tiny-storys这种对语言流畅性要求较高的验证集上效果更加明显。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWaEAeOf2mUa7H24Own24qSpdUBO5jLMn5uG7EKhTBBuZzxYiaxkOy7L6A/640?wx_fmt=png&from=appmsg)

不同验证集上WanJuan-CC与Refinedweb模型的困惑度

而对于较大参数量的模型，下游任务的准确率可以更好地反映数据的质量。作者选择了三大类下游任务：英文文本补全(LAMBADA,StoryCloze)，英文通用能力(SuperGLUE)，英文常识问答(HellaSwag,PIQA,WinoGrande)共六个下游任务任务进行评测。

实验结果如表所示。实验结果表明WanJuan-CC在英文文本补全和英文通用能力上有明显提升，而在英文常识问答中HellaSwag有下降，PIQA上有轻微下降，WinoGrande上明显提升。综合来看，WanJuan-CC在下游任务上的表现优于RefinedWeb。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWaicoJBguM51aJP57FGlSNjhSFx9T92bfZdkKWYrNibq3QGXdVcRAUvM0w/640?wx_fmt=png&from=appmsg)

WanJuan-CC与Refinedweb模型在不同下游任务上的准确性

WanJuan-CC作为书生·浦语2.0（InternLM2）大模型的关键语料，其文本质量和高信息密度所带来的效果也经过了模型的有效验证，在仅使用约60%的训练数据即可达到使用第二代数据训练1Ttokens的性能表现，大幅提升模型训练效率，并在相同语料规模上取得了更好的模型性能提升。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vI9nYe94fsFyAlbJsfzxMAzNHIggUDWatJX350NnqKwqiasJj3RvK5qflxT9wNeuCcFkNOL0ZTaIYcxO9AN8QNQ/640?wx_fmt=png&from=appmsg)

WanJuan-CC所使用的数据处理技术可大幅提升数据质量和模型训练效率

4\. 总结
------

总结来说，WanJuan-CC为大规模语言模型训练领域做出了重要贡献。它为研究人员和实践者提供了一个安全、高质量、开源的数据集。未来的工作可以集中在进一步优化数据处理流水线以提高数据质量和安全性，并探索该数据集在更多样化的自然语言处理任务中的应用。

  

* * *

  

WanJuan-CC数据集，扫码直达↓

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD7xWviaiaF3MeibI9Qk8qS7cCSx9dk8micKvjepjptTaxhhUsIExRia1o5Vuqxiajh20ty5nd5jZJj4mL1A/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/OpenDataLab/WanJuanCC**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言