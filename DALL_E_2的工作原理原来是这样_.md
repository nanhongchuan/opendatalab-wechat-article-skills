     DALL-E 2的工作原理原来是这样！ \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

DALL-E 2的工作原理原来是这样！
===================

原创 Ryan O'Connor OpenDataLab 2022-04-21 16:32 上海

> 原文地址: [https://mp.weixin.qq.com/s/IVL712E6LSzKbuntkSlCXA](https://mp.weixin.qq.com/s/IVL712E6LSzKbuntkSlCXA)

![](https://mmbiz.qpic.cn/mmbiz_jpg/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmo9t5HgH5TBCuTsicbibe4yMnI6ibqTXVNPyBib2BFeVOPg7No5euZCzFhA/640?wx_fmt=jpeg)  

CLIP+修改版GLIDE双管齐下。

  

OpenAI的模型DALL-E 2于本月初发布，刚一亮相，便在图像生成和图像处理领域卷起了新的风暴。

只需要给到寥寥几句文本提示，DALL-E 2就可以按文本指示生成全新图像，甚至能将毫不相关的物体以看似合理的语义方式组合在一起。

比如用户输入提示“一碗汤是另一个次元的入口”后，DALL-E 2便生成了以下的魔幻图片。

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFm54ZVc31lxIMzYb6IFj76OegtcekicfAshmYoNse3vhtYZic0ibic1M7JRw/640?wx_fmt=png)

“一碗汤是另一个次元的入口” 图源：https://openai.com/dall-e-2/

DALL-E 2不仅能按用户指令生成明明魔幻，却又看着十分合理不明觉厉的图片。作为一款强大的模型，目前我们已知DALL-E 2还可以：

*   生成特定艺术风格的图像，仿佛出自该种艺术风格的画家之手，十分原汁原味！
    

*   保持一张图片显著特征的情况下，生成该图片的多种变体，每一种看起来都十分自然；
    

*   修改现有图像而不露一点痕迹，天衣无缝。
    

感觉有了DALL-E 2，艺术家都可以下岗了。

DALL-E 2目前曝光的功能令人瞠目结舌，不禁激起了众多AI爱好者的讨论，这样一个强大模型，它的工作原理到底是什么？！

  

  

**1**

  

**工作原理：简单粗暴**

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmQnVYqn8fchZHR0BZtoEJGU2L52w8Eb5g8tOCtBrSxnBTHCJtSAtf5w/640?wx_fmt=png)

"一只在吹喷火喇叭的柯基”——DALL-E 2图片生成流程解析 图源：https://arxiv.org/abs/2204.06125

针对图片生成这一功能来说，DALL-E 2的工作原理剖析出来看似并不复杂：

1.  首先，将文本提示输入文本编码器，该训练过的编码器便将文本提示映射到表示空间。
    
2.  接下来，称为先验的模型将文本编码映射到相应的图像编码，图像编码捕获文本编码中包含的提示的语义信息。
    
3.  最后，图像解码模型随机生成一幅从视觉上表现该语义信息的图像。
    

  

  

**2**

  

**工作细节：处处皆奥妙**

可是以上步骤说起来简单，分开看来却是每一步都有很大难度，让我们来模拟DALL-E 2的工作流程，看看究竟每一步都是怎么走通的。

我们的第一步是先看看DALL-E 2是怎么学习把文本和视觉图像联系起来的。

### 

**第一步 - 把文本和视觉图像联系起来**

输入“泰迪熊在时代广场滑滑板”的文字提示后，DALL-E 2生成了下图：

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmkNe0yiawkQZSMS41viahics7qZ21icx5upqSg9OdMQ9cyrj0iaDDthkibrHQ/640?wx_fmt=png)

图源：https://www.assemblyai.com/blog/how-dall-e-2-actually-works/

DALL-E 2是怎么知道“泰迪熊”这个文本概念在视觉空间里是什么样子的？

其实DALL-E 2中的文本语义和与其相对的视觉图片之间的联系，是由另一个OpenAI模型CLIP（Contrastive Language-Image Pre-training）学习的。

CLIP接受过数亿张图片及其相关文字的训练，学习到了给定文本片段与图像的关联。

也就是说，CLIP并不是试图预测给定图像的对应文字说明，而是只学习任何给定文本与图像之间的关联。CLIP做的是对比性而非预测性的工作。

整个DALL-E 2模型依赖于CLIP从自然语言学习语义的能力，所以让我们看看如何训练CLIP来理解其内部工作。

#### **CLIP训练**

训练CLIP的基本原则非常简单:

1.  首先，所有图像及其相关文字说明都通过各自的编码器，将所有对象映射到m维空间。
    
2.  然后，计算每个(图像，文本)对的cos值相似度。
    
3.  训练目标是使N对正确编码的图像/标题对之间的cos值相似度最大化，同时使N2 - N对错误编码的图像/标题对之间的cos值相似度最小化。
    

训练过程如下图所示:

![](https://mmbiz.qpic.cn/mmbiz_gif/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmTtP5kcsFJTiaeKghnZnKQJOrKMFbr8FLI3adxJfD8bArciaeDMO2Jjkg/640?wx_fmt=gif)

CLIP训练流程

#### **CLIP对DALL-E 2的意义**

CLIP几乎就是DALL-E 2的心脏，因为CLIP才是那个把自然语言片段与视觉概念在语义上进行关联的存在，这对于生成与文本对应的图像来说至关重要。

### **第二步 - 从视觉语义生成图像**

训练结束后，CLIP模型被冻结，DALL-E 2进入下一个任务——学习怎么把CLIP刚刚学习到的图像编码映射反转。CLIP学习了一个表示空间，在这个表示空间当中很容易确定文本编码和视觉编码的相关性， 我们需要学会利用表示空间来完成反转图像编码映射这个任务。

而OpenAI使用了它之前的另一个模型GLIDE的修改版本来执行图像生成。GLIDE模型学习反转图像编码过程，以便随机解码CLIP图像嵌入。

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmicCaKTzLNh1IB1krIzKIribmicicS1acibLLqO5zlYickibLxUIm30K7Fg3SA/640?wx_fmt=png)

“一只吹喷火喇叭的柯基”一图经过CLIP的图片编码器，GLIDE利用这种编码生成保持原图像显著特征的新图像。 图源：https://arxiv.org/abs/2204.06125

如上图所示，需要注意的是，我们的目标不是构建一个自编码器并在给定的嵌入条件下精确地重建图像，而是在给定的嵌入条件下生成一个保持原始图像显著特征的图像。为了进行图像生成，GLIDE使用了扩散模型（**Diffusion Model**）。

#### **何为扩散模型？**

扩散模型是一项受热力学启发的发明，近年来越来越受到学界欢迎。扩散模型学习通过逆转一个逐渐噪声过程来生成数据。如下图所示，噪声处理过程被视为一个参数化的马尔可夫链，它逐渐向图像添加噪声使其被破坏，最终（渐近地）导致纯高斯噪声。扩散模型学习沿着这条链向后走去，在一系列步骤中逐渐去除噪声，以逆转这一过程。

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmJrhYUYHI5xqj5d49BtXeGpJl8thpRP3tb1iaR0E7HSzJQduRPMHQvXw/640?wx_fmt=png)

扩散模型示意图 图源：https://arxiv.org/pdf/2006.11239.pdf

如果训练后将扩散模型“切成两半”，则可以通过随机采样高斯噪声来生成图像，然后对其去噪，生成逼真的图像。大家可能会意识到这种技术很容易令人联想到用自编码器生成数据，实际上扩散模型和自编码器确实是相关的。

#### 

**GLIDE的训练**

虽然GLIDE不是第一个扩散模型，但其重要贡献在于对模型进行了修改，使其能够生成有文本条件的图像。

GLIDE扩展了扩散模型的核心概念，通过增加额外的文本信息来增强训练过程，最终生成文本条件图像。让我们来看看GLIDE的训练流程：

![](https://mmbiz.qpic.cn/mmbiz_gif/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmcyc9P25B14UxueQbpPmmus2KAMcw0zg3fxq8N72ppG7gj1qib9fcV3w/640?wx_fmt=gif)

下面是一些使用GLIDE生成的图像示例。作者指出，就照片真实感和文本相似度两方面而言，GLIDE的表现优于DALL-E(1)。

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmTK6569hhOiciaKxkYqIzzwyicqu27CbSxadEThuqZlQKXRVTsUjEIL8fQ/640?wx_fmt=png)

由GLIDE生成的图像示例 图源https://arxiv.org/pdf/2112.10741.pdf

DALL-E 2使用了一种改进的GLIDE模型，这种模型以两种方式使用投影的CLIP文本嵌入。第一种方法是将它们添加到GLIDE现有的时间步嵌入中，第二种方法是创建四个额外的上下文标记，这些标记连接到GLIDE文本编码器的输出序列。

#### **GLIDE对于DALL-E 2的意义**

GLIDE对于DALL-E 2亦很重要，因为GLIDE能够将自己按照文本生成逼真图像的功能移植到DALL-E 2上去，而无需在表示空间中设置图像编码。因此，DALL-E 2使用的修改版本GLIDE学习的是根据CLIP图像编码生成语义一致的图像。

### **第三步 -  从文本语义到相应的视觉语义的映射**

到了这步，我们如何将文字提示中的文本条件信息注入到图像生成过程中?

回想一下，除了图像编码器，CLIP还学习了文本编码器。DALL-E 2使用了另一种模型，作者称之为先验模型，以便从图像标题的文本编码映射到对应图像的图像编码。DALL-E 2的作者用自回归模型和扩散模型进行了实验，但最终发现它们的性能相差无几。考虑到扩散模型的计算效率更高，因此选择扩散模型作为 DALL-E 2的先验。

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFm177tic8ORbSCxwiclyicQ4Bs4XWVQYKXgCOjuuOsEmvlfRcdqugKbibGZw/640?wx_fmt=png)

从文本编码到相应图像编码的先验映射 修改自图源：https://arxiv.org/abs/2204.06125

#### **先验训练**

DALL-E 2中扩散先验的运行顺序是：

1.  标记化的文本；
    
2.  这些标记的CLIP文本编码；
    
3.  扩散时间步的编码；
    
4.  噪声图像通过CLIP图像编码器；
    
5.  Transformer输出的最终编码用于预测无噪声CLIP图像编码。
    

### **第四步 - 万事俱备**

现在，我们已经拥有了DALL-E 2的所有“零件”，万事俱备，只需要将它们组合在一起就可以获得我们想要的结果——生成与文本指示相对应的图像:

1.  首先，CLIP文本编码器将图像描述映射到表示空间；
    
2.  然后扩散先验从CLIP文本编码映射到相应的CLIP图像编码；
    
3.  最后，修改版的GLIDE生成模型通过反向扩散从表示空间映射到图像空间，生成众多可能图像中的一个。
    

![](https://mmbiz.qpic.cn/mmbiz_png/cNFA8C0uVPu42hg5YUicQOnYxa22s2fFmQnVYqn8fchZHR0BZtoEJGU2L52w8Eb5g8tOCtBrSxnBTHCJtSAtf5w/640?wx_fmt=png)

DALL-E 2图像生成流程的高级概述 修改自图源：https://arxiv.org/abs/2204.06125

以上就是DALL-E 2的工作原理啦~

希望大家能注意到DALL-E 2开发的3个关键要点：

*   DALL-E 2体现了扩散模型在深度学习中的能力，DALL-E 2中的先验子模型和图像生成子模型都是基于扩散模型的。虽然扩散模型只是在过去几年才流行起来，但其已经证明了自己的价值，我们可以期待在未来的各种研究中看到更多的扩散模型~
    

*   第二点是我们应看到使用自然语言作为一种手段来训练最先进的深度学习模型的必要性与强大力量。DALL-E 2的强劲功能究其根本还是来自于互联网上提供的绝对海量的自然语言&图像数据对。使用这些数据不仅消除了人工标记数据集这一费力的过程所带来的发展瓶颈；这些数据的嘈杂、未经整理的性质也更加反映出深度学习模型必须对真实世界的数据具有鲁棒性。
    

*   最后，DALL-E 2重申了Transformer作为基于网络规模数据集训练的模型中的最高地位，因为Transformer的并行性令人印象十分深刻。 
    

  

本文经授权转载自微信公众号「AI科技评论」（ID：aitechtalk）

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言