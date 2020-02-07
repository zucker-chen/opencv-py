## 轮廓及对象测量

#### 轮廓发现
轮廓发现是基于图像边缘提取的基础寻找对象轮廓的方法，所以边缘提取的阈值选定会影响最终轮廓发现结果。
###### API
```
cv.findContours(image, mode, method, contours, hierarchy, offset)
参数：
    1 要寻找轮廓的图像 只能传入二值图像，不是灰度图像
    2 轮廓的检索模式，有四种：
        cv.RETR_EXTERNAL表示只检测外轮廓
        cv.RETR_LIST检测的轮廓不建立等级关系
        cv.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层
        cv.RETR_TREE建立一个等级树结构的轮廓
    3 轮廓的近似办法
        cv.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
        cv.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
返回值:
    contours:一个列表，每一项都是一个轮廓，不会存储轮廓所有的点，只存储能描述轮廓的点
    hierarchy:一个ndarray, 元素数量和轮廓数量一样， 
        每个轮廓contours[i]对应4个hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，
        分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数
```
```
cv.drawContours(image, contours, contourIdx, color, thickness, lineType, hierarchy, maxLevel, offset)
参数：
    image: 是一张图片，可以是原图或者其他。
    contours: 是轮廓，也可以说是cv.findContours()找出来的点集，一个列表。
    contourIdx: 是对轮廓（第二个参数）的索引，当需要绘制独立轮廓时很有用，若要全部绘制可设为-1。
    color: 是轮廓的颜色和厚度
```

#### 轮回属性获取方法
* cv.contourArea(contour)   # 面积
* cv.moments(contour)       # 中心
* cv.boundingRect(contour)  # 外界矩形
* cv.approxPolyDP()         # 多变拟合，可画出很多几何图形


