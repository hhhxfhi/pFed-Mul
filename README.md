# pFed-Mul: 基于联邦学习的多任务学习框架
## 概述
本项目实现了一个基于联邦学习的多任务学习框架 (pFed-Mul)，特别适用于处理 CelebA 人脸数据集和 DogCat 数据集。框架支持同时训练多个相关任务 (如人脸属性识别和分类)，并通过联邦学习机制保护数据隐私。

## 环境要求
请参照environment.ymal文件中的环境要求

## 数据集准备
本项目一共训练了两个数据集：CelebA和Dogcat。数据集可以在“./data”文件夹下对应的文件中找到下载链接，下载后的数据集文件结构如下：
### ·CelebA
>./data/celeba/
>├── Anno/
>└── image/
### ·Dogcat
>./data/dogcat/
>├── train/
>│   ├── cats/
>│   └── dogs/
>└── test/
>   ├── cats/
>   └── dogs/

## 项目结构
>pFed-Mul/
>├── data/                  # 数据集存放位置
>├── result/                # 实验结果存放位置
>├── model/                 # 模型定义和预处理代码
>│   ├── preprocess.py      # 数据预处理
>│   └── models.py          # 模型架构
>│   └──main.py             # 主训练脚本
>│   └──main_syn.py         # 合成数据训练脚本
>├── txtToCsv.py            # TXT到CSV格式转换脚本
>├── paper_experiments     # 批量实验脚本
>└── environment.ymal       # 依赖文件

## 实验
实验结果均保存在result文件夹中。实验可以直接运行paper_experiment文件夹中的脚本。
