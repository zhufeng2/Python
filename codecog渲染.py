import pyperclip
while(1==1):
    c=input("����latex��ʽ��")
    if c=="0":
        break
    else:
        d="<img src=\"https://latex.oncodecogs.com/svg.image? "+c+"\" />"
        print(d)
        pyperclip.copy(d)
        pyperclip.paste()