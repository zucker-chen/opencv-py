## 图像梯度/边缘检测
图像梯度可以把图像看成二维离散函数，图像梯度其实就是这个二维离散函数的求导。
注意用于图像边缘检测

#### Sobel算子
1. Sobel算子用来计算图像灰度函数的近似梯度。Sobel算子根据像素点上下、左右邻点灰度加权差，在边缘处达到极值这一现象检测边缘。对噪声具有平滑作用，提供较为精确的边缘方向信息，边缘定位精度不够高。当对精度要求不是很高时，是一种较为常用的边缘检测方法。  
2. Sobel具有平滑和微分的功效。即：Sobel算子先将图像横向或纵向平滑，然后再纵向或横向差分，得到的结果是平滑后的差分结果。  
###### API
`Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst`
```
src参数表示输入需要处理的图像。
ddepth参数表示输出图像深度，针对不同的输入图像，输出目标图像有不同的深度。
　　具体组合如下： 
　　src.depth() = CV_8U, 取ddepth =-1/CV_16S/CV_32F/CV_64F （一般源图像都为CV_8U，为了避免溢出，一般ddepth参数选择CV_32F）
　　src.depth() = CV_16U/CV_16S, 取ddepth =-1/CV_32F/CV_64F 
　　src.depth() = CV_32F, 取ddepth =-1/CV_32F/CV_64F 
　　src.depth() = CV_64F, 取ddepth = -1/CV_64F 
　　注：ddepth =-1时，代表输出图像与输入图像相同的深度。 
dx参数表示x方向上的差分阶数，1或0 。
dy参数表示y 方向上的差分阶数，1或0 。
dst参数表示输出与src相同大小和相同通道数的图像。
ksize参数表示Sobel算子的大小，必须为1、3、5、7。
scale参数表示缩放导数的比例常数，默认情况下没有伸缩系数。
delta参数表示一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中。
```

#### Scharr算子
Scharr算子是Sobel算子的增强版，效果更突出。
###### API
`Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]) -> dst`
参数和Sobel算子的几乎差不多，意思也一样，只是没有ksize大小。

#### 拉普拉斯算子
拉普拉斯算子（Laplace Operator）是n维欧几里德空间中的一个二阶微分算子。
###### API
`Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst`
```
src参数表示输入需要处理的图像。
ddepth参数表示输出图像深度，针对不同的输入图像，输出目标图像有不同的深度。
　　具体组合如下： 
　　src.depth() = CV_8U, 取ddepth =-1/CV_16S/CV_32F/CV_64F （一般源图像都为CV_8U，为了避免溢出，一般ddepth参数选择CV_32F）
　　src.depth() = CV_16U/CV_16S, 取ddepth =-1/CV_32F/CV_64F 
　　src.depth() = CV_32F, 取ddepth =-1/CV_32F/CV_64F 
　　src.depth() = CV_64F, 取ddepth = -1/CV_64F 
　　注：ddepth =-1时，代表输出图像与输入图像相同的深度。 
dst参数表示输出与src相同大小和相同通道数的图像。
ksize参数表示用于计算二阶导数滤波器的孔径大小，大小必须是正数和奇数。
scale参数表示计算拉普拉斯算子值的比例因子，默认情况下没有伸缩系数。
delta参数表示一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中。
borderType表示判断图像边界的模式。这个参数默认值为cv2.BORDER_DEFAULT。
```

#### Canny边缘提取
Canny边缘检测算子目标是找到一个最优的边缘检测算法。
###### 最优边缘检测的含义
* 好的检测- 算法能够尽可能多地标识出图像中的实际边缘。  
* 好的定位- 标识出的边缘要尽可能与实际图像中的实际边缘尽可能接近。  
* 最小响应- 图像中的边缘只能标识一次，并且可能存在的图像噪声不应标识为边缘。  
###### 算法步骤
* 高斯模糊 - GaussianBlur  
* 灰度转换 - cvtColor  
* 计算梯度 – Sobel/Scharr  
* 非最大信号抑制  
* 高低阈值输出二值图像  
###### API （有2个接口函数）
`Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) -> edges`
```
image-8位输入图像
threshold1 -设置的低阈值
threshold2 -设置的高阈值，一般高低阈值的比例为3：1或者2：1
edges -参数表示输出边缘图像，单通道8位图像。
apertureSize -参数表示Sobel算子的大小。
L2gradient -参数表示一个布尔值，如果为真，则使用更精确的L2范数进行计算（即两个方向的倒数的平方和再开方），否则使用L1范数（直接将两个方向导数的绝对值相加）。
```
`Canny(dx, dy, threshold1, threshold2[, edges[, L2gradient]]) -> edges`
```
dx -输入图像的x导数（x导数满足16位，选择CV_16SC1或CV_16SC3）
dy -输入图像的y导数（y导数满足16位，选择CV_16SC1或CV_16SC3）
threshold1 -设置的低阈值
threshold2 -设置的高阈值，一般高低阈值的比例为3：1或者2：1
```


