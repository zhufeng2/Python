# matplotlib��ͼ
## ��λ��ƶ����ͼ��
����������`subplot`��`subplots`��`fig, axes = plt.subplots(23)��`����ʾһ������figure�ϴ�����2*3������ʹ��`plt.subplot()`ֻ��һ��һ������ӡ�
����ʾ����
```python
fig = plt.figure()
ax = plt.subplot(231)
ax = plt.subplot(232)
ax = plt.subplot(233)
ax = plt.subplot(234)
ax = plt.subplot(235)
ax = plt.subplot(236)
```
## ֧������
```python
# -*- coding: gbk -*-
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.pylab import mpl
mpl.rcParams['font.family']='SimHei'# ָ��Ĭ������
mpl.rcParams['axes.unicode_minus'] = False # �������ͼ���Ǹ���'-'��ʾΪ���������
```
![](https://raw.githubusercontent.com/zhufeng2/image/master/46466fab6541a43801597631097d693c.png)

## artist����
>alpha : ͸���ȣ�ֵ��0��1֮�䣬0Ϊ��ȫ͸����1Ϊ��ȫ��͸��
animated : ����ֵ���ڻ��ƶ���Ч��ʱʹ��
axes : ��Artist�������ڵ�Axes���󣬿���ΪNone
clip_box : ����Ĳü���
clip_on : �Ƿ�ü�
clip_path : �ü���·��
contains : �ж�ָ�����Ƿ��ڶ����ϵĺ���
figure : ���ڵ�Figure���󣬿���ΪNone
label : �ı���ǩ
picker : ����Artist����ѡȡ
transform : ����ƫ����ת
visible : �Ƿ�ɼ�
zorder : ���ƻ�ͼ˳��

## Axeis����
Axis ���������������ϵĿ̶��ߡ��̶��ı������������Լ��������������ݡ�



