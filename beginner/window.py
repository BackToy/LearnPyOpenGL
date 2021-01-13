try:
    from OpenGL.GLUT import *
except Exception as msg:
    print("未正确安装PyOpenGL，错误代号：", msg)


def update():
    pass


glutInit()  # 初始化glut库
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # 设置单缓冲RGB颜色模式
glutInitWindowSize(640, 480)  # 设置窗体大小
glutInitWindowPosition(0, 0)  # 设置窗体位置
glutCreateWindow('PyOpenGL window')  # 创建窗体，标题为PyOpenGL window
glutDisplayFunc(update)  # 注册回调函数
glutMainLoop()  # 进入glut主循环
