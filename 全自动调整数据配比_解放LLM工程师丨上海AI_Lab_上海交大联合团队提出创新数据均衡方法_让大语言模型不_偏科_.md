     全自动调整数据配比，解放LLM工程师丨上海AI Lab&上海交大联合团队提出创新数据均衡方法，让大语言模型不“偏科” \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

全自动调整数据配比，解放LLM工程师丨上海AI Lab&上海交大联合团队提出创新数据均衡方法，让大语言模型不“偏科”
==========================================================

原创 OpenDataLab 2025-06-10 19:30 上海

> 原文地址: [https://mp.weixin.qq.com/s/RWvGtqYapemoIU1ECF0WUw](https://mp.weixin.qq.com/s/RWvGtqYapemoIU1ECF0WUw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**🔍 研究背景**

  

大型语言模型 (LLM) 凭借其强大的理解和逻辑推理能力，在多个领域展现了惊人的能力。然而，除了增加模型参数，高质量的数据对提升LLM性能同样关键。 

  

当对模型进行监督微调（SFT）时，研究人员发现LLM在多任务场景下常出现"偏科"现象——部分能力突出而部分能力并未涨进，甚至退化。这种不平衡的现象导致大模型在不同的领域上能力不同，进而影响用户体验。 

  

为了解决这一问题，来自上海 AI 实验室 OpenDataLab 团队和上海交通大学等的研究者迅速将目光聚焦到SFT训练的训练集上，提出是否可以通过调整训练集的组成来缓解LLM“偏科”的情况？直觉上来看，直接将LLM的弱势科目的训练数据增加一倍，就可以让最后的结果发生变化，但这种方法看似可行，然而由于训练数据之间的复杂耦合关系，效果有限。

  

最后，研究者们通过构建 IDEAL（Innovative Data Equilibrium Adaptation Framework）——一种创新的数据均衡适应框架，建模量化每个领域数据对最终结果的影响，科学地调整训练数据集的组成，实验表明，IDEAL 方法优化混合 SFT 数据集中不同领域数据的分布，有效提高模型在多个能力上的对齐和性能表现。

  

非常实用的一项研究，快来看看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWswugPM93Xibd0cNtXwbPay51GaNv7kVKeV22yg3wczHQA9v0QBnP7Y3OmvEdslcDEWk1v6qMPFGg/640?wx_fmt=png&from=appmsg)

📜 论文信息

● 标题：《IDEAL: Data Equilibrium Adaptation for Multi-Capability Language Model Alignment》

  

● 论文链接：

https://arxiv.org/abs/2505.12762

  

● 代码库：

https://anonymous.4open.science/r/IDEAL-678C520/README.md

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**🚀 IDEAL方法**

  

问题建模： 

首先按照不同的领域准备高质量的训练数据集：，并给出对应的用于验证的验证集：。通过在训练集上面训练模型，获得训练集上的最优参数，论文希望在验证集上的损失达到最小。为了能够方便的调整训练集，论文引入了对应的变量，并将这个优化问题显示地建模了出来：

  

（左右滑动查看）

  

论文从理论角度给出了各个领域数据调整对于最优模型在验证集上影响的大小（具体可见原论文中的Lemma 1）：

  

（左右滑动查看）

  

高效计算： 

由于式子中存在参数二阶矩阵的逆的操作，计算的资源消耗非常大。为了能够扩展到LLM的参数量级，论文采用了K-FAC的理论来近似简化计算Hessian矩阵的逆。通过挑选模型参数中的“重要”层的数值来近似刻画各个领域数据对于最后模型性能的影响，并最后通过合理的放缩超参数m来控制最后的调整比例大小：

  

（左右滑动查看）

  

整体的算法流程图如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWF4j4qfl7sbcE4rHKbonyPczfA6ua3J0vJrXichkGXN9xIlJex1Lbgg8kvrUJQlXWOueaHiala3VoQ/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**📊 实验结果**

  

论文主要以Llama3.1 8B模型作为Base model，测试了IDEAL对四个典型领域上多任务训练的模型的提升效果。可以看到，无论是epoch1还是epoch3，IDEAL都能够在2轮迭代后将原先不擅长的Coding能力显著提升。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAWF4j4qfl7sbcE4rHKbonyPS3XJgQ07Im0Z1BjRwa0YLGRFfiarWDWPYft7Sl56IJNiaic5gC8XNpRXQ/640?wx_fmt=png&from=appmsg)

  

除此之外，论文还有其他的发现：

*   一般随机初始的训练集分布都是有进一步优化的空间：文章中，无论在在四个领域四个benchmark，还是5个领域8个benchmark上，无论初始分布是各个领域是数量相等的或者不等的分布上，IDEAL都实现了对于平均结果的提升。
    

*   SFT阶段训练数据的数量不是关键：因为以往的re-weighting工作会控制整体的训练数据量，我们将对比的方法DoReMi和DOGE，都提升了整体的数据量到IDEAL对应的数量，但实验结果证明，提升数据量而没有改变数据混合分布，对于模型的提升效果甚微。
    

*   如果数据分布配比不合适，更多数据量，训练地更久，反而会导致更加不均衡的模型效果。我们发现相比训练epoch1，训练同样的数据3epoch会导致数据之间的负面冲突被放大，导致最终的模型性能更加不均衡。
    

*   论文还指导了超参数m的选取：m的取值最好选在0.15。因为理论要求，应该在原始分布的周围优化数据配比，所以m应该选取不大的步长。而选取过小的步长，对于模型最终的效果影响也会较小。综上所属，论文在m=0.1，0.15，和0.3三个设定的实验中更加推荐0.15的取值。
    

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

**🌟 应用价值**

  

IDEAL解决了得到各个领域高质量训练数据之后如何配比组合成为统一的训练集的问题。通过迭代优化的方式优化训练集的各个领域数据数量。避免了之前研究者需要按经验，人工调整各个数据集配比的dirty work，具有较大的实用价值。

欢迎关注：

👇

📜 论文信息

● 标题：IDEAL: Data Equilibrium Adaptation for Multi-Capability Language Model Alignment

● 作者：上海交通大学、上海AI实验室、清华大学等

● Anonymous GitHub代码库

https://anonymous.4open.science/r/IDEAL-678C520/README.md

● ArXiv论文

https://arxiv.org/abs/2505.12762

  

**——The  End——**

**相关阅读：**

[MinerU教程第二弹丨MinerU 本地部署保姆级“喂饭”教程](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

2025-05-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUUOH1ib8viafCJ0mFGr96SWphia1CXYlB7PYcd0mOyDymiaPiboxic4YrUJMsYFiaqZ4mJWtY8VxpqumSuQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550587&idx=1&sn=c5e384ed79be3ac63f6f8755b770fbfd&scene=21#wechat_redirect)

[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

2025-05-09

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2DfiaWj7tD6u36J9MUptoIn8mjrdEE46UKxxIePWjHAujAAXkRVZR4rA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[用“万卷·丝路”数据集打造阿拉伯语版DeepSeek（附免费算力与教程）](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

2025-05-07

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVVE4CUaZgloMDBwxJp0ZKlqtIEr8eYASLlgX0y2BK3sIyyrE5SErdqfyR4wCyo1Sng8m0ibNA46Qw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[多语言语料库万卷·丝路2.0开源，数据模态全面升级，搭建文化交流互鉴AI桥梁](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550189&idx=1&sn=cf85998f0df64b5454504cf22589caca&scene=21#wechat_redirect)

2025-03-22

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWpiaQyypfXugnluAuNdTb2xbwXGXEm21O9eEukHmxlcaXsroDrQJFBNCGGGVCAVxssO82WpqDFBhA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550189&idx=1&sn=cf85998f0df64b5454504cf22589caca&scene=21#wechat_redirect)

  

  

  

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言