"""
os 模块处理文件实例
"""
import os

# # 获取文件大小
# print("文件大小：", os.path.getsize("../day02/demo/text.txt"))
#
# # 查看文件列表
# print(os.listdir("../day03"))
#
# # 查看文件是否存在
# print(os.path.exists("../day02/demo/text.txt"))
#
# # 查看文件是否为普通文件
# print(os.path.isfile("../day02/demo/text.txt"))
#
# # 删除文件
# os.remove("../day02/test.txt")

path = input("请输入目录位置：")
file_list = os.listdir(path)
for file in file_list:
    filename = path + "/" + file
    if os.path.getsize(filename) < 1024 and os.path.isfile(filename):
        os.remove(filename)
