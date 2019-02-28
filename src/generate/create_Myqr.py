""""
使用myqr库生成定制化二维码图像
"""
from MyQR import myqr

data = input("请输入要保存到二维码中的信息：")
version = input("请输入版本号(1-40)：")
error_level = input("请输入纠错级别(H、M、L、Q):")
name = input('请输入要保存二维码名字:')
version = int(version)

# 生成
myqr.run(
    words=data,  # 信息
    version=version,  # 版本
    level=error_level,  # 纠错级别
    picture='G:/pycharm_project/Final_TCT/src/png/tct.png',  # 背景填充
    colorized=True,  # 是否彩色
    contrast=1.0,
    brightness=1.0,
    save_name=name + '.png',  # 保存图片
    save_dir='G:/pycharm_project/Final_TCT/src/png/'
)
