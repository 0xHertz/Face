# OpenCV安装
```shell
> pip install opencv-python
```
# 什么是OpenCV
OpenCV是一个旨在解决计算机视觉问题的Python库。OpenCV最初由Intel在1999年开发，但是后来由Willow Garage资助。它支持很多编程语言，如C++，Python，Java等等。它也支持多种平台，包括Windows，Linux和MacOS。

OpenCV Python只是一个与Python一起使用的原始C++库的包装类。通过使用它，所有OpenCV数组结构都能被转化为`NumPy`数组或从`NumPy`数组转化而来。这样就可以轻松地将其与其他使用`NumPy`的库集成。例如，`SciPy`和`Matplotlib`等库。
# OpenCV案例
## 图片基础操作
### 加载
```python
# colored img
    img = cv2.imread("2.png",1)
    # Black&white img
    img1 = cv2.imread("2.png",0)
```
### 查看图片信息
* 查看图片分辨率
```python
print(type(img))
    print(img.shape)
    print(img1.shape)
```
### 展示图片
```python
# show pic
    cv2.imshow("Penguins", img1)
    cv2.waitKey(0)# hold
    cv2.destroyAllWindows()
```
### 修改图片信息
* 调整图片大小
```python
# change pic shape
    resizedImg = cv2.resize(img, (300,300))# only change high & wide, can not change channal
    cv2.imshow("Penguins", resizedImg)
    cv2.waitKey(0)# hold
    cv2.destroyAllWindows()
```
## 人脸识别
1. 想一想我们的先决条件。我们首先需要一个图像。然后，我们需要创建一个`级联分类器`，它最后会给我们提供面部特征。

2. 这一步要使用到OpenCV读取图像和特征文件。所以这个时候，原始数据点是NumPy数组的形式。我们要做的就是搜索面部 NumPy n维数组的行和列的值。这是具有面部矩形坐标的数组。

3. 最后一步是使用矩形面框显示图像。
```python
import cv2  

# Create a CascadeClassifier Object  

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  

# Reading the image as it is  

img = cv2.imread("photo.jpg") 

# Reading the image as gray scale image  

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  

# Search the co-ordintes of the image  
# use detectMultiScale methd, 检测输入图像中不同大小的对象。检测到的对象作为矩形列表返回

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05,  minNeighbors=5)  

for x,y,w,h in faces:  
    # 这个函数的作用是在图像上绘制一个简单的矩形
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)  

resized = cv2.resize(img, (int(img.shape[1]/7),int(img.shape[0]/7)))   

cv2.imshow("Gray", resized)  

cv2.waitKey(0)  

cv2.destroyAllWindows()
```
## 使用OpenCV捕获视频
```
testFrame.py
testVedio.py
```
## 使用OpenCv的运动检测器
```
testMove,py
```
# Face
