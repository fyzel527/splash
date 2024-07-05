from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import plyfile


def generate_gaussian_splash_ply():
    # 读取PLY文件
    plydata = plyfile.PlyData.read(r"D:\Gaussic\gaussian-splatting\output\6a33d5a9-4\point_cloud\iteration_30000"
                                   r"\point_cloud.ply")
    x = plydata['vertex']['x']
    y = plydata['vertex']['y']
    z = plydata['vertex']['z']

    # 绘制高斯泼溅
    plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z)
    plt.title("Gaussian Splash")

    # 将图像保存为PNG格式的字符串
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')


def splash_view(request):
    return render(request, 'splash/splash.html')

