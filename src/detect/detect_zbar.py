""""
测试文件
在静态图片中进行二维码定位，画出轮廓，并打印四个顶点信息
使用库：pyzbar
author:青衣
"""

# 导入依赖
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


# 根据图像中二维码位置信息计算小车位置信息，假设版，有待使用摄像头具体实验
def location(points):
    arr = np.array(points)
    if len(arr) != 4:
        print("ERROR! The data is not complete!")
    else:
        x1 = (arr[0][0] - arr[3][0]) / 2 + arr[0][0]
        x2 = (arr[1][0] - arr[2][0]) / 2 + arr[1][0]
        x = (x1 + x2) / 2
        place = x * 1 + 2
        print('The location of the car is:', place)


# 图像中二维码定位，画出轮廓边缘线，蓝色
def display(im, decodedObjects):
    # 循环pyzbar解码信息
    for decodedObject in decodedObjects:
        points = decodedObject.polygon
        # 打印二维码四个顶点坐标
        print(points)
        # 打印解析出来的信息
        if len(decodedObjects):
            zbarData = decodedObjects[0].data
        else:
            zbarData = 'NO INFORMATION !!!!!!'
        print("ZBAR : {}".format(zbarData))
        # 如果点不形成四边形，则找到凸包
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        # 凸包数量
        n = len(hull)
        location(hull)
        # 画轮廓线，用cv2 画线函数line
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # 显示结果
    cv2.imshow("Results", im)
    cv2.waitKey(0)


# 静态图路径，注意斜杠方向，反斜杠要加解析符
inputImage = 'G:/pycharm_project/Final_TCT/src/png/t1.png'
inputImage = cv2.imread(inputImage)
decodedObjects = pyzbar.decode(inputImage)
display(inputImage, decodedObjects)
