from tkinter import *


sc=Tk()
sc.geometry("350x400")
sc.title("Sorathiya")
sc.configure(bg="#17161b")

equation =""

def show(value):
    global equation
    equation+=value
    label_result.config(text = equation)

def clear():
    global equation
    equation = ""
    label_result.config(text = equation)

def calculat():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text = result)


label_result=Label(sc,text = "",width = 25,height = 2,font = "Arial 30")
label_result.pack()

Button(sc,text = "C",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#3697f5",command = lambda :clear()).place(x=10,y=100)
Button(sc,text = "%",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("%")).place(x=90,y=100)
Button(sc,text = "/",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("/")).place(x=170,y=100)
Button(sc,text = "*",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("*")).place(x=250,y=100)

Button(sc,text = "7",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("7")).place(x=10,y=150)
Button(sc,text = "8",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("8")).place(x=90,y=150)
Button(sc,text = "9",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("9")).place(x=170,y=150)
Button(sc,text = "-",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("-")).place(x=250,y=150)

Button(sc,text = "4",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("4")).place(x=10,y=200)
Button(sc,text = "5",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("5")).place(x=90,y=200)
Button(sc,text = "6",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("6")).place(x=170,y=200)
Button(sc,text = "+",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("+")).place(x=250,y=200)

Button(sc,text = "1",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("1")).place(x=10,y=250)
Button(sc,text = "2",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("2")).place(x=90,y=250)
Button(sc,text = "3",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("3")).place(x=170,y=250)
Button(sc,text = "=",font = "Arial 15 bold",width = 5,height = 3,bd = 2,fg = "#fff",bg = "#fe9037",command = lambda :calculat()).place(x=250,y=250)

Button(sc,text = "0",font = "Arial 15 bold",width = 11,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show("0")).place(x=15,y=300)
Button(sc,text = ".",font = "Arial 15 bold",width = 5,height = 1,bd = 2,fg = "#fff",bg = "#2a2b36",command = lambda :show(".")).place(x=170,y=300)


sc.mainloop()