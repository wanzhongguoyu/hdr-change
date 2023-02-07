# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:28:12 2022

@author: lin
"""


def hdr_need():
    import os

    """
    导入 os包
    得到所需的 hdr文件   block1和block2的 hdr位置

    Returns: hdr_path

            所需hdr的list的绝对路径

    warning: 不通用 可参考

    """

    # 导入hdr
    path = os.getcwd()
    hdr_path_all = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == 'NIRS.hdr':
                hdr_path_all.append(os.path.join(root, file))

    hdr_path = []
    for path in hdr_path_all:
        if ('block1' in path) or ('block2' in path):
            hdr_path.append(path)

    return hdr_path
