from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import io
import os
import sys
import base64
import plyfile
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def generate_gaussian_splash_ply():
    # 读取PLY文件
    plydata = plyfile.PlyData.read(r"C:\Users\Fyzel\Documents\gs_1234.ply")
    vertex = plydata['vertex']

    # 提取坐标
    x = vertex['x']
    y = vertex['y']
    z = vertex['z']

    # 检查是否包含颜色信息
    if 'red' in vertex and 'green' in vertex and 'blue' in vertex:
        colors = np.vstack((vertex['red'], vertex['green'], vertex['blue'])).T / 255.0
    else:
        colors = None

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 绘制点云，带颜色
    if colors is not None:
        ax.scatter(x, y, z, c=colors, marker='o', s=1)
    else:
        ax.scatter(x, y, z, c='b', marker='o', s=1)

    ax.set_title("Gaussian Splash")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 将图像保存为PNG格式的字符串
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')


def splash_view(request):
    image = generate_gaussian_splash_ply()
    return render(request, 'splash/splash.html', {'image': image})


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
