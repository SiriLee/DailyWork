from tkinter import *
from tkinter import messagebox
# 头文件

# 1.创建窗口
window = Tk()

# 设置窗口大小
window.geometry('640x480')
# 标题
window.title('Hello')

var = StringVar()  # 存放可变可变内容

is_show = False  # 是否显示变量


# 事件函数
def say_hello():
    global is_show  # 说明全局变量
    if is_show is False:
        var.set('Hello world!')  # 设置内容
        is_show = True
    else:
        var.set('')
        is_show = False


def get_number():
    content = entry1.get()  # 获取输入框的内容
    var.set(content)  # 显示输入框内容


# 组件--按钮
btn = Button(window, text='Click me!', font=('黑体', 14), width=15, fg='white', bg='blue', command=say_hello)
# 显示
btn.pack()
btn = Button(window, text='Let me show your number!', font=('黑体', 14), width=30, fg='white', bg='blue',
             command=get_number)
btn.pack()  # 打一个新的包可用同一个变量在创建一个按钮

# 组件--label标签
lb = Label(window, textvariable=var, fg='green', bg='pink', font=('黑体', 18), width=30)
lb.pack()

# 放在某个位置
lb.place(x=20, y=215, width=600, height=50)

# 输入框 show表示输入内容显示样式 如果是NONE 输入什么显示什么 如果设置其他样式 输入什么显示设置的什么
entry = Entry(window, show='')
entry.pack()

entry1 = Entry(window, show='*')
entry1.pack()

msg = messagebox


def clear():
    # 询问是否确定
    res = msg.askokcancel('Hey', 'Are you sure?')
    if res is True:
        var.set('')


# 组件--弹框
btn = Button(window, text='clear all!', font=('黑体', 14), width=15, fg='white', bg='blue', command=clear)
btn.pack()

# 事件循环
window.mainloop()
