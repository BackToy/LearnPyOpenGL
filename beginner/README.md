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
在[用PyOpenGL叩开3D的心扉——OpenGL全解析4](https://eyehere.net/2011/learn-opengl-3d-by-pyopengl-4/)一文中。作者给出了10中基本图形的绘制函数列表及其对应的结果，这里对部分函数做一些举例。
#### 运行流程
里面用print大法对程序运行结构做了一个探究，程序在注册回调函数时并没有调用它，而是在进入glutMainLoop()之后才调用了回调函数，至于glutMainLoop()之后的3根本没有出现，也就是说程序一直在进行Loop。
#### 颜色
如果不指定颜色，OpenGL默认前景色为白色，背景色为黑色。颜色有两类好几种实现方法，RGB（红绿蓝）或者RGBA（多一个不透明度）
glColor打头，3、4表示参数个数，f代表[0,1]区间的浮点数，ub表示[0,255]之间的无符号整形吧？？更多详见[openGL 函数-glVertex* 指定顶点的值](https://blog.csdn.net/qq844352155/article/details/28465919)
```python
glColor4f(0.0, 1.0, 0.0, 1.0)  # 设置画笔颜色为绿色，不透明度为1
glColor3f(0.0, 1.0, 0.0)
glColor3ub(0, 255, 0)
glColor3fv([0.0, 1.0, 0.0])
```
颜色填充与否取决于设置，默认为颜色填充，可设置为不填充，此设置会保留
```python
glPolygonMode(GL_FRONT, GL_LINE)  # 设置不填充模式
glPolygonMode(GL_BACK, GL_FILL)
```
如果之前设置了不填充画了一个球，现在想画一个填充的爱心，那就的重新设置为填充模式了
```python
glPolygonMode(GL_FRONT, GL_FILL)  # 设置填充
glPolygonMode(GL_BACK, GL_LINE)
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
### [视景体](./glOrtho.py)
glOrtho(left, right, bottom, top, zNear, zFar)、glOrtho2D(left, right, bottom, top)用来创建一个正交的视景体（View Volume），说人话就是用一个长方姓（体）内部区域表示我们能看到的区域，如果要表示的物体大小不变，随着这个视景体区域越大，看到的物体就会越小。

![glOrthos示意图](./img/glOrtho.drawio.svg)  
设置视景体之后再次设置视景体会在当前的基础上进行设置，而不是从全局大小上设置，比如先看全局1/4的区域，然后再看1/8的区域，此时看到的全局的1/32，如果想看到全局的1/8，就需要在设置视景体之前重置观察矩阵`glLoadIdentity()`。

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
- [用PyOpenGL叩开3D的心扉——OpenGL全解析](https://eyehere.net/category/python/)
- [一步步学OpenGL3.3+  - Mr_厚厚](https://blog.csdn.net/cordova/category_9266966.html)
- [OpenGL的glViewport()函数和glOrtho()函数用法](https://blog.csdn.net/sj19890401/article/details/19976667)
- []()
