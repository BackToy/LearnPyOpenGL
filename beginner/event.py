#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :  event.py
@Time    :  2021/01/14 09:07:59
@Author  :  Kearney
@Version :  0.0.0
@Contact :  191615342@qq.com
@License :  GPL 3.0
@Desc    :  对对应的事件进行回调函数注册，在回调函数中对全局变量做更新并处理
'''

from __future__ import division  # 精确除法
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)

PX = PY = 100
WIDTH = 400
HEIGHT = 200


def drawpoint():
    """绘制点,如何在PX，PY点进行绘制呢？？2s,2i,2d试过都不正常"""
    print("drawpoint")
    glColor3ub(255, 0, 0)
    glPointSize(25)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex2f(PX / WIDTH, PY / HEIGHT)  # 点的坐标
    glEnd()


def update():
    print("update")
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawpoint()
    glFlush()
    print("update down")


def reshape(width, height):
    """窗体大小发生变化时回调
    参数：
        width：修改大小后的窗体宽度
        height：修改大小后的窗体高度
    """
    print("reshape", width, height)


def mouseclick(button, state, x, y):
    """鼠标单击时发生回调
    参数：
        button：0~2，左、中、右键
        state：0按下，1抬起释放
        x, y：鼠标在窗体中的位置坐标
    """
    print("mouseclick", button, state, x, y)
    global PX, PY
    PX = x
    PY = y


def mousemotion(x, y):
    """鼠标按下并拖动时回调
    参数：
        x, y：鼠标在窗体中的位置坐标
    """
    print("mousemotion", x, y)


def keydown(key, x, y):
    """窗体被激活时的键盘响应事件
    参数：
        key：键盘对应按键
        x, y：鼠标在窗体中的位置坐标
    """
    print("keydown", key, x, y)


def mouseenter(enter):
    """鼠标进入或离开窗体时回调
    参数：
        enter：0离开窗体，1进入窗体
    """
    print("mouseenter", enter)


def mousemove(x, y):
    """鼠标移动响应事件
    参数：
        x, y：鼠标在窗体中的位置坐标
    """
    print("mousemove", x, y)


glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)  # 设置窗体大小
window = glutCreateWindow('PyOpenGL Event')
glutDisplayFunc(update)  # 注册回调函数

glutReshapeFunc(reshape)  # 注册响应窗口改变的函数reshape()
glutMouseFunc(mouseclick)  # 注册响应鼠标点击的函数mouseclick()
glutMotionFunc(mousemotion)  # 注册响应鼠标拖拽的函数mousemotion()
glutKeyboardFunc(keydown)  # 注册键盘输入的函数keydown()
glutEntryFunc(mouseenter)  # 注册
glutPassiveMotionFunc(mousemove)  # 注册
glutMainLoop()
