## 图片像素操作
对图像进行相加、相减、与、或、异或、非

#### 算术运算
```python
    cv.add(img1, img2)          # 可以提高亮度
    cv.subtract(img1, img2)     # 可以降低亮度
    cv.multiply(img1, img2)     # 可以增加对比度
    cv.divide(img1, img2)       # 很少用
```


#### 位操作
主要针对二值化后的图像操作
```python
    cv.bitwise_and(img1,img2,dst)   # 逻辑与，求交集
    cv.bitwise_or(img1,img2,dst)    # 逻辑或，求并集
    cv.bitwise_not(img1,dst)        # 逻辑非，求补集
    cv.bitwise_xor(img1,img2,dst)   # 异或，相同为0，相异为1
```