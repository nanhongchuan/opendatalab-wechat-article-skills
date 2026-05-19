     教程 | 给大模型插上小语种“翅膀”，附ms-swift韩语继续预训练与指令微调教程 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

教程 | 给大模型插上小语种“翅膀”，附ms-swift韩语继续预训练与指令微调教程
==========================================

原创 OpenDataLab 2025-04-16 21:09 上海

> 原文地址: [https://mp.weixin.qq.com/s/XvuF5Tl\_0N-IXXewSAHPzw](https://mp.weixin.qq.com/s/XvuF5Tl_0N-IXXewSAHPzw)

推荐语

3月22日，上海人工智能实验室发布了全新升级的[“万卷·丝路2.0”多语言多模态语料库](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550189&idx=1&sn=cf85998f0df64b5454504cf22589caca&scene=21#wechat_redirect)，在阿语、俄语、韩语、越南语、泰语5个语种基础上，新增塞尔维亚语、匈牙利语、捷克语3个稀缺语料数据，涵盖四大数据模态共计1,150万条数据。

  

实践证明，在小语种场景下，利用“万卷·丝路”语料库对通用大模型进行微调，使轻量化模型在多语言处理领域展现出超越大模型的卓越表现。本文将基于该语料库数据，分享来自魔搭社区的大模型继续预训练与指令微调详细教程，教你如何为AI插上更强的小语种能力的“翅膀”，欢迎大家动手实践。

  

数据集地址：  
https://www.modelscope.cn/organization/OpenDataLab

  

一键微调框架：  

https://github.com/modelscope/ms-swift

  

01

  

数据集介绍

  

“万卷·丝路2.0”具有多语言、大规模、多模态、高质量的特点：

1. 语种数量扩充：

在阿拉伯语、俄语、韩语、越南语、泰语5个语种基础上，新增塞尔维亚语、匈牙利语、捷克语等3个稀缺语料数据。

  

2. 数据模态、总量全面升级：

在纯文本数据基础上，新增图片-文本、音频-文本、视频-文本、特色指令微调SFT四大模态数据，覆盖多模态研究全链路；整体数据总量超过1150万条，音视频时长超过2.6万小时，满足多种研究任务的需求。

  

3. 超精细数据，多场景适用：

经成熟数据生产管线及安全加固，结合过滤算法与当地专家人工精细化地标注质检，“万卷·丝路2.0”  已成为覆盖多模态、多领域的大规模高质量数据集，含20余种细粒度多维分类标签及详细的文本描述，适配文化旅游、商业贸易、科技教育等不同场景，为开发者提供得力助手。

  

开源内容

图片-文本累计开源超过200W条； 音频-文本开源超过1600小时； 音频-文本开源超过2.5w小时； SFT数据开源18w条；

  

开源数据详情：

语种名称

图文模块数据量（张数）

音频模块时长（小时）

视频模块时长（小时）

SFT模块数据量

阿语

220,000

200

1738

23,000

俄语

250,000

212

3491

23,000

韩语

530,000

202

3412

23,000

越南语

450,000

205

2901

23,000

泰语

100,000

201

5684

23,000

塞尔维亚语

80,000

206

2578

23,000

匈牙利语

220,000

208

3470

23,000

捷克语

270,000

202

2453

23,000

####   

02

  

数据集赋能大模型性能跃迁

  

经严格评测验证，“万卷·丝路”展现出显著的模型赋能效应：基于7B参数基础模型训练，实现综合性能跃升52.3%；在700亿参数的大模型训练中，仍保持12.8%的性能增益。值得注意的是，依托“万卷·丝路”，使轻量化模型在多语言处理领域展现出超越大模型的卓越表现。

![](https://mmbiz.qpic.cn/mmbiz_png/8ZLuyaibrZbl9Hwmhhf4XNCibEG5KIWdkerPszlW1kYhfPEiakfmCoic0nHibTtxTicdxTQr53xP3VzCRmiaMCiauFOkibQ/640?wx_fmt=png&from=appmsg)

  

03

  

韩语数据集继续预训练与指令微调实践

  

  

以下是以“万卷·丝路”韩语数据为代表，进行大模型继续预训练与指令微调实践教程，欢迎大家实践与复现：

● 模型准备：Llama-3.1-8B-Instruct

● 数据准备：从“万卷·丝路”多语言多模态语料库抽取部分韩语纯文本预训练数据（OpenDataLab/WanJuan-Korean）、18w条韩语指令微调数据（OpenDataLab/WanJuanSiLu2\_sft\_ko）  

● 训练框架：ms-swift、Megatron-SWIFT；（使用Megatron-SWIFT和ms-swift分别对OpenDataLab/WanJuan-Korean和OpenDataLab/WanJuanSiLu2\_sft\_ko进行继续预训练和指令微调）  

> 训练框架介绍：
> 
> ms-swift是魔搭社区官方提供的大模型与多模态大模型训练部署框架。
> 
> ms-swift开源地址：
> 
> https://github.com/modelscope/ms-swift
> 
>   
> 
> Megatron-SWIFT在ms-swift的基础上
> 
> 引入了Megatron的并行技术来加速大模型的训练，包括数据并行、张量并行、流水线并行、序列并行，上下文并行，具有更快的训练速度。
> 
> Megatron-SWIFT文档查看：
> 
> https://swift.readthedocs.io/zh-cn/latest/Instruction/Megatron-SWIFT训练.html

● 操作步骤：

#### 环境准备

在开始微调之前，请确保您的环境已准备妥当。

    git clone https://github.com/modelscope/ms-swift.git

#### a. 使用Megatron-SWIFT对OpenDataLab/WanJuan-Korean数据集进行继续预训练

首先，你需要额外安装Megatron-SWIFT依赖：

    pip install pybind11

    

当然你也可以直接使用镜像：

    modelscope-registry.us-west-1.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda12.4.0-py311-torch2.5.1-modelscope1.25.0-swift3.2.2

    

由于数据集很大，这里只下载部分数据集进行训练。

    # 下载数据集

（关于HF权重格式与mcore格式转换，参考Megatron-SWIFT文档：https://swift.readthedocs.io/zh-cn/latest/Instruction/Megatron-SWIFT%E8%AE%AD%E7%BB%83.html）

  

Megatron-SWIFT训练脚本如下（更快的训练速度）：

    NPROC_PER_NODE=4 \

    

训练显存资源：

![](https://mmbiz.qpic.cn/mmbiz_png/8ZLuyaibrZbl9Hwmhhf4XNCibEG5KIWdkerVDIlt3NYZf0hLzr4Eib2RCGMTbIm8OLLT1SranULoOJlBhM8S5dI2Q/640?wx_fmt=png&from=appmsg)

  

训练loss曲线：

![](https://mmbiz.qpic.cn/mmbiz_png/8ZLuyaibrZbl9Hwmhhf4XNCibEG5KIWdkeFRKZL2eCAuNdVfW1ribIxY6phoX0heUFqtOaKibiaFhlgvvVYoxPPpoVA/640?wx_fmt=png&from=appmsg)

####   

#### b. 使用ms-swift对OpenDataLab/WanJuanSiLu2\_sft\_ko数据集进行指令微调

    NPROC_PER_NODE=4 \

    

#### 效果评估

目前主流的大语言模型大多具备多语言能力，在多种不同语言上都展现出了强大的生成能力。目前评估多语言任务效果的数据集有以下几个：

*   Belebele数据集：
    
    仅关注多项选择形式的阅读理解。
    
      
    
*   BenchMAX数据集：
    
    关注大模型的核心性能，这些能力包括但不限于指令遵循能力、推理能力、长文本理解能力、代码生成能力、工具使用能力以及翻译能力。
    

  

BenchMAX是一个包含多语言，覆盖多种重要任务和17种多样化的语言的评测基准。对于每个能力，BenchMAX包含了一至两个不同的测试集，并且绝大多数测试集都经过母语使用者的标注，保证了数据集的高质量。

  

论文地址：  

https://arxiv.org/pdf/2502.07346

  

数据集地址：  

https://github.com/CONE-MT/BenchMAX

  

评测结果显示，通过上述继续预训练与指令微调后的模型在韩语阅读理解任务指标提升2个点，说明模型在多语言方面能力得到了改进、提升。

  

研究员也结合热门使用场景，给出更多应用建议：后续可以增加商贸领域的韩语SFT数据，扩增商品场景的韩语视觉-文本SFT数据提升，以适配更多出海、跨语言商贸合作等场景。

  

* * *

  

以上就是本次教程分享，诚邀您扫码提交“万卷·丝路”数据集使用反馈。您的建议将支持“万卷·丝路”多语言多模态语料库成为更质量的AI基础设施，助力全球开发者构建跨语言智能工具与应用，以人工智能赋能高质量共建“一带一路”。

![](https://mmbiz.qpic.cn/mmbiz_png/8ZLuyaibrZbnRkYy0EUwlRxT2GLmeQIPdBRYOD7gX01GvialSIx4iaM2yO2hm8Kxic2RhHibtxjfMxuzYSS7q8TicKuA/640?wx_fmt=png&from=appmsg)

更多交流请添加小助手微信获取更多高质量、大规模、安全可信的数据集沟通更多关于数据集的合作事项👇

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXvuwoX1MnPTK5CU4AUjky31SQt9NqTySzQhEOuveRaGvqNRJiaFiaWY024lkgHJicXWXg6oSRFr50icg/640?wx_fmt=jpeg)

    

    点击阅读原文，即可跳转数据集~

* * *

  

👇点击关注OpenDataLab公众号获取

更多高质量语料信息~

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言