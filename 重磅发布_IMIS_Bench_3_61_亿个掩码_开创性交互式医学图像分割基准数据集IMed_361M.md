     重磅发布！IMIS-Bench：3.61 亿个掩码！开创性交互式医学图像分割基准数据集IMed-361M \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

重磅发布！IMIS-Bench：3.61 亿个掩码！开创性交互式医学图像分割基准数据集IMed-361M
====================================================

原创 GMAI OpenDataLab 2024-12-06 18:37 上海

> 原文地址: [https://mp.weixin.qq.com/s/Iqwt02K2f\_KrKeA90Fe4Zg](https://mp.weixin.qq.com/s/Iqwt02K2f_KrKeA90Fe4Zg)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVSCdGKP5Y0yK1sCvrKdbx3zVQtLvbUwz2sbb2k76RdN7Gm6OWB2pKIw/640?wx_fmt=png&from=appmsg)

**交互式医学图像分割 (****IMIS）**通过结合用户交互输入（如点击、边界框或文本提示），将人工智能的高效计算与临床专家的专业经验紧密融合，能够实时生成符合临床需求的高质量分割结果。然而，该领域长期面临数据规模和质量的双重瓶颈，缺乏类似自然图像领域 SA-1B 数据集那样大规模、高密度、标注精确的数据集。这限制了交互式医学图像分割技术的研究深度和实际应用广度。因此，构建大规模、高密度的交互式医学图像分割数据集，不仅是突破当前技术瓶颈的重要环节，更是推动人工智能深度融入医疗实践、赋能临床决策的关键基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVhiaoDwJG4N40x7rAsDC9pqJTvcAducy3CyEzo9f4bAdFPz7q0PO5eGg/640?wx_fmt=png&from=appmsg)

图1. IMed-361M示例图像

  

为突破交互式医学图像分割技术瓶颈，推动人工智能深度融入医疗实践，**上海人工智能实验室** **GMAI 团队**重磅推出 **IMIS-Bench**，一个交互式医学图像分割基准框架，涵盖大规模数据集IMed-361M和IMIS基线模型。

**发布主页：**_https://uni-medical.github.io/IMIS-Benchmark/_

**相关论文：**_https://arxiv.org/pdf/2411.12814_

**代码仓库：**_https://github.com/uni-medical/IMIS-Bench_

**数据地址：**_https://opendatalab.com/GMAI/IMed-361M_

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

****IMIS-Bench三大亮点****

01

**前所未有的数据规模与掩码数量**

**IMed-361M 数据集**是迄今为止规模最大、标注最密集的交互式医学图像分割数据集。通过整合来自多个医学数据平台的**640万张图像**和**3.61亿个掩码**，覆盖**14种成像模态**几乎所有解剖目标和病灶，该数据集为深度学习模型的训练和评估提供了前所未有的支持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVDDxibcxbPicQHMo4duN7qD8Ds4IbpTKqGQslkN0CKPhJkHJCAru4xhdQ/640?wx_fmt=png&from=appmsg)

图2. IMed-361M数据集基本信息

  

02

**全面的 IMIS 基线模型**

IMIS-Net基线支持多种交互输入（如点击、边界框和文本提示），能够模拟连续交互场景，对分割结果进行动态优化。无论在简单场景还是复杂场景中，IMIS-Net都展现出卓越的性能，为医学图像分割任务提供了更高的灵活性和精度，推动了交互式分割技术的新发展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaV9pBqDZhlVia3DpVGKQUdXvoOwyRicYh8BHhbcSRFxZnqJnUYa8AU9jgw/640?wx_fmt=png&from=appmsg)

图3. IMIS-Net的训练过程模拟了K个连续的交互式分割步骤

###   

03

**广泛的性能评估与交互策略研究**

### IMIS-Bench 提供了一个统一的基准框架，对 IMIS-Net 和现有交互式分割方法进行了全面、系统的性能评估。实验表明，IMIS-Net 在多种模态和任务场景下显著超越现有技术。同时，团队还对多种交互策略对分割性能的影响进行了深入研究，为模型的优化和交互设计提供了宝贵的指导。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**迄今为止规模最大，掩码最丰富的交互式医学图像数据集**

  

01

****数据收集与预处理****

团队整合了来自全球多个医疗数据平台（如 TCIA1、OpenNeuro2、NITRC3、Grand Challenge4、Synapse5、CodaLab6 和 GitHub7）多个公开可用的医学图像分割数据集，涵盖 2D 和 3D 图像以及各种格式（例如 .jpg、.npy、.nii）。根据SA-Med2D-20M协议对所有收集到的医学图像进行标准化，然后应用以下排除标准：

(1) 排除长宽比大于 1.5 的 3D 切片图像及其相应的掩模；

(2) 排除前景区域占总像素数不到千分之一的蒙版，以保留高质量数据和掩码。然后，手动检查并更正数据集中的错误对齐和信息错误。最后，对于具有多个连通分量的注释，我们根据临床需求对其进行区分和标记，以避免单点交互可能引起的误解。

  

02

****交互式掩码****

利用SAM对物体感知能力为每幅图像生成尽可能多的候选掩码。生成的掩码经过阈值过滤、非最大值抑制和去除背景掩模等策略优化，提高掩码的准确性。此外，针对生成的掩模未能充分分离具有模糊边界的结构问题，结合原始ground truth，通过替换和迭代单连通区域等手段进一步校正掩码，并应用形态学操作去除噪音和填补小孔。最终获得了2.73亿个“交互式掩模”，可用于训练交互式分割模型，覆盖几乎所有可识别的医学图像中的对象。

  

03

******统计与分析******

**IMed-361M数据集**是迄今为止最大、公开可用的多模态交互式医学图像分割数据集，包含640万张图像、8760万个ground truth和2.734亿个交互式掩码，平均每张图像56个掩码。该数据集覆盖14种成像模态和204个分割目标，包括各主要器官及病变，涉及人体几乎所有部位。图像分辨率主要集中在256×256到1024×1024之间，确保研究场景的广泛适应性，大多数掩模占用的图像面积不足2%，反映了医学分割的细粒度特性。手动去除不相关的标注并应用过滤策略，仅保留有效掩模，从而增强模型在不同场景中的适应能力。

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbthUne2wt37WKgcibL0OAa1OicRrJsHWVy560pS3dYhwK54eCNU1cc7cYQ/640?wx_fmt=png)

**实验结果**

  

01

****与其他交互式分割模型单次交互的性能对比****

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVVzdqPtFgQWkia7AA1y7IgDlf7W5S0DhWUyuTgtNXanLxBJCURX0eTicw/640?wx_fmt=png&from=appmsg)

图4. IMIS-Net与其他交互式分割模型单次交互的性能比较

  

02

******交互策略对模型的影响******

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVFUMzGpCsias2rNVJiaXKpvfzRbrYRMWuaibJxV4pRov4uRPEopvWFqEuA/640?wx_fmt=png&from=appmsg)

图5. 不同交互策略对交互式分割模型的性能影响

  

03

****Zero-shot性能****

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVxsxp190K8GcMylcNwEeFnkTicUoanQezYo7ISNPeNzksdn0yuyJ7yiaQ/640?wx_fmt=png&from=appmsg)

图6. 在三个外部数据集上的Zero-shot性能

  

04

******数据规模对IMIS-Net的影响******

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVtCuOibswnnTH7FJzSlScibesk2oDXG20JtWeM7a8ouy4iccVKFsQibuZ8w/640?wx_fmt=png&from=appmsg)

图7. 数据规模对IMIS-Net的影响

  

05

******可视化结果******

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAXYau1QsBVGaiavYgkSQHHiaVicdm1xCgxKFichukO3csZGJz443tfC6y80qNDALhJsSWfZ412cAEmEiag/640?wx_fmt=png&from=appmsg)

图8. 定性分析结果

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtj26pXrkrg01CLfjkbowLYStD7QnicVgczEmwwnNS5tq2HKpyAPDJibmA/640?wx_fmt=png)

****总结****

  

本研究提出了 IMed-361M，一个专注于交互式医学图像分割的基准数据集。该数据集包含了各种模态的大量医学图像、广泛的分割场景以及密集的掩码，超越了现有仅限于单一任务或简单集成的数据集。利用该数据资源，团队开发了通用的交互式医学图像分割基线模型IMIS-Net，使用户能够通过交互方式（包括点击、边界框、文本提示及其组合）生成符合临床需求的分割结果。与现有基础模型的对比实验结果表明，IMIS-Net在性能上具有显著优势，并在未见过的场景中展现出较强的可迁移性。值得注意的是，IMIS-Net通常需要更少的交互即可达到相当的性能，提高了其在实际应用中的实用性。

  

IMed-361M 数据集将极大地促进医学影像领域基础模型的发展，并为不同模型之间的公平评估奠定基础。IMIS-Net 提供了通用的技术支持，可应用于多种临床场景，加速人工智能技术在医疗领域的广泛应用。但这项工作仍面临一些挑战。例如，如何更有效地获取交互式掩码的语义信息，以及将这一方法扩展到更全面和更精细的医学图像分析场景，仍是未来需要进一步探索和改进的方向。

  

欢迎医院、研究院、高校、公司等机构的合作，请邮件联系_hejunjun@pjlab.org.cn_

如果您使用代码、模型或数据，请引用GMAI的论文：
-------------------------

    @article{cheng2024interactivemedicalimagesegmentation,

  

**更多精彩数据内容，尽在OpenDataLab**

_https://opendatalab.org.cn/_

  

  

  

  

  

  

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言