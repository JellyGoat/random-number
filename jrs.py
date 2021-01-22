from random import shuffle
import tkinter as tk
from platform import system
import os
from sys import argv
from random import shuffle
from tkinter.messagebox import *
import copy
import pygal


# create the screen
window = tk.Tk()
window.geometry("800x600")
window.title("Random Selector | 随机抽取器 version 1.0.0")
window.iconphoto(False, tk.PhotoImage(
    file=os.path.join(".", "datas", "icon.png")))


# Global varies
global select_pool
select_pool = list([])
global selecting_pool
selecting_pool = list([])
global frequency
frequency = dict({})
global selecting_frequency
selecting_frequency = dict({})
global total_count
total_count = 0
global selecting_count
selecting_count = 0
global freq_diagram
freq_diagram = pygal.Bar()
freq_diagram._title = "抽取池的频数分布直方图"
freq_diagram._x_title = "抽取池元素"
freq_diagram._y_title = "元素剩余（或已抽取）频数"


# button functions


def Exit_Button_Onclick():
    # exit the program
    exit(0)


def Refresh_Button_Onclick():
    # refresh this turn through this function
    global selecting_pool
    global selecting_frequency
    global select_pool
    global frequency
    selecting_pool = copy.deepcopy(select_pool)
    shuffle(selecting_pool)
    selecting_frequency = copy.deepcopy(frequency)


def Reread_Button_Onclick():
    # reread anything from the choices.txt
    # but anything left this turn is preserved
    global select_pool
    global frequency
    global freq_diagram
    fin = open(os.path.join(".", "datas", "choices.txt"), mode="r+")
    select_pool = fin.readlines()
    fin.close()
    for alternative in select_pool:
        alternative = alternative.strip()
        if alternative is "":
            while alternative in select_pool:
                select_pool.remove(alternative)
    select_pool.sort()
    frequency.clear()
    for alternative in set(select_pool):
        frequency[alternative] = select_pool.count(alternative)
    freq_diagram.x_labels = list(set(select_pool))


def Save_Button_Onclick():
    global select_pool
    fout = open(os.path.join(".", "datas", "choices.txt"), mode="w+")
    for alternative in select_pool:
        fout.write(str(alternative) + '\n')
    fout.close()


def Rend_freq_to_file():
    global freq_diagram
    freq_list = list([])
    for selection, count in frequency.items():
        freq_list.append(count)
    freq_diagram.add("总抽取池", copy.deepcopy(freq_list))
    freq_list.clear()
    for left_freq in selecting_frequency.values():
        freq_list.append(left_freq)
    freq_diagram.add("剩余抽取池", copy.deepcopy(freq_list))
    freq_list.clear()
    for selection in frequency.keys():
        freq_list.append(frequency[selection] - selecting_frequency[selection])
    freq_diagram.add("已抽取数量", copy.deepcopy(freq_list))
    del freq_list
    freq_diagram.render_in_browser()
    freq_diagram = pygal.Bar()
    freq_diagram._title = "抽取池的频数分布直方图"
    freq_diagram._x_title = "抽取池元素"
    freq_diagram._y_title = "元素剩余（或已抽取）频数"


# buttons
# exit button
exit_button = tk.Button(
    window,
    text="退出程序",
    bg="lightblue",
    fg="black",
    font=("微软雅黑", 14),
    width=15,
    height=1,
    relief="flat",
    command=Exit_Button_Onclick
)
exit_button.place(
    x=50,
    y=500,
    anchor="nw"
)
# refresh button
refresh_button = tk.Button(
    window,
    text="刷新本次抽取池",
    bg="lightblue",
    fg="black",
    font=("微软雅黑", 14),
    width=15,
    height=1,
    relief="flat",
    command=Refresh_Button_Onclick
)
refresh_button.place(
    x=50,
    y=150,
    anchor="nw"
)
# Run the function first
# Reread_Button_Onclick()
# reread button
reread_button = tk.Button(
    window,
    text="重新读取抽取池",
    bg="lightblue",
    fg="black",
    font=("微软雅黑", 14),
    width=15,
    height=1,
    relief="flat",
    command=Reread_Button_Onclick
)
reread_button.place(
    x=50,
    y=210,
    anchor="nw"
)

# Labels
# Main title
main_title = tk.Label(
    window,
    text="Random Selector | 随机抽取器",
    font=("等线", 20),
    width=40,
    height=2,
    bg="pink",
    anchor="center"
)
main_title.place(
    x=400,
    y=10,
    anchor="n"
)
# selected subtitle
subtitle = tk.Label(
    window,
    text="随机抽取池信息",
    font=("等线", 17),
    width=20,
    height=1,
    bg="pink"
)
subtitle.place(
    x=500,
    y=100,
    anchor="n"
)
# former selection
former_side_lable = tk.Label(
    window,
    text="上一次选择",
    font=("微软雅黑", 14),
    width=13,
    height=2,
    bg="pink",
    anchor="center"
)
former_side_lable.place(
    x=380,
    y=150,
    anchor="n"
)
# former selection content
former_content = tk.Label(
    window,
    text="这里还什么都没有选٩(๑>◡<๑)۶",
    width=23,
    height=2,
    font=("微软雅黑", 14),
    bg="cornsilk",
    anchor="center"
)
former_content.place(
    x=620,
    y=150,
    anchor="n"
)


# add menu to this selector
menu_bar = tk.Menu(window)
# file operations
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(
    label="保存当前抽取池到配置文件",
    command=Save_Button_Onclick
)
file_menu.add_command(
    label="从配置中读取抽取池",
    command=Reread_Button_Onclick
)


# something else to complete
window.config(menu=menu_bar)
# main loop here
window.mainloop()
