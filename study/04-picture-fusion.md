## 图片融合
实现RGB图片与黑白图片融合，及RGB Sensor与Mono Sensor融合

## 海康融合效果
* RGB Sensor 图片：
![](.04-picture-fusion_images/rgb.jpg)
* Mono Sensor 图片：
![](.04-picture-fusion_images/mono.jpg)
* 海康融合效果图片：
![](.04-picture-fusion_images/hik.jpg)

## opencv 融合过程
* 转换为YUV
* 将mono图片的Y分量进行均值化处理
* rgb及mono图片Y分量范围压缩成0~128
* 将rgb及mono图片的Y分量进行加权合并

## opencv融合效果：
![](.04-picture-fusion_images/opencv.jpg)


