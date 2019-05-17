# coding=utf-8

import pip
import os

from subprocess import call

# def path_process(path: str):
#     tmp_path = []
#     lens = len(path)
#     for i in lens:
#         tmp_path.append(path[i])
#         if i < lens - 1:
#             if p == '\':
#                 tmp_path.append(p)
#     return tmp_path


def install(file_name):
    
    with open(file_name, 'r') as f:
        for i in f:
            call(
                'pip install ' + i,
                shell=True
            )

def update(file_name):

    with open(file_name, 'r') as f:
        for i in f:
            call(
                'pip install --upgrade ' + i,
                shell=True
            )

def update_vnconda(file_name):
    with open(file_name, 'r') as f:
        for i in f:
            call(
                'pip install ' + i,
                shell=True
            )


if __name__ == "__main__":
    # 暂时屏蔽安装 dataclasses 
    # dataclasses; python_version<="3.6"
    # path = os.getcwd()
    # print(path, type(path))
    # path = path_process(path)
    # print(path)
    file_name = r"C:\Users\Administrator\Anaconda3\envs\install_vnpy\requirements_vn_hard.txt"

    # install packages
    install(file_name)

    # # update
    # update(file_name)

    # update vnconda
    # update_vnconda(file_name)
