a=input("chose your type of tempreture:F or C\n")
if a=="F":
    b=float(input("please input the concreat number:"))
    c=(b-32)/1.8
    print(c)
elif a=="C":
    F=float(input("please input the concreat number:"))
    f=1.8*F+32
    print(f)
