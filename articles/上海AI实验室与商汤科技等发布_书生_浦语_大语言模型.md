     上海AI实验室与商汤科技等发布“书生·浦语”大语言模型 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

上海AI实验室与商汤科技等发布“书生·浦语”大语言模型
===========================

原创 Shanghai AI Lab OpenDataLab 2023-06-07 13:53 上海

> 原文地址: [https://mp.weixin.qq.com/s/Pb-kFo49oxCCRwKX5NgGZw](https://mp.weixin.qq.com/s/Pb-kFo49oxCCRwKX5NgGZw)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUicOjWA1e3xAfyksNKeJDABTp4MAhD0vW8SVOTgV1gxqHiceI03C2yITQ/640?wx_fmt=png)

随着AI大语言模型越来越多地表现出接近人类的智能，面向人类设计的高难度、综合性考试被越来越多地引入对语言模型的智能水平进行评测。OpenAI在其关于GPT-4的技术报告中就主要通过各领域的考试对模型能力进行检验。2023年高考开考，中文大语言模型是否能够在高考中赶超ChatGPT呢？

  

6月7日，上海人工智能实验室（上海AI实验室）、商汤科技联合香港中文大学、复旦大学及上海交通大学发布千亿级参数大语言模型“书生·浦语”（InternLM）。“书生·浦语”具有**1040亿参数**，是在包含**1.6万亿token**的多语种高质量数据集上训练而成。全面评测结果显示，“书生·浦语”不仅在知识掌握、阅读理解、数学推理、多语翻译等多个测试任务上表现优秀，而且具备很强的综合能力，因而在综合性考试中表现突出，在多项中文考试中取得超越ChatGPT的成绩，其中就包括中国高考各科目的数据集（GaoKao）。

  

“书生·浦语”相关技术报告已在网上公开：https://github.com/InternLM/InternLM-techreport（点击阅读原文直达链接），报告对模型的技术特点以及测试结果进行了详细阐述。

  

**综合“大考”：“书生·浦语”多项成绩领先于ChatGPT**

“书生·浦语”联合团队选取了20余项评测对其进行检验，其中包含全球最具影响力的四个综合性考试评测集：

由伯克利加州大学等高校构建的多任务考试评测集MMLU；

由微软研究院推出的学科考试评测集AGIEval（含中国高考、司法考试及美国SAT、LSAT、GRE和GMAT等）；

由上海交通大学、清华大学和爱丁堡大学合作构建的面向中文语言模型的综合性考试评测集C-Eval；

由复旦大学研究团队构建的高考题目评测集Gaokao。

实验室联合团队对“书生·浦语”、GLM-130B、LLaMA-65B、ChatGPT和GPT-4进行了全面测试，针对上述四个评测集的成绩对比如下（满分100分）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVU029c1QFg2UbVIkR0lLr5UcJ7kQ3Fs725I8lerZ7rAUmNdG3FNMS9DQ/640?wx_fmt=png)

可以看到，“书生·浦语”不仅显著超越了GLM-130B 和 LLaMA-65B等学术开源模型，还在AGIEval、C-Eval以及Gaokao等多个综合性考试中领先于ChatGPT；在以美国考试为主的MMLU上实现和ChatGPT持平。这些综合性考试的成绩反映出“书生·浦语”扎实的知识掌握程度和优秀的综合能力。

虽然 “书生·浦语”在考试评测上取得优秀成绩，但在测评中也可以看到，大语言模型仍然存在不少能力局限性。“书生·浦语” 受限于2K的语境窗口长度（GPT-4的语境窗口长度为32K），在长文理解、复杂推理、撰写代码以及数理逻辑演绎等方面还存在明显局限。另外，在实际对话中，大语言模型还普遍存在幻觉、概念混淆等问题；这些局限使得大语言模型在开放场景中的使用还有很长的路要走。

  

**四个综合性考试评测数据集结果**

**MMLU**是由伯克利加州大学（UC Berkeley）联合哥伦比亚大学、芝加哥大学和UIUC公共构建的多任务考试评测集，涵盖了初等数学、物理、化学、计算机科学、美国历史、法律、经济、外交等多个学科。细分科目结果如下表所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVU9AGb0rY74ia4SrNwwbzVJTQr546wgwAlUC4e9zGLI1fxxtnfk8xfRVw/640?wx_fmt=jpeg)

（粗体表示最佳结果，下划线表示第二）

**AGIEval**是由微软研究院在今年新提出的学科考试评测集，主要目标是通过面向的考试来评估语言模型的能力，从而实现模型智能和人类智能的对比。这个评测集基于中国和美国各类考试构建了19个评测大项，包括了中国各科高考、司法考试以及美国的SAT、LSAT、GRE和GMAT等重要考试。值得一提的是，在这19个大项有9个大项是中国高考，通常也列为一个重要的评测子集 AGIEval（GK）。下列表格中，带GK的是中国高考科目。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUAqkugtuZQnTc3JXT8ibh4CITD2H50L0yQ8WP86L1eRg03bbyRrfn75Q/640?wx_fmt=jpeg)

（粗体表示最佳结果，下划线表示第二）

**C-Eval**是由上海交通大学、清华大学和爱丁堡大学合作构建的面向中文语言模型的综合性考试评测集。它包含了52个科目的近14000道考题，涵盖数学、物理、化学、生物、历史、政治、计算机等学科考试，以及面向公务员、注册会计师、律师、医生的职业考试。测试结果可以通过leaderboard获得。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUKZJJ3e6ylicydJxQMPg3nUAbLNzuhpEqBob7E8hUYOVdVzEcxlLysWA/640?wx_fmt=jpeg)

（https://cevalbenchmark.com/static/leaderboard.html）

**Gaokao**是由复旦大学研究团队构建的基于中国高考题目的综合性考试评测集，包含了中国高考的各个科目，以及选择、填空、问答等多种题型。在GaoKao测评中，“书生·浦语”在超过75%的项目中均领先ChatGPT。

![](https://mmbiz.qpic.cn/mmbiz_png/icoPP1A2zIX9f3ol82YEFUpNwR270eYgqbMEHbvO1RSgl0EsDaUmBA20JTNbA7ibZduiaajaSQiaSPe8vlTBRdSysQ/640?wx_fmt=png)

  

**分项评测：阅读理解、推理能力表现出色**  

为了避免“偏科”，研究人员还通过多个学术评测集，对“书生·浦语”等语言模型的分项能力进行了评测对比。结果显示，“书生·浦语”不仅在中英文的阅读理解方面表现突出，并且在数学推理、编程能力等评测中也取得了较好的成绩。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUwwCj0iaezDxcaon0nNlW31oeCnNvd9LxK05vMJFHs0t35XuU4SNmibvQ/640?wx_fmt=jpeg)

在**知识问答**方面，“书生·浦语”在TriviaQA和NaturalQuestions两项评测上得分为69.8和27.6，均超越LLaMA-65B（得分为68.2和23.8）。

在**阅读理解（英语）**方面，“书生·浦语”明显领先于LLaMA-65B和ChatGPT。浦语在初中和高中英语阅读理解中得分为92.7和88.9，⽽ChatGPT得分为85.6和81.2，LLaMA-65B则更低。

在**中文理解**方面，“书生·浦语”的成绩全面超越主要的两个中文语言模型ERNIE-260B和GLM-130B。

在**多语翻译**方面，“书生·浦语”在多语种互译中的平均得分为33.9，显著超越LLaMA（平均得分15.1）。

在**数学推理**方面，“书生·浦语”在GSM8K和MATH这两项被广泛用于评测的数学考试中，分别取得62.9和14.9的得分，明显领先于Google的PaLM-540B（得分为56.5和8.8）与LLaMA-65B（得分为50.9和10.9）。

在**编程能力**方面，“书生·浦语”在HumanEval和MBPP这两项最具代表性的考评中，分别取得28.1和41.4的得分（其中经过在代码领域的微调后，在HumanEval上的得分可以提升至45.7），明显领先于PaLM-540B（得分为 26.2和36.8）与LLaMA-65B（得分为23.7和37.7）。

此外，研究人员还对“书生·浦语”的安全性进行评测，在TruthfulQA（主要评价回答的事实准确性）以及CrowS-Pairs（主要评价回答是否含有偏见）上，“书生·浦语”均达到领先水平。

* * *

  

**上海人工智能实验室**

我国人工智能领域的新型科研机构，开展战略性、原创性、前瞻性的科学研究与技术攻关，突破人工智能的重要基础理论和关键核心技术，打造“突破型、引领型、平台型”一体化的大型综合性研究基地，支撑我国人工智能产业实现跨越式发展，目标建成国际一流的人工智能实验室，成为享誉全球的人工智能原创理论和技术的策源地。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUjQ75AV2KSWpWBNDnOvWkuI2PWW6v7WzBrCcvYPyq27F8SicMPJnLicOA/640?wx_fmt=png)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言