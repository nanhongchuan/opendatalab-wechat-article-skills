     视频理解又一力作！VideoMamba: 用于高效视频理解的状态空间模型 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

视频理解又一力作！VideoMamba: 用于高效视频理解的状态空间模型
====================================

原创 Sakura.D​ OpenDataLab 2024-04-17 18:40 上海

> 原文地址: [https://mp.weixin.qq.com/s/QCV8AfdtOwDuNQCOXQZ3Sw](https://mp.weixin.qq.com/s/QCV8AfdtOwDuNQCOXQZ3Sw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

来源：知乎 Sakura.D

近期，上海人工智能实验室 通用视觉团队 提出了一个仅基于状态空间模型(SSM)的高效视频理解架构**VideoMamba**，并通过大量的实验证明了它具备一系列良好的特性，包括：

(1) Visual Domain Scalability; 

(2) Short-term Action Sensitivity; 

(3) Long-term Video Superiority; 

(4) Modality Compatibility。

  

这使得VideoMamba在一系列视频benchmark上取得不俗的结果，**尤其是长视频benchmark，为未来更全面的视频理解提供了更高效的方案**。一起来看看！（文末整理了视频理解相关数据集资源，欢迎下载）

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETM1ppax1D2vz0jcalZ2Mv16Qtzib796ibRQs6TN8eJBDmuP4aYlOxq8qg/640?wx_fmt=png&from=appmsg)

  

* * *

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETPoMiaMtlPPBPhWrnY8duBnZj1ruqChKbWQiaFvaoGicj5eus1ss5O2YkA/640?wx_fmt=png&from=appmsg)

**论文地址：**

_https://arxiv.org/pdf/2403.06977.pdf_  

  

**Github：**

_https://github.com/OpenGVLab/VideoMamba_  

  

**模型地址：**

_https://huggingface.co/OpenGVLab/VideoMamba_

_**Online Demo:**_

__https://huggingface.co/spaces/OpenGVLab/VideoMamba__

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

****研究背景****

视频表征学习长期以来存在两大痛点，一是短clip里存在大量的时空冗余，二是长上下本需要复杂的时空关联。曾经风靡一时的3D CNN和video transformer，分别使用卷积和自注意力机制解决了两大难题。在作者之前的工作UniFormer\[1\]里，他们尝试将卷积和自注意力无缝地结合，尽管它能同时解决两大难题，但对于长视频仍力不从心。而Gemini\[2\]和Sora\[3\]的爆火，使得长视频理解与生成成为了研究的重心，这亟需更高效的视频表征模型。

  

幸运的是，NLP领域这两年涌现了不少高效算子，如**S4**\[4\], **RWKV**\[5\]和**RetNet**\[6\]。而**Mamba**\[7\]提出动态状态空间模型(S6)，能以线性复杂度进行长时的动态建模。这引领了一系列视觉任务的适配，如Vision Mamba\[8\]和VMamba\[9\]，提出了多向SSM机制用于处理2D图片，这些模型不仅能与基于注意力的架构媲美，而且大大减小显存开销。

  

考虑到视频产生的超长token序列，一个自然而然的问题便是，Mamba对视频理解是否同样有效？答案是肯定的。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

****研究方法****

  

 结构

在进入VideoMamba结构的介绍之前，先看看用于1D序列的Mamba block，和用于视觉任务的双向Mamba block。这里不再赘述SSM和Mamba的底层原理，感兴趣的同学可以通过油管视频学习。

_https://www.youtube.com/watch?v=8Q\_tqwpTpVU_

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETVVIHL1R6tyFmXnBRFkzIKC49Rc8HTIDTP3NgjGqlvD2YWLiaj8Yv9jw/640?wx_fmt=png&from=appmsg)

双向Mamba在单向Mamba的基础上，引入了对反向序列的SSM，这使得双向Mamba能更好地对2D序列建模，从而提升对视觉输入的感知能力。基于双向Mamba，他们按照ViT\[10\]的设计，引入\[CLS\] token和空间位置编码，并针对视频建模，引入3D patch embedding和空间位置编码，提出了如下所示的VideoMamba：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETmDMfwQcnqDdJialtezMZib7dBV4gMtZ4C1Fjm2Am6TOY4OibOrzzoeexw/640?wx_fmt=png&from=appmsg)

为了应用双向Mamba处理时空信息，他们拓展原本的2D扫描到不同的双向3D扫描：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETNXo6w80ccUy2yZyGMrhcqk7CnLOzWFaAGelATQZnlda1UBg3sCIgKQ/640?wx_fmt=png&from=appmsg)

其中空间优先扫描最简单，实验证明效果也最好。基于该架构，他们提出了三种不同size的模型，VideoMamba-Ti，VideoMamba-S和VideoMamba-M。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETZzfzLq1q2AbmA4bqiaibJZnx8ROjWMmd24m3sIAFCibBEzpDOuRRZhMHg/640?wx_fmt=png&from=appmsg)

但在实验里，当他们增大VideoMamba规模时，非常容易过拟合，导致大模型的结果甚至差于小模型。为此，他们提出了Self-Distillation策略，使用训练好的小模型当老师，引导大模型训练，有效地避免模型过拟合，而只需少量额外的开销。

  

  

 掩码建模

近来，VideoMAE\[11\]引入掩码建模，显著增强了模型对细粒度时序的理解能力，而UMT\[12\]进一步提出高效的掩码对齐策略，不仅大大减小了训练开销，还使得模型能鲁棒地处理各种单模态和多模态任务。为了增强VideoMamba对时序的敏感性，同时验证它和文本模态的兼容性，他们借鉴UMT的方式，引入CLIP-ViT当teacher，进行两阶段蒸馏训练。

  

不同于UMT使用多层对齐，由于VideoMamba和ViT存在架构差异，作者只对齐模型最后一层，考虑到Mamba block对连续token更友好，他们设计了逐行掩码策略：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIET7icVOhqQcNLoZia5tlMODfVkJvrnoTvVHQonxpwEPiav6VT0690LtopOg/640?wx_fmt=png&from=appmsg)

  

同时他们也考虑了注意力掩码策略，这能保持语义性更强的邻近token。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

****实验****

  

 纵向扩展

作者首先在ImageNet上进行了图像分类实验如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETZKo3kHnrD9eP1UvD6WVbYPMty5KrSibejNV7zfraOgbZIuNr3uC91OA/640?wx_fmt=png&from=appmsg)

可见在没有Self-Distillation (SD)时，VideoMamba-M和VideoMamba-B都会在训练的最后过拟合，其中VideoMamba-B尤为严重。而在引入SD后，VideoMamba-M收敛符合期望，且明显强于老师模型VideoMamba-S。为了避免老师模型带偏训练，他们引入了Early Stop策略，即提前移除蒸馏引导，实验发现并无提升。完整ImageNet对比如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIET5SiaLxr6lShDgN4NU1rhU2aicSyVGy8czEJUZwc7UibAJc2stbCjQwUQw/640?wx_fmt=png&from=appmsg)

和无层次化结构的其他模型相比，VideoMamba优于其他CNN和ViT的模型，如ConvNeXt和ViT。随着模型规模和分辨率放大，性能稳定提升。

###   

  

 短视频理解

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETcJK4fhMVrAbI4Mkhmgx0iadicKiaJia4fZicMnegMmbwQwCdfNdfvE12tSA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETXbThAK70NMxqEicaF2r9Q3sb9bWic0mpsg1QuCKHOqjtECoT7q2ZeZkQ/640?wx_fmt=png&from=appmsg)

在上述K400和SthSthV2的短视频分类任务中，作者同样观察到VideoMamba良好的放缩性，且显著优于基于注意力的视频模型如TimeSformer和ViViT，与结合卷积和自注意力的UniFormer性能相当。再者，在引入掩码训练后，VideoMamba性能显著提升，在细粒度动作分类SthSthV2数据集上，显著好于基于ViT的UMT。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETtGIYhuRhH4mNNkOBpicebmMomuic2O2r4DaXmq9D5opgQETeJvBG74wQ/640?wx_fmt=png&from=appmsg)

进一步的消融实验表明，spatial-first扫描方案效果最好。不同于ImageNet上性能随分辨率逐渐提升，视频数据集上分辨率对性能影响有限，而帧数对性能影响明显。对于掩码建模，逐行掩码优于随机掩码策略，且注意力掩码策略最有效；对齐最后一层效果最好；合适的掩码比例和Droppath能较好提升训练效果。

###   

  

 长视频理解

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETwJOotzOYTJtxAF69ouiazy80dgFkDcnTwCucLWXicD1slPXaHHf4I6rg/640?wx_fmt=png&from=appmsg)

他们在Breakfast，COIN和LVU上评估了VideoMamba对长时视频的理解能力，相较于以往feature-based的方法，VideoMamba仅需要输入稀疏采样的32-64帧，效果便大幅领先，且模型规模更小。

  

  

 多模态视频理解

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD57C7ibmCKTevPSFLLjgpIETKVKwDVQKz2V0y0HbFjrFribPFYy47rOHIttIQrlWVSiaDTQvZFfUHHTA/640?wx_fmt=png&from=appmsg)

作者将VideoMamba和BERT连接，构造多模态模型，并使用大规模多模态数据进行预训练，在多个视频文本检索任务上进行了性能评估。实验揭示VideoMamba同样能很好地作为多模态的视觉编码器，随着预训练数据的增加，能持续提升多模态理解的能力，且由于以ViT为视觉编码器的UMT，尤其是在包含长视频（ANet和DiDeMo）和更复杂场景（LSMDC）的数据集上。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

****结论****

上海人工智能实验室 通用视觉团队提出了仅基于状态空间模型的视频理解架构VideoMamba，全面的实验表明VideoMamba对视频理解具有一系列良好特性，希望它可以为未来长视频的表征学习指明道路。

  

**● 相关数据集下载：**

**ImageNet-1K**

_https://opendatalab.org.cn/OpenDataLab/ImageNet-1K_

  

### **ImageNet-22K**

_https://opendatalab.org.cn/OpenDataLab/ImageNet-21k_

  

### **Kinetics 400**

### _https://opendatalab.org.cn/OpenMMLab/Kinetics-400_

### 

### **Something-Something V2**

### _https://opendatalab.org.cn/OpenDataLab/sthv2_

###   

### **Breakfast (The Breakfast Actions Dataset)**

_https://opendatalab.org.cn/OpenDataLab/Breakfast_

###   

**COIN**

_https://opendatalab.org.cn/OpenDataLab/COIN_

### **DiDeMo (Distinct Describable Moments)**

_https://opendatalab.org.cn/OpenDataLab/DiDeMo_

  

### **LSMDC (Large Scale Movie Description Challenge)**

_https://opendatalab.org.cn/OpenDataLab/LSMDC_

  

参考文献  

\[1\]UniFormer https://github.com/Sense-X/UniFormer

\[2\]Gemini https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/

\[3\]Sora https://openai.com/sora

\[4\]S4 https://github.com/state-spaces/s4

\[5\]RWKV https://www.rwkv.com/

\[6\]RetNet https://github.com/microsoft/unilm/tree/master/retnet

\[7\]Mamba https://github.com/state-spaces/mamba

\[8\]Vim https://github.com/hustvl/Vim

\[9\]VMamba https://github.com/MzeroMiko/VMamba

\[10\]ViT https://github.com/google-research/vision\_transformer

\[11\]VideoMAE https://github.com/MCG-NJU/VideoMAE

\[12\]UMT https://github.com/OpenGVLab/unmasked\_teacher

* * *

  

更多精彩数据集，请访问OpenDataLab官网

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言