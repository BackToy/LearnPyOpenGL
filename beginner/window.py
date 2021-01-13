from OpenGL.GLUT import glutInit, glutCreateWindow, \
    glutDisplayFunc, glutMainLoop


def update():
    pass


glutInit()  # 初始化glut库
glutCreateWindow('PyOpenGL window')  # 创建glut窗口标题为PyOpenGL window
glutDisplayFunc(update)  # 注册回调函数
glutMainLoop()  # 进入glut主循环
