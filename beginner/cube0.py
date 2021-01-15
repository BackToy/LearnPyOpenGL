#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  cube.py
@Time    :  2021/01/15 15:35:57
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  绘制一个立方体边框
'''
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)

WIDTH = 400
HEIGHT = 200


def init():
    """初始化"""
    glClearColor(0.0, 0.0, 0.0, 0.0)  # 设置“清除颜色”为黑色

    glLoadIdentity()  # 重置观察矩阵
    # 设置视点与视角
    gluLookAt(0.0, 0.0, 7.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    #  设置为投影模式
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # 重置观察矩阵
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)  # 设置
    glMatrixMode(GL_MODELVIEW)


def update():
    glClear(GL_COLOR_BUFFER_BIT)  # 将画面重置为指定的颜色-黑色
    glutWireCube(3.0)  # 绘制立方体的边框
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow('cube')
init()
glutDisplayFunc(update)
glutMainLoop()
