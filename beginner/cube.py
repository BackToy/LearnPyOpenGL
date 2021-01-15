#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  cube.py
@Time    :  2021/01/14 18:04:02
@Author  :  Kearney
@Version :  0.0.1
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  自动旋转的立方体  
'''
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)

WIDTH = 840
HEIGHT = 640


def drawColorCube():
    """绘制一个六色的正方体"""
    glBegin(GL_QUADS)  # 绘制多个四边形
    glColor3f(1.0, 0.0, 0.0)  # 红色
    # 绘制立体的六个面
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glColor3ub(255, 150, 0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glColor3f(0.0, 0.0, 1.0)  # 蓝色
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(0.0, 1.0, 0.0)  # 绿色
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glColor3f(1.0, 1.0, 0.0)  # 金黄色
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 1.0, 1.0)  # 白色
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()


def init():
    global WIDTH, HEIGHT
    # 设置深度缓存
    # glClearDepth(1.0)
    # 设置深度测试类型
    # glDepthFunc(GL_LESS)
    # 允许深度测试
    glEnable(GL_DEPTH_TEST)

    # 设置观察矩阵
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(WIDTH) / float(HEIGHT), 1, 10)  # 设置屏幕宽高比
    glMatrixMode(GL_MODELVIEW)
    # 移动位置
    glTranslatef(1.5, 0.0, -7.0)


def update():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 绕x、y轴旋转0.005度
    glRotate(0.005, 1.0, 1.0, 0.0)

    drawColorCube()
    glutSwapBuffers()  # 交换缓存


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow('PyOpenGL cube')
init()
glutDisplayFunc(update)
glutIdleFunc(update)  # 设置程序空闲时调用的函数
glutMainLoop()
