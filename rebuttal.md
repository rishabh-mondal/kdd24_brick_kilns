# Extended Author Response

- [Overall response](#overall-response)
    - [Scatter plot of Brick Kilns in IG Plain](#scatter-plot-of-brick-kilns-in-ig-plain)
    - [Number of Brick Kilns Detected per State](#number-of-brick-kilns-detected-per-state)
    - [Population Within K km of Brick Kilns](#population-within-k-km-of-brick-kilns)
- [Reviewer-1/nbj2](#reviewer-1nbj2)
- [Reviewer-2/7T6L](#reviewer-27t6l)
- [Reviewer-3/A4cD](#reviewer-3a4cd)
- [Reviewer-4/Qbky](#reviewer-4qbky)


## Overall response

### Scatter plot of Brick Kilns in IG Plain

![](images/ig_plain_bk.png)

### Number of Brick Kilns Detected per State

| state            |   # of Brick Kilns |
|:-----------------|-------------------:|
| Uttar Pradesh    |               7510 |
| Haryana          |               2351 |
| Punjab           |               2327 |
| West Bengal      |               2291 |
| Bihar            |               1726 |
| Jharkhand        |                366 |
| uttarakhand      |                233 |
| Madhya Pradesh   |                212 |
| Himachal Pradesh |                151 |
| Total            |              17167 |

### Population within K km of Brick Kilns

|            state |   < 0.8 km |   < 2 km |   < 5 km |   Total Population |
|:-----------------|-----------:|---------:|---------:|-------------------:|
|    Uttar Pradesh |    13.81 M |  63.32 M | 168.83 M |           233.00 M |
|            Bihar |     4.00 M |  19.76 M |  58.08 M |           124.90 M |
|      West Bengal |     4.35 M |  18.54 M |  50.47 M |           102.10 M |
|   Madhya Pradesh |   258.06 K |   1.40 M |   5.84 M |            84.69 M |
|        Jharkhand |   406.06 K |   2.04 M |   8.32 M |            38.94 M |
|           Punjab |     1.95 M |  10.03 M |  25.64 M |            31.04 M |
|          Haryana |     1.12 M |   6.34 M |  19.36 M |            29.63 M |
|      Uttarakhand |   319.41 K |   1.31 M |   3.91 M |            11.64 M |
| Himachal Pradesh |   175.10 K | 680.47 K |   2.11 M |             7.61 M |
|            Total |    26.40 M | 123.42 M | 342.55 M |           663.55 M |

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

| | | |
|:-------------------------:|:-------------------------:|:-------------------------:|
|![](images/negative/11.67,78.09.png)|![](images/negative/30.31,75.05.png)|![](images/negative/19.06,73.03.png)|
|![](images/negative/28.59,77.31.png)|![](images/negative/21.17,81.38.png)|![](images/negative/24.25,78.16.png)|

## Reviewer-4/Qbky
