     城市级别神经渲染数据集 MatrixCity | ICCV2023 精选 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

城市级别神经渲染数据集 MatrixCity | ICCV2023 精选
====================================

原创 OpenDataLab 2024-01-08 17:37 上海

> 原文地址: [https://mp.weixin.qq.com/s/y-gxDFilghUA9qOUP\_NwVw](https://mp.weixin.qq.com/s/y-gxDFilghUA9qOUP_NwVw)

![](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**推荐语**

  

如何更加高效、可控地实现城市场景逼真建模与自动化生成？本期将给大家介绍一篇来自 ICCV 2023 的论文，由上海人工智能实验室、香港中文大学组成的研究团队，分享最新的大规模城市场景合成数据集、数据处理系列工具。数据已上架OpenDataLab，欢迎大家下载、探索~

> 作者:李奕萱 

  

来介绍一下我们 ICCV 2023的论文《**MatrixCity: A Large-scale City Dataset for City-scale Neural Rendering and Beyond**》。

这篇论文提出了一个高质量、大规模、环境可控且属性丰富的城市场景合成数据集 MatrixCity；并开源了相应的插件， 这个插件可以自动收集大规模、高质量的城市数据， 控制光照、人流、车流、雾等， 获得真实的深度图、法线图以及BRDF分解属性。

项目主页：

_https://city-super.github.io/matrixcity_

  

论文链接：

_https://arxiv.org/pdf/2309.16553.pdf_

  

数据集链接：

● Hugging face: 

_https://huggingface.co/datasets/BoDai/MatrixCity/tree/main_

  

● OpenXLab: 

_https://openxlab.org.cn/datasets/bdaibdai/MatrixCity_

  

● 百度网盘 (password: hqnn) ：

_https://pan.baidu.com/share/init?surl=87P0e5p1hz9t5mgdJXjL1g_ 

**插件链接：**

_https://github.com/city-super/MatrixCity_

  

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbtD7sKr3BO3LpS0ia8WEXrOVe78ZFTDcgficEjpAiby2EKK0SaLywnxDxag/640?wx_fmt=png)

**简介**

近年来异常火爆的NeRF在新视角合成领域已经取得令人惊艳的效果，但大多仅被应用于单个物体或小规模场景。为了加速神经辐射场应用于大规模城市场景的进程，我们开发了一个数据采集插件可实现轨迹的自动化生成和多种真值属性提取，同时基于虚幻引擎 5 的 City Sample 场景建立了一个高质量、大规模、环境可控且属性丰富的城市级神经渲染数据集 MatrixCity，以供研究人员进行城市场景神经渲染的探究。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6gdib2zsMGCicqFpX0Mrpmr5T8XCDkg7SzTlHI46CCXDyMdUGuJbibfupWx6g0zpPKTcbkcAEKyY2yw/640?wx_fmt=jpeg&from=appmsg)

  

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD7ViaLWVRvic3vEhu3bG6ssbt5lhhqGWrC8Qibaa12icjL4ibuEWWicV2fhEHTEDaHAkT4ZNibtraVBMI4rw/640?wx_fmt=png)

**详细介绍**

首先介绍我们为收集数据所开发的插件以及数据采集的方式：

针对高空数据，首先我们将场景根据高度进行分块处理，每个块预设好拍摄的高度和拍摄区域，利用插件进行相机轨迹的自动化生成，每个采集位置放置四个倾斜角(pitch)相同，偏航角(yaw)差90度的相机。针对街景数据，我们首先标注道路两端的位置，利用插件进行相机轨迹的自动化生成，每个采集位置放置六个相机来模拟立方体贴图的全景图片，最后再使用虚幻引擎的movie render queue功能进行图像渲染。

除了可以自动化生成飞行轨迹外，我们的插件还有控制环境变量、提取额外真值属性等功能，方便大家更好的使用。

**总结一下，我们的插件可实现：**

● 大规模场景的轨迹自动化生成。

● 得到真实的深度图，法线贴图以及BRDF分解属性。

● 依赖虚幻引擎自身对于光照、人流、车流、雾的模拟，可实现对动态真实城市场景的模拟。

值得一提的是，该插件可适用于UE的任何项目！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6gdib2zsMGCicqFpX0Mrpmr5wic8bED46qrfoeRMiaTn58fXtsZJUh9C95998WKN8FzLSOibFlFibnDrdA/640?wx_fmt=jpeg&from=appmsg)

  

更详细的采集流程见下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6gdib2zsMGCicqFpX0Mrpmr5JZjYAU3t9ZmeJvYia0rxecpZAKlC4NsSxhOskkVvDvotUiaUtopwgjvQ/640?wx_fmt=png&from=appmsg)

收集完数据后，不得不介绍一下我们的matrixcity数据集的特性：

**1\. 高质量**：我们在虚幻引擎5中构建的该数据集。就像数据集示例展示的一样，图像具备逼真的渲染质量、精细的纹理和几何形状、真实的光照和阴影效果，同时提供准确的相机姿态。

**2\. 大规模**：我们从引擎中提供的两个城市地图（Small City和Big City）中收集数据，分别得到了17万和34万张图像。这些图像覆盖的面积相当于真实场景中的 2.7  和 25.3  ，其中包含了各种建筑物、路标、停放的车辆，代表了多样且真实的城市场景。

**3\. 环境可控**：因为合成数据的自由性，我们能够实现对多种环境因素的灵活控制，包括光照、雾、人流、车辆拥挤度等，而这些因素在现实世界中往往是不可解耦和控制的。

**4\. 属性丰富**：我们能够以最小的成本提取额外的信息，如深度图、法线图、BRDF分解属性（如漫反射、镜面反射、粗糙度等）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7yjDpC9UfD6gdib2zsMGCicqFpX0Mrpmr5vzBv9GhqFTWp7DODicmT43YReRDr4JRFbdjaePTaibnicPgOZkicNKLUkw/640?wx_fmt=png&from=appmsg)

因此，matrixcity数据集与其他城市场景数据集的区别也就不言而喻了：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6gdib2zsMGCicqFpX0Mrpmr5icF9wJZWVPrL66Q6mAFodmnq1SxyluWvzxibz2OzKCfUuY2Muq4wkh1Q/640?wx_fmt=jpeg&from=appmsg)

之后我们又挑选了5个较有代表性的方法，在matrixcity数据集上构建了城市场景新视角合成任务的一个较为完整的基准：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7yjDpC9UfD6gdib2zsMGCicqFpX0Mrpmr5xicDg8XF7aeezYIP0CGqqvwyQ1agNQf6bxmTbQ6fPdRAKKl6txSKINg/640?wx_fmt=jpeg&from=appmsg)

所以这个数据集有什么用呢？🤔

**1\. 支持各种重建任务：**

您可以用我们的数据集和插件测试各种情形下的新视角合成或表面重建任务（稀疏重建、光照变化、位姿不准、动态场景 ...）。考虑到真实场景影响因素之多，不妨现在合成场景将您的idea实现吧。

**2\. 支持深度估计、逆渲染等扩展任务：**

考虑到现实场景获取无误差深度图、法线图以及BRDF分解属性的难度，我们通过渲染管线的解耦合，给这些任务提供了数据保障。

**3\. 支持城市场景生成任务**：

针对 AIGC 爆火的当下，我们利用合成场景的优势，实现对复杂城市场景的逼真模拟，为城市场景生成算法提供一个还不错的数据。

如果您觉得还可以，帮我们点一个star吧！谢谢！！！

  

**参考文献：**  

\[1\] Mildenhall B, Srinivasan P P, Tancik M, et al. Nerf: Representing scenes as neural radiance fields for view synthesis\[J\]. Communications of the ACM, 2021, 65(1): 99-106.

\[2\] Sun C, Sun M, Chen H T. Direct voxel grid optimization: Super-fast convergence for radiance fields reconstruction\[C\]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022: 5459-5469.

\[3\] Müller T, Evans A, Schied C, et al. Instant neural graphics primitives with a multiresolution hash encoding\[J\]. ACM Transactions on Graphics (ToG), 2022, 41(4): 1-15.

\[4\] Barron J T, Mildenhall B, Verbin D, et al. Mip-nerf 360: Unbounded anti-aliased neural radiance fields\[C\]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022: 5470-5479.

\[5\] Chen A, Xu Z, Geiger A, et al. Tensorf: Tensorial radiance fields\[C\]//European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022: 333-350.

\[6\] Martin-Brualla R, Radwan N, Sajjadi M S M, et al. Nerf in the wild: Neural radiance fields for unconstrained photo collections\[C\]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021: 7210-7219.

\[7\] Barron J T, Mildenhall B, Tancik M, et al. Mip-nerf: A multiscale representation for anti-aliasing neural radiance fields\[C\]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021: 5855-5864.

  

\-END-

更多公开数据集，欢迎访问OpenDataLab官网查看与下载：

扫码直达↓

![](https://mmbiz.qpic.cn/mmbiz_png/7yjDpC9UfD55Zk4re0xaqLnRdw69ZRllcUQh93cDbibbmfLyB1ia9BJibfLNGVgIVXKAamAYs14k7fqT1slM80h7Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

点击阅读原文或浏览器访问：

**https://opendatalab.org.cn/**

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言