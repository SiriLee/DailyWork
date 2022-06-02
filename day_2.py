from tkinter import *
root = Tk()

root.geometry('750x500')

price = StringVar(value='***')

top = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), text='当前商品的价格是：')
price_label = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), textvariable=price)
question = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), text='请输入商品的价格')
instruction = Label(bg='#F2F2F2', fg='black', font=('幼圆', 12), width=300)

top.place(x=20, y=20)
price_label.place(x=170, y=20)
question.place(x=20, y=60)


root.mainloop()
