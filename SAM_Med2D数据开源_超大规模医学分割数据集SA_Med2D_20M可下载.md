     SAM-Med2D数据开源！超大规模医学分割数据集SA-Med2D-20M可下载 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

SAM-Med2D数据开源！超大规模医学分割数据集SA-Med2D-20M可下载
========================================

原创 通用医疗GMAI OpenDataLab 2023-11-29 14:40 上海

> 原文地址: [https://mp.weixin.qq.com/s/3p3EiIHTH6gthnN2Tue-ig](https://mp.weixin.qq.com/s/3p3EiIHTH6gthnN2Tue-ig)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD7GTicGRHLveInsn4DSib6m2dGaYDW6UWz3egJ3uB8JJ4ickib3Uja8VvrwcCs60wFBaHibsc8NiaBlcvEg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247524116&idx=1&sn=51ac0acca9f8e5834ab24ecff0f0c25c&chksm=c10c0df6f67b84e000840d9b0208b6d379a18bece0c193748b6a3fa6be61355666a59e3aa5bb&scene=21#wechat_redirect)

**点击图片→报名寻星计划→****上传原创数据集，领好礼****![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_78@2x.png)**

![](https://mmbiz.qpic.cn/mmbiz_png/ImBWRPFV69t1smBmbKPhmFhgLCwSRAMheY54qz3EibC9AvuicBsVu2tp0KdiaXeMKEYIrEEXMgPsbQGDhm8riaUSLg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

  

  

由于医学图像和自然图像之间存在较大差异，以及缺少大规模医学图像基准数据集，这是导致AI在医学领域进展缓慢的原因之一。构建大规模基准数据集和可靠的基线模型，能够推动AI在医疗领域的快速发展。因此我们开发了通用医疗分割模型 **SAM-Med2D**，并希望能够加速医疗向更通用的方向转变（了解详情：[_SAM-Med2D：打破自然图像与医学图像的领域鸿沟，医疗版 SAM 开源了！_](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247523590&idx=1&sn=ed8a3ef09f1187b29e8f6595c13b72f1&chksm=c10c0fe4f67b86f2f7fc52d6135a7dd96ea875dd78e806650b42c8ee04a8127be0838cad8241&scene=21#wechat_redirect)）。

  

**SA-Med2D-20M是 SAM-Med2D 使用的数据集** ，该数据集由**460万张医学图像和近2000万个对应的掩膜构成，涵盖了10种模态、31个主要器官和219个类别，是迄今为止最大的医学图像分割数据集。**如今，我们在许可范围内开源了SA-Med2D-20M，欢迎大家规范使用数据，并向我们反馈意见。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzkP7WJYKoqFwiaDAodCvTHQ6gV8XwbNW9u1ibHTuop6WupYM8LibcyVJiayZSP6121rKSHUFjMF3Rct4w/640?wx_fmt=jpeg&from=appmsg)

**论文链接：**

_https://arxiv.org/abs/2311.11969_

  

**SAM-Med2D系列工作开源链接（点击“阅读原文”直达）：**

_https://github.com/OpenGVLab/SAM-Med2D_

  

**数据下载链接：**

_https://openxlab.org.cn/datasets/GMAI/SA-Med2D-20M_

  

SA-Med2D-20M数据集中的数据来源于大量公开和私有数据集，涵盖人体器官、组织、细胞、病灶等多种多样的医学图像分割目标和十种不同的医学成像模态，具有显著的多样性。

  

  

  

 01 背景

  

基础模型（Foundation Models）在自然语言、通用视觉等领域的巨大成功离不开海量的训练数据。以Segment Anything Model（SAM）为例，它通过在1100万图像和11亿掩膜（Mask）的数据上成功训练出了分割一切的基础分割模型。

  

尽管目前的基础模型（如SAM）在自然图像分割方面效果显著，但如图1所示，**由于自然图像与医学图像之间存在重大的领域差异（Domain Gap），这些模型通常在多模态的医学数据集上难以取得令人满意的分割结果**。其中，医学图像数据的缺乏直接导致难以针对医学图像任务来训练一个视觉基础模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vx2eozEd9vibZJY360923Fib0prW1qYRoYNRhYAb21PcUicOdKYqU2aibWkA/640?wx_fmt=png&from=appmsg)

图1：自然图像和医学图像的领域差异（Domain Gap）

  

虽然没有单个大规模的医学图像数据集，但是**海量的小而精的公开医学图像数据集**为构建一个大规模医学图像数据集创造了条件。为了推进基础模型在医学图像分析中的发展，来自**上海人工智能实验室通用视觉团队**的研究者们通过收集和整理大量的公开和私人数据集后构建了一个超大规模的医学图像分割数据集: **SA-Med2D-20M**（图2），该数据集**共有460万张医学图像和1970万个相应的掩膜，涵盖了10种模态、31个主要器官和219个类别**，其分割目标覆盖了几乎全身，是一个大规模且具有数据多样性的医学图像分割数据集。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzkP7WJYKoqFwiaDAodCvTHQ69ibtBD8dLzabyPa20iadkPpYSP8vY3SvvqnXnYotLY85u8zsMBqdxeVQ/640?wx_fmt=jpeg&from=appmsg)

图2：SA-Med2D-20M由460万张医学图像和1970万个相应的掩膜组成

  

  

 02 SA-Med2D-20M 数据集概览

‍

2.1 子数据集信息统计

SA-Med2D-20M中的医学图像大部分**来源于公开的医学分割数据**，这些公开的数据集是从TCIA、OpenNeuro、NITRC、Grand Challenge、Synapse、CodaLab、GitHub等公开网络平台上获取的。按照这些数据集的病例（Case）数量和解剖结构情况可以对它们进行统计分析，其分布情况如图3所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxLvrfWtbOx31HqBSiclCBwCEDq0BQb6HBeIibZGNgJXv96J9s1iaicvIoaQ/640?wx_fmt=png&from=appmsg)

图3：所用到的子数据集的分布情况

  

由图3(a)可知，超过120个数据集的图像数量少于10,000或掩膜数量少于100,000。此外，即使是我们收集的最大的数据集，也只包含了不到500,000张图像和6,000,000个掩码。因此，收集和发布这样一个庞大而多样化的医学图像数据集极具挑战性。

  

图3(b)也按照不同解剖结构来统计分析了SA-Med2D-20M数据集中的子数据集的分布情况。其中，包含病灶（Lesion）的数据集在所有类别中所占比例最大，这表明人们对医学图像中的病变或肿瘤自动分割非常感兴趣，因为这对帮助医疗专业人员至关重要。值得注意的是，有17个数据集（Others类别）很难归类到特定的解剖结构，这是由于原始数据集未能提供详细的解剖信息。

  

2.2 模态信息统计

SA-Med2D-20M包括**10种模态**，详见表1，其分布如图4所示。CT和MR模态在图像和掩膜的数量上都占主导地位，这主要归因于它们在公共医学图像分割数据集中的广泛存在。此外，由于CT和MR扫描的是3D维度，研究者在三个轴上分别对其进行切分，这个过程会产生大量切片（Slice），这也会导致大量的图像和掩膜。

  

继CT和MR之后，大多数模态的图像数量处于1,000到10,000之间，掩膜数量则处于1,000到20,000之间。

  

值得注意的是，显微镜和组织病理学图像在该版本SA-Med2D-20M中各包含不到1,000张图像。研究团队计划在未来的数据集更新迭代中更加关注并扩增这些不太常见的模态数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxseFYHM2aFBib7wgiayX62Be3fZ7f1mvnTJlXlWmswiaTGWlLCvYXibMJTA/640?wx_fmt=png&from=appmsg)表1：不同模态的图像和掩膜数量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxwSgEBib0NYYkbCqB4Fkdc4uoQyfEsTzouU73QnErMSy1Cn1832qOF1Q/640?wx_fmt=png&from=appmsg)图4：SA-Med2D-20M的模态分布情况

  

2.3 解剖结构信息统计

根据解剖结构和病变的存在，SA-Med2D-20M数据集被分为不同的类别，包括**头颈部（Head and Neck）**、**胸部（Thorax）**、**腹部（Abdomen）**、**骨盆（Pelvic）**、**病变（Lesion）**和**其他（Others）**，如图5所示。

  

各类别所包含的图像和掩膜数量如图6所示，其中，头颈部（Head and Neck）的图像和掩膜数量最多，因为该解剖结构存在大量多模态的脑部数据集，例如BraTS和ISLES系列。相比之下，其他（Others）类别包含的图像和掩膜最少。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxQDBvzibJEQhT8BMOlicIe7Wv90LrmqB5UUWuOpnpYvHxp225wxOoWQww/640?wx_fmt=png&from=appmsg)图5：SA-Med2D-20M所涵盖的解剖结构及各结构对应的示例图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxrhOiaQaibGYxsLLHFsPFKwrvZvkNnwKTkozLF5hno7eyw8eeVJn87nCg/640?wx_fmt=png&from=appmsg)图6：各解剖结构的图像和掩膜数量

  

2.4 类别信息统计

SA-Med2D-20M**含219个类别标签**，其详细分布如图7所示。总体来说SA-Med2D-20M的类别是长尾分布的。具体而言，47个类别的掩膜在100,000至1,000,000之间，51个类别的掩膜在1,000至10,000之间。最常见的范围是10,000至100,000个，共有88个类别。此外，还有28个类别的掩膜的数量少于1,000个。

  

从具体的类别来看，增强性肿瘤（enhancing tumor）和水肿（edema）这两类的掩膜数量最多。联合（union）类别专门用于解决多个类别之间像素重叠的问题，这些类别的掩膜覆盖两个以上的类别。此外，标签未知（unknown）是指原始数据集未提供特定标签信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxQOru4Q8PqSUYtxahfxWFibcFLtmm4LEDGVCpLiaicYphz1ESd4jhrE0Qw/640?wx_fmt=png&from=appmsg)

图7：各类别的掩膜数量

  

  

 03 SA-Med2D-20M 数据集的构建流程

3.1 数据收集

构建SA-Med2D-20M的第一步是收集用于医学图像分割的数据集。研究团队首先从TCIA、OpenNeuro、NITRC、Grand Challenge、Synapse、CodaLab、GitHub等公开网络平台上收集大量的医学图像数据集。

  

在收集海量数据后，需要对各个类型的数据集进行归档和统一的数据格式处理。具体包括了**图像归一化**、**掩膜的拆分****和合并**等处理，最终通过统一的命名方式将处理好的图像和掩膜存为png格式的图片。

  

3.2 图像归一化

由于医学影像数据集的像素/体素的强度（intensity）差异较大，这会给模型的训练带来不利影响。因此，首先需要将不同模态的医学图像进行归一化。**采用最大最小归一化的方式**:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzkP7WJYKoqFwiaDAodCvTHQ63RFnXuhaMMyQsjn3zMu1XWuGTscGS8s7JknK0AAVRsibkZILp410OXA/640?wx_fmt=jpeg&from=appmsg)

其中，和分别为图像中的最小和最大值。归一化之后的图片将沿着三个轴进行切分，从而得到所有3D图像的切片（Slice）。此外，对于最短边缘小于最长边缘长度一半的切片图像，将对其舍弃，以防止后续对图像进行Resize等数据处理操作时目标区域变得过于模糊。图8展示了整个图像处理的过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxN160yfk8KGdooUnztmrO91icLL3rmepQINibYdcJBMNCayicsPyVveiazA/640?wx_fmt=png&from=appmsg)图8：图像归一化到存储的过程

  

3.3 掩膜的处理

研究者对掩膜的处理主要分为三步，图9显示了处理掩膜的整个流程：

(1) 将原始的语义掩膜拆分为二进制掩膜，这种方式与SAM类似。

(2) 进一步将二进制前景进行分离和合并的处理。分离是为了将具备多个联通域的类别拆分为多个单联通域目标，例如肺可以拆分为左肺和右肺；合并是在一个大的掩膜中合并其包含的其他掩膜，例如在一个肾中包含了病灶区域，通过第一步二进制拆分之后，肾区域将会出现一块中空区域，合并操作就是将这些中空区域进行补全。

(3) 去除不符合标准的掩膜。该步骤将去掉前景占比非常小的掩膜（0.153%）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UBMGKFIQrzktYg7bicEo1aZGnD19285vxJvQibw8BqV6gtsWicFKWT8TkYZfNWllXSX6bib3P9LEQkLjKjg3iaKkiaWA/640?wx_fmt=png&from=appmsg)图9：掩膜的处理流程

  

 04 SA-Med2D-20M 数据集的应用与展望

SA-Med2D-20M为构建医学图像基础模型提供了宝贵的数据资源。具体而言，其超大的数据规模和丰富多样的数据种类可以用于预训练大规模的医疗基础模型，从而应用于广泛的下游任务；

  

另一方面，SA-Med2D-20M根据模态、解剖结构和类别标签等对数据进行了分类汇总，这种分类汇总的组织形式也方便研究人员能够有效地选择与特定任务和应用相关的数据（可以显著减少数据收集所需的时间），并使用这部分数据来针对特定任务从头开始训练一个针对特定任务（Task-Specific）的模型。最后，相信在SA-Med2D-20M发布后，它可以显著缓解数据采集的挑战并加速医学图像分析中的数据迭代过程。

**欢迎所有的合作，包括医院、研究院、高校、公司等。请联系**_hejunjun@pjlab.org.cn_  

  

**论文链接：**

_https://arxiv.org/abs/2311.11969_

**开源链接（点击“阅读原文”直达）：**

_https://github.com/OpenGVLab/SAM-Med2D_

**下载链接：**

_https://openxlab.org.cn/datasets/GMAI/SA-Med2D-20M_

  

\-END-

**寻星计划火热进行中**

**开源数据集领好礼**

**戳下方了解**  

👇

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6OTUAUZZos5lC2WkZxnic2Ht7tZib7huCibtp3EcJgM7VxxaZJhicXqI7meVrGKwnkuK88xQEnMZko3w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=MzkxMjMxMjIwNQ==&mid=2247524116&idx=1&sn=51ac0acca9f8e5834ab24ecff0f0c25c&chksm=c10c0df6f67b84e000840d9b0208b6d379a18bece0c193748b6a3fa6be61355666a59e3aa5bb&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言