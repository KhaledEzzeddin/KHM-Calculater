#----------tk Lib
from tkinter import *
#----------Window
win =Tk()
#----------win title
win.title("KCalculator")
#----------location and Size x y
win.geometry("350x390+100+100")
#----------win model
win.configure(background="#c1bebe")
#----------control size x
win.resizable(width=False,height=False)
#----------image
icon=PhotoImage(file="calcicon.png",)
win.call("wm","iconphoto",win._w,icon)
input=StringVar()
opr=""
def clkbtn(numbers):
    global opr
    opr+=(str(numbers))
    input.set(opr)
def resbtn():
    global opr
    res=float(eval(opr))
    input.set(res)
    opr=res
def clrbtn():
    global opr
    opr=""
    input.set("")
#Result
tres=Entry(win,state=DISABLED,textvariable=input,relief=FLAT,width=20,font=("times",16,"bold"),background="#dad8d8",bd=6,justify="right")
tres.place(x=30,y=30)
#button
#buttdel
btnd=Button(win,command=clrbtn,cursor="hand2",text="Delete",padx=10,pady=2,width=2,height=1,font=("",9,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btnd.place(x=270,y=30)
#num7
btn7=Button(win,command=lambda:clkbtn(7),cursor="hand2",text="7",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn7.place(x=35,y=80)
#num8
btn8=Button(win,command=lambda:clkbtn(8),cursor="hand2",text="8",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn8.place(x=113,y=80)
#num9
btn9=Button(win,command=lambda:clkbtn(9),cursor="hand2",text="9",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn9.place(x=190,y=80)
#num*
btnx=Button(win,command=lambda:clkbtn("*"),cursor="hand2",text="*",padx=10,pady=2,width=1,height=2,font=("times",13,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btnx.place(x=270,y=80)
#num4
btn4=Button(win,command=lambda:clkbtn(4),cursor="hand2",text="4",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn4.place(x=35,y=150)
#num5
btn5=Button(win,command=lambda:clkbtn(5),cursor="hand2",text="5",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn5.place(x=113,y=150)
#num6
btn6=Button(win,command=lambda:clkbtn(6),cursor="hand2",text="6",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn6.place(x=190,y=150)
#num\
btndv=Button(win,command=lambda:clkbtn("/"),cursor="hand2",text="/",padx=10,pady=2,width=1,height=2,font=("times",13,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btndv.place(x=270,y=150)
#num1
btn1=Button(win,command=lambda:clkbtn(1),cursor="hand2",text="1",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn1.place(x=35,y=220)
#num2
btn2=Button(win,command=lambda:clkbtn(2),cursor="hand2",text="2",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn2.place(x=113,y=220)
#num3
btn3=Button(win,command=lambda:clkbtn(3),cursor="hand2",text="3",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn3.place(x=190,y=220)
#num+
btnpl=Button(win,command=lambda:clkbtn("+"),cursor="hand2",text="+",padx=10,pady=2,width=1,height=2,font=("times",13,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btnpl.place(x=270,y=220)
#num.
btnp=Button(win,command=lambda:clkbtn("."),cursor="hand2",text=".",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btnp.place(x=35,y=290)
#num0
btn0=Button(win,command=lambda:clkbtn(0),cursor="hand2",text="0",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btn0.place(x=113,y=290)
#num=
btne=Button(win,command=resbtn,cursor="hand2",text="=",padx=10,pady=2,width=4,height=2,font=("times",12,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btne.place(x=190,y=290)
#num-
btnmi=Button(win,command=lambda:clkbtn("-"),cursor="hand2",text="-",padx=10,pady=2,width=1,height=2,font=("times",13,"bold"),activebackground="#c1bebe",relief=FLAT,background="#716f6f",fg="black")
btnmi.place(x=270,y=290)
#----------end window
win.mainloop()
