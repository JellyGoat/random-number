from random import shuffle
import tkinter as tk
from platform import system
import os
from sys import argv
from random import shuffle
from tkinter.messagebox import *


# create the screen
window = tk.Tk("Random Stand Up!")
window.geometry("800x600")

# title lable
Title_Lable = tk.Label(window, text="抽号器 version 0.1.0", bg="pink",
                       font=("Fira code", 12), width=30, height=2)
Title_Lable.pack()
# Name echo lable
Random_Name = tk.StringVar()
Random_Name.set("下一位：等待您的抽号")
Name_Lable = tk.Label(window, textvariable=Random_Name, bg="pink",
                      font=("等线 Light", 14), width=30, height=3)
Name_Lable.place(x=250, y=192, anchor="nw")

'''
                       <-- 分割： 按钮 ->
'''

# let you to input the names


def Disabled():
    pass


Name_List = [None]
Name_List.pop()


def Search_File(path: str, file_name: str):
    files = os.listdir(path)
    if file_name in files:
        return True
    else:
        return False


def Create_File(path: str, file_name: str):
    fcreate = open(os.path.join(path, file_name), "w+")
    fcreate.close()


def Open_Names_File():
    global Name_List
    file_name = os.path.join(".", "names.txt")
    if not Search_File(".", "names.txt"):
        Create_File(".", "names.txt")
    os.system(file_name)
    fin = open(file_name, "r")
    Name_List = fin.read().split()
    shuffle(Name_List)
    if "--debug" in argv:
        print(Name_List)


Input_Name_Button = tk.Button(window, text="更新或输入名字", bg="lightblue",
                              font=("等线 Light", 12), width=18, height=2,
                              command=Open_Names_File, activebackground="pink",
                              relief="flat")
Input_Name_Button.place(x=50, y=100, anchor="nw")
# next name button


def Echo_Next():
    if len(Name_List) is not 0:
        Random_Name.set(Name_List[0])
        del Name_List[0]
    else:
        Random_Name.set("本轮已结束，请更新列表")


Next_Button = tk.Button(window, text="抽下一位", bg="lightblue",
                        font=("等线 Light", 12), width=18, height=2,
                        command=Echo_Next, activebackground="pink",
                        relief="flat")
Next_Button.place(x=50, y=200, anchor="nw")
# remove temp button


def Remove_Temp_File():
    try:
        os.remove(os.path.join(".", "names.txt"))
    except FileNotFoundError:
        showerror("错误", "还没有生成临时文件")

Remove_Button = tk.Button(window, text="删除临时文件", bg="lightblue",
                          font=("等线 Light", 12), width=18, height=2,
                          command=Remove_Temp_File, activebackground="pink",
                          relief="flat")
Remove_Button.place(x=50, y=300, anchor="nw")

window.mainloop()
