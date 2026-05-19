     跳出 SOTA 内卷，我们发了个“好用至上”的文档解析模型 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

跳出 SOTA 内卷，我们发了个“好用至上”的文档解析模型
=============================

原创 OpenDataLab 2026-04-10 14:47 上海

> 原文地址: [https://mp.weixin.qq.com/s/\_1NSslkjC-FFfUswqUEgvw](https://mp.weixin.qq.com/s/_1NSslkjC-FFfUswqUEgvw)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

  

最新的MinerU2.5-Pro模型发布了。  

  

但这次，我们最想聊的，还不是它的排名。（预告下，文末还是会放成绩单）

  

这两年，大模型很热，OCR模型可能更热。

  

大家都在卷文档解析，具体卷什么呢？

  

卷架构，卷参数，卷谁又换了新的backbone，卷谁又把模型做得更复杂。但文档解析这件事，真还在“拼命改模型结构”这个阶段吗？我们团队认真研究了下，发现未必。

  

我们在最新的MinerU2.5-Pro这篇论文里讲得很直接：我们把多个不同架构、不同参数规模的主流模型，放到同一批真实世界PDF上做系统性交叉分析，最后看到一个很关键的现象——这些模型在同一批难样本上，失败模式高度一致。复杂嵌套表格，大家一起翻车；密集公式，大家一起丢符号；非常规排版，大家一起识别混乱。既然连不同路线的模型都会在同一个地方摔跤，那问题多半就不只是谁的模型架构设计得更巧，而是大家共用的训练数据，本身存在系统性短板。

  

这其实是个挺值得琢磨的判断。过去文档解析圈子里，一个很自然的思路是：效果不够，就改模型。但MinerU2.5-Pro这次偏偏反着来。模型架构，一行不改。对，就是这么干脆。论文里写得很清楚：MinerU2.5-Pro保持了MinerU2.5原有的1.2B参数架构完全不变，所有性能提升都来自数据工程和训练策略优化。不是换了新结构，不是堆了更大的模型，而是把所有精力押在“数据到底怎么做”这件事上。

  

为什么敢这么做？因为我们看到了真正的瓶颈。

  

一边，是覆盖不够。我们在论文中提到，MinerU2.5之前的训练数据不到1000万页，而且高频类别占比过大，标准论文、单栏报告很多，但复杂嵌套表格、密集公式布局这些真正拉开差距的长尾场景，反而明显不足。另一边，是难样本标注难。越是能提升模型上限的数据，自动标注反而越不靠谱。表格结构容易错，公式转写容易偏，噪声一旦进了训练集，后面模型学到的东西也会跟着歪。

  

所以MinerU2.5-Pro这次干的，不是“换个模型再发一遍”。而是先把数据这口井，重新挖深。

  

第一步，先把数据规模做大。

  

不是一般的大。

  

是从不到1000万，扩到6550万。这里真正重要的，不是“多了几倍”，而是如何变多。因为简单堆数据，很多时候只是把旧偏差再复制一遍。MinerU2.5-Pro用的是一套Diversity-and-Difficulty-Aware Sampling，也就是多样性—难度感知采样，不只是补量，更是补短板，专门去修正长尾场景覆盖不足的问题。

  

第二步，让多个模型互相“阅卷”。

  

这一步很妙。

  

一个样本到底难不难，让单个模型自己打分，容易被它的盲区骗到。那就换个办法：让多个异构模型分别去解析同一份文档，再看它们输出的一致性（背靠背打分）。论文里把这套方法叫Cross-Model Consistency Verification。更直白点说：大家都一致，就是Easy；外部模型一致、我们的模型偏差大，就是最有学习价值的Medium；所有模型都不一致，那就是真正的Hard。

  

第三步，专门啃最难的那批数据。

  

这也是最“费功夫”的地方。

  

因为Hard样本最值钱，但也最容易标错。于是MinerU2.5-Pro设计了一套Judge-and-Refine流水线。说人话，就是把模型输出的公式和表格重新渲染出来，再跟原始文档一起做视觉对照。以前是看代码、看字符串，现在是直接看“成品”有没有跑偏。一个对齐符号丢了，一个表格结构错了，渲染后往往会特别显眼。自动校正实在搞不定的，再交给人工专家处理。论文里把这叫render-then-verify iterative correction，更形象的解释就是，像让一个校对员直接看排版成品，而不是只审源代码。

  

第四步，数据分层，训练也分层。

  

这点也很关键。

  

不是所有数据都该一锅炖，也不是所有训练都该一步到位。MinerU2.5-Pro这次是三阶段渐进训练：先用大规模自动标注数据做预训练，再用高质量难样本精调，最后再用进一步对齐输出格式、结构习惯，以及任务级指标（ 用GRPO做对齐）。论文里的消融结果给得很清楚：Stage 1带来+1.31，是最大单阶段增益；Stage 2再加+0.96，其中表格TEDS提升最明显；Stage 3再加+0.45，主要把公式CDM继续往上推。三步下来，把总分从92.98推到95.69。

说到底，这次MinerU2.5-Pro干成的，不是什么玄学。

  

它做的是一件很朴素、但行业里一直没有被系统做好过的事：把数据做得更全，把难样本找得更准，把标注做得更真。

  

同样的模型架构，为什么最后能把分数继续往上顶？答案就在这张训练阶段消融表里：先做大规模训练，再攻难样本，最后用对齐训练把关键指标磨出来。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/uo0n2KqOLAZGvpCCRmzhkBkLvRykYqE4T4WBHuEkglcKEHvP4k9poLicj2V92JNxMgIiaPCkT3mgctsoZru1liasmA0PzXyxEV0IdYxoAX6Cic0/640?wx_fmt=jpeg)

（在OmniDocBench v1.6 上的训练阶段消融实验）

  

这还没完。

  

MinerU2.5-Pro这次甚至连评测本身也一起往前推了一步。我们在做模型时发现，OmniDocBench v1.5的元素匹配逻辑存在系统性偏差：同样正确的解析结果，只因为输出分块粒度不同，比如一个多行公式被拆成多个单行，得分就可能差很多。这样一来，榜单看着热闹，比较却未必公平。

  

于是这次我们又做了OmniDocBench v1.6，发布出来了。我们引入多粒度自适应匹配，还单独加了Hard子集，把评测分成Base/Hard/Full三层。这样看成绩，才更接近真实能力。当然，我们也深知，评测榜单只可能无限逼近对模型真实能力进行公允的评价，却无法替代用户在使用时的真实主观感受。

  

写到这里，其实这篇文章真正想说的东西，已经差不多清楚了。这次发MinerU2.5-Pro，重点不只是“又做出一个更强的模型”。而是想回答一个更大的问题：当模型架构逐渐成熟，文档解析下一步到底该怎么往前走？

  

MinerU2.5-Pro给出的答案很明确：别只盯着架构，数据工程本身，就是增量。 我们在论文结论也说得很直白：在当前这个阶段，协同优化训练数据的覆盖度、信息量和标注准确性，带来的收益，可能比单纯继续改模型结构更大。  

  

这也正是“好用至上”这五个字背后的意思。

  

真正有需求的用户，没那么在乎你又换了什么模型新结构。

大家更在乎的是：

一份复杂论文，你能不能读准？

一个合同表格，你能不能抽全？

一页密集公式，你能不能少错几个符号？

一个表格内的图像和公式，你能不能解出来？

一个复杂版式的PDF，最后喂给知识库和Agent的数据，能不能真的可靠？

  

这些，才叫好用。

  

好了，讲到这里，也该看成绩单了。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAYicpPB3uT2Bv4r7Oj74l2eAcESAcKA20FzFVVKibvUR0b9Hzq15JwwfWv5sPK9GomGpiawaHGnlXibsLnNDwp27IzEic6co92YdVfU/640?wx_fmt=jpeg&from=appmsg)

（在 OmniDocBench v1.6 Base/Hard/Full 上的性能对比）

  

OmniDocBench v1.6上，MinerU2.5-Pro的综合得分做到95.69，从同架构基线92.98提升2.71；Base子集96.12，Hard子集94.08。其中，公式识别CDM 97.29、表格识别TEDS 93.42 都拿到了最佳表现；在Hard子集上，它比第二名92.01拉开了2.07分差。更关键的是，这一切是在1.2B参数、且不改模型架构的前提下实现的。论文里也明确写到，它超过了包括200倍以上参数规模模型在内的现有方法。

  

总之，这次我们最想讲的，不只是“我们又拿了个SOTA”。而是：

跳出SOTA内卷，文档解析这件事，也许该重新回到“是不是真好用”上来了，能不能让用户使用的过程中觉得“真的好”，而不是卷在某个评测集上 的SOTA。

  

从MinerU，到MinerU2.5，再到MinerU2.5-Pro，我们一直在做的，其实是同一件事：把文档解析这块地基打得更牢。目前，模型权重、推理代码和论文已经开源。本月，MinerU各类在线产品（含API）也会更新上线最强的MinerU2.5-Pro模型，并接入MinerU官方 Skill，用户一键安装就能体验。

  

榜单会变，SOTA会换，这都正常。

  

但“好用”这件事，不该跟着OCR的热度一起起落。它应该是一个更硬的标准：复杂文档来了，长尾场景来了，真到生产环境里了，到底好不要用。

  

说到底，benchmark上的分数是结果，排行是故事。而“好用”，才是文档解析领域真正的分量。

  

MinerU2.5-Pro模型（可下载模型进行体验）

● 论文地址：

https://arxiv.org/pdf/2604.04771

  

● HuggingFace的模型地址：

https://huggingface.co/opendatalab/MinerU2.5-Pro-2604-1.2B

  

● ModelScope的模型地址：

https://modelscope.cn/models/OpenDataLab/MinerU2.5-Pro-2604-1.2B

  

END  

  

**相关阅读：  
**

  

  

[MinerU-Diffusion发布：我们想重新回答，文档 OCR 到底该怎么做](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551745&idx=1&sn=32f28edfba35c37043d66f28dc254890&scene=21#wechat_redirect)

2026-03-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAanjOc0Y7utkLlOWLzhzOIaib1rNGia9egfP05ib0RiaAgQ2eUrSDibh79ssibicAGprFFsUmyeIeH9HuUsuzgb4aWBLFTbQ0upszBh1M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551745&idx=1&sn=32f28edfba35c37043d66f28dc254890&scene=21#wechat_redirect)

[总激励200万！2026 MinerU数据智能与前沿语料挑战赛正式启幕，筑基 AGI4S 高质量语料新高地！](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

2026-02-06

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbgD2vP9QPR0XKXLQTSUt6ledgMJyDU6v5WQXrCSpFS4CHCKTChAANic5J0mG9aDyYJZ1icuQ3BflZELSOUP8HDyy1iasz49ianpYo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551519&idx=1&sn=e3df51fad2aaac4c06ee9a0c955a6dd8&scene=21#wechat_redirect)

[MinerU 实战训练营来了！免费学 MinerU 部署、微调、Agent 搭建](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551728&idx=1&sn=938bbae1c68af433f85ba95267aac517&scene=21#wechat_redirect)

2026-03-24

[![](https://mmbiz.qpic.cn/mmbiz_jpg/uo0n2KqOLAYlsICsvsibibQia2K54IvK5euJhnguRE8JPkLJBHphIVibqZJJCKmFVficcYVMVtrqTibHRB1ENRSMBwFw9iaNn5fwNp4KCrUJmnq3r8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551728&idx=1&sn=938bbae1c68af433f85ba95267aac517&scene=21#wechat_redirect)

[一句话，让你的🦞看懂PDF，MinerU 官方 Skill 来了！附赠开发者“全家桶”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

2026-03-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uo0n2KqOLAbZZOF5ZU4633TUhZvib1DtcPjUoonLTDianYHpSU7f41y5eMfmkHsZJ5rvLLa95chfTKAw2iaI4OgZVsJZVBNfXkszm2iaPsxyF2M/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247551685&idx=1&sn=e0e236d01f3942a808d9c25b3ab33431&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言