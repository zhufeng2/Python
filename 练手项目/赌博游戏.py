import random
money=1000
print("你的总资产为1000")
#巧妙运用布尔类型的值对这种循环进行合适的控制
d=False
while money>0:
    print("请下注金额（至少为100元）:")
    money_1=int(input())
    if money_1<100:
        print("钱太少了，加亿点点，不要这么小气")
    elif money_1>money:
        print("你的金额不足了，请充值")
    else:
        money_2=money-money_1
        print("你的剩余金额为："+str(money_2))
        a=random.randint(1,6)
        b=random.randint(1,6)
        c=a+b
        if c==7 or c==11:
            print("你掷的两次色子的和为："+str(c))
            print("you are win!")
            money=money+money_1
            print('你的剩余金额为:' + str(money))
        elif c==2 or c==3 or c==12:
            print("你掷的两次色子的和为："+str(c))
            print("you are lose!")
            money=money-money_1
            print('你的剩余金额为:' + str(money))
        else:
            d=True
        while d:
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            c = a + b
            if c == 7 or c == 11:
                print("你掷的两次色子的和为："+str(c))
                print("you are win!")
                money = money + money_1
                print('你的剩余金额为:'+str(money))
                d=False
            elif c == 2 or c == 3 or c == 12:
                print("你掷的两次色子的和为："+str(c))
                print("you are lose!")
                money = money-money_1
                print("你的剩余金额为："+str(money))
                d=False
            else:
                d=True
else:
    print("你的金额不足，请充值")

