# 每一位数的三次方相加正好等于这个数本身
#range(st,en,step)
#这里的数据类型非常重要
for i in range(100,1000):
    a=int(i%10)
    b=int((i/10)%10)
    c=int((i/100)%10)
    if(a*a*a+b*b*b+c*c*c==i):
        print(i)