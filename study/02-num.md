#### numpy 模块使用说明
> python的图片使用一个array装起来，然而numpy可以生成多维的array，从而可以操作图片的array

#### numpy基础函数介绍
* 生成B/G/R三通道全0的图片（全黑）  
`img = np.zeros([400, 400, 3], np.uint8)` 
* 生成3通道全白图片  
`img = np.ones([400, 400, 3], np.uint8) * 255` 
* 修改某通道图片数据，如B通道置128
`img[:, :, 0] = np.ones([400, 400]) * 128`