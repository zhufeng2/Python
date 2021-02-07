## 关键：
```python
import matplotlib.pyplot as plt
plt.plot(*****)
plt.show()
plt.axis([xmin, xmax, ymin, ymax])
plt.setp()
```
```python
lines = plt.plot(x, y)
# 使用键值对
plt.setp(lines, color='r', linewidth=2.0)
# 或者使用 MATLAB 风格的字符串对
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.show()
```

## 如何在一张图中画多个函数图像
```python

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```
![](https://raw.githubusercontent.com/zhufeng2/image/master/%E4%B8%8B%E8%BD%BD.png)

**例子:**
```python
import matplotlib.pyplot as plt 
import numpy as np 
def f(x):
    return np.sin(x**2)
x1=np.linspace(0,10,100)
x2=np.linspace(0,10,1000)
y2=np.sin(x)
plt.figure(1)
plt.subplot(211)
plt.plot(x1,f(x1),'bo',x2,f(x2),'k')
plt.subplot(212)
plt.plot(x,y2,'r--')
plt.show()
```
![](https://raw.githubusercontent.com/zhufeng2/image/master/1.png)

可以添加的一些设置：
```python
plt.axis([-5,5,-1,1])# plt.axis([xmin, xmax, ymin, ymax])
plt.text(0,-0.5,r'$y=\sin(x^2)$')#  图标，前面是方文字的坐标
plt.grid(True)#是否有网格
```

另外的注释方法：
```python
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()
```
效果：
![](https://raw.githubusercontent.com/zhufeng2/image/master/2.png)

```python
# -*- coding: gbk -*-

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.pylab import mpl
mpl.rcParams['font.family']='SimHei'# 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
plt.figure(1)
plt.figure(2)
axs1=plt.subplot(121)
axs2=plt.subplot(122)
x=np.linspace(0,3,100)
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.figure(1)
plt.plot(x,np.exp(x**2))
plt.sca(axs1)
plt.plot(x,np.sin(x**2))
plt.sca(axs2)
plt.plot(x,np.cos(x*2))
plt.show()
```

