#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  cube.py
@Time    :  2021/01/15 15:35:57
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  绘制一个立方体，设置透视投影和消隐，单击鼠标切换视角
'''
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)

WIDTH = 400
HEIGHT = 200
STATE = 0


def drawColorCube():
    """绘制一个六色的正方体"""
    glBegin(GL_QUADS)  # 绘制多个四边形
    glColor3f(1.0, 0.0, 0.0)  # 红色
    # 绘制立体的六个面
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glColor3f(0.0, 1.0, 0.0)  # 绿色
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glColor3f(0.0, 0.0, 1.0)  # 蓝色
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(1.0, 1.0, 0.0)  # 黄色

    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glColor3f(0.0, 1.0, 1.0)  # 青蓝色
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 0.0, 1.0)  # 紫色
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()


def mouseclick(button, state, x, y):
    """鼠标单击时发生回调：单击鼠标左键，STATE在1~3之间循环
    参数：
        button：0~2，左、中、右键
        state：0按下，1抬起释放
    """
    global STATE
    if state == 0 and button == 0:
        if STATE < 3:
            STATE += 1
        else:
            STATE = 1


def init():
    """初始化"""
    glClearColor(0.0, 0.0, 0.0, 0.0)  # 设置“清除颜色”为黑色

    # glShadeModel(GL_FLAT)  # 设置颜色插值为平面模式
    # 设置深度缓存
    glClearDepth(1.0)
    # 设置深度测试类型
    glDepthFunc(GL_LESS)
    # 允许深度测试
    glEnable(GL_DEPTH_TEST)

    glLoadIdentity()  # 重置观察矩阵
    gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)  # 设置视点与视角

    glMatrixMode(GL_PROJECTION)  #  设置为投影模式
    glLoadIdentity()  # 重置观察矩阵
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)


def update():
    global STATE
    print("update", STATE)
    if STATE == 1:  # 根据STATE切换视角
        glLoadIdentity()
        gluLookAt(-3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 2:
        glLoadIdentity()
        gluLookAt(3.0, -3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif STATE == 3:
        glLoadIdentity()
        gluLookAt(-3.0, -3.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # 将画面、深度重置
    drawColorCube()
    glutSwapBuffers()  # 交换缓存


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow('cube')
init()
glutDisplayFunc(update)
glutMouseFunc(mouseclick)  # 注册响应鼠标点击的函数mouseclick()
glutMainLoop()
