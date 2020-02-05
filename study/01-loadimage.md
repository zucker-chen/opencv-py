## 加载图片方法
#### 本地图片打开  
* `src = cv.imread(r"C:\Users\Administrator\Pictures\ye.jpg")`  
* `r"C:\U.png"` 解释：  
    * 字符串前加 r，则字符串的'\'不会被转义  

#### 网络图片打开
* `cap = cv.VideoCapture(url)`  
* `cv.VideoCapture(url)`方法可以打开网络图片、视频与本地摄像头  

#### 图片属性获取
* 获取图片宽高及通道  
    * `print(img.shape)`   
    * `w = img.shape[0]`  
    * `h= img.shape[1]`  
    * `c = img.shape[2]`  

#### 图片各通道拆分及合并
```python
    r, g, b = cv.split(img))
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    bgr = cv.merge([b, g, r])
```
