""""
opencv4实时监测视频中二维码，蓝线标注，打印顶点坐标
author：青衣
"""

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# 获取摄像头
cap = cv2.VideoCapture(0)
# 读取帧视频
hasFrame, frame = cap.read()
# 视频写入本地
vid_writer = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                             (frame.shape[1], frame.shape[0]))


# 根据图像中二维码位置信息实时计算小车位置信息并输出
def location(points):
    arr = np.array(points)
    if len(arr != 4):
        print("ERROR! The data is not complete!")
    else:
        x1 = (arr[0][0] - arr[3][0]) / 2 + arr[0][0]
        x2 = (arr[1][0] - arr[2][0]) / 2 + arr[1][0]
        x = (x1 + x2) / 2
        place = x * 1 + 2
        print(place)


# 图像中二维码定位，画出轮廓边缘线，蓝色
def display(im, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # 如果点不形成四边形，则找到凸包
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        # 凸变形定点数（凸包数）
        n = len(hull)

        # 画轮廓线
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    # 显示结果图像
    cv2.imshow("Results", im)


# 持续检测
while 1:
    # 摄像头读取图像
    hasFrame, inputImage = cap.read()
    if not hasFrame:
        break
    # 对每一帧图像进行二维码定位解码
    decodedObjects = pyzbar.decode(inputImage)
    if len(decodedObjects):
        zbarData = decodedObjects[0].data
    else:
        zbarData = ''
    # 识别出来在视频中显示信息，否则显示未检测出二维码
    if zbarData:
        cv2.putText(inputImage, "ZBAR : {}".format(zbarData), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                    cv2.LINE_AA)
    else:
        cv2.putText(inputImage, "ZBAR : QR Code NOT Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                    cv2.LINE_AA)

    # 进行处理后图像显示
    display(inputImage, decodedObjects)
    cv2.imshow("Result", inputImage)
    vid_writer.write(inputImage)
    # 键盘按 1 退出
    if (cv2.waitKey(1) & 0xFF) == ord('1'):
        break
cv2.destroyAllWindows()
vid_writer.release()
