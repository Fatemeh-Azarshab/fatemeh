from tkinter import*
import tkinter.messagebox
#==========setting=============
root=Tk()
root.title("calculator")
root.geometry("400x200")
root.resizable(width=FALSE,height=FALSE)
color="red"
root.configure(bg=color)
#=========variables===========
num1=StringVar
num2=StringVar
result=StringVar
#===========frames=============
topfirst=Frame(root,width=400,height=50,bg=color)
topfirst.pack(side=TOP)
topsecond=Frame(root,width=400,height=50,bg=color)
topsecond.pack(side=TOP)
topthird=Frame(root,width=400,height=50,bg=color)
topthird.pack(side=TOP)
topforth=Frame(root,width=400,height=50,bg=color)
topforth.pack(side=TOP)
#===========functions===========
def errormsg(msg):
    if msg=="error":
        tkinter.messagebox.showerror("error","somthing went wrong ")
    elif msg=="divison zero error":
        tkinter.messagebox.showerror("divison error","can not divison by 0")

def plus():
    try:
        value=float(num1.get()) + float(num2.get())
        result.set(value)
    except:
        errormsg("error")
def minus():
    try:
        value=float(num1.get()) - float(num2.get())
        result.set(value)
    except:
        errormsg("error")
def mul():
    try:
        value=float(num1.get()) * float(num2.get())
        result.set(value)
    except:
        errormsg("error")
def div():
    if num2.get()=="0":
        errormsg("divison zero error")
    elif num2.get!="0":
        try:
            value=float(num2.get()) / float(num2.get())
            result.set(value)
        except:
            errormsg("error")


#===========buttons=============
btnplus=Button(topthird,text="+",highlightbackground=color,width=10,command=lambda:plus())
btnplus.pack(side=LEFT,padx=10,pady=10)

btnminus=Button(topthird,text="-",highlightbackground=color,width=10,command=lambda:minus())
btnminus.pack(side=LEFT,padx=10,pady=10)

btnmul=Button(topthird,text="*",highlightbackground=color,width=10,command=lambda:mul())
btnmul.pack(side=LEFT,padx=10,pady=10)

btndiv=Button(topthird,text="/",highlightbackground=color,width=10,command=lambda:div())
btndiv.pack(side=LEFT,padx=10,pady=10)
#===========Entries & Labels======
#first number
lblfirstnum=Label(topfirst,text="pleas enter number1:",bg=color)
lblfirstnum.pack(side=LEFT,padx=10,pady=10)
firstnum=Entry(topfirst,highlightbackground=color,textvariable=num1)
firstnum.pack(side=LEFT)
#second number
lblsecondnum=Label(topsecond,text="pleas enter number2:",bg=color)
lblsecondnum.pack(side=LEFT,padx=10,pady=10)
secondnum=Entry(topsecond,highlightbackground=color,textvariable=num2)
secondnum.pack(side=LEFT)
#result number
lblresultnum=Label(topforth,text="result:",bg=color)
lblresultnum.pack(side=LEFT,padx=10,pady=10)
resultnum=Entry(topforth,highlightbackground=color,textvariable=result)
resultnum.pack(side=LEFT)



root.mainloop()