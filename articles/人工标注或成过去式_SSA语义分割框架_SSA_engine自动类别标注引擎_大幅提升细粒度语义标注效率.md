     人工标注或成过去式？SSA语义分割框架、SSA-engine自动类别标注引擎，大幅提升细粒度语义标注效率 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

人工标注或成过去式？SSA语义分割框架、SSA-engine自动类别标注引擎，大幅提升细粒度语义标注效率
====================================================

原创 ZVG实验室 OpenDataLab 2023-04-19 17:07 上海

> 原文地址: [https://mp.weixin.qq.com/s/vAd6hz8NnqKjobPe-x6zVA](https://mp.weixin.qq.com/s/vAd6hz8NnqKjobPe-x6zVA)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**推荐语**

  

4月5日，Meta发布 Segment Anything 模型和 SA-1B 数据集，引发CV届“地震”，其凭借一己之力，成功改写了物体检测、数据标注、图像分割等任务的游戏规则。

  

复旦大学ZVG实验室团队基于此最新开源了**SSA语义分割框架**和**SSA-engine自动注释引擎**，可以为所有mask自动地生成细粒度语义标签，填补了SA-1B中缺乏的细粒度语义标注的空白，为构建大规模语义分割数据集打下基础，也可以用于多模态的特征对齐等研究。

  

最后，我们提供了包含SA-1B在内的多个数据集快速下载地址，欢迎大家关注与探索。

  

本文已授权，作者丨复旦大学ZVG实验室

  

![](https://mmbiz.qpic.cn/mmbiz_gif/Ak9PbJX9eib4qbYuuSbHUAYatUHk1GY7c80tNX6IjK6hkpB3Ym1QrKsGxngtumKicuDweyMEHaGnbGyIKeW1hia1Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

****Semantic Segment Anything****

**复旦大学ZVG实验室**  

  

**Repo**: 

_https://github.com/fudan-zvg/Semantic-Segment-Anything_

**Demo**:

_https://replicate.com/cjwbw/semantic-segment-anything_

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD60hoHI1TBqUdhK64qiaO41iboavVzwkndk0uJRiaaOWlzselFtaSk3x3plTYIYJlGfluP4KBppcmicqg/640?wx_fmt=png)

  

SAM是一种强大的图像分割模型，SA-1B是目前为止最大的分割数据集。然而，SAM缺乏为每个mask预测语义类别的能力。为了弥补上述不足，**我们提出了一个基于SAM的语义分割框架，不仅能准确地分割mask，还能预测每个mask的语义类别，**称为**Semantic Segment Anything  (SSA)**。

  

此外，我们的**SSA可以作为一个自动化的稠密开放词汇标注引擎，称为Semantic segment anything labeling engine  (SSA-engine)，**为SA-1B或任何其他数据集提供丰富的语义类别注释。该引擎显著减少了人工注释及相关成本的需求。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4icYShnYBh4c2MTZJe5UjKicp08hwDzFUaaI4uNa2d4uia5WU2CzoDrhlicRhBuWvy3faicAiaCGbCP9fA/640?wx_fmt=png)

  

  

 为什么我们需要SSA：

**1.** SAM是一种高度可泛化的图像分割算法，可以提供精确的mask分割。SA-1B是迄今为止最大的图像分割数据集，提供了精细的mask分割注释。但是，**SAM和SA-1B都没有为每个mask提供类别预测或注释**。这使得研究人员难以直接使用强大的SAM算法来解决语义分割任务，或者利用SA-1B来训练自己的模型。

  

**2.** 先进的close-set分割器，如Oneformer，open-set分割器，如CLIPSeg，以及image caption方法，如BLIP，可以提供丰富的语义注释。不过，**它们的mask分割预测可能无法分割出像SAM那么精确和细腻的边界**。

  

**3.** 因此，通过将SAM和SA-1B的精细图像分割mask与这些先进模型提供的丰富语义类别标注相结合，我们可以**生成具有更强泛化能力的语义分割模型，以及一个大规模语义分割的图像分割数据集**。

  

  

 SSA能做什么？

**● SSA**: 这是第一个利用SAM进行语义分割任务的开放框架。它支持用户将其现有的语义分割器与SAM无缝集成，无需重新训练或微调SAM的权重，从而实现更好的泛化和更精确的掩模边界。

  

**● SSA-engine**: SSA-engine为大规模的SA-1B数据集提供了密集的开放词汇类别注释。在手动审核和精细化之后，这些注释可以用于训练分割模型或细粒度的CLIP模型。

  

下面为大家详细介绍一下。

  

SSA：语义分割一切

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4icYShnYBh4c2MTZJe5UjKichjmsMfkJQtRkeicyO3AcDF4YsJFGUw80cIWzJMiaNEDicWe8OOnQU8KPw/640?wx_fmt=png)

在引入SAM之前，大多数语义分割应用场景已经有了自己的模型。这些模型可以为区域提供粗略的类别分类，但在边缘处模糊不清，缺乏精确的掩模。为了解决这个问题，**我们提出一种利用SAM来增强原有模型性能的开放框架——SSA，即使用原始语义分割模型提供类别，同时利用强大的SAM提供掩模**。

  

如果您已经在数据集上训练了一个语义分割模型，您不需要为了更精准的分割能力，重新训练一个基于SAM的新模型。相反，您可以**继续使用旧模型作为语义分支（Semantic branch）。SAM强大的泛化和图像分割能力可以提高原有模型的性能。**值得注意的是，SSA适用于原本的分割器预测的掩模边界不是非常精确的场景，如果原有模型的分割已经非常精确了，则SSA很难带来提升。

  

SSA包含两个分支，**Mask Branch**和**Semantic Branch**，以及一个投票模块来决定每个mask的类别。

  

**1\. Mask branch（蓝色）**。SAM可以作为Mask branch提供一组有清晰边界的mask。

  

**2\. Semantic branch（紫色）**。这个分支为每个像素提供语义类别，它由一个语义分割器实现，用户可以自定义用户感兴趣的类别的分割器。这个分割器不需要具有非常精细的边界预测能力，但应该尽可能准确地对每个区域进行分类。

  

**3\. Semantic Voting module（红色）**。这个模块根据mask的位置裁剪出相应的像素类别。在这些像素类别中，像素数量排名第一的类别将被视为该mask的分类结果。

  

SSA-engine：自动化类别标注引擎

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4icYShnYBh4c2MTZJe5UjKicRUx1NYlbicUQ0JTIKAaN6Tcic4s1wHttLFnS8glSEic7icjgRq66ygHSDQ/640?wx_fmt=png)

**SSA-engine是一个自动化注释引擎，可以为SA-1B数据集或者任何一个数据集提供初始的语义标注**。SSA-engine利用close-set分割模型来预测基础类别，并结合image caption模型来提供open-vocabulary的标注。得益于这样的设计，SSA-engine一方面可以为大多数样本提供令人满意的类别标注，另一方面，可以利用image caption方法提供更详细的语义类别标注。

  

SSA-engine填补了SA-1B缺乏的细粒度语义标注的空白，显著减少了人工类别标注需求。它有潜力成为训练大规模视觉感知模型和更细粒度CLIP模型的基础。

  

**SSA-engine由三个组件组成：**

**1\. Close-set语义分割器（绿色）**。它是两个分别在COCO和ADE20K数据集上训练close-set语义分割模型，用于分割图像并获取粗略的类别信息。预测的类别仅包括简单、基本的类别，以确保每个mask都获得相关的标签。

  

**2\. Open-vocabulary分类器（蓝色）**。利用image caption模型来描述与每个mask对应的图像区域。然后提取名词或短语作为候选的open-vocabulary类别。这个过程提供了更多样化的类别标签。

  

**3\. 最终决策模块（橙色）**。SSA-engine使用一个类别过滤器（即CLIP）从l来自Close-set语义分割器和Open-vocabulary分类器的类别列表中，过滤出最合理的top-k个预测。最后，Open-vocabulary Segmentor（即CLIPSeg）根据top-k类别和图像区域预测最适合的类别。

  

  

 实验

**1. 推理时间**

我们在单个NVIDIA A6000 GPU上测试了模型的推理速度，结果如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD74fgsGzZMkDeLQVqA0zGQM5wTPKp5iaDPOQx8BNkPibttcv4u2GBybe0qY4l9jhPdf0qZdibvmoBiczw/640?wx_fmt=png)

在被用于测试的200张图像中，平均每张图像包含了99.9个mask。

  

**2. 显存开销**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD74fgsGzZMkDeLQVqA0zGQMenHIEr0TMfgH1o7xCCQPp89qj3sfG7vVZEngB9EHVSpa5aRYI42wIw/640?wx_fmt=png)

**3.** **Close-set的语义分割结果**

为了验证SSA架构的提升，我们选用了Huggiing face上的**不同参数量和精度的Segformer模型（包括B0，B2和B5版本）**，作为一个mask预测没有那么准确的Seamntic branch。实验结果表明，**在原本的语义分割模型（作为Semantic branch）的性能一般的情况下，SSA可以带来明显的准确度提升**。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD74fgsGzZMkDeLQVqA0zGQMl3bWeFFLn88SJ439a9FcJftiasShFbIf7eDfpicF2qDuoWkHOo4poXvw/640?wx_fmt=png)

注意，本实验的Segformer的模型权重和代码均由NVIDIA公开，下载自Hugging face，而这些模型的mIoU略低于Github仓库中的实验结果。

  

**4.** **Close-set的语义分割结果**

我们**验证了SSA在雾天语义分割数据集Foggy Driving上的性能**。实验中，我们是用了OneFormer作为Semantic branch，其权重和代码来自于Hugging face。

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD74fgsGzZMkDeLQVqA0zGQMmyXW5ZjoTticJZfJnZQbX3Uk8vECFsKQqcmQEdoV1URrHkVuibpBXZTQ/640?wx_fmt=png)

  

  

 实测效果

**SSA的Close-set语义分割实测**

**1\. Cityscapes**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD74fgsGzZMkDeLQVqA0zGQMY6PxtLaPcfltAHBN8vkJdJdDHURz7rLeVTh7esYbjT48YcaDq7BPwg/640?wx_fmt=png)

**2. ADE20K**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD74fgsGzZMkDeLQVqA0zGQMqeFNCqh7sygPgoL3HWAMtPPj2U4TAicX5aGibKzUAKkQoiaOnMtUgQrkA/640?wx_fmt=png)

**3\. Foggy Driving**

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD74fgsGzZMkDeLQVqA0zGQMql9OgopaEEricDdfQbnLcV8u6sicjPusdIqHKTDia5MnKz8VeBIftIJlA/640?wx_fmt=png)

SSA-engine的Open-vocabulary标注实测

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD4icYShnYBh4c2MTZJe5UjKic0DNoaWRetLaKgm0dtLvdH5ib4RiaAo3fMLWTv0rSic5FE7RWHCoxtkTOg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD60hoHI1TBqUdhK64qiaO41ibscYypNpum9RwmGuW4iaIKeSbx456wD18SHtbgnwQIvrQ46w1iatibib94Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD60hoHI1TBqUdhK64qiaO41ibqsCkjNAX3bnibVmz3q46EW3feeIWQibd8cjkko4YUujYbT2iazWjDTp7w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD60hoHI1TBqUdhK64qiaO41ibfp0MmZfMkyLqfftUSkMv1qsszqQicSUSibRPGCSYOZLllTpJbqDheX9g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD60hoHI1TBqUdhK64qiaO41ibRsFo7u4HSKGMTm8nQ6E8WOfTqumd8g7KO3ic72nhX3ZU5590x90I8wg/640?wx_fmt=png)

  

  

 快速安装：

    git clone git@github.com:fudan-zvg/Semantic-Segment-Anything.gitcd 

（左右滑动查看）

  

**1\. SSA的快速上手**

**1.1 数据准备**

● 下载 ADE20K 或者 Cityscapes dataset,并在 data 文件夹解压.

● 下载SAM 的权重并放在 ckp 下.

    mkdir ckp && cd ckp

（左右滑动查看）

  

****1.2 SSA模型推理****

使用8卡GPU在**ADE20K**上推理SSA

    python scripts/main_ssa.py --ckpt_path ./ckp/sam_vit_h_4b8939.pth --save_img --world_size 8 --dataset ade20k --data_dir data/ade20k/ADEChallengeData2016/images/validation/ --gt_path data/ade20k/ADEChallengeData2016/annotations/validation/ --out_dir output_ade20k_test

（左右滑动查看）

使用8卡GPU在**Cityscapes**上推理SSA‍

    python scripts/main_ssa.py --ckpt_path ./ckp/sam_vit_h_4b8939.pth --save_img --world_size 8 --dataset cityscapes --data_dir data/cityscapes/leftImg8bit/val/ --gt_path data/cityscapes/gtFine/val/ --out_dir output_cityscapes

（左右滑动查看）

  

******1.3 SSA验证******

获取 **ADE20K**的验证结果

    python evaluation.py --gt_path data/cityscapes/gtFine/val/ --result_path output_cityscapes/ --dataset cityscapes

（左右滑动查看）

获取 **Cityscapes**的验证结果

    python evaluation.py --gt_path data/cityscapes/gtFine/val/ --result_path output_cityscapes/ --dataset cityscapes

（左右滑动查看）

  

**2.SSA-engine的快速上手**

● 下载SA-1B数据集并放在data路径下

● 运行SSA-engine对SA-1B进行自动类别标注

    python scripts/main_ssa_engine.py --data_dir=data/examples --out_dir=output --world_size=8 --save_img

（左右滑动查看）

  

  

 致谢

**● Segment Anything** 提供 SA-1B 数据集。

**● HuggingFace** 提供代码和预训练模型。

**● CLIPSeg**、**OneFormer**、**BLIP** 和 **CLIP** 提供强大的语义分割、图像说明和分类模型。

  

  

 引用

如果您觉得我们的工作对您有帮助，请引用我们的仓库：

    @misc{chen2023semantic,

（左右滑动查看）

  

  

 数据集快速下载链接

**COCO 2017**

_https://opendatalab.com/COCO\_2017_

  

**ADE20K**
----------

_https://opendatalab.com/ADE20K\_2016_

**CityScapes**
--------------

_https://opendatalab.com/CityScapes_

**Foggy Driving**
-----------------

_https://people.ee.ethz.ch/~csakarid/SFSU\_synthetic/_
------------------------------------------------------

  

**SA-1B**
---------

_https://opendatalab.com/SA-1B_
-------------------------------

  

  

\-END-

更多公开数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言