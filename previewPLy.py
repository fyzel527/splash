from plyfile import PlyData

def read_ply_file(file_path):
    # 读取PLY文件
    plydata = PlyData.read(file_path)

    # 打印文件头部信息
    print("PLY文件头部信息：")
    print(plydata.header)

    # 打印顶点信息
    vertex_data = plydata['vertex']
    print("\n顶点信息：")
    for name in vertex_data.data.dtype.names:
        print(f"{name}: {vertex_data[name]}")

    # 如果存在面信息，打印面信息
    if 'face' in plydata:
        face_data = plydata['face']
        print("\n面信息：")
        for name in face_data.data.dtype.names:
            print(f"{name}: {face_data[name]}")

# 替换为你的PLY文件路径
file_path = r"D:\Gaussic\gaussian-splatting\output\6a33d5a9-4\point_cloud\iteration_30000\point_cloud.ply"
read_ply_file(file_path)
