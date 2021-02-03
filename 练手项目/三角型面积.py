#输入三条边长，如果能构成三角形就计算周长和面积
print("plaese input the first number:\n")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a:
    C=a+b+c
    print("周长为:",C)
    p=(a+b+c)/2
    s=(p * (p - a) * (p - b) * (p - c))** 0.5
    print("面积为:",s)
else:
    print("该边长无法构成三角型")