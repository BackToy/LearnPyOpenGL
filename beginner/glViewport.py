#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  glViewport.py
@Time    :  2021/01/15 11:06:04
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  单击鼠标左键切换不同的视见区域
'''

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *

except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)

STATE = 0
WIDTH = 800
HEIGHT = 600


def mouseclick(button, state, x, y):
    """鼠标单击时发生回调：单击鼠标左键，STATE在1~5之间循环
    参数：
        button：0~2，左、中、右键
        state：0按下，1抬起释放
        x, y：鼠标在窗体中的位置坐标
    """
    global STATE
    if state == 0 and button == 0:
        if STATE < 5:
            STATE += 1
        else:
            STATE = 1


def drawpoint():
    """绘制点"""
    glColor3ub(255, 0, 0)  # 设置画笔颜色为红色
    glPointSize(25)  # 设置基本像素点的大小
    glEnable(GL_POINT_SMOOTH)  # 开启点平滑
    glBegin(GL_POINTS)  # 开始草图画点模式
    glVertex2f(0.0, 0.0)  # 点的坐标
    glEnd()


def drawline():
    """绘制线段"""
    glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置画笔颜色为绿色，不透明度为1
    glLineWidth(5)  # 设置线宽
    glBegin(GL_LINES)  # 开启在草图画线模式

    glVertex2f(-1.0, -1.0)  # 起始点坐标
    glVertex2f(0.5, 0.5)  # 终点坐标

    glVertex2f(-1.0, -1.0)  # 起始点坐标
    glVertex2f(1.0, -1.0)  # 终点坐标
    glEnd()  # 关闭画线模式


def drawtriangle():
    """绘制三角形"""
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)  # 设置画笔颜色为蓝色
    glVertex2f(-1.0, 0.0)
    glVertex2f(-0.5, 0.0)
    glVertex2f(1.0, 1.0)
    glEnd()


def drawquad():
    """绘制四边形"""
    # 画一个填充的矩形
    glBegin(GL_QUADS)  # 默认为填充模式
    glColor3f(0, 1, 1)  # 设置画笔颜色为青蓝色
    glVertex2f(0.5, 0.0)
    glVertex2f(0.5, -0.8)
    glVertex2f(1.0, -0.8)
    glVertex2f(1.0, 0.0)
    glEnd()


def update():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    global STATE
    print(STATE)
    """根据STATE的值设置不同的视见区域，STATE默认为0"""
    if STATE == 1:  # 取消掉下面两行注释你发现了什么？？？
        glViewport(0, 0, int(WIDTH / 2), int(HEIGHT / 2))
    elif STATE == 2:
        glViewport(0, 0, int(WIDTH / 3), int(HEIGHT / 3))
    elif STATE == 3:
        glViewport(100, 100, WIDTH, HEIGHT)
    elif STATE == 4:
        glViewport(100, 100, int(WIDTH / 2), int(HEIGHT / 2))
    elif STATE == 5:
        glViewport(0, 0, WIDTH, HEIGHT)

    drawpoint()
    drawline()
    drawtriangle()
    drawquad()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)  # 设置窗体大小
glutCreateWindow('PyOpenGL glOrtho')
glutMouseFunc(mouseclick)
glutDisplayFunc(update)
glutMainLoop()
