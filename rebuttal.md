## Extended Author Response

- [Reviewer-1/nbj2](#reviewer-1nbj2)
- [Reviewer-2/7T6L](#reviewer-27t6l)
- [Reviewer-3/A4cD](#reviewer-3a4cd)
- [Reviewer-4/Qbky](#reviewer-4qbky)
- [Results](#results)
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


### Results

#### Population within K km of Brick Kilns

|     state |   < 1 km |   < 2 km |   < 5 km |   < 10 km |   Total Population |
|:----------|---------:|---------:|---------:|----------:|-------------------:|
|    punjab |   2.99 M |  10.03 M |  25.64 M |   30.50 M |            31.04 M |
|   haryana |   1.79 M |   6.34 M |  19.36 M |   28.62 M |            29.63 M |
| jharkhand | 585.60 K |   2.04 M |   8.32 M |   19.75 M |            38.94 M |
|     bihar |   6.01 M |  19.76 M |  58.08 M |   85.90 M |           124.90 M |
