# Extended Author Response

- [Extended Author Response](#extended-author-response)
  - [Overall response](#overall-response)
    - [Scatter plot of Brick Kilns in IG Plain](#scatter-plot-of-brick-kilns-in-ig-plain)
      - [Fixed Chimney Bull's Trench Kilns (FCBK)](#fixed-chimney-bulls-trench-kilns-fcbk)
      - [Zigzag Kilns](#zigzag-kilns)
    - [Number of Brick Kilns Detected per State](#number-of-brick-kilns-detected-per-state)
    - [Population within K km of Brick Kilns](#population-within-k-km-of-brick-kilns)
    - [Contribution of brick kilns to PM2.5 pollution in Delhi-NCR](#contribution-of-brick-kilns-to-pm25-pollution-in-delhi-ncr)
    - [Estimation of emissions:](#estimation-of-emissions)
      - [Assuming 15000 bricks per day per kiln](#assuming-15000-bricks-per-day-per-kiln)
      - [Assuming 30000 bricks per day per kiln](#assuming-30000-bricks-per-day-per-kiln)
    - [Compliance with rivers](#compliance-with-rivers)
      - [Punjab](#punjab)
      - [Haryana](#haryana)
      - [Uttar Pradesh](#uttar-pradesh)
      - [Bihar](#bihar)
      - [West Bengal](#west-bengal)
      - [Jharkhand](#jharkhand)
      - [Madhya Pradesh](#madhya-pradesh)
      - [Himachal Pradesh](#himachal-pradesh)
      - [Uttarakhand](#uttarakhand)
    - [Compliance with hospitals](#compliance-with-hospitals)
      - [Punjab](#punjab-1)
      - [Haryana](#haryana-1)
      - [Uttar Pradesh](#uttar-pradesh-1)
      - [Bihar](#bihar-1)
      - [West Bengal](#west-bengal-1)
      - [Jharkhand](#jharkhand-1)
      - [Madhya Pradesh](#madhya-pradesh-1)
      - [Himachal Pradesh](#himachal-pradesh-1)
      - [Uttarakhand](#uttarakhand-1)
  - [Reviewer-1/nbj2](#reviewer-1nbj2)
  - [Reviewer-2/7T6L](#reviewer-27t6l)
  - [Reviewer-3/A4cD](#reviewer-3a4cd)
  - [Reviewer-4/Qbky](#reviewer-4qbky)


## Overall response

We thank the reviewers for their constructive and actionable feedback. We want to re-emphasize that our aim in this paper is towards deployability and not novelty. Specifically, we want to target *Data and Benchmarking for Data Science Application Domains (including curation validation and release of large-scale data, experiments, performance benchmarking)* area mentioned in [KDD ADS Scope](https://kdd2024.kdd.org/applied-data-science-ads-track-call-for-papers/).

Brick kilns not only contribute significantly to air pollution [[1](https://link.springer.com/article/10.1007/s11869-012-0187-2)] but as per [[2](https://www.sciencedirect.com/science/article/abs/pii/S1352231014006888)] also employ a large number of labors including children.

We believe that our work and the associated curated datasets, benchmarks, and most importantly compliance studies will further the research in this area.

Based on the reviewers comments, and ongoing deployments, we are happy to share some (revised) statistics and points with the reviewers.

1. Our study encompasses regions in India where 47% of the population resides.

1. We have detected and hand-verified **17167 brick kilns from 9 states** in the Indo-Gangetic plain. We plan to release their exact locations to accelerate research in this direction.

1. We have been extensively working with air quality experts and discussing with pollution control boards who are highly appreciative and plan to incorporate our technologies in their work.

1. We have expanded our compliance study, which is the most important aspect as per various stakeholders, as it leads to specific interventions. We discuss those now. As per pollution control board, the compliance issues are as follows:
    * No two brick kilns should be within 1 km of each other: In our study we found that **50% of the brick kilns are within 1 km of other kiln/kilns**.
    * Brick kilns should be at least 800 m from human habitation. As per our findings, 4% of the population lives within 800 m from brick kilns.
    * Brick kilns should be at least 500 m from rivers. As per our findings, 9% of the brick kilns are within 500 m of rivers.
    * Brick kilns should be at least 800 m from hospitals. As per our findings, 16% of the brick kilns are within 800 m of hospitals.
    * 1.5% of brick kilns violate both the 800 m rule from hospitals and 500 m rule from rivers.

1. Our work is fully reproducible and we have released the [code](https://github.com/rishabh-mondal/kdd24_brick_kilns).

1. We have further segregated the brick kilns based on two types of kilns: Zigzag and FCBK (Fixed Chimney Bull's Trench Kiln). We found that **70% of the brick kilns are Zigzag kilns and rest are FCBK**.

2. We ran a Chemical Transport Model, [WRF-CAMx](https://www.camx.com/) over Delhi-NCR region for Nov-Dec 2023 with help of an air quality expert and found that brick kilns contribute 8% of PM2.5 pollution in the region.

1. We estimate PM2.5 emissions from brick kilns to be 1261 to 2522 tons per day. If all FCBK kilns are converted to Zigzag, this range will reduce to 1050 to 2101 tons per day i.e. a reduction of 16%.

Following are the detailed statistics and plots to support the points mentioned above.

### Scatter plot of Brick Kilns in IG Plain

#### Fixed Chimney Bull's Trench Kilns (FCBK)
![](images/ig_plain_bk_fcbk.png)

#### Zigzag Kilns
![](images/ig_plain_bk_zigzag.png)

### Number of Brick Kilns Detected per State

| state            | # of Brick Kilns |
| :--------------- | ---------------: |
| Uttar Pradesh    |             7510 |
| Haryana          |             2351 |
| Punjab           |             2327 |
| West Bengal      |             2291 |
| Bihar            |             1726 |
| Jharkhand        |              366 |
| uttarakhand      |              233 |
| Madhya Pradesh   |              212 |
| Himachal Pradesh |              151 |
| Total            |            17167 |

### Population within K km of Brick Kilns

| state            | < 0.8 km |   < 2 km |   < 5 km | Total Population |
| :--------------- | -------: | -------: | -------: | ---------------: |
| Uttar Pradesh    |  13.81 M |  63.32 M | 168.83 M |         233.00 M |
| Bihar            |   4.00 M |  19.76 M |  58.08 M |         124.90 M |
| West Bengal      |   4.35 M |  18.54 M |  50.47 M |         102.10 M |
| Madhya Pradesh   | 258.06 K |   1.40 M |   5.84 M |          84.69 M |
| Jharkhand        | 406.06 K |   2.04 M |   8.32 M |          38.94 M |
| Punjab           |   1.95 M |  10.03 M |  25.64 M |          31.04 M |
| Haryana          |   1.12 M |   6.34 M |  19.36 M |          29.63 M |
| Uttarakhand      | 319.41 K |   1.31 M |   3.91 M |          11.64 M |
| Himachal Pradesh | 175.10 K | 680.47 K |   2.11 M |           7.61 M |
| Total            |  26.40 M | 123.42 M | 342.55 M |         663.55 M |

### Contribution of brick kilns to PM2.5 pollution in Delhi-NCR

![](images/kdd24_pm25_brick_kiln_contribution.png)


### Estimation of emissions:
We get the following emission factors (g/brick) from [[Guttikunda et al., 2012](https://link.springer.com/article/10.1007/s11869-012-0187-2)]: {"PM2.5": 6.8, "PM10": 9.7, "SO2": 4.6, "NOx": 4.7, "CO": 90.0, "CO2": 520, "BC": 2.8}

Small scale kilns make less than 15000 bricks per day, while large scale kilns make more than 30000 bricks per day [[Guttikunda et al., 2012](https://link.springer.com/article/10.1007/s11869-012-0187-2)]. So, on an average, we computed emissions for 15000 and 30000 bricks per day per kiln.

#### Assuming 15000 bricks per day per kiln
Emissions in tons per day.


|                  |   PM2.5 |   PM10 |    SO2 |    NOx |      CO |     CO2 |     BC |   Total |
| :--------------- | ------: | -----: | -----: | -----: | ------: | ------: | -----: | ------: |
| bihar            |  114.28 | 163.02 |  77.31 |  78.99 | 1512.54 | 8739.12 |  47.06 | 10732.3 |
| haryana          |  149.47 | 213.22 | 101.11 | 103.31 | 1978.29 | 11430.1 |  61.55 | 14037.1 |
| himachal_pradesh |    9.98 |  14.23 |   6.75 |   6.89 |  132.03 |  762.84 |   4.11 |  936.83 |
| jharkhand        |   35.01 |  49.94 |  23.68 |   24.2 |  463.32 | 2676.96 |  14.41 | 3287.51 |
| madhya_pradesh   |   18.65 |   26.6 |  12.61 |  12.89 |  246.78 | 1425.84 |   7.68 | 1751.04 |
| punjab           |  153.92 | 219.56 | 104.12 | 106.38 | 2037.15 | 11770.2 |  63.38 | 14454.7 |
| uttar_pradesh    |  595.72 | 849.78 | 402.99 | 411.75 | 7884.54 | 45555.1 |  245.3 | 55945.2 |
| uttarakhand      |   17.07 |  24.36 |  11.55 |   11.8 |  225.99 | 1305.72 |   7.03 | 1603.52 |
| west_bengal      |  167.34 | 238.71 |  113.2 | 115.66 | 2214.81 | 12796.7 |  68.91 | 15715.3 |
| Total            | 1261.43 | 1799.4 | 853.32 | 871.87 | 16695.5 | 96462.6 | 519.41 |  118463 |

#### Assuming 30000 bricks per day per kiln
Emissions in tons per day.

|                  |   PM2.5 |    PM10 |     SO2 |     NOx |      CO |     CO2 |      BC |   Total |
| :--------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| bihar            |  228.56 |  326.04 |  154.62 |  157.98 | 3025.08 | 17478.2 |   94.11 | 21464.6 |
| haryana          |  298.94 |  426.43 |  202.23 |  206.62 | 3956.58 | 22860.2 |  123.09 | 28074.1 |
| himachal_pradesh |   19.95 |   28.46 |    13.5 |   13.79 |  264.06 | 1525.68 |    8.22 | 1873.65 |
| jharkhand        |   70.01 |   99.87 |   47.36 |   48.39 |  926.64 | 5353.92 |   28.83 | 6575.03 |
| madhya_pradesh   |   37.29 |   53.19 |   25.23 |   25.77 |  493.56 | 2851.68 |   15.36 | 3502.08 |
| punjab           |  307.84 |  439.12 |  208.24 |  212.77 |  4074.3 | 23540.4 |  126.76 | 28909.4 |
| uttar_pradesh    | 1191.44 | 1699.56 |  805.98 |   823.5 | 15769.1 | 91110.2 |  490.59 |  111890 |
| uttarakhand      |   34.15 |   48.71 |    23.1 |    23.6 |  451.98 | 2611.44 |   14.06 | 3207.05 |
| west_bengal      |  334.68 |  477.41 |   226.4 |  231.32 | 4429.62 | 25593.4 |  137.81 | 31430.6 |
| Total            | 2522.87 |  3598.8 | 1706.65 | 1743.75 | 33390.9 |  192925 | 1038.83 |  236927 |

### Compliance with rivers

#### Punjab

![](images/punjab_bk_river.png)

#### Haryana

![](images/haryana_bk_river.png)

#### Uttar Pradesh

![](images/uttar_pradesh_bk_river.png)


#### Bihar

![](images/bihar_bk_river.png)

#### West Bengal

![](images/west_bengal_bk_river.png)

#### Jharkhand

![](images/jharkhand_bk_river.png)

#### Madhya Pradesh

![](images/madhya_pradesh_bk_river.png)

#### Himachal Pradesh

![](images/himachal_pradesh_bk_river.png)

#### Uttarakhand

![](images/uttarakhand_bk_river.png)


### Compliance with hospitals

#### Punjab

![](images/punjab_bk_hosp.png)

#### Haryana

![](images/haryana_bk_hosp.png)


#### Uttar Pradesh

![](images/uttar_pradesh_bk_hosp.png)

#### Bihar

![](images/bihar_bk_hosp.png)

#### West Bengal

![](images/west_bengal_bk_hosp.png)

#### Jharkhand

![](images/jharkhand_bk_hosp.png)

#### Madhya Pradesh

![](images/madhya_pradesh_bk_hosp.png)

#### Himachal Pradesh

![](images/himachal_pradesh_bk_hosp.png)

#### Uttarakhand

![](images/uttarakhand_bk_hosp.png)


## Reviewer-1/nbj2

> The proposed method is based on pre-trained SimCLR or JigSaw, both are published more than 3 years ago. There are a lot of advanced alternatives such as DINOv2 and iBOT. The justification of not using these advanced pre-trained models is not clear.

We thank the reviewer for the suggestion. Based on the suggestion, we experimented with 4 other SSL methods: 1) Simsiam; 2) DCL; 3) BYOL; and 4) Dino. 


> The technical conclusion is trivial. For example, as indicated in lines 168-172, few shot learning on pre-trained model significantly enhancing the performance is a well-known outcome.




## Reviewer-2/7T6L

## Reviewer-3/A4cD

> W4: The paper mentions that since power plants and brick kilns usually have chimneys to emit exhaust gas, the algorithm may misdetect this category, so the model is fine-tuned on the power plant dataset, but chemical plants, steel plants, oil refineries, etc., can become one of the confusing data sources, and more dimensions of information can be considered to improve the problem of error detection.

We thank the reviewer for the actionable suggestion. We downloaded 36 images including 13 chemical plants, 13 steel plants, and 10 oil refineries and ran inference on them. We observed that the model did not misclassify any of these images as brick kilns. A few example images are attached here. All images are stored at [`images/negative`](images/negative/).

|                                      |                                      |                                      |
| :----------------------------------: | :----------------------------------: | :----------------------------------: |
| ![](images/negative/11.67,78.09.png) | ![](images/negative/30.31,75.05.png) | ![](images/negative/19.06,73.03.png) |
| ![](images/negative/28.59,77.31.png) | ![](images/negative/21.17,81.38.png) | ![](images/negative/24.25,78.16.png) |

## Reviewer-4/Qbky