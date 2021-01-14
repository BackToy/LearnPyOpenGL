#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  word.py
@Time    :  2021/01/14 14:43:18
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  使用PyOpenGL绘制非中文字符串
https://www.walkerfree.com/article/114
暂时无法理解观察矩阵的深度
'''
try:
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)

WIDTH = 400
HEIGHT = 200


def init():
    """初始化设置"""
    glClearColor(0.0, 0.0, 0.0, 0.0)  # 设置为黑色背景
    glClearDepth(1.0)  # 设置深度缓存
    glDepthFunc(GL_LESS)  # 设置深度测试类型
    glEnable(GL_DEPTH_TEST)  # 允许深度测试
    glShadeModel(GL_SMOOTH)  # 启动平滑阴影
    glMatrixMode(GL_PROJECTION)  # 设置观察矩阵
    glLoadIdentity()  # 重置观察矩阵
    # 设置屏幕宽高比
    gluPerspective(45.0, float(WIDTH) / float(HEIGHT), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)  # 设置观察矩阵


def DrawText(string):
    """绘制字符串函数"""
    for c in string:  # 循环处理字符串，每次绘制一个字符
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))


def Draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # 清除颜色和深度缓存
    # 重置观察矩阵
    glLoadIdentity()
    # 移动位置
    glTranslatef(0.0, 0.0, -1.0)
    # 设置颜色为绿色
    glColor3f(0.0, 1.0, 0.0)
    # 定位文字
    glRasterPos2f(0.0, 0.0)
    # 绘制文字
    DrawText('PyOpenGL')
    # 交换缓存
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WIDTH, HEIGHT)
window = glutCreateWindow('PyOpenGL Word')
init()
glutDisplayFunc(Draw)
glutMainLoop()
