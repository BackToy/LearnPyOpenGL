# pyopengl-零基础入门
## 目录
### [创建一个窗体](./window.py)
显示一个最基本的窗体，并对其大小、位置、显示模式进行设置。

常见的窗体模式如下图
![常见GLUT模式解释](./img/GlutMode.png)
- GLUT_SINGLE   :   单缓冲区窗口,当不需要用户交互时用单缓冲，需要用户交互时要用双缓冲。
- GLUT_DOUBLE   :   双缓冲区窗口,这是产生流畅动画必须选的。

设置窗体大小和位置的两个函数参数都是横轴、纵轴像素大小，其中位置是相对于屏幕左上角。
```python
glutInitWindowSize(600, 250)  # 
glutInitWindowPosition(200, 400)    # 
```
### [点线面](./plp.py)
在[写给 python 程序员的 OpenGL 教程](https://xufive.blog.csdn.net/article/details/86565130)一文中。作者天元浪子给出了10中基本图形的绘制函数列表，这里对部分函数做一些举例。
#### 运行流程
里面用print大法对程序运行结构做了一个探究，程序在注册回调函数时并没有调用它，而是在进入glutMainLoop()之后才调用了回调函数，至于glutMainLoop()之后的3根本没有出现，也就是说程序一直在进行Loop。
#### 颜色
颜色有两类好几种实现方法，RGB（红绿蓝）或者RGBA（多一个不透明度）
glColor打头，3、4表示参数个数，f代表[0,1]区间的浮点数，ub表示[0,255]之间的无符号整形吧？？更多详见[openGL 函数-glVertex* 指定顶点的值](https://blog.csdn.net/qq844352155/article/details/28465919)
```python
glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置画笔颜色为绿色，不透明度为1
glColor3f(0.0, 1.0, 0.0)
glColor3ub(0, 255, 0)
glColor3fv([0.0, 1.0, 0.0])
```
#### 点的坐标
`glVertex2f(-1.0, -1.0)`表示给出的点的坐标为(-1.0, -1.0)-窗体左下角，右上角为(1.0, 1.0)
`glVertex3f(-1.0, -1.0, 0.0)`表示点的坐标为(x,y,z)类型，z=0.0时和上面表示一样  
绘制图形时并不直接给出一串点的坐标，而是通过一个个顶点的方式在glBegain()、glEnd()之间给出，需要注意的是，绘制多边形时是由顶点之间的线段连接起来的，这些线段不能交叉。
```python
# 如果把plp.py中的drawquad函数换位以下内容，观察所绘制出的四边形
def drawquad():
    """绘制四边形"""
    glBegin(GL_QUADS)
    glColor3f(0, 1, 1)  
    glVertex2f(0.5, 0.0)
    glVertex2f(0.5, -0.8)
    glVertex2f(1.0, 0.0)    # 点的顺序发生了变化
    glVertex2f(1.0, -0.8)
    glEnd()
```
### [键鼠事件](./event.py)
对对应的事件进行回调函数注册，在回调函数中对全局变量做更新并处理。有鼠标点击（含按下和释放）、拖动、移动、键盘、窗体大小修改事件。窗体拖动咋整哦-.-
### [绘制字符串](./word.py)
使用PyOpenGL绘制非中文字符串
## flake8 F403 F405
代码中如果使用flake8检查，会提示大量的F403+F405错误，我是用的是VS Code，在.vscode/setting.json中加入一些设置便可以不提示这两个烦人的红叉叉
```
"python.linting.flake8Args": [
    "--extend-ignore = F403,F405"
]
```
## 致谢
对以下内容的作者表示感谢
- [写给 python 程序员的 OpenGL 教程](https://xufive.blog.csdn.net/article/details/86565130)
- [一篇就够的超良心pyOpenGL入门教程，不香喷我！](https://blog.csdn.net/edj_13/article/details/104673528)
- [OpenGL学习进程（3）第一课：初始化窗体](https://www.cnblogs.com/MenAngel/p/5619808.html)
- [openGL 函数-glVertex* 指定顶点的值](https://blog.csdn.net/qq844352155/article/details/28465919)
- [Python中的除法](https://blog.csdn.net/sicofield/article/details/8613877)
- [Python 入门基础知识 - 多媒体编程 - 使用PyOpenGL绘制3D图形](https://www.walkerfree.com/search/?key=opengl&submit=Search)
- []()
