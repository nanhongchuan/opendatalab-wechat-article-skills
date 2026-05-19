     上海AI Lab开源首个可替代GPT-4V的多模态大模型 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

上海AI Lab开源首个可替代GPT-4V的多模态大模型
============================

原创 任同学 OpenDataLab 2024-06-04 19:10 上海

> 原文地址: [https://mp.weixin.qq.com/s/LT8DjRYAHOI6y-igoFR\_Pg](https://mp.weixin.qq.com/s/LT8DjRYAHOI6y-igoFR_Pg)

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X27fvSLnBOmMibUoWo1ib5973PS2E9ibkCvAuWYkOt5yjxCuic3ziajd3q2Vw/640?wx_fmt=png)

 夕小瑶科技说 原创  
 作者 | 任同学

> 与开源和闭源模型相比，**InternVL 1.5** 在 OCR、多模态、数学和多轮对话等 18 个基准测试中的 8 个中取得了最先进的结果。

上海AI Lab 推出的 InternVL 1.5 是一款开源的多模态大语言模型 (MLLM)，旨在弥合开源模型和专有商业模型在多模态理解方面的能力差距。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2UgEWaaCOKAaicCBqNib4GlNdY8pY9KTORIWRO3SnrIGU1b8vq2SBsIMA/640?wx_fmt=png)

  
论文称，InternVL 1.5 在四个特定基准测试中超越了 Grok-1.5V、GPT-4V、Claude-3 Opus 和 Gemini Pro 1.5 等领先的闭源模型，特别是在与 OCR 相关的数据集中。

论文用下面一张图非常生动地展示了他们为 **达到 AGI 星球** 所做的努力：

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2wQqbDXBsdWFkia3YxzibIgnt2ncBIapfb5KicmdksPN4OxibOkWXnUcZPQ/640?wx_fmt=png)

  
图中主要涉及 InternVL 的三个改进：（1）强视觉编码器：为大规模视觉基础模型 **InternViT-6B** 探索了一种持续学习策略，提高了其视觉理解能力，并使其可以在不同的LLM中迁移和重用。（2）动态高分辨率：根据输入图像的长宽比和分辨率，将图像划分为1到40个448×448像素的图块，最高支持4K分辨率输入。（3）高质量的双语数据集：收集了高质量的双语数据集，涵盖常见场景、文档图像，并用英文和中文问答对进行注释，显着提高了 OCR 和中文相关任务的性能。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2JSV7UeJUcsvWPYnhxIhHgFGqwxe7qu0Ta3guRsOsaqmib25bwG5RDfg/640?wx_fmt=png)

  
总体的结构则是采用与流行的多模态大模型类似的 ViT-MLP-LLM 架构，通过MLP映射器将预训练好的InternViT-6B与InternLM2-20b结合在一起。同时还使用一个简单的Pixel Shuffle 技巧将视觉标记的数量减少到四分之一。

对于动态高分辨率，研究人员则是从预定义的比例中动态匹配最佳宽高比，将图像划分为448×448像素大小的块，并为全局上下文创建缩略图。该方法最大限度地减少了纵横比失真，并在训练期间适应不同的分辨率。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2f8Bk9QxpnxvIl1zy8Tcf3dPTNeEUQys9McIwVticdsZ6t9HShNo5mQg/640?wx_fmt=png)

▲图4.动态分辨率。

在训练过程中，视觉标记的数量范围为 256 到 3,328。在测试过程中，图块数量最多可以增加到 40 个，从而产生 10,496 个视觉标记，从而实现最高4K分辨率的输入。

论文中也提供了模型在预训练和微调阶段使用的各类任务以及对应的数据集，并且都是公开数据集。为了构建大规模 OCR 数据集，研究人员还利用 PaddleOCR 对 Wukong 数据集的图像执行中文 OCR，对 LAION-COCO 数据集的图像执行英文 OCR。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2Xna3YTR8B9sjLHBkbYAwMs9HtGnK9hDtKyTHVIbaLcuU83OL5FAjMQ/640?wx_fmt=png)

▲图5.(a) 预训练阶段使用的数据集

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2LbQgzmBkCNAyYT3ficHM5b3A70uh3nt2nueGRNrlurbgSerBxV9nV6Q/640?wx_fmt=png)

▲图5.(b) 微调阶段使用的数据集。

而InternVL 1.5 的具体性能表现如何？如下图所示，InternVL 1.5 在大多数基准测试中都表现出领先的性能！

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X22MEcjohAJ2icB8DdoLNtMqXnHFiapcy9opEVicVBuyjnZzqBTJh5J6htw/640?wx_fmt=png)

▲图6.在 16 个多模式基准上与 SoTA 模型进行比较。

与 **TextMonkey、DocOwl-1.5 和 LLaVA-NeXT** 等其他开源模型相比，**InternVL 1.5** 在这些基准测试中显着缩小了与专有模型的差距。

然而，虽然 InternVL 1.5 超越了 **MM1**，并且在 MMMU 上与 **Gemini Pro 1.0** 相当，但它比其前身 **InternVL 1.2** 略有下降。作者也对此进行了分析，并称这可以被认为是适当的降低，且可以归因于语言模型规模较小，这种现象也可以在下图中的 MMT-Bench 结果中观察到。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X21icjDEMDlAMGtMjSXkHjUU2ibDiagarzsvtp7m0Llm5QoyiclKNSExUSXQ/640?wx_fmt=png)

▲图7. 在ConvBench和MMT-Bench上与SoTA模型的比较。

针对InternVL在不同分辨率下的性能，研究人员也进行了实验。论文称，尽管在训练期间仅使用 1 到 12 个图块，但可以在测试期间将零样本任务扩展到 40 个图块（即，4K分辨率）。

但是作者也发现并不是所有任务都需要高分辨率，从图8来看，与 OCR 相关的任务（例如 DocVQA、InfoVQA、TextVQA 和 OCRBench）受益于分辨率的提高，而 AI2D、MMMU、MMBench 和 HallusionBench 等任务在更高分辨率下表现出轻微下降。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2g1w5Dp6iaAUzZ9N4eWNanggGRFKoDcRs6tsFZM8DlOjL07NPSlmOXVg/640?wx_fmt=png)

▲图8.不同图像分辨率下 InternVL 1.5 性能的比较。X 轴代表图块数量，Y 轴代表基准性能。最高值及其相应的图块数量会突出显示。

总体而言，InternVL 1.5 对动态分辨率表现出很强的鲁棒性。它可以根据每项任务的具体要求调整分辨率，确保在高分辨率有利的情况下实现最佳性能，在不利于高分辨率的情况下节省资源。

为了充分践行自己对标 GPT-4V的目标，论文中的 General QA、OCR-related QA、科学理解、中国传统文化、目标定位、多图像对话的示例上均与 GPT-4V进行对比，蓝色字体显示出色的答案，而红色字体显示错误的答案。

为了方便读者阅读，（如果非中文）下面的蓝色（或红色）字体的部分均进行中文翻译。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2vq2XCFL0Bg85MFH4XSu8DNzBQwTI3ltkwf5iaCREguI8nVX0iaOHEmGA/640?wx_fmt=png)

▲General QA 的示例。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2BrNlWCRaWzZWfDpENzVOKTI0sTWX9FicP2uh0kDYiakb58tY7ZmXTlmQ/640?wx_fmt=png)

▲OCR-related QA 示例。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X21aG3iag4aWKmKqyRGEib7gXwntXLfxiaQhicG59nbBaAicmVia2xcpxPktkw/640?wx_fmt=png)

▲科学理解的例子。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2slt4yicQoEiaWHMbOcVyqt3QDgvQibNjeZCNPsicgjtPbrzw9K9obAicegQ/640?wx_fmt=png)

▲中国传统文化的范例。蓝色突出显示了出色的答案

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2UdCibZ7mwkKK83IdEuHvQ55qXyIUouBLbXaDIdcZXc8I6Y3Ku5C9RCA/640?wx_fmt=png)

▲目标定位的示例。

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X279xCoOfiaiayX1AHhHlVleswubxQZqXQxaib9z8DOkIbibupEiaBV5Y7lqw/640?wx_fmt=png)

▲多图像对话示例。

最后，我们也可以在官方demo中进行试玩：

> https://internvl.opengvlab.com

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2yibXcmls1sIVOZcEbrQD8O08X8iacnWtKrA9ZPMn5u6QhhuG7mIJBTibg/640?wx_fmt=png)

不得不说，这个效果真的很惊喜！不过也存在一些问题，比如说当用 InternVL 1.5 的 arxiv 首页询问的时候，它居然杜撰了自己的作者！看来多模态大模型上的幻觉问题也要赶紧着手研究了~

![](https://mmbiz.qpic.cn/mmbiz_png/5fknb41ib9qHYiaN30FiatgNyias27l6t6X2Pz00uoI6FfhnbVJEZibZNyQuCtplEic46ib4Kiat3ONVSgOjUsNoRA0RGg/640?wx_fmt=png)

  

#### 在线试用(点击“阅读原文”直达） https://internvl.opengvlab.com

#### 加入InternVL交流群：添加小助手，发送“internvl”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UBMGKFIQrzlo6vkt9TTV2pMUZjO0Kdn1MAMhuZYBDjL7QGJgauyemSU0FYJReLRAibbGnfiba7TmzROxTXl4IbzQ/640?wx_fmt=jpeg&from=appmsg)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言