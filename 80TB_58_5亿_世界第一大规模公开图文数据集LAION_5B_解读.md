     80TB！58.5亿！世界第一大规模公开图文数据集LAION-5B 解读 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

80TB！58.5亿！世界第一大规模公开图文数据集LAION-5B 解读
====================================

原创 专注于AI 数据的 OpenDataLab 2022-10-08 20:13 上海

> 原文地址: [https://mp.weixin.qq.com/s/jzliYUJ6M-ojKny--92zGA](https://mp.weixin.qq.com/s/jzliYUJ6M-ojKny--92zGA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

  

继去年LAION-400M\[1\]这个史上最大规模多模态图文数据集发布之后，今年又又又有LAION-5B\[2\]这个超大规模图文数据集发布了。

  

其包含 58.5 亿个 CLIP \[5\]过滤的图像-文本对的数据集，比 LAION-400M 大 14 倍，是世界第一大规模、多模态的文本图像数据集，共80T数据，并提供了色情图片过滤、水印图片过滤、高分辨率图片、美学图片等子集和模型，供不同方向研究。

  

一起来看看。

  

****今年大火的DALL·**E** 2 再次掀起了多模态图文匹配研究热潮。****

**在图文匹配领域，CLIP\[5\]模型使得在ImageNet上的zero-shot分类精度从11.5%提升到76.2%，受此启发，ALIGN\[3\]、BASIC\[4\]等大型图文多模态模型进一步改进，除了本身的模型优化之外，目前的进展其实都比较依赖底层的上亿图文对数据，但这些数据集及模型仅有少数公开，所以LAION提出了LAION-5B及在该数据集上训练的模型，并提供web界面提供预先计算的向量和搜索功能。**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6Cll2HpyRFj730sD3koNjlb5dQYSpWL7cs1taq1zwBG2FgOQbOr3dJPibOcpJLf6cHQlU2BvwyaAg/640?wx_fmt=png)

  

**图1: LAION-5B检索样例**

**数据来源：https://laion.ai/blog/laion-5b/**

  

**LAION-5B通过CommonCrawl获取文本和图片，OpenAI的CLIP计算后获取图像和文本的相似性，并删除相似度低于设定阈值的图文对（英文阈值0.28，其余阈值0.26），500亿图片保留了不到60亿，最后形成58.5亿个图文对，包括23.2亿的英语，22.6亿的100+语言及12.7亿的未知语言。**

  

**官网：**

**https://laion.ai/blog/laion-5b/**

  

**数据集信息：**

**https://opendatalab.org.cn/LAION-5B**

  

**论文：**

**https://openreview.net/pdf?id=M3Y74vmsMcY**

  

**LAION-400M介绍****：**

**https://mp.weixin.qq.com/s/vzyOF4esJCkBZDMiNScE5A**

  

******今天介绍围绕以下几个点展开：******

● 数据集背景信息

● LAION-5B有什么

● LAION-5B可以做什么任务

● 如何使用LAION-5B训练

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**数据集背景****信息**

CLIP\[5\]、DALLE\[6\]这些模型证明了大规模多模态数据的重要性，即使不需要手动标注，也能超越很多优秀的有监督模型，经典如CLIP使用400M对网络图文对进行训练，不仅在ImageNet上zero-shot超越在ImageNet 1.2M有监督数据上训练的resnet50性能1.9%，并且能够识别普通视觉模型无法识别的素描图、油画图、艺术图等(图2)。

  
紧接着发布的ALIGN\[3\]、GLIDE\[12\]等证实了这一点，但是这些大型数据集都没有开源，因此这一领域的研究，只集中在少数几个机构中，2021年公布的LAION-400M\[1\]是当时最大的公开图文数据集，本次发布的LAION-5B\[2\]是LAION-400M的14倍，足够规模的公开数据使得该领域的研究更多元化，能够让更多的研究者参与到这一领域的研究中。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6Cll2HpyRFj730sD3koNjl5KvkHncXNnHl8x7ia1VPruX03Z23jqhic2fdVYiaZGbkNloYyicbibontGA/640?wx_fmt=png)

  

图2: CLIP能够识别素描图、油画图和艺术图，但ResNet对这些识别较差

数据来源：https://openai.com/blog/clip/

  

各个机构陆续发布过多模态数据集及图像数据集，但是由于数量不多或并未公开，并不能在多模态预训练模型上取得较好的效果，这里将LAION和以前的部分数据集进行了简单对比。

  

**1.1 图文对数据集**

最开始，数据集均通过人工注释生成，如**COCO**\[7\]和**Visual Genome**\[8\]，COCO Captions在COCO图片数据基础上，由人工标注图片描述得到。Visual Genome是李飞飞2016年发布的大规模图片语义理解数据集，含图像和问答数据，标注密集，语义多样。这两个数据集主要用于图像生成描述（Visual Genome也可以用于图像问答），然而由于图片数量较少，仅有330k和5M对，模型发展受到限制。

  

后来逐渐出现了非人工注释的多模态数据集，如**Conceptual Captions 3M**\[9\]和**Conceptual Captions 12M**\[16\]，对应描述从网站的alt-text属性过滤而来。随着CLIP模型的出现，大规模预训练模型逐渐成为多模态领域趋势，类似的还有**ALT200M**\[10\]和**ALIGN1.8B**\[3\]，数据集规模逐渐扩大到数十亿，虽然没有经过人工注释，但由于数据量大，在NLP、零样本视觉推理、多模态检索等多种下游任务中仍能取得良好甚至SOTA的效果。但可惜的是，CLIP所使用的4亿图文对以及ALIGN等数据集均没有公开。

  

去年公开的**LAION-400M**拥有4亿图文对，是当时最大的公开图文数据集，一经公开获取了很好的反响，也有多个模型基于该数据进行训练取得了较好效果，但相较官方CLIP仍有轻微差距，并且LAION-400M中含有大量令人不适的图片，对于模型，尤其是生成模型影响较大。比如stable diffusion模型，很多人会用来生成色情图片，产生了不好的影响，更大更干净的数据集成为需求。

  

这次公开的**LAION-5B**除了扩大规模之外，还提供了一些模型进行过滤，LAION训练了色情内容识别模型NSFW过滤绝大部分不适图片，水印检测模型可以过滤水印图片，由于部分隐私或不适内容若删除会影响研究丰富性，所以在总体数据内不会删除，会提供不同的子集用于不同用途。

  

**1.2 图像数据集**

大型如Instagram-1B、JFT300M、JFT3B均为私有数据集，暂未公开。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6Cll2HpyRFj730sD3koNjl8KToL17xtUVE6yThFLqibXDvQ4FichL1icJhp2aRg2KEK9csXttFm0VIA/640?wx_fmt=png)

图3: 数据集大小比较，公开数据集(top)和私有数据集(bottom)。LAION-5B比其他公开数据集大100倍，数据来源：\[2\]

  

LAION-5B的数据规模目前最大，可以对许多未公开的多模态模型进行训练并获得较好效果，并公开了第一个开源的**CLIP**模型。并且数据多样，包含各种领域图片，对于后续研究提供了更多的方向，比如数据重叠、图片噪声、不适图片筛选、低资源语言、自然语言对于多模态的作用、模型偏差等等。

  

但如果将LAION-5B直接应用于工业，需要注意清洗图片，因为LAION-5B中含水印图片及不适图片，模型会因此产生偏差。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**LAION-5B有什么**

在LAION400M发布之后，在接连的研究中发现了未过滤引起的问题，受这些启发，除了50亿图文对之外，LAION还提供了多种子集。之前的研究中，为了限制生成模型不生成种族主义图片，尝试在训练集中删除了与暴力相关的物体、人和面部的图像，然而，这显然限制了模型的通用能力—比如人脸生成。因此，为了研究的多样性，在整体数据集中并没有删除此类内容，而是提供了多种子集。

  

除此之外，LAION还提供了复现的**CLIP**等模型，展示了基于LAION训练的模型拥有不输于原模型的能力。和**KNN**索引、**Web**界面方便检索合适的图片。

  

当然，为了大规模数据集方便下载，LAION也提供了**img2dataset**分布式下载，可以指定图像和文本大小，可以20个小时内单个节点下载1亿张图像（1Gbps速度，32G内存和16个内核的i7 CPU）

  

****2.1 子集****
--------------

LAION-5B中包括23.2亿的英语，22.6亿的100+语言及12.7亿的未知语言，我们将子集分别标记为：

**●** **laion2B-en**

**● **laion2B-**multi**

**● **laion1B-**nolang**

  

LAION训练了一个基于CLIP嵌入的色情内容识别模型NSFW，可以过滤3%的不适图片，NSFW准确率约96%，过滤后有子集：

**● laion2B-en-safety**

****●** laion2B-multi-safety**

****●** laion1B-nolang-safety**

  

LAION训练了一个水印识别模型，过滤后有子集：

****●** laion2B-en-watermark**

****●** laion2B-multi-watermark**

****●** laion1B-nolang-watermark**

  

一个170M的超分辨率子集：

****●** **laion**\-high-resolution**

  

一个120M的美学图片子集，可以用来做图片生成：

****●** **laion**\-aesthetic**

  

更多可以参考：

https://huggingface.co/laion

  

****2.2 开源模型****
----------------

对现有未开源的多模态模型，LAION在子集上重新训练或微调，取得了较好的效果。

  

**CLIP**：通过openCLIP开源了CLIP模型，分别在LAION-400M和LAION-5B上训练，前者效果略低于OpenAI，后者zero-shot效果高于OpenAI。

  

**BLIP**：重新在LAION-400M中115M子集上训练，再使用CLIP对候选描述排序，评测后优于其他模型，用于描述生成和图文匹配。

  

**Glide**：在LAION-2B对Glide模型进行微调，获得了不错的效果。

  

除此之外，还提供了水印识别模型和色情内容识别模型**NSFW**。

  

****2.3 KNN index/web界面****
---------------------------

LAION使用autofaiss工具构建了KNN索引，共800GB。

  

为了方便使用，将索引集成到网站中。web界面基于查询图像/文本来搜索图像/文本。通过CLIP的embedding来检索语义相似性较高的图像文本，鉴于高分辨率图片的丰富性，可以生成图像子集来训练自定义模型，也可以选择特定训练目的的图像分辨率。

  

检索网站左侧添加了**safe mode**，可以筛选不适图片。

  

检索网站：

https://rom1504.github.io/clip-retrieval/?back=https%3A%2F%2Fknn5.laion.ai&index=laion5B&useMclip=false

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6Cll2HpyRFj730sD3koNjluIRgbiborZkbNcYUKwxd2bHxMmLbicZiclBGs7ibibZQFhkN3zweuUGwdvg/640?wx_fmt=png)

图4: web检索demo

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**LAION可以做什么任务**

LAION提供了大规模的图文数据，可以用来做大部分多模态及CV工作，多模态方面包括大规模预训练、图文匹配、图像生成（图像生成、图像修复/编辑等）和文本生成（图像生成文本、VQA等）等下游任务，CV方面包含分类等，LAION也提供了使用数据集训练的模型作为参考。

  

****3.1**** ****图文匹配及多模态预训练****

包括但不限于任务：多模态预训练、图文匹配、图文检索。

  

CLIP模型使用对比学习将图像和文本嵌入到相同空间，标志着图像-文本的多模态的进展，用于图文匹配/检索、zero-shot分类等领域。但CLIP并未公开训练数据，因此LAION分别使用LAION-400M和LAION-2B重新训练了CLIP模型，准确率和OpenAI版本不相上下。

  

****3.2**** ****生成任务****

**● 图像生成**

包括但不限于任务：高分辨率图像生成、图像修复/编辑、文本生成图片、条件图像生成。

  

LAION提供了子集来过滤不适图片和水印图片，为图像生成进一步提供了条件。目前有不少模型可以基于LAION子集来生成，DALLE\[6\]这种自回归模型或者GLIDE\[12\]这种扩散模型，以下给出几个例子：

  

\- **Stable Diffusion**\[13\]使用LAION-5B的子集，在压缩的空间对图像进行重建，可生成百万像素的高分辨率图片，用于图像修复、图像生成等。

  

\- **VQ-Diffusion**\[14\]模型使用矢量量化变异自动编码器，在LAION-400M训练文本生成图像的模型，获得更高的图像质量。

  

\- **Imagen**\[15\]在LAION-400M的子集上训练，使用强大的语言模型抽取特征，并指导生成对应文本的高质量图像，击败DALLE-2\[20\]实现SOTA。

  

\- 也可以挑选其中领域图片进行生成，如人脸生成**FARL**\[17\]。

  

**● 文本生成**

包括但不限于任务：图像生成文本、VQA、Visual Entailment

  

\- **BLIP**\[18\]重新在LAION-400M中115M子集上训练，再使用CLIP对候选描述排序，评测后优于其他模型，用于描述生成和图文匹配。

  

\- **MAGMA**\[19\]在LAION子集上训练，基于适配器的微调来增强语言模型的生成，为视觉问题生成答案，仅使用simVLM的0.2%的数据量但生成了较好的结果。

  

****3.3 分类任务****

可以做zero-shot、finetune和训练。

  

通过web搜索子集或官方提供的子集，可以做构建**分类识别**，**水印识别**、**色情内容识别**、**面部特征学习**等等。也可以通过提供的大规模预训练模型，在下游任务做**zero-shot**和**finetune**。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6Cll2HpyRFj730sD3koNjlKWVkYCxhSiaEyorXBWEpiayCkic3iaqSoHkeW2sibPRTCHOg2j2PiauRctMg/640?wx_fmt=png)

  

图5: 对比了WIT(官方)、在LAION-400M和LAION-2B-en上训练的CLIP模型在下游数据集的zero-shot性能对比，可以看到LAION训练的模型性能优越。数据来源：\[2\]

  

****3.4 其他任务****
----------------

  

LAION数据丰富，可以筛选需要的数据做其他任务，比如可以在LAION-2B-multi中筛选指定语言数据做**低资源语言任务**，可以做**数据重叠对模型的影响、模型偏见**等等。

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**如何使用LAION**

对于有丰富GPU资源的同学，在训练任务时，可以使用全集/子集数据进行大规模训练。对于资源相对有限的同学，无法进行大规模训练，依然可以使用LAION预训练模型进行zero-shot、finetune等研究，也可以将其作为图像资源池自行检索所需图像。

  

****4.1 大规模训练****
-----------------

可以使用全集/子集来训练，完成多模态、视觉领域相关任务，往往对资源需求较大。

  

● 全集为58.5亿图文对，通过CLIP过滤，含有少量噪声和不适数据。

  

● 子集参考2.1中提供的多种子集，包括但不限于无不适图片子集、无水印子集、超分辨率子集、美学子集等等。

  

● 如果没有合适的子集，也可以通过web检索页面，到合适的数据下载，可以生成图像子集进行训练，也可以选择适合训练的图像分辨率，该方法的好处是可以根据自定义场景选择图片。

  

****4.2 少量训练****
----------------

对于资源有限的工程师，可以选择LAION-5B中所需数据和LAION-5B提供的预训练模型，进行训练。

  

● **数据方面**

可以选取LAION-5B的部分数据进行训练，比如通过web检索界面检索自定义场景图片，或者使用有/无水印图片、高分辨率图片、美学分数较高图片等等，进行小规模训练。

  

**● 模型方面**

可以使用LAION提供的预训练模型对下游进行zero-shot、few-shot或finetune。

\- **zero-shot/few-shot**：官方提供了大规模预训练的开源模型，CLIP、BLIP等，效果显著，基于LAION训练的CLIP性能与原模型不相上下。基于LAION-400M训练的CLIP性能可以参考图6。

  

\- **finetune**：官方提供了微调方式供参考：https://github.com/mlfoundations/wise-ft，也可以采取常规的finetune方式进行训练。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6Cll2HpyRFj730sD3koNjlv4lJZZdYsmdbm1AKxa6AvYqJS4qPD1ZvuG5xTCI6kAkO43Y9cbxM2g/640?wx_fmt=png)

  

图6: CLIP基于LAION-400M对ImageNet、ImageNetV2、Birdsnap、Country211、Flowers102、GTSRB、Standford Cars、UCR101等数据集进行测试，和OpenAI的CLIP性能不相上下。

数据来源：https://github.com/mlfoundations/open\_clip

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtr8mXdAliagEZQibic5U8ZicIyGDlmfEQX3WiccXcKgtfzdS45XzcaAAZHLg/640?wx_fmt=png)

**总结**

LAION-5B，这个包含超过50亿图像文本对的数据集，进一步扩展了语言视觉模型的开放数据集规模，使得更多研究者能够参与到多模态领域中。并且为了推动研究，提供了多个子集用于训练各种规模的模型，也可以通过web界面检索构建子集训练。已有多个模型和论文证明了基于LAION子集训练的模型能够取得良好甚至SOTA的效果。

  

  

参考文献  

\[1\] Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, and Aran Komatsuzaki. Laion-400m: Open dataset of clip-filtered 400 million image-text pairs. arXiv preprint arXiv:2111.02114, 2021.

\[2\]Christoph Schuhmann, Romain Beaumont, Cade W Gordon, Ross Wightman, mehdi cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Patrick Schramowski, Srivatsa R Kundurthy, Katherine Crowson, Richard Vencu, Ludwig Schmidt, Robert Kaczmarczyk, Jenia Jitsev. LAION-5B: An open large-scale dataset for training next generation image-text models,2022.URL https://openreview.net/pdf?id=M3Y74vmsMcY

\[3\]Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc V. Le, Yun- Hsuan Sung, Zhen Li, and Tom Duerig. Scaling up visual and vision-language representation learning with noisy text supervision. CoRR, abs/2102.05918, 2021. URL https://arxiv. org/abs/2102.05918.

\[4\]Hieu Pham, Zihang Dai, Golnaz Ghiasi, Hanxiao Liu, Adams Wei Yu, Minh-Thang Luong, Mingxing Tan, and Quoc V Le. Combined scaling for zero-shot transfer learning. arXiv preprint arXiv:2111.10050, 2021.

\[5\]Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In International Conference on Machine Learning, pages 8748–8763. PMLR, 2021.

\[6\]Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever. Zero-shot text-to-image generation. CoRR, abs/2102.12092, 2021. URL https://arxiv.org/abs/2102.12092.

\[7\]Tsung-YiLin,MichaelMaire,SergeBelongie,JamesHays,PietroPerona,DevaRamanan,Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in context. In European conference on computer vision, pages 740–755. Springer, 2014.

\[8\]Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A Shamma, et al. Visual genome: Connecting language and vision using crowdsourced dense image annotations. International journal of computer vision, 123(1):32–73, 2017.

\[9\]Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2556–2565, Melbourne, Australia, July 2018. Association for Computational Linguistics. doi: 10.18653/v1/P18-1238. URL https://aclanthology.org/P18-1238.

\[10\]Xiaowei Hu, Zhe Gan, Jianfeng Wang, Zhengyuan Yang, Zicheng Liu, Yumao Lu, and Li- juan Wang. Scaling up vision-language pre-training for image captioning. arXiv preprint arXiv:2111.12233, 2021.

\[11\]Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg, and Li Fei-Fei. ImageNet Large Scale Visual Recognition Challenge. International Journal of Computer Vision (IJCV), 115(3):211–252, 2015. doi: 10.1007/s11263-015-0816-y.

\[12\]Alex Nichol, Prafulla Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela Mishkin, Bob McGrew, Ilya Sutskever, and Mark Chen. Glide: Towards photorealistic image generation and editing with text-guided diffusion models, 2021. URL https://arxiv.org/abs/2112.10741.

\[13\]Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High- resolution image synthesis with latent diffusion models. CoRR, abs/2112.10752, 2021. URL https://arxiv.org/abs/2112.10752.

\[14\]Shuyang Gu, Dong Chen, Jianmin Bao, Fang Wen, Bo Zhang, Dongdong Chen, Lu Yuan, and Baining Guo. Vector quantized diffusion model for text-to-image synthesis. CoRR, abs/2111.14822, 2021. URL https://arxiv.org/abs/2111.14822.

\[15\]Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho, David J Fleet, and Mohammad Norouzi. Photorealistic text-to-image diffusion models with deep language understanding, 2022. URL https://arxiv.org/abs/ 2205.11487.

\[16\]Soravit Changpinyo, Piyush Sharma, Nan Ding, and Radu Soricut. Conceptual 12m: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 3558–3568, 2021.\[17\]YinglinZheng,HaoYang,TingZhang,JianminBao,DongdongChen,YangyuHuang,LuYuan, Dong Chen, Ming Zeng, and Fang Wen. General facial representation learning in a visual- linguistic manner. CoRR, abs/2112.03109, 2021. URL https://arxiv.org/abs/2112. 03109.

\[18\]Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language- image pre-training for unified vision-language understanding and generation, 2022. URL https://arxiv.org/abs/2201.12086.

\[19\]Constantin Eichenberg, Sidney Black, Samuel Weinbach, Letitia Parcalabescu, and Anette Frank. MAGMA - multimodal augmentation of generative models through adapter-based finetuning. CoRR, abs/2112.05253, 2021. URL https://arxiv.org/abs/2112.05253.

\[20\]Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents, 2022. URL https://arxiv.org/abs/ 2204.06125.

（上下滑动查看）  

  

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD5bPPuyXe8kQwYWIQMu6RQWGHAZZTxLiacZfK3Ijel9Xia8os9qsNnhVm351BMPOtAjBPVuq6nV8aCQ/640?wx_fmt=jpeg)

**作者丨******Jorie****

希望世界和平无bug

\- End -

  

**还有哪些你关心的话题？**

**扫码入群,欢迎交流** ![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD6qKD9WCiaOd8HjSjiaMeTBNgCrp5PMqHnMAft2j0rj5bfyIzEajecZWhadWjhISZN7EquicHRHReYiaA/640?wx_fmt=png)

最新数据集上架动态

最全数据集内容解读

最牛大佬在线答疑

最活跃的同行圈子

……

  

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/7yjDpC9UfD7NEyym4C8KBFplT20DM2vqAUAysVwzco8icviaYQ6McYIHep7ythBW0oZic97dXnhS6LbnoyibAqCbLQ/640?wx_fmt=jpeg)

添加小助手微信，发送“入群”，等待邀请

  

‍

_**↓**查看LAION-5B_‍

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言