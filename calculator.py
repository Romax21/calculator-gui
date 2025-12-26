import tkinter as tk

def add_number(number) : 
    currValue = input_field.get()
    input_field.set(currValue + number)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator GUI")

input_field = tk.StringVar()
inputEntry = tk.Entry(root,width=40,textvariable=input_field,justify='right',font=('arial',20),state='readonly')
input_field.set("")

inputEntry.pack(padx=10,pady=(20,10),fill='x')

output_field = tk.StringVar()
outputEntry = tk.Entry(root,width=40,textvariable=output_field,justify='right',font=('arial',20),state='readonly')
output_field.set("333")

outputEntry.pack(padx=10,pady=10,fill='x')

buttonFrame = tk.Frame(root,bg='lightgrey')

button1 = tk.Button(buttonFrame,text='1',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('1'))
button1.grid(row=0,column=0,sticky='nsew')
button2 = tk.Button(buttonFrame,text='2',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('2'))
button2.grid(row=0,column=1,sticky='nsew')
button3 = tk.Button(buttonFrame,text='3',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('3'))
button3.grid(row=0,column=2,sticky='nsew')
button4 = tk.Button(buttonFrame,text='4',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('4'))
button4.grid(row=1,column=0,sticky='nsew')
button5 = tk.Button(buttonFrame,text='5',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('5'))
button5.grid(row=1,column=1,sticky='nsew')
button6 = tk.Button(buttonFrame,text='6',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('6'))
button6.grid(row=1,column=2,sticky='nsew')
button7 = tk.Button(buttonFrame,text='7',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('7'))
button7.grid(row=2,column=0,sticky='nsew')
button8 = tk.Button(buttonFrame,text='8',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('8'))
button8.grid(row=2,column=1,sticky='nsew')
button9 = tk.Button(buttonFrame,text='9',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('9'))
button9.grid(row=2,column=2,sticky='nsew')
button00 = tk.Button(buttonFrame,text='00',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('00'))
button00.grid(row=3,column=0,sticky='nsew')
button0 = tk.Button(buttonFrame,text='0',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('0'))
button0.grid(row=3,column=1,sticky='nsew')
buttonEq = tk.Button(buttonFrame,text='=',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('='))
buttonEq.grid(row=3,column=2,sticky='nsew')
buttonPlus = tk.Button(buttonFrame,text='+',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('+'))
buttonPlus.grid(row=0,column=3,sticky='nsew')
buttonMinus = tk.Button(buttonFrame,text='-',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('-'))
buttonMinus.grid(row=1,column=3,sticky='nsew')
buttonMulti = tk.Button(buttonFrame,text='*',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('*'))
buttonMulti.grid(row=2,column=3,sticky='nsew')
buttonDiv = tk.Button(buttonFrame,text='/',font=('arial',20),bd=0,bg='white',fg='black',command=lambda:add_number('/'))
buttonDiv.grid(row=3,column=3,sticky='nsew')

buttonFrame.pack(padx=10,pady=10,fill='both')

for i in range(4) : 
    buttonFrame.columnconfigure(i,weight=1)
    buttonFrame.rowconfigure(i,weight=1)

root.mainloop()