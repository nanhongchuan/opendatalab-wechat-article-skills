     从感知推理到AGI4S，OpenDataLab近期入选顶会论文速览 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

从感知推理到AGI4S，OpenDataLab近期入选顶会论文速览
=================================

原创 爱学习的 OpenDataLab 2025-12-26 17:12 上海

> 原文地址: [https://mp.weixin.qq.com/s/x9KlfZnjOXl-HlfjPguDWA](https://mp.weixin.qq.com/s/x9KlfZnjOXl-HlfjPguDWA)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7yjDpC9UfD5Fk0NBJ7dbXDia22rOZUkW96YCA68Gp4IBtguxRGoExUAj8tH5Qd8eibGpnQqjIGQ2P8eHgOibibyS1w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

  

近期，**上海人工智能实验室（上海****AI****实验室）OpenDataLab团队**在多模态感知与理解、大模型推理增强、AGI4S及合成图像检测等前沿领域取得多项进展。团队多篇高质量论文连续入选NeurIPS 2025、KDD 2026等国际顶级学术会议。

上述研究成果涵盖了从基础理论创新到大规模基准构建，再到高效模型部署的全方位探索，反映了团队在Data-Centric AI研究方向的深入实践。

  

### 01｜视觉感知：从“看见”到“洞察”的飞跃

会议：NeurIPS 2025

论文：BLINK-Twice: You see, but do you observe? A Reasoning Benchmark on Visual Perception

大模型真的有视觉常识吗？**BLINK-Twice**基准测试向现有的多模态模型（MLLM）发起了挑战。它专注于那些需要“深度观察”而非简单“识别”的任务，比如视觉错觉、强制透视等。该工作揭示了模型在面对视觉冲突时，往往容易过度依赖语言先验而非图像事实。

*   **看点：** 重新定义了多模态模型的视觉逻辑，是衡量模型“感知深度”的新标尺。
    
*   **链接：**https://arxiv.org/abs/2510.09361
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUErF25RmMkX9p2nREV80Rrtr4ibIRvdAGwyHfI8t0vTnWqicMj4EIa4Or66EdQmJaENCvRD8XicbMicg/640?wx_fmt=png&from=appmsg)

  

* * *

###   

### 02｜多步推理：模拟人类“看图思考”的过程

会议：NeurIPS 2025

论文：Multi-step Visual Reasoning with Visual Tokens Scaling and Verification

处理复杂视觉任务时，人类会反复端详、局部放大。受此启发，团队提出了一个**多步视觉推理框架**。模型可以根据需要动态调整视觉 Token 的分辨率，并通过内部的“验证者”机制，决定是否需要针对细节进行新一轮的推理迭代。

*   **看点：** 赋予了模型“慢思考”的能力，显著增强了对遮挡物体及微小细节的抓取精度。
    
*   **链接：**https://arxiv.org/abs/2506.07235
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUErF25RmMkX9p2nREV80RrRCkTR5fbnMib0mvtmLHkIjk3KdwgTph24eWBfKv21ic9aHDxiaPEvJqBQ/640?wx_fmt=png&from=appmsg)

  

* * *

###   

### 03｜推理增强：代码辅助下的逻辑 Scaling

会议：NeurIPS 2025

论文：Scaling Code-Assisted Cot for Model Reasoning

如何自动化获取高质量、可验证的思维链（CoT）数据？**Caco 框架**提供了一个优雅的解法：利用代码作为逻辑桥梁。它将复杂的逻辑问题转化为可执行的代码，通过自动校验结果来确保推理链条的正确性，并由此合成了 130 万条高质量数据。

*   **看点：** 开辟了无需人工干预即可大规模提升模型逻辑推理能力的新路径。
    
*   **链接：**https://arxiv.org/abs/2510.04081
    
    ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUErF25RmMkX9p2nREV80RrEufuKeQEbLdUXkRkzzZhBtBRk1FWI6Yrxv3LliaZ8rick3unyn5CIXQw/640?wx_fmt=png&from=appmsg)
    
      
    

* * *

  

04｜AGI4S：让语言模型精准“读懂”3D分子

会议：KDD 2026

论文：Tokenizing 3D Molecule Structure with Quantized Spherical Coordinates

在药物研发中，如何让语言模型（LM）处理复杂的 3D 分子结构一直是个难题。团队提出了**Mol-StrucTok方法**，通过量化球面坐标系，巧妙地将连续的 3D 原子坐标“离散化”为 Token。这不仅保证了物理上的 SE(3) 不变性，更让 LM 能够像生成文本一样高效生成 3D 分子。

*   **看点：** 生成速度比传统扩散模型快了近 28 倍，为 AI 辅助药物设计开启了极速模式。
    
*   **链接：**https://arxiv.org/abs/2412.01564
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUErF25RmMkX9p2nREV80RrVhFSwkW4WJ036JcEpiauibUQD1MVWXR7qoibCu77pykpLNAiczusHjkq0g/640?wx_fmt=png&from=appmsg)

  

  

* * *

  

### 05｜效率进阶：鱼与熊掌兼得的“渐进式蒸馏”

会议：NeurIPS 2025

论文：Efficient Multi-modal Large Language Models via Progressive Consistency Distillation

视觉 Token 的冗余一直是多模态模型的“算力杀手”。**EPIC 框架**通过“渐进式一致性蒸馏”技术，在不改动模型结构的前提下，大幅压缩了视觉输入。这种方法让模型在损失极小精度的情况下，实现了部署效率的跨越式提升。

*   **看点：** 优化了 KV Cache 占用，让高性能多模态大模型在终端设备上的部署变得更现实。
    
*   **链接：**https://arxiv.org/abs/2510.00515
    
    ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUErF25RmMkX9p2nREV80Rr3iaYkMMiaXV4v9CfJnavWP9yjGPuibr6icsKibH4Lsp5YqcEAwc6W0C0Njw/640?wx_fmt=png&from=appmsg)
    
      
    

* * *

###   

### 06｜信任边界：识破 AIGC 的“蛛丝马迹”

会议：NeurIPS 2025

论文：Spot the Fake: Large Multimodal Model-Based Synthetic Image Detection with Artifact Explanation

面对真假难辨的生成图像，光说“它是假的”还不够。**FakeVLM** 不仅能精准识别合成图像，还能给出“有理有据”的自然语言解释，指出具体的伪影（Artifacts）位置。与其配套的 **FakeClue** 数据集，更是为该领域提供了宝贵的微观标注资源。

*   **看点：** 将伪造检测带入了“可解释性”时代，是治理 AI 误导性内容的关键技术支持。
    
*   **链接：**https://arxiv.org/abs/2503.14905
    
    ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUErF25RmMkX9p2nREV80RrX4SpeGHXpd1w2qDCFTiaKcgCUpyaJuSm7cuXodTRdsgcKIrTxHosvww/640?wx_fmt=png&from=appmsg)
    
      
    

* * *

###   

### 07｜抑制幻觉：精细化编辑下的特征对齐

会议：NeurIPS 2025

论文：Hallucination at a Glance: Controlled Visual Edits and Fine-Grained Multimodal Learning

为了解决模型在面对微小视觉变化时产生的幻觉，团队构建了包含 5 万对精细修改图文对的**MED 数据集**。通过引入特征级一致性损失，模型被训练得对“像素级语义漂移”更加敏感，从而在推理时变得更加严谨。

*   **看点：** 攻克了多模态领域长期存在的“幻觉”痛点，提升了模型的稳健性。
    
*   **链接：**https://arxiv.org/abs/2506.07227
    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAUErF25RmMkX9p2nREV80RrOicu4cJy6xFJfS4RHCZ0BTYZhcxtqjKPBUpKsw48tQfoBte6tkexv1w/640?wx_fmt=png&from=appmsg)

  

* * *

###   

关于 OpenDataLab

OpenDataLab正持续打造面向 Al-Ready 的下一代大模型数据基础设施，希望通过对数据的持续性深入研究，为业界提供更优质、更有价值的数据工具与解决方案。

想要获取更多研究细节、源码或模型权重，欢迎访问我们的学术主页：

https://opendatalab.github.io/

![图片](https://mmbiz.qpic.cn/mmbiz_png/55LhWNqR1eEIvTRaeSGqOic2WdN4owxXx4UzauQgeevfp7WbH82nic0ict9rBIHza7ZkYRxXupK0a8IIPDyicUpjPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

END  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hkUN8E95VAVbP7SgPzUZSbTKQF7ftQZSqvlNRLUiaulic4TPu7FFhCHvUVqQAkxn7uxtIRC8QegvibdibSrlnkwuxg/0?wx_fmt=png) OpenDataLab

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言