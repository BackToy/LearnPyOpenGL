#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)


def drawpoint():
    """绘制点"""
    glColor3ub(255, 0, 0)  # 设置画笔颜色为红色
    glPointSize(25)  # 设置基本像素点的大小
    glEnable(GL_POINT_SMOOTH)  # 开启点平滑
    # glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
    # glEnable(GL_BLEND)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
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

    # 画一个矩形的边框
    glPolygonMode(GL_FRONT, GL_LINE)  # 设置不填充模式
    glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_QUADS)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, -0.8)
    glVertex2f(0.4, -0.8)
    glVertex2f(0.4, 0.0)
    glEnd()

    glColor3f(1, 0, 1)  # 设置颜色
    # glPolygonMode(GL_FRONT, GL_FILL)  # 填充设置，取消注释对比以下
    # glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_QUADS)
    glVertex2f(0.1, 0.1)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.3, -0.5)
    glVertex2f(0.3, 0.1)
    glEnd()


def update():
    print("4")
    glClear(GL_COLOR_BUFFER_BIT)  # 清除上次显示的结果

    drawpoint()
    drawline()
    drawtriangle()
    drawquad()

    glFlush()  # 将草图上的内容进行绘制，不调用的话不会进行绘制


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow('PyOpenGL PLP')
print("1")
glutDisplayFunc(update)  # 注册回调函数
print("2")
glutMainLoop()
print("3")
