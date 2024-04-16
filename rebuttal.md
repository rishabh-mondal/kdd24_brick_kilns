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
    - [Compliance with hospitals](#compliance-with-hospitals)
      - [Punjab](#punjab-1)
      - [Haryana](#haryana-1)
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

1. We ran [WRF-CAMx](https://www.camx.com/) simulation over Delhi-NCR region for Nov-Dec 2023 and found the brick kilns contribute 8% of PM2.5 pollution in the region.

1. We estimate PM2.5 emissions from brick kilns to be 1751 to 3502 tons per day.

Following are the detailed statistics and plots for the points mentioned above.

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
Emission factors (g/brick): {"PM2.5": 6.8, "PM10": 9.7, "SO2": 4.6, "NOx": 4.7, "CO": 90.0, "CO2": 520, "BC": 2.8}

#### Assuming 15000 bricks per day per kiln

|                  |   PM2.5 |    PM10 |     SO2 |     NOx |      CO |     CO2 |      BC |   Total |
| :--------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| uttar_pradesh    | 459.612 | 655.623 | 310.914 | 317.673 |  6083.1 | 35146.8 | 189.252 |   43163 |
| haryana          | 143.881 | 205.242 | 97.3314 | 99.4473 | 1904.31 | 11002.7 | 59.2452 | 13512.1 |
| punjab           | 142.412 | 203.147 | 96.3378 | 98.4321 | 1884.87 | 10890.4 | 58.6404 | 13374.2 |
| west_bengal      | 140.209 | 200.004 | 94.8474 | 96.9093 | 1855.71 | 10721.9 | 57.7332 | 13167.3 |
| bihar            | 105.631 |  150.68 | 71.4564 | 73.0098 | 1398.06 | 8077.68 | 43.4952 | 9920.01 |
| jharkhand        | 22.3992 | 31.9518 | 15.1524 | 15.4818 |  296.46 | 1712.88 |  9.2232 | 2103.55 |
| uttarakhand      | 14.2596 | 20.3409 |  9.6462 |  9.8559 |  188.73 | 1090.44 |  5.8716 | 1339.14 |
| madhya_pradesh   | 12.9744 | 18.5076 |  8.7768 |  8.9676 |  171.72 |  992.16 |  5.3424 | 1218.45 |
| himachal_pradesh |  9.2412 | 13.1823 |  6.2514 |  6.3873 |  122.31 |  706.68 |  3.8052 | 867.857 |
| Total            | 1050.62 | 1498.68 | 710.714 | 726.164 | 13905.3 | 80341.6 | 432.608 | 98665.6 |

#### Assuming 30000 bricks per day per kiln

|                  |   PM2.5 |    PM10 |     SO2 |     NOx |      CO |     CO2 |      BC |   Total |
| :--------------- | ------: | ------: | ------: | ------: | ------: | ------: | ------: | ------: |
| uttar_pradesh    | 919.224 | 1311.25 | 621.828 | 635.346 | 12166.2 | 70293.6 | 378.504 | 86325.9 |
| haryana          | 287.762 | 410.485 | 194.663 | 198.895 | 3808.62 | 22005.4 |  118.49 | 27024.3 |
| punjab           | 284.825 | 406.294 | 192.676 | 196.864 | 3769.74 | 21780.7 | 117.281 | 26748.4 |
| west_bengal      | 280.418 | 400.009 | 189.695 | 193.819 | 3711.42 | 21443.8 | 115.466 | 26334.6 |
| bihar            | 211.262 |  301.36 | 142.913 |  146.02 | 2796.12 | 16155.4 | 86.9904 |   19840 |
| jharkhand        | 44.7984 | 63.9036 | 30.3048 | 30.9636 |  592.92 | 3425.76 | 18.4464 |  4207.1 |
| uttarakhand      | 28.5192 | 40.6818 | 19.2924 | 19.7118 |  377.46 | 2180.88 | 11.7432 | 2678.29 |
| madhya_pradesh   | 25.9488 | 37.0152 | 17.5536 | 17.9352 |  343.44 | 1984.32 | 10.6848 |  2436.9 |
| himachal_pradesh | 18.4824 | 26.3646 | 12.5028 | 12.7746 |  244.62 | 1413.36 |  7.6104 | 1735.71 |
| Total            | 2101.24 | 2997.36 | 1421.43 | 1452.33 | 27810.5 |  160683 | 865.217 |  197331 |

### Compliance with rivers

#### Himachal Pradesh

![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/14b46669-a70b-4c56-a105-26ad7a0d15f9)

#### Jharkhand

![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/3a4d1bc4-2cda-4098-94a6-1be9c5ae45b4)

#### Punjab

![](images/punjab_bk_river.png)
<!-- Fix height with original aspect ratio-->
<!-- <img src="images/punjab_bk_river.png" width="100%" height="auto"> -->

#### Haryana

![](images/haryana_bk_river.png)

#### Madhya Pradesh
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/945e5cb5-a684-4725-9e29-9418a0844751)

#### West Bengal
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/8983674e-ec10-4fad-a1ac-f6eaeb50f7e3)

#### Uttar Pradesh
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/707f4360-1d73-4310-8635-4d01540f84bc)

#### Uttarakhand
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/47f755eb-18ef-440a-9172-74d73fe4ad78)




### Compliance with hospitals

#### Himachal Pradesh
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/41ea9697-647e-4a66-a5ac-16c791268d1c)


#### Jharkhand
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/4225b3ad-40e9-4f14-b004-fd897ea60fa2)


#### Punjab

![](images/punjab_bk_hosp.png)

#### Haryana

![](images/haryana_bk_hosp.png)

#### Madhya Pradesh
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/6e2c45a0-2f8b-40f1-a793-2c58af4c1624)


#### West Bengal
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/b561a260-28d5-4831-be36-74c7d68e5979)


#### Uttar Pradesh
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/f0c31488-b300-4ee4-bcea-53a52fb75ecd)



#### Uttarakhand
![image](https://github.com/rishabh-mondal/kdd24_brick_kilns/assets/129105116/aa83d287-a159-48f0-939c-a11f62740542)




## Reviewer-1/nbj2

## Reviewer-2/7T6L

## Reviewer-3/A4cD

> W4: The paper mentions that since power plants and brick kilns usually have chimneys to emit exhaust gas, the algorithm may misdetect this category, so the model is fine-tuned on the power plant dataset, but chemical plants, steel plants, oil refineries, etc., can become one of the confusing data sources, and more dimensions of information can be considered to improve the problem of error detection.

We thank the reviewer for the actionable suggestion. We downloaded 36 images including 13 chemical plants, 13 steel plants, and 10 oil refineries and ran inference on them. We observed that the model did not misclassify any of these images as brick kilns. A few example images are attached here. All images are stored at [`images/negative`](images/negative/).

|                                      |                                      |                                      |
| :----------------------------------: | :----------------------------------: | :----------------------------------: |
| ![](images/negative/11.67,78.09.png) | ![](images/negative/30.31,75.05.png) | ![](images/negative/19.06,73.03.png) |
| ![](images/negative/28.59,77.31.png) | ![](images/negative/21.17,81.38.png) | ![](images/negative/24.25,78.16.png) |

## Reviewer-4/Qbky
