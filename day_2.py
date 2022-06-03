from tkinter import *
from tkinter import messagebox
import random

'''————————————————————————————————————数据库————————————————————————————————————'''
real_price = random.randint(0, 1000)  # 随机生成真实价格
root = Tk()
msg = messagebox
try_again = messagebox
go_away = messagebox
choice = True


# 提交后的比较函数
def compare():
    global choice
    global real_price
    your_price = int(enter.get())
    if 0 <= your_price <= 1000:
        if your_price > real_price:
            info.set('太大了!')
        elif your_price < real_price:
            info.set('太小了！')
        else:
            info.set('恭喜你，答对了！')
            price.set(f'{real_price}')

            # 是否再开一局
            choice = try_again.askyesno(title='Hey', message='再来一局吗？')
            if choice is True:
                real_price = random.randint(0, 1000)
                enter.delete(first=0, last=len(enter.get()))
            else:
                go_away.showinfo('Good bye', '你可以退出了')
    else:
        msg.showerror(title='Warning', message='不合法数据!')


'''————————————————————————————————————数据库————————————————————————————————————'''
root.geometry('750x500+350+200')  # 窗口大小

# 可变字符串
price = StringVar(value='***')
info = StringVar(value='请输入价格')

# 四个标签
top = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), text='当前商品的价格是：')
price_label = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), textvariable=price)
question = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), text='请在0-1000间输入商品的价格')
instruction = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), textvariable=info)

# 输入框
enter = Entry(root, width=30)

# 提交按钮
btn = Button(root, font=('幼圆', 16), fg='white', bg='blue', text='提交', command=compare)

# 把所有东西放在不同位置
top.place(x=20, y=20)
price_label.place(x=170, y=20)
question.place(x=20, y=60)
instruction.place(x=550, y=375)

enter.place(x=20, y=100)

btn.place(x=250, y=100)


root.mainloop()
