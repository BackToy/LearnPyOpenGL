#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *

except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)

STATE = 0


def mouseclick(button, state, x, y):
    """鼠标单击时发生回调：单击鼠标左键，STATE在1~3之间循环
    参数：
        button：0~2，左、中、右键
        state：0按下，1抬起释放
        x, y：鼠标在窗体中的位置坐标
    """
    global STATE
    if state == 0 and button == 0:
        if STATE < 3:
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
    """根据STATE的值设置不同的视景体，STATE默认为0"""
    if STATE == 1:  # 取消掉下面两行注释你发现了什么？？？
        # glLoadIdentity()  # 重置观察矩阵
        glOrtho(0.0, 1.0, -1.0, 0.0, -1.0, 1.0)
    elif STATE == 2:
        # glLoadIdentity()  # 重置观察矩阵
        glOrtho(0.0, 0.6, -0.6, 0.0, -1.0, 1.0)
    elif STATE == 3:
        glLoadIdentity()  # 重置观察矩阵

    drawpoint()
    drawline()
    drawtriangle()
    drawquad()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutCreateWindow('PyOpenGL glOrtho')
glutMouseFunc(mouseclick)  # 注册响应鼠标点击的函数mouseclick()
glutDisplayFunc(update)  # 注册回调函数
glutMainLoop()
