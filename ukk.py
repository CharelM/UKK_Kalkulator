import tkinter
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("600x650+150+250")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value): #function
    global equation
    equation+=value
    label_result.config(text=equation)

def delete_one():
     global equation
     equation = equation[:-1]
     label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result=eval(equation)
        except:
                result ="error"
                equation = ""
    label_result.config(text=result)

label_result= Label(root,width=30, height=3, text="",font=("arial",30)) #layar kalkulator
label_result.pack()

Button(root,text="CA", width=8, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#CD0404",command=lambda: clear()).place(x=30,y=150)
Button(root,text="C", width=8, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#CD0404",command=lambda: delete_one()).place(x=240,y=150)
Button(root,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("/")).place(x=450,y=150)

Button(root,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("7")).place(x=30,y=250)
Button(root,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("8")).place(x=170,y=250)
Button(root,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("9")).place(x=310,y=250)
Button(root,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("-")).place(x=450,y=250)

Button(root,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("4")).place(x=30,y=350)
Button(root,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("5")).place(x=170,y=350)
Button(root,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("6")).place(x=310,y=350)
Button(root,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("+")).place(x=450,y=350)

Button(root,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("1")).place(x=30,y=450)
Button(root,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("2")).place(x=170,y=450)
Button(root,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("3")).place(x=310,y=450)
Button(root,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("*")).place(x=450,y=450)

Button(root,text="0", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show("0")).place(x=170,y=550)
Button(root,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#F0F8FF",command=lambda: show(".")).place(x=30,y=550)
Button(root,text="=", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#000000", bg="#3697f5",command=lambda: calculate()).place(x=308,y=550)


root.mainloop()  #//perulangan