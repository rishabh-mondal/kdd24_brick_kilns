<p align="center">
  <img src="logo_image.jpeg" alt="KDD24 Brick Kilns Image" width="300">
</p>

# Scalable Methods for Brick Kiln Detection from Satellite Imagery
<p align="center">
  <a href="https://arxiv.org/abs/2402.13796">
    <img src="https://img.shields.io/badge/arXiv-2402.13796-green.svg" alt="arXiv">
  </a>
</p>

# Outline
* [Data details](#data-details)
* [Code details](#code-details)
* [Tables and figures](#tables-and-figures)

# Data details
[Download Brick Kilns Data](download_brick_kilns_data.ipynb) | Data download using Google static API

[Live downoading status of brick kilns data](watch_brick_kilns_live.ipynb) | Live downloading status of brick kilns data

[Preprocessing Brick Kilns Data](data_preprocessing.ipynb) | Data preprocessing

# Code details

We have the following code files:

1. [Zero Shot Learing](Experiments.py) | Model trained on Bangladesh train dataset and tested on Bangaldesh test and Indian test dataset.

2. [Table 2 (Sr.1 - Sr.11)](Experiments.py) | Model trained on Bangladesh train and X% of delhi dataset and tested on Bangaldesh test and Indian test dataset w/o Imagenet weights.

3. [Table 2 (Sr.12 - Sr.22)](Experiments.py) | Model trained on Bangladesh train and X% of delhi dataset and tested on Bangaldesh test and Indian test dataset with Imagenet weights.

4. [Table 2, Row 23-28](Experiments.py) Jigsaw SSL

    Key details:
    * Pretraining: Jigsaw SSL
    * Pretraining dataset: Bangladesh+Delhi
    * Downstream training dataset: Bangladesh train + X% Delhi train
    * Evaluation dataset: Indian test

4. (Table 2, Row 29-34) | [Pretext Task](SimCLR_pretext.ipynb)|[Downstream Task](Simclr_downstream.ipynb) SimCLR SSL 

    Key details:
    * Pretraining: SimCLR SSL
    * Pretraining dataset: Bangladesh+Delhi
    * Downstream training dataset: Bangladesh train + X% Delhi train
    * Evaluation dataset: Indian test    


5. (Table 3) | [Prediction](predict.ipynb) | Model trained on Bangladesh train and 50% of delhi dataset and tested on various district of India with Imagenet weights.



