'''General Calculator'''

from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ''
    text_Input.set('')

def btnEquals():
    global operator
    result = str(eval(operator))
    text_Input.set(result)
    operator = ''
    

cal = Tk()
cal.title('General Calculator')


operator = ''
text_Input = StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30,
                   insertwidth=3,bg='violet',justify='right').grid(columnspan=4)

#Now we will create the buttons
#Creating first row buttons
button7 = Button(cal,text='7',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(7))
button7.grid(row=1,column=0)

button8 = Button(cal,text='8',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(8))
button8.grid(row=1,column=1)

button9 = Button(cal,text='9',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(9))
button9.grid(row=1,column=2)

buttonAdd = Button(cal,text='+',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick('+'))
buttonAdd.grid(row=1,column=3)

#Creating second row buttons
button4 = Button(cal,text='4',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(4))
button4.grid(row=2,column=0)

button5 = Button(cal,text='5',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(5))
button5.grid(row=2,column=1)

button6 = Button(cal,text='6',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(6))
button6.grid(row=2,column=2)

buttonSub = Button(cal,text='-',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick('-'))
buttonSub.grid(row=2,column=3)

#Creating third row buttons
button1 = Button(cal,text='1',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(1))
button1.grid(row=3,column=0)

button2 = Button(cal,text='2',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(2))
button2.grid(row=3,column=1)

button3 = Button(cal,text='3',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(3))
button3.grid(row=3,column=2)

buttonMul = Button(cal,text='*',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick('*'))
buttonMul.grid(row=3,column=3)

#Creating fourth row buttons
button0 = Button(cal,text='0',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick(0))
button0.grid(row=4,column=0)

buttonClr = Button(cal,text='C',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=btnClear)
buttonClr.grid(row=4,column=1)

buttonEqu = Button(cal,text='=',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=btnEquals)
buttonEqu.grid(row=4,column=2)

buttonDiv = Button(cal,text='/',padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
                 command=lambda:btnClick('/'))
buttonDiv.grid(row=4,column=3)





cal.mainloop()
