```python
#创建一个指定维数的数组
import numpy as np
a=np.array(1,13).reshape((3,4))
print(a)
#对数组进行切片处理，获取第一，二列
sub_a=a[:2,:2]
print(sub_a)
```
对数组的值进行修改，则直接赋值运算即可。如果不想改变原来的值，只是对这个数组进行一点点的修改
则直接调用copy函数：
``` python  
sub_aa=np.copy(a[:2,:2])
#然后对sub_aa中的值进行直接的赋值修改
print(sub_aa)
```
reshape函数的操作：
reshape和np.reshape的语法会有一点区别
```python
b=np.reshape(a,(3,4))
#numpy package中的reshape函数用法
#转换为一维数组的操作
c=b.reshape(12)
c=b.reshape(-1)
c=b.ravel()
c=b.flatten()
```
数组之间的连接：hstack,vstack
```python
a=np.array([1,2,3,4],[4,5,6,7])
b=np.array([5,6,7,8],[4,3,2,1])
水平连接
c=np.hstack([a,b])
#垂直连接
d=np.vstack([a,b])
```
concatenate函数，参数axis,二维情况下axis=0 ，1，三维情况下aixs=0，1，2
```python
#reshape第一个参数代表几个，
第二个参数代表行，第三个参数代表列
a=np.arange(1,13).reshape(1,2,6)
b=np.arange(110,113).reshape(1,2,6)
r_3=concatenate([a,b],axis=0)
#此时得到的结果是两个两行六列的数组
r_4=concatenate([a,b],axis=1)
```
    



