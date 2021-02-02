import pyperclip
while(1==1):
    c=input("输入latex公式：")
    if c=="0":
        break
    else:
        d="<img src=\"https://latex.oncodecogs.com/svg.image? "+c+"\" />"
        print(d)
        pyperclip.copy(d)
        pyperclip.paste()
