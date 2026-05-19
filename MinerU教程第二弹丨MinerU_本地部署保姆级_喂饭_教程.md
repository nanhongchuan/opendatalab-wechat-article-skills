     MinerU教程第二弹丨MinerU 本地部署保姆级“喂饭”教程 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU教程第二弹丨MinerU 本地部署保姆级“喂饭”教程
================================

原创 MinerU OpenDataLab 2025-05-16 17:04 上海

> 原文地址: [https://mp.weixin.qq.com/s/ylVXT0dB\_tcDG6zFPmwo8A](https://mp.weixin.qq.com/s/ylVXT0dB_tcDG6zFPmwo8A)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

新来的小伙伴看这里！👋 是不是刚接触 MinerU 有点懵？安装报错、部署卡住、配置一头雾水……别慌！今天这篇超基础教程，就是你的“救命指南”！从零开始，手把手带你搞定本地部署🌟 快上车！  

🚀**什么是MinerU？**
----------------

MinerU是一款由上海人工智能实验室 OpenDataLab 团队开发的开源 PDF 转 Markdown 工具，可以高质量地提取 PDF 文档内容，生成结构化的 Markdown 格式文本，可用于RAG、LLM语料准备等场景。本指南将帮助您在本地部署并使用 MinerU。

  

各位开发大神，一定要好好仔仔细细地研读一下 MinerU github  readme 。同时也可以浏览项目issue，很多常见问题都可以迎刃而解！

  

**MinerU Readme 地址（中文）：**https://github.com/opendatalab/MinerU/blob/master/README\_zh-CN.md

  

敲黑板！MinerU 仓库中有些目录虽然常被开发者忽视，但它们对于理解项目架构与功能扩展却至关重要。以下是对部分关键文件夹的简要介绍：

    MinerU/

⭐ MinerU **功能特性**
-----------------

MinerU具有以下核心功能：

1\. 文档处理

● 删除页眉、页脚、脚注、页码等元素，确保语义连贯

● 保留原文档的结构，包括标题、段落、列表等

● 提取图像、图片描述、表格、表格标题及脚注

  

2\. 格式转换

● 自动识别并转换文档中的公式为LaTeX格式

● 自动识别并转换文档中的表格为HTML格式

  

3\. 运行环境

● 支持纯 CPU 环境运行

● 支持 GPU 加速，提升处理效率

🔧本地部署**系统要求**
--------------

在开始安装前，请确保您的系统满足以下要求：

### **基础环境**

● Python 3.10～3.13

● Conda（包管理器）

### 

### **GPU****加速要求（可选）**

● NVIDIA显卡（显存≥6GB）

基础环境配置推荐：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAV1Y3nsqIAGKAXqohDzTibPEM2qwBg1zdElJjdQuFbygbO29GicMpibYskhjuq9kxfqE8EjqyjWpcmfQ/640?wx_fmt=png&from=appmsg)

更多详情，请查看：

https://github.com/opendatalab/MinerU/blob/master/README\_zh-CN.md

**接下来是具体的安装步骤：**
----------------

**⚙️ 1.环境配置**
-------------

### **1.1 创建Conda环境**

需指定Python版本>=3.10

    conda create -n mineru 'python=3.12' -y

**1.2 下载模型文件**

首次使用需下载模型文件，提供两种下载方式：

**📥 方法一**：从Hugging Face下载模型（国际用户推荐）

    pip install huggingface_hub

**📥 方法二**：从ModelScope下载模型（国内用户推荐）

    pip install modelscope 

📁 模型默认存储路径示例：

    model_dir: C:\Users\用户名\.cache\modelscope\hub\models\opendatalab\PDF-Extract-Kit-1___0/models

**💡提示**：

下载完成后，系统会自动在用户目录下生成 `magic-pdf.json` 配置文件，你可以在这个配置文件中修改部分配置，实现不同功能的开关，如表格识别、公式识别关闭或开启（默认二者都是开启的，关闭只需将对应的值改 'true' 为 'false' ）。

用户目录位置：

● Windows：`C:\Users\用户名`

● Linux：`/home/用户名`

● macOS：`/Users/用户名`

`   `

> 🧠 补充说明：
> 
> ● 之前用 'pip install -U "magic-pdf\[full\]"' 安装的依赖已经保存在mineru环境里。
> 
> ● 只要没有删除这个环境或修改环境目录，这些内容都会保留。
> 
> ● 每次关掉终端后再次使用，只需运行 'conda activate mineru' 即可。

  

**🚀 2.** **GPU****加速配置**
-------------------------

### **2.1** **CUDA****加速设置**

这里以 Windows（NVIDIA 显卡） 为例。如果您的 NVIDIA 显卡显存 ≥ 6GB，可配置 CUDA 加速。这里我们以 CUDA 12.8 安装为例：  

（还需提前安装 NVIDIA 显卡所匹配的 pytorch 版本，但安装步骤此处不做展开，可根据下方“提示”及第二篇文章自行配置）  

    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

修改用户目录中配置文件 `magic-pdf.json` ：

    {

**💡提示：**

`● Pytorch` 是 MinerU 运行所必须的深度学习模型的依赖库，执行第1节步骤会自动安装适配 CPU 场景的 Pytoch ，如果使用 GPU，还需重新调整 Pytorch 版本以适配对应的 GPU ；Windows 和 Linux 系统对于 `Pytorch` 的安装也存在差异，具体安装细节与说明，请参考本期第二篇文章《零基础入门：MinerU 和 PyTorch、CUDA的关系》。  

  

🧩 3. 功能测试

### **3.1 单文件测试**

执行以下命令自动测试功能：

    cd demo

**💡 提示**: `./` 是指是一个相对路径，它表示当前工作目录（也就是你在终端中运行命令时所在的目录）；执行完上述命令后，检查 output 文件夹，有输出文件说明部署成功。

  

### **3.2 批量PDF转换**

📋 操作步骤：

✅ 步骤 1：获取批量转换脚本

下载名为 `batch_demo.py` 的 Python 文件。你可以将此文件保存在你希望执行转换的任何目录下。

    下载地址：https://github.com/opendatalab/MinerU/blob/master/demo/batch_demo.py

✅ 步骤 2：准备 PDF 文件

在 `batch_demo.py` 文件的目录下新建如下文件夹：

    pdfs  # batch_demo.py 相对于脚本的路径 

✅ 步骤 3：执行批量转换：

打开你的终端或命令提示符，导航到你保存 `batch_demo.py` 文件的目录。例如，如果你的 `batch_demo.py` 文件保存在 `demo` 文件夹中，你可以执行以下命令：

    cd demo

✅ 步骤 4：查看转换结果：

转换后的结果将默认输出到与 `batch_demo.py` 文件同级目录下的一个名为 `output` 的文件夹中。

    output  # 相对于脚本的路径

按照上述步骤，你已经成功本地部署 MinerU 并可以进行 PDF 文档解析了。不过很多小伙伴还有 MinerU 本地 API 服务的需求，比如我们上一篇文章提到的 MinerU Dify插件教程里的场景二，那接下来就来看看怎么配置 MinerU 本地 API。
-----------------------------------------------------------------------------------------------------------------------------------

（点击回顾：[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)）
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  

---

**🔌 4. 搭建本地** **API** **服务**
-----------------------------

### **4.1 Conda 方式安装**

#### **✅ 步骤 1：创建Conda环境**

需指定 Python 版本为3.10

    conda create -n mineru_api 'python=3.10' -y

#### **✅ 步骤 2：安装依赖**

    # 进入api目录

#### **✅ 步骤 3：启动服务**

    # 启动服务

### **4.2 Docker安装方式**

#### **✅ 步骤 1：构建方式**

    docker build -t mineru-api .

#### **✅ 步骤 2：启动命令**

    docker run --rm -it --gpus=all -p 8000:8000 mineru-api

**💡 提示** 上述任意一种方式安装完成后，可以通过如下地址访问（测试）

    http://localhost:8000/docs

**📝 5. 如何彻底卸载通过 Conda 安装的 MinerU（含 magic-pdf\\\[full\]）？**
-----------------------------------------------------------

#### **✅ 步骤 1：退出当前环境（如果你还在\`mineru\` 环境中）**

    conda deactivate

#### **✅ 步骤 2：删除整个 Mineru 虚拟环境**

    conda remove -n mineru --all

确保输出中没有 `mineru` 环境，说明已经卸载彻底。

> 💡提示: 如果你是在 Conda 的 base 默认环境中 安装并运行了 MinerU API（通过 \`pip install -r requirements.txt\` 安装依赖），这意味着：
> 
> ● 所有的依赖都混在 base 环境里；
> 
> \- 没有单独的虚拟环境，卸载时需要精准清理特定依赖。

  

**🗑️ 6. 如何卸载 MinerU** **API****？**
-----------------------------------

### **6.1 卸载你通过 Conda 和 pip 安装的 MinerU** **API** **环境，可以按照以下步骤进行清理：**

#### **✅ 步骤 1：删除 Conda 环境**

你创建的 Conda 环境名为 `mineru_api`，可使用以下命令删除它：

    conda deactivate

这将删除整个 `mineru_api` 环境及其所有依赖。

  

#### **✅ 步骤 2：可选：删除项目目录（如果你克隆了 GitHub 项目）**

如果你通过 `git clone` 下载了 MinerU 项目文件，可以直接删除目录，例如：

    rm -rf path/to/MinerU

例如你是在 `~/projects/MinerU` 目录下：

    rm -rf ~/projects/MinerU

#### **✅ 步骤 3：可选：清理 pip 缓存**

如果你想进一步清理 pip 下载的缓存文件：

    pip cache purge

### **6.2 卸载你通过Docker 构建和运行 MinerU 的 PDF 解析** **API** **镜像，主要包括以下两步：**

#### **✅ 步骤 1：停止并移除容器（如果有残留）**

你用了 `--rm` 参数（`docker run --rm`），这意味着**容器在停止后会自动删除**，所以**无需手动删除容器**，这一步可以跳过。

但你可以用以下命令确认没有运行中的 MinerU 容器：

    docker ps

如果看到 `mineru-api` 仍在运行，可以手动停止：

    docker stop <容器ID或名称>

#### **✅ 步骤 2：删除镜像**

删除名为 `mineru-api` 的镜像：

    docker rmi mineru-api

如遇“镜像正在使用”的提示，可加 `-f` 强制删除：

    docker rmi -f mineru-api

#### **✅ 步骤 3：可选：清理构建缓存**

Docker 会留下很多中间层镜像和缓存文件，如果你想释放空间：

    docker system prune -a

⚠️ **警告**：该命令会删除所有未使用的容器、网络、镜像、构建缓存。慎用！

  

至此，相信你已经掌握了 MinerU 本地部署、API构建、卸载等操作，快去试试吧![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_06.png)。

  

如果上述操作对你来说仍显得复杂，或者始终缺少相应的硬件条件，那强烈推荐!!!你使用官方提供的 MinerU 客户端，无需编写代码、零学习成本，即可快速完成文档免费转换：

https://mineru.net/

  

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/hkUN8E95VAXoJ0W0JezMA8IuicDhTpfxQScyWyBSvWva6gTdoIdJjhuU70DvSFT6u4ft5R4EbsGzfwlTZeuaKhw/640?wx_fmt=gif&from=appmsg)

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END

  

**相关阅读：**

  

  

[MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[2025-05-09](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2DfiaWj7tD6u36J9MUptoIn8mjrdEE46UKxxIePWjHAujAAXkRVZR4rA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550543&idx=1&sn=5d83f1601148cadf2a649a9cecf3c74b&scene=21#wechat_redirect)

[用“万卷·丝路”数据集打造阿拉伯语版DeepSeek（附免费算力与教程）](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[2025-05-07](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAVVE4CUaZgloMDBwxJp0ZKlqtIEr8eYASLlgX0y2BK3sIyyrE5SErdqfyR4wCyo1Sng8m0ibNA46Qw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550505&idx=1&sn=d308cfa0bcd208b3a099620cf6edf25e&scene=21#wechat_redirect)

[MinerU 偷偷放大招！3大新功能上线、模型重磅升级，解析效率超级加倍……](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[2025-04-14](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUBlUJUFkG3acE1KjtVb7X1jUoqEZqSTu6b1NHzoPYiaicQjBaQ6NCG78GYurSgtzE1ITE3Q4WCux1Q/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550445&idx=1&sn=d437ea556b627de70719149b66a5f78a&scene=21#wechat_redirect)

[【MinerU × LazyLLM】PDF无损拆包，让RAG更懂你的文章！附PDF解析组件选型与RAG案例分享](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550423&idx=1&sn=aae4f098fd607829e3df9fef37814fe8&scene=21#wechat_redirect)

[2025-04-08](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550423&idx=1&sn=aae4f098fd607829e3df9fef37814fe8&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUk7Csn0E5A7R5kcqCt7p1btpsj2Oqmus7IGicuxnkZSWEddwcDeMrFO8eicLszAj8RqIBF1icL29Sqg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550423&idx=1&sn=aae4f098fd607829e3df9fef37814fe8&scene=21#wechat_redirect)

[多语言语料库万卷·丝路2.0开源，数据模态全面升级，搭建文化交流互鉴AI桥梁](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550189&idx=1&sn=cf85998f0df64b5454504cf22589caca&scene=21#wechat_redirect)

[2025-03-22](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550189&idx=1&sn=cf85998f0df64b5454504cf22589caca&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAWpiaQyypfXugnluAuNdTb2xbwXGXEm21O9eEukHmxlcaXsroDrQJFBNCGGGVCAVxssO82WpqDFBhA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzkxMDc0MDU5Mg==&mid=2247550189&idx=1&sn=cf85998f0df64b5454504cf22589caca&scene=21#wechat_redirect)

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言