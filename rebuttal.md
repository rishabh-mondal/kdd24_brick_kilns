## Extended Author Response

- [Reviewer-1/nbj2](#reviewer-1nbj2)
- [Reviewer-2/7T6L](#reviewer-27t6l)
- [Reviewer-3/A4cD](#reviewer-3a4cd)
- [Reviewer-4/Qbky](#reviewer-4qbky)
- [New Results](#new-results)
    - [Number of Brick Kilns Detected per State](#number-of-brick-kilns-detected-per-state)
    - [Population Within K km of Brick Kilns](#population-within-k-km-of-brick-kilns)

### Reviewer-1/nbj2

### Reviewer-2/7T6L

### Reviewer-3/A4cD

> W4: The paper mentions that since power plants and brick kilns usually have chimneys to emit exhaust gas, the algorithm may misdetect this category, so the model is fine-tuned on the power plant dataset, but chemical plants, steel plants, oil refineries, etc., can become one of the confusing data sources, and more dimensions of information can be considered to improve the problem of error detection.

We thank the reviewer for the actionable suggestion. We downloaded 36 images including 13 chemical plants, 13 steel plants, and 10 oil refineries and ran inference on them. We observed that the model did not misclassify any of these images as brick kilns. A few example images are attached here. All images are stored at [`images/negative`](images/negative/).

| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|![](images/negative/11.67,78.09.png)|![](images/negative/30.31,75.05.png)|![](images/negative/19.06,73.03.png)|
|![](images/negative/28.59,77.31.png)|![](images/negative/21.17,81.38.png)|![](images/negative/24.25,78.16.png)|

### Reviewer-4/Qbky


### New Results

#### Number of Brick Kilns Detected per State

| state            |   # of Brick Kilns |
|:-----------------|-------------------:|
| Uttar Pradesh    |               5823 |
| Haryana          |               2351 |
| Punjab           |               2327 |
| West Bengal      |               2291 |
| Bihar            |               1726 |
| Jharkhand        |                366 |
| Madhya Pradesh   |                212 |
| Himachal Pradesh |                151 |
| Total            |              15247 |

#### Population within K km of Brick Kilns

|     state |   < 1 km |   < 2 km |   < 5 km |   < 10 km |   Total Population |
|:----------|---------:|---------:|---------:|----------:|-------------------:|
|  Uttar Pradesh |  16.13 M |  48.30 M | 135.26 M |  202.15 M |           233.00 M |
|     Bihar |   6.01 M |  19.76 M |  58.08 M |   85.90 M |           124.90 M |
|    West Bengal |   6.33 M |  18.54 M |  50.47 M |   79.70 M |           102.10 M |
| Madhya Pradesh | 448.60 K |   1.40 M |   5.84 M |   12.32 M |            84.69 M |
| Jharkhand | 585.60 K |   2.04 M |   8.32 M |   19.75 M |            38.94 M |
|    Punjab |   2.99 M |  10.03 M |  25.64 M |   30.50 M |            31.04 M |
|   Haryana |   1.79 M |   6.34 M |  19.36 M |   28.62 M |            29.63 M |
| Himachal Pradesh | 261.14 K | 680.47 K |   2.11 M |    4.16 M |             7.61 M |

#### Compliance with rivers

##### Punjab

![](images/punjab_bk_river.png)
<!-- Fix height with original aspect ratio-->
<!-- <img src="images/punjab_bk_river.png" width="100%" height="auto"> -->

##### Haryana

![](images/haryana_bk_river.png)

#### Compliance with hospitals

##### Punjab

![](images/punjab_bk_hosp.png)

##### Haryana

![](images/haryana_bk_hosp.png)
