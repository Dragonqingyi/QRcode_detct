""""
使用qrcode库生成二维码
"""

import qrcode

data = input("请输入要保存到二维码中的信息：")
version = input("请输入版本号(1-40)：")
error_choose = input("请输入纠错级别(H、M、L、Q):")
name = input('请输入要保存二维码名字:')
version = int(version)
error_level = ''
if error_choose == 'H':
    error_level = qrcode.ERROR_CORRECT_H
elif error_choose == 'M':
    error_level = qrcode.ERROR_CORRECT_M
elif error_choose == 'L':
    error_level = qrcode.ERROR_CORRECT_L
else:
    error_level = qrcode.ERROR_CORRECT_Q


def genetateQr(data, version, error, name):
    qr = qrcode.QRCode(version=version,
                       error_correction=error,
                       box_size=10,
                       border=4)
    qr.add_data(data)  # 添加数据
    qr.make(fit=True)
    img = qr.make_image()  # 填充背景图
    name = name + '.png'  # 设置图片名称
    img.save('G:/pycharm_project/Final_TCT/src/png/' + name)


# 生成
genetateQr(data, version, error_level, name)
