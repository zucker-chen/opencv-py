## 图像模板匹配
模板匹配就是在整个图像区域中发现与给定子图像匹配的小块区域

#### API
* matchTemplate 函数：在模板和输入图像之间寻找匹配,获得匹配结果图像 
* minMaxLoc 函数：在给定的矩阵中寻找最大和最小值，并给出它们的位置

#### 几种常见的模板匹配算法：
1. TM_SQDIFF是平方差匹配；TM_SQDIFF_NORMED是标准平方差匹配。利用平方差来进行匹配,最好匹配为0.匹配越差,匹配值越大。
2. TM_CCORR是相关性匹配；TM_CCORR_NORMED是标准相关性匹配。采用模板和图像间的乘法操作,数越大表示匹配程度较高, 0表示最坏的匹配效果。
3. TM_CCOEFF是相关性系数匹配；TM_CCOEFF_NORMED是标准相关性系数匹配。将模版对其均值的相对值与图像对其均值的相关值进行匹配,1表示完美匹配,-1表示糟糕的匹配,0表示没有任何相关性(随机序列)。

#### 多目标匹配
有时候，如果你要匹配的模板，在图形中多次出现，那么就需要多对象匹配。
多对象匹配的原理很简单，因为opencv里的模板匹配，是将图形里的每一处和模板进行对比，所以同一个模板下，多对象匹配情况下，结果矩阵里会有好几个值，和最大（小）值接近，如果我们设置一个阈值，在这个阈值以上（以下）的值都提取出来，再分别得到他们的坐标，理论上只要这个阈值设置的恰当，就可以将多对象都匹配出来。
* `np.where[condition， x, y]`
* `zip(*loc[::-1])`
