     论文解读：高质量三维物体大型数据集OmniObject3D｜CVPR 2023 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

论文解读：高质量三维物体大型数据集OmniObject3D｜CVPR 2023
=======================================

原创 Shanghai AI Lab OpenDataLab 2023-06-28 18:48 上海

> 原文地址: [https://mp.weixin.qq.com/s/6iI9YLtJC7u\_eK\_9jkg0Lw](https://mp.weixin.qq.com/s/6iI9YLtJC7u_eK_9jkg0Lw)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUicOjWA1e3xAfyksNKeJDABTp4MAhD0vW8SVOTgV1gxqHiceI03C2yITQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

人工智能领域最有学术影响力的顶级会议之一CVPR 2023在上周公布了最佳论文等奖项，由上海人工智能实验室（上海AI实验室）、香港中文大学、商汤科技、香港科技大学以及南洋理工大学S-Lab联合提出的高质量三维物体大型数据集OmniObject3D入围本届CVPR最佳论文候选（Award Candidate）。本届CVPR论文投稿总量达9155篇，最佳论文候选为12篇，入选率仅为1.3‰，入围者包括谷歌、上海AI实验室、斯坦福大学、康奈尔大学等在内的世界顶尖企业及机构。

  

上海AI实验室联合团队在题为《OmniObject3D: Large-Vocabulary 3D Object Dataset for Realistic Perception, Reconstruction and Generation》的论文中提出目前学术界最大的真实世界三维扫描模型数据集——OmniObject3D 。该项工作将为未来的三维视觉研究提供广阔空间。

  

**项目主页：**

https://omniobject3d.github.io (点击阅读原文直达链接)

**数据集下载：**

https://opendatalab.com/OpenXD-OmniObject3D-New

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oDpticHyXWJErTTdLy5icYFFYzFpnECj8Uhjzcc1xAxnJXmib0E9UZ1cn981MNFNl9Uy96VBwfEhjGf3JyB2Znv2Q/640?wx_fmt=jpeg)

OmniObject3D覆盖200余个类别约6千个三维物体的数据；同时含有丰富的标注，包括了高精表面网格、点云、多视角渲染图像，和实景采集的视频；此外还通过专业的扫描设备保证了物体数据的精细形状和真实纹理。该数据集将有力促进真实世界中感知、重建和生成领域的发展。利用该数据集，研究人员探讨了点云识别、神经渲染、表面重建、三维生成等多种学术任务的鲁棒性和泛化性，提出了众多有价值的发现，并验证了其从感知、重建、到生成领域的开放应用前景。OmniObject3D及其对应的标准将为学术研究和工业应用带来新的启迪和发展机会。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8Uy80rr3wySXwKysMKIMnZk5BIMNia97pUgjn853fNdUX6ibOOW5ib9wbug/640?wx_fmt=png)

  

**大规模、高质量数据集：解决3D视觉研究及应用痛点**  

面向真实 3D 物体的感知、理解、重建与生成是计算机视觉领域一直倍受关注的问题，也在近年来取得了飞速的进展。然而，由于社区中长期缺乏大规模的实采 3D 物体数据库，大部分技术方法仍依赖于 ShapeNet等仿真数据集。再者，仿真数据与真实数据之间的外观和分布差距巨大，限制了它们在现实生活中的应用。

为了解决这一困难，近年来也有一些优秀的工作如 CO3D 等，从视频/多视角图片中寻求突破点，并利用 SfM 的方式重建 3D 点云。然而这种方式得到的点云往往难以提供完整、干净、精准的 3D 表面和纹理。因此，迫切需要一个大规模且高质量的真实世界 3D 物体扫描数据集，以推进3D视觉研究和下游应用的发展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UPWyXUKyKFCRYxP3YopQrB5hNnyJAf6SGia72W4sTftiaJWUG08f78FTQ/640?wx_fmt=png)

仿真数据与真实扫描数据的对比：仿真数据的纹理和几何往往比较简单且失真

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UDo0J10mNBXRYVvujmorgckZliaMKCwJm77eIianINSBJy7V6fSo7xCHQ/640?wx_fmt=jpeg)多视角图片重建点云与真实扫描数据的对比。重建点云往往含有噪声，且无法恢复精细的表面与纹理，在没有拍摄到的位置存在大面积空洞

  

**涵盖四种模态信息、四大下游任务评估**  

OmniObject3D 为每一个物体提供了四种模态信息，包括：带纹理的高精模型、点云、多视角渲染图像、实景拍摄的环绕视频。同时针对每段拍摄视频平均抽取了 200 帧，并提供前景掩码和 SfM 重建的相机位姿和稀疏点云。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UuicaMpHeJQIbCRBqCgWI9SPWbeKQNl3EZRiaQfA4L5ybYia8xQbP8yfoA/640?wx_fmt=png)模态示例与文件层级

数据集的整体类别内物体数量呈长尾分布，与 ImageNet、COCO、LVIS 和 ShapeNet 等热门 2D 及 3D 数据集中的常见类别高度共享。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UgOdcZC6q32kQ8fSXUPmgC9aSR43FgiafnDYwPZdlWQ0KqQMohoDaPqw/640?wx_fmt=png)每个类别内物体数量分布图

OmniObject3D 为学界带来了广泛的探索空间，在本篇论文中，研究团队通过点云分类鲁棒性、新视角合成、表面重建、3D 物体生成等四个下游任务对OmniObject3D进行了评估与分析。

  

  

**点云分类鲁棒性**

**Point Cloud Classification Robustness**

物体点云分类是 3D 感知中最基本的任务之一。OmniObject3D 可通过解耦 out-of-distribution styles & out-of-distribution corruptions 来实现更全面的点云分类鲁棒性分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8U3uFK3z0JibUHGKDtb43F3GlTibFqsOuFIFlicveETAKKos7siaiaMIibM8kw/640?wx_fmt=png)

OmniObject3D 提供了一个干净的真实世界物体点云数据集，实现了针对 OOD styles & OOD corruptions 的鲁棒性进行细粒度分析

具体来说，OmniObject3D 针对CAD 模型与真实扫描模型之间的差异引入了 OOD styles，以及针对常见点云破坏因子产生了 OOD corruptions。

在之前的研究工作中，含噪的真实物体数据集如 ScanObjectNN 将两种情况耦合，无法实现解耦分析；主动加入破坏因子的仿真数据集如 ModelNet-C则仅仅反映了第二种情况。OmniObject3D 则具备将两种情况解耦分析的要素。

通过对十种最常见的点云分类模型进行测试，可以揭示其与 ModelNet-C 数据集中结论的异同。在应对这两个挑战时，如何实现一个真正鲁棒的点云感知模型仍需深入探索。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UkdQysNcTCNUjCUenYh6CyBpesvlDwibSfbcVVqNnExhW0CMmVsX03cQ/640?wx_fmt=png)

点云分类鲁棒性实验结果

  

  

**新视角合成**

**Novel View Synthesis**

自NeRF提出以来，新视角合成一直是领域内的热门方向。基于OmniObject3D，团队研究了两种赛道下的新视角合成方法：其一是利用密集视角图片输入，对单一场景进行优化训练；其二则是挖掘数据集中不同场景之间的先验，探索类 NeRF 模型的泛化能力。

首先，对于单场景优化的模型，可以观察到，基于体素的方法更擅长建模高频纹理信息，而基于隐式模型的方法则相对更能抵抗表面凹陷或弱纹理等容易产生几何歧义的情况。

数据集中，物体多变而复杂的形状和外观为这项任务提供了一个全新的评估基准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UzrLBMjVwqqt8zHDSaZtI8TOibEUQCmdgw5tfxfdic0fViba7aRPEhe7xA/640?wx_fmt=png)

多个常见方法的单场景优化效果示例

相对于拟合的单个场景的模型，跨场景可泛化框架在本数据集上的表现更令人期待。网络从很多同类别、甚至跨类别的数据中学习到可以泛化的信息，即可针对一个全新场景的稀疏视角输入做出新视角预测。

实验表明，作为一个几何和纹理信息丰富的数据集，OmniObject3D 有助于促使模型学到对新物体甚至新类别的泛化能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UcKxqAJ7tBVBngsibCLxjOJX9eU0vz9iaeF4AicqOthLNlDXTmoJ11Yd2Q/640?wx_fmt=gif)

泛化性模型效果示例

  

  

**表面重建**

**Surface Reconstruction**

除新视角合成外，如果能恢复物体的显式表面，将更加有助于下游应用的开发。同时，OmniObject3D的数据具备精准且完整的三维表面，能够充分支持表面重建精度的评测需要。团队也为表面重建任务设置了两条赛道：稠密视角采样下的表面重建，以及稀疏视角采样下的表面重建。  

稠密视角下表面重建结果展示了数据集内几何形状的显著多样性。精准的扫描使得Chamfer Distance 可以作为重建精度的度量。通过将类别划分为三个“难度”等级，可以观察到所有方法在不同等级上的结果存在明显的差距。

与仅包含 15 个场景的标准 DTU基准相比，OmniObject3D在这项任务上提供了更全面的评估结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UH69OwqDLlrErEibVsnKw6B8Rb77vUN4U5faxCPLHiabKuxJakcDCeVrQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UeicG3dI1reJcQpX24Dsro2biaVPVz6DHUVJpaq3fgBEYY35qEHfapKyg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/oDpticHyXWJErTTdLy5icYFFYzFpnECj8U4icYAEoOEurGS7htK5ZTs3zKNxicISKooR9JlBdy6hk2O9gGdqFsHIng/640?wx_fmt=gif)

  

稠密视角表面重建示例

稀疏视图表面重建是一个更具挑战性的任务，在所有方法的结果中都观察到了明显瑕疵，均未达到能够满足实际应用的水平。

除了专为稀疏视角表面重建设计的方法外，团队还评估了前面提到的泛化性新视角合成模型的几何恢复能力——数据集提供的精准 3D Ground Truth 在评测中再次发挥了优势，然而其表现同样无法令人满意。

综上所述，该问题的探索空间仍然巨大，而 OmniObject3D 为该领域的进一步研究提供了扎实的数据基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UuLUJ2HhcT5Ov3SCBmrXdFy6gxnOla7jWJRkwToicBEYPOAcDJYhVK4w/640?wx_fmt=png)

稠密和稀疏视角表面重建效果示例

  

  

**3D 物体生成**

**3D Object Generation**

除了重建之外，OmniObject3D 还可以用来训练真实 3D 物体的生成模型。团队采用 GET3D框架同时生成形状和纹理，并尝试使用单个模型从数据集中同时学习多种类别的生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8U8EnpOJS4hHZLxjecbhHVwU3XiaPNmVCoxdAiaaj86KXNhneSfRAFPvhQ/640?wx_fmt=png)

带纹理的 3D 物体生成

通过在隐空间插值，可以观察到生成模型跨类别变化的特性。在论文中，团队还着重探讨了由于训练数据不平衡导致的生成语义分布失衡特点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UhAMmSaKOzDpzQsuH4PYbusXNQcmGoyniaqhdBWtLkxvuGWiasWTXviaFQ/640?wx_fmt=png)

形状和纹理低维隐码插值结果

未来，上海AI实验室联合团队将致力于不断扩大和更新OmniObject3D数据集以满足更广泛的研究需求。除了现有的应用，团队还计划进一步发展其他下游任务，如 2D / 3D 物体检测和 6D 姿态估计等。除了感知和重建任务外，OmniObject3D有望在AIGC 时代为推动真实感 3D 生成发挥至关重要的作用。

论文标题：

OmniObject3D: Large-Vocabulary 3D Object Dataset for Realistic Perception, Reconstruction and Generation

  

论文连接：

https://arxiv.org/abs/2301.07525

  

项目主页：

https://omniobject3d.github.io/

  

Github：

https://github.com/omniobject3d/OmniObject3D/tree/main

  

数据集下载：

https://opendatalab.com/OpenXD-OmniObject3D-New

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8UIlfria7x3AIeJkeAMuHmicO69O02or0CuD75JO6LZjgfAsYYxibemRINQ/640?wx_fmt=png)

扫码下载数据集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJErTTdLy5icYFFYzFpnECj8U78TBs1CHM220vlU7oHibKAxv2laDFMdcpRv06ouJQkWReCNt23IXzfw/640?wx_fmt=png)

扫码关注OpenDataLab

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oDpticHyXWJH4UO8ia4A76HlWlE4xXdfVUjQ75AV2KSWpWBNDnOvWkuI2PWW6v7WzBrCcvYPyq27F8SicMPJnLicOA/640?wx_fmt=png)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言