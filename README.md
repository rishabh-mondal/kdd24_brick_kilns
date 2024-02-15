<div style="width: 20px; height: 20px; overflow: hidden; margin: 0 auto;">
  <img src="logo_image.jpeg" alt="KDD24 Brick Kilns Image" style="max-width: 50%; max-height: 50%; display: block; margin: 25 auto;">
</div>


# kdd24_brick_kilns
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



