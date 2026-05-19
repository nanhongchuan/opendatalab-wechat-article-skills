     MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

MinerU教程第一弹丨Dify插件超详细配置攻略和工作流搭建案例，不允许还有人不会
==========================================

原创 MinerU OpenDataLab 2025-05-09 12:04 上海

> 原文地址: [https://mp.weixin.qq.com/s/fLd6yzM3KttWofXCdgDomA](https://mp.weixin.qq.com/s/fLd6yzM3KttWofXCdgDomA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

近期，MinerU 与 Dify 联合研发的 MinerU 插件在 Dify 市场上架了！大量社区的小伙伴们在社群里询问，应该如何使用 Dify 中 MinerU 插件来搭建工作流。今天，使用教程，它来啦！

  

MinerU Dify 插件主页：

https://marketplace.dify.ai/plugins/langgenius/mineru

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2St1TiaRxYPInakhqPZuRSzeZHhquvIibicOlYWgjT5sRpILauicXMGvjnA/640?wx_fmt=png&from=appmsg)

我们先来看一下大家使用 Dify 和 MinerU 插件的场景，大致可分为如下环境：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2hWodcpCjFW0licTkaibC5sLtnrl2BW8HphTFcKXrpqpJ044iblqZGdqpg/640?wx_fmt=png&from=appmsg)

针对不同的使用场景，一些配置会有些许不同，一定要注意我们的提示哦（都是社区小伙伴们部署时的血泪教训![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_6@2x.png)），接下来就跟着小编一步步地操作，就能在 Dify 中愉快地使用 MinerU 了。

**01**

 **场景一：在 Dify  MinerU 插件中配置 MinerU 官方在线 API 服务**

1\. 登录你的 Dify 平台；

2\. 进入 【工具】 -> 【插件市场】，搜索 `MinerU` 插件并添加。

传送门：`   `

`https://marketplace.dify.ai/plugins/langgenius/mineru`

3\. 配置 `MinerU` 插件参数： 

● 先访问 MinerU 官网申请在线 API，审批通过后方可使用：

https://mineru.net/apiManage

\* 注意关闭代理，否则页面无法访问

  

● 在 Dify 平台逐项填写授权字段：

    # MinerU服务的Base URL

4. 保存配置，就可以在 Dify 应用中成功使用 MinerU 工具来处理 PDF等文件啦！

  

填写示意：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2rcCuGIXf86Ky2UjslvNnNRictUeUuqGChcnVqDw4AhOhyMoCkayViaPw/640?wx_fmt=png&from=appmsg)

**02**

**场景二：在 Dify  MinerU 插件中配置 MinerU 本地服务**

**💡提示：此场景前提是您已在本地部署**了 MinerU，并参照 MinerU GitHub  Repo 中 projects 文件夹中的 web\_api 项目，构建部署了 MinerU 本地 API 服务，然后在 Dify 中进行授权配置。

MinerU web\_api 传送门：

https://github.com/opendatalab/MinerU/tree/master/projects/web\_api

1\. 登录你的 Dify 平台

2\. 进入【工具】 -> 【插件市场】，搜索 `MinerU` 插件并添加

3\. 获取本机 IP 地址

为了让 Dify 正确访问 MinerU API，需要使用局域网 IP 地址（**不****能**使用 `127.0.0.1` 或 `localhost`）。请根据你的系统获取本机 IP：

● Windows：打开命令提示符 cmd，输入下方命令，查找 "IPv4 地址":

    ipconfig

● macOS：打开终端（Terminal），输入下方命令，查找 IP

    #无线网络：

**● Linux**：打开终端，执行：

    ip hostname -I

记录下你的 IP 地址，例如：`192.168.1.100`。

  

4\. 配置 `MinerU` 插件参数：

    # MinerU服务的Base URL

5\. 保存配置，就可以在 Dify 应用中成功使用 MinerU 工具来处理 PDF等文件啦！

  

填写示意：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAX1F8KxicOsUDcFSo8FiaPsHa90pduyWfgPY50Uia8WiajhyFupSE7mFgoicMhrhLe25WvYKP8ibqlRwnVg/640?wx_fmt=png&from=appmsg)

**03**

**使用 Dify 中 MinerU 插件的常见问题**

 **![Image](https://mmbiz.qpic.cn/mmbiz_gif/tA04TpZzA5icXo4TaHlmr9bEQw37s35bmb6FGJKwvUkOaicGibqTEFLQQdDuA1LbiaGQdXYrcsGgArYNvbLhGVPwzg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1) 本地部署的 Dify，在执行过程中遇到如下错误怎么办**

    1Run failed: Failed to transform tool message: PluginInvokeError: {"args":{},"error_type":"Exception","message":"Error extracting page from PDF: Request URL is missing an 'http://' or 'https://' protocol."}

（报错示意）

  

为了解决上述问题，接下来你需要设置 Dify 的配置文件：

  

1\. 找到 Dify 部署目录，打开 `.env` 文件，修改 `FILES_URL` 配置项，依据你的部署方式填写：

● Docker Compose 部署：`FILES_URL` 设置为 ‘`http://api:5001'`

**● 其他部署方式**：`FILES_URL` 设置为 '`http://Dify宿主机IP:5001'`  

（如 `http://192.168.1.100:5001`，这里的 IP 通常是运行 Dify 的机器的 IP，即前文提到的“本地IP”端口。`5001` 是 Dify API 服务的默认端口）。

  

2\. 确认 Dify API 服务的 `5001` 端口已对外暴露（可检查 `docker-compose.yaml` 文件的端口映射）。

  

3\. 保存 `.env` 文件。

  

**4. 重启 Dify 服务**以使配置生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2OJSGM9oU37icOLjsyh0KmrMcBiciabib8ZWibKsJ3fwc1JXibeg8DulbcNVQ/640?wx_fmt=png&from=appmsg)

**💡 提示**:

1\. 如果你使用本机 IP 设置 `FILES_URL` ，那么当你的网络环境发生变化 (例如连接了不同的 WiFi)，你的本机 IP 地址可能会改变。届时需要：

● 重新获取本机 IP 地址；

● 更新 Dify 中 MinerU 插件的 Base URL 配置；

● 如有必要 (如果 Dify 的 `FILES_URL` 配置的是 IP 地址而不是 `api`)，更新 Dify 的 `.env` 文件并重启 Dify 服务。

  

2\. 在使用 Dify 的 MinerU 插件时，尤其是在处理文件上传时，如果不配置此步骤，可能会遇到类似 ‘`Request URL is missing an 'http://' or 'https://' protocol`’的错误。这是常是因为 Dify 的 `API` 服务无法正确访问其自身的文件服务。

**04**

**实践案例：用 MinerU 插件在 Dify 中搭建工作流**

接下来，我们将带你在 Dify 中通过 MinerU 插件快速搭建一个文件问答工作流，帮助你更高效地使用 MinerU 进行文档解析和问答。

  

1\. 环境准备

首先，请根据前文提示完成以下配置：

● 安装并启用 MinerU 插件；

● 在 Dify 设置中，配置好模型供应商及对应的 Token（API 密钥）。

  

2\. 创建空白工作流应用

● 进入 Dify，点击【工作室】按钮，选择“创建空白应用”；

● 类型选择【工作流】；

● 设置应用名称与图标，可选填应用描述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2CUybqxmA8iaNkJoB6c4G51FmeaXZ3LfMViccwx5FIibdDRvBHc4pv31ag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2Hl776An0UicrAhrbGkF0F3ic6jCWNJibcKoC6GB4f7L9sXXBk07Vn0Xlg/640?wx_fmt=png&from=appmsg)

（点击放大查看）

**3\. 在【开始】节点中添加两个输入字段：**

`● uploadfile`：用于上传文件；

● question`：用户提问文本。`

![](https://mmbiz.qpic.cn/mmbiz_png/A8x5yjdSQQqrdKKic3vaCh62siaFibeGnmYibB87G1ibwScC2PU0FDRce9YjM6NCia3tcswCfLArTHKZ8mudYRUmOc8w/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2iczibOmQQmquw89AibNw95Uq3x3HABoKBTITTTMToxJfKKMXhzdnUHJiaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2IibQOhZKrbGsGwQITHicYaJy8dARgo9qjpS4CILf6DVEJCcljXFp0YcA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Stm7gBGmv6BibuxVUyh8hYcxm0KxZqxWvPTJ458sTfEgoNcib5zqibyFaNpcic6cViaibBhFXgEKOGpMAylTBfb3LWMg/640)

4\. 添加 MinerU 插件节点：

● 点击【开始】节点下方的【添加】按钮；

● 选择【工具】类型，添加【MinerU 插件】节点；

● 在插件输入变量中，绑定【开始】节点的 `uploadfile` 字段作为输入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2Y5jesQicA2KWtbxfd72Mzib8eGcoSaYaOw4efvWJHavJwaVwia202RF1A/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia27Yhy92p41icHjDuN4mX5NzmK9qsGPoia7xhNPaSPDFmI4qGb0bA0GicDw/640?wx_fmt=png&from=appmsg)

**5\. 添加 LLM 节点，进行问答处理：**  

● 在【MinerU 插件】节点下方点击【添加】，选择【LLM】节点；

● 设置 LLM 节点的提示词（Prompts）如下：  

\- 上下文字段（Context）：引用【MinerU 插件】节点输出的 `Parse File` 字段；

**\- System 字段提示词**：可填写说明，如：`Parse File 是用户上传文件解析出的内容，用户提到的“文件”“文档”等即指该内容；`

**\- User 字段提示词**：引用【开始】节点中的 `question` 字段作为用户问题输入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2BGdLsRJUNLfdc3696LxARN2j4SeJicvFn2kxria34Lrn3fnmWDZlv83A/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2nDiaGpbf1qaA0a9brM26vytdeCeQMPqiaH4zm8fTshV6OC07p9YKZ3jA/640?wx_fmt=png&from=appmsg)

**6\. 设置【结束】节点输出：**

● 在【结束】节点中，选择【LLM】节点的输出字段 `text` 作为最终输出变量。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2j1LlPFMno0ATPQCyon6bIar4btCeDL3wKz4xLYodnX0AukqsALsEDw/640?wx_fmt=png&from=appmsg)

**7\. 运行并测试工作流：**  

● 点击页面右上角【运行】按钮，测试上传文件与提问功能；

● 测试通过后，点击【发布】下拉菜单中的【运行】按钮，即可在浏览器中打开最终应用页面。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2BIZMMIClnAElg8njSyDS4heNia2GvvYWaAibfcib5Vr0UR0z4quficySMA/640?wx_fmt=png&from=appmsg)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2O31ueK6sduQnnU1MP5FhCtJgbpv1iaBxmfAM7jQSc6mmPLJTaYiavibpQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2Uia0d51ZZTOtaAMkpHQp1PMNbzt0bNxAaEkFqWOTGx7Gbv6bm2X7Fzg/640?wx_fmt=png&from=appmsg)

通过以上教程，相信你已经掌握了 MinerU 插件的基本使用方法。如果在操作过程中还有疑问，欢迎在公众号后台回复关键词 **“MinerU插件”**，即可获取我们为你准备的完整配置文件（YAML）。后续，MinerU 插件也会接入 Dify 的知识库，相关功能，研发小哥正在努力开发中。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2xVlnhVyzqlk5Ye82fVr8b0SOsrYR6Z3GmtYFDunRRkOBERquXT4bqQ/640?wx_fmt=png&from=appmsg)

  

当然，我们更期待你发挥创意，基于 Dify 中的 MinerU 插件打造更多高效实用的工作流！

MinerU Dify 插件 Github Repo 如下，欢迎大家 Star，并疯狂提交 pr ![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_5@2x.png)：  

https://github.com/langgenius/dify-official-plugins/tree/fd9c1f8acb6047a15a1b2cc80bd529171072799b/tools/mineru  

  

如果你在使用 MinerU 插件过程中探索出了更优的工作流方案，欢迎投稿分享给我们！一经采用，我们将赠送 **OpenDataLab 精美周边礼品** 作为感谢。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hkUN8E95VAUrBuruQvhhKnwMIuI10Uia2iczIibo6fYzpVw4zs5vK6hCWPIxlj9wIl98QXAxgQvY4sjib2gFQpoUpw/640?wx_fmt=jpeg)

  

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END

  

**相关阅读：**

  

  

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