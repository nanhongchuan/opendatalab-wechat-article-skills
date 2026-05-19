     零基础入门：MinerU 和 PyTorch、CUDA的关系 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

零基础入门：MinerU 和 PyTorch、CUDA的关系
==============================

原创 OpenDataLab 2025-05-16 17:04 上海

> 原文地址: [https://mp.weixin.qq.com/s/a2n\_rkQu6cXf-1Xufpss8w](https://mp.weixin.qq.com/s/a2n_rkQu6cXf-1Xufpss8w)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

  

💡一句话总结

MinerU 是一个用 PyTorch 跑模型的程序，PyTorch 支持多种加速方式（如 CUDA、MPS），让它跑得快就需要依赖这些加速工具。

  

PyTorch官网安装教程（可根据系统情况选择不同版本：https://pytorch.org/get-started/locally/  

  

---

一张图看清楚它们的关系：
------------

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUUOH1ib8viafCJ0mFGr96SWpVib4oyrd9U9u83VicEMsgQk1zI0Sj97FX0UO0ENxklHxueDNUWSZz1zw/640?wx_fmt=jpeg)

**01**

  **先解释一些名词在 MinerU 中的作用：**

🔧 PyTorch：是跑深度学习模型的库，有 CPU 和 GPU 版本，简称 torch。MinerU 用它跑公式、OCR、表格等模型，✅ 必须安装。

  

⚙ torchvision：是 PyTorch 的辅助库，用于图像处理、模型加载等。MinerU 在图像类模型或视觉任务中会用到，✅ 建议安装。

  

💻 NVIDIA 显卡驱动（Driver）：是控制和管理 NVIDIA 显卡硬件的软件层，它是 CUDA 与 GPU 正常通信的基础。如果使用 NVIDIA GPU，✅ 必须安装。

  

💾 CUDA-Toolkit：是 NVIDIA 提供的一整套 GPU 编程工具，包含 CUDA、cuDNN、编译器等，能提供开发和运行 GPU 应用的完整支持，避免手动配置底层。若用 pip 安装 PyTorch，❌ 可不单独安装。

  

💿 CUDA：是 NVIDIA 显卡的加速平台，依赖显卡驱动，必须配合 NVIDIA 显卡使用。它能让 PyTorch 用 NVIDIA GPU 跑得更快，使用 NVIDIA GPU 时必须安装，❌ CPU 用户则不需要。

  

📦 Anaconda：是 Python 科学计算平台，集成大量依赖库，便于管理环境。用它安装 PyTorch 等依赖更方便，也可避免系统冲突，❌ 推荐新手或团队开发使用。

  

🔖 MPS：是 Apple macOS M 系列芯片的 Metal 加速接口，Mac 上用来调用 Apple 芯片 GPU，❌ 只在 macOS 上使用。

**🚀小科普：**

**CUDA 主要适用于安装了 NVIDIA 显卡的 Linux 和 Windows 系统；MacOS 用 MPS 加速。**

**02**

  **只想 MinerU 运行（不求快）：**

MinerU 运行依赖 `PyTorch`、`torchvision`，你可以只装 `PyTorch` 与`torchvision` 的CPU 版本

    pip install torch torchvision  # 用 CPU 跑，速度慢，但简单

然后再安装 MinerU，详见：https://github.com/opendatalab/MinerU/blob/master

接下来就可以使用 MinerU 解析 pdf 文件了。

  

**03**

  **想要 MinerU 加速运行：**

要根据你所使用的平台和硬件选择合适的方式：

#### 1\. Windows（装有 NVIDIA 显卡）的加速方式：

注意！需要您的显卡是2017年后生产的带有 Tensor Core 的显存 6 GB以上，可进行以下流程，并测试`CUDA` 推理加速效果：

● 安装 NVIDIA **显卡****驱动**：它们通常包括了支持 `CUDA` 的相关软件包

● 安装 CUDA Toolkit：（需要安装符合 `Pytorch` 要求的 `CUDA` 版本，MinerU 目前支持`Pytorch`的版本为 11.8/12.4/12.6/12.8）

\- CUDA 11.8 下载地址：  

https://developer.nvidia.com/cuda-11-8-0-download-archive

\- CUDA 12.4 下载地址：  

https://developer.nvidia.com/cuda-12-4-0-download-archive

\- CUDA 12.6 下载地址：  

https://developer.nvidia.com/cuda-12-6-0-download-archive

\- CUDA 12.8 下载地址：  
https://developer.nvidia.com/cuda-12-8-0-download-archive

  

● 安装 P`ython` 与 `Anaconda （如果已安装，可以跳过本步骤）`  

● 安装 MinerU，详见：

https://github.com/opendatalab/MinerU/blob/master

  

● 覆盖安装支持 `CUDA` 的 P`yTorch` 和 `torchvision` (请根据`CUDA`版本选择合适的`index-url`，具体可参考torch官网)

    pip install --force-reinstall torch torchvision --index-url https://download.pytorch.org/whl/cu124

● 修改配置文件：将【用户目录】中配置文件 `magic-pdf.json` 中 `device-mode` 的值改为 "cuda"

    {

2\. Ubuntu 22.04 LTS加速方式：  

**● 检测是否已安装 NVIDIA** **显卡****驱动**

    nvidia-smi

**如果看到类似如下的信息，说明已经安装了nvidia驱动，可以跳过下一条安装步骤（⚠️CUDA Version 显示的版本号应 >= 12.4，如显示的版本号小于12.4，请升级驱动）**

    +---------------------------------------------------------------------------------------+

**● 安装 NVIDIA** **显卡****驱动**

**如没有驱动，则通过如下命令安装专有驱动**

    sudo apt-get update

**安装完成后，重启电脑**

    reboot

**● 安装  Anaconda（**如果已安装Anaconda  ，可以跳过本步骤）****

    wget -U NoSuchBrowser/1.0 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2024.06-1-Linux-x86_64.sh

**最后一步输入   yes  ，关闭终端重新打开。**

**● 安装 MinerU**

**● 修改配置文件**

**修改【用户目录】中配置文件 magic-pdf.json 中 device-mode 的值**

    {

**3\. MacOS（M 系列芯片）的加速方式：**

● 安装 `Anaconda`

● 安装 MinerU，详见：

https://github.com/opendatalab/MinerU/blob/master

● 修改配置文件：MacOS 支持 MPS 加速（苹果自家的加速后端），只需要安装 MinerU 后，在 `magic-pdf.json` 配置文件中将 `device-mode` 参数设置为 "`mps"` `来启用 MPS 加速`

    {

**04**

  **🧩总结**

`● PyTorch` 是 MinerU 运行必须安装的核心库

● CUDA、MPS 是 MinerU 的加速方式，因平台和硬件不同而异

● MinerU 间接利用这些加速方式来提速模型运行

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END

  

**相关阅读：**

  

  

[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[2025-05-09](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2DfiaWj7tD6u36J9MUptoIn8mjrdEE46UKxxIePWjHAujAAXkRVZR4rA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[用“万卷·丝路”数据集打造阿拉伯语版DeepSeek（附免费算力与教程）](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[2025-05-07](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVVE4CUaZgloMDBwxJp0ZKlqtIEr8eYASLlgX0y2BK3sIyyrE5SErdqfyR4wCyo1Sng8m0ibNA46Qw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[MinerU大上新！桌面客户端、新版API、国产化适配版全都有，更多功能等你解锁](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549851&idx=1&sn=0c3208dfa19356b9044d2ff7d6fa6b93&scene=21#wechat_redirect)

[2025-01-21](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549851&idx=1&sn=0c3208dfa19356b9044d2ff7d6fa6b93&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUKVun2ZibS4hY5pJBgBL1SwjZwQnCpZGXK3S5NjReNlpg01xwpV4rvW676SChOO9uSwTzzQRWdhGA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549851&idx=1&sn=0c3208dfa19356b9044d2ff7d6fa6b93&scene=21#wechat_redirect)

[多语言语料库“万卷·丝路”发布，AI赋能共建“一带一路”](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[2025-01-09](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAXk2oA4FMPVDMdcDVCU27qrcoZJcm8XvX9zEvQMy5Nico74zGOeIyvq1Doc1Zr5ly2RYm8TavQR3rg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247549665&idx=1&sn=162dc8cb8d7088f405e061f7fd9c079d&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言