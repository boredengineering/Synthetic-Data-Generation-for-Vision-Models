# Synthetic-Data-Generation-for-Vision-Models
 A collection of methods to generate Synthetic Data for Vison Models.

Nvidia DLI lab on using SDG for training Vision Models is a great introductory material with a lot of potential, therefore this repository is an attempt to enhance the original lab with more material on the subject of SDG.

The learning objective is to evaluate several ways to leverage Synthetic Data Generation for training and finitunning several Vision Models

The files: model.onnx and model.pth too big for Github

## TO-DO

Must develop a stable pipeline to deploy the following resources from NGC:
- Nucleus Server
- Farm Server
- Triton Inference Server

Must implement the examples from Megatron-DeepSpeed such as: ViT and more ....

Must implement the SLURM cluster.

Must implement educational models like Andrej Karpathy minGPT but adapted for vision and several research papers.

Implement examples using other datasets.

Surface Defect Datasets:
- [Metal Surface Defects Dataset](https://www.kaggle.com/datasets/fantacher/neu-metal-surface-defects-data/code)
- [Kolektor Surface-Defect Dataset 2 (KolektorSDD2/KSDD2)](https://www.vicos.si/resources/kolektorsdd2/)
- [NEU Surface Defect Database](https://www.kaggle.com/datasets/kaustubhdikshit/neu-surface-defect-database/code)

## Nvidia Omniverse Replicator
NVIDIA Omniverse Replicator streamlines synthetic data generation (SDG) using 3D assets into a single application.

- [Bootstrapping Object Detection Model Training with 3D Synthetic Data](https://developer.nvidia.com/blog/bootstrapping-object-detection-model-training-with-3d-synthetic-data/)
- [How to Train a Defect Detection Model Using Synthetic Data with NVIDIA Omniverse Replicator](https://developer.nvidia.com/blog/how-to-train-a-defect-detection-model-using-synthetic-data-with-nvidia-omniverse-replicator/)


- [Nvidia Replicator Documentation](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html)
- [Nvidia Replicator Tutorials and Examples](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html#replicator-tutorials)
- [Replicator Api documentation](https://docs.omniverse.nvidia.com/py/replicator/1.6.4/index.html)
- [Synthetic Data Examples](https://github.com/NVIDIA-Omniverse/synthetic-data-examples)

Publications on Synthetic Data

- [How much real data do we actually need: Analyzing object detection performance using synthetic and real data](https://arxiv.org/abs/1907.07061)

## Models
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM/tree/main)
Megatron ([1](https://arxiv.org/pdf/1909.08053.pdf), [2](https://arxiv.org/pdf/2104.04473.pdf), and [3](https://arxiv.org/pdf/2205.05198.pdf)) is a large, powerful transformer developed by the Applied Deep Learning Research team at NVIDIA. This repository is for ongoing research related to training large transformer language models at scale. We developed efficient, model-parallel ([tensor](https://arxiv.org/pdf/1909.08053.pdf), [sequence](https://arxiv.org/pdf/2205.05198.pdf), and [pipeline](https://arxiv.org/pdf/2104.04473.pdf)), and multi-node pre-training of transformer based models such as [GPT](https://arxiv.org/abs/2005.14165), [BERT](https://arxiv.org/pdf/1810.04805.pdf), and [T5](https://arxiv.org/abs/1910.10683) using mixed precision.

- [Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed)
DeepSpeed version of NVIDIA's Megatron-LM that adds additional support for several features such as MoE model training, Curriculum Learning, 3D Parallelism, and others. The examples_deepspeed/ folder includes example scripts about the features supported by DeepSpeed.

- [FasterViT: Fast Vision Transformers with Hierarchical Attention](https://github.com/NVlabs/FasterViT)

## Terraform
Use terraform to easily deploy cloud infrastructure for running the labs.

### Limitations
Terraform depends on the AWS Service APIs and AWS Parallel Cluster is not an AWS Service so the most GPUs we can leverage for a cluster for synchronous parallel computing when deploying instances with Terraform is limited to a single instance.

