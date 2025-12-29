import tkinter as tk

def add_zero() : 
    curr = input_field.get()
    # when curr is empty, add the zero
    if not curr : 
        input_field.set(curr + '0')
        return
    l = len(curr)
    # when the last digit is a non zero number, add the zero
    if curr[l-1] in '123456789' : 
        input_field.set(curr + '0')
        return
    # when the last digit is one of these operator, "324+" -> "324+0"
    if curr[l-1] in '+*/' : 
        input_field.set(curr + '0')
        return
    # when l is 1 and the char is '-'
    if curr[l-1] == '-' : 
        # when it is just "-", 0 will consume it since -0 is 0
        if l == 1 : input_field.set('0')
        # otherwise it is something like "398-" -> "398-0"
        else : input_field.set(curr + '0')
        return
    # when the last char is zero
    if curr[l-1] == '0' : 
        if l == 1 : return
        # something like "123-0"
        if curr[l-2] in '+-*/' : return
        input_field.set(curr + '0')

def add_doubleZero() : 
    curr = input_field.get()
    # when curr is empty
    if not curr : 
        input_field.set(curr + '0')
        return
    l = len(curr)
    # when the last digit is a non zero number
    if curr[l-1] in '123456789' : 
        input_field.set(curr + '00')
        return
    # when the last digit is one of these operator
    if curr[l-1] in '+*/' : 
        input_field.set(curr + '0')
        return
    # when l is 1 and the char is '-'
    if curr[l-1] == '-' : 
        # when it is just "-", 0 will consume it since -0 is 0
        if l == 1 : input_field.set('0')
        # otherwise it is something like "398-" -> "398-0"
        else : input_field.set(curr + '0')
        return
    # when the last char is zero
    if curr[l-1] == '0' : 
        # curr is "0"
        if l == 1 : return
        
        # something like "123-0"
        if curr[l-2] in '+-*/' : return
        input_field.set(curr + '00')

def add_number(number) : 
    # let's say number is '1'
    curr = input_field.get()
    if not curr : 
        input_field.set(number)
        return
    l = len(curr)
    if curr[l-1] == '0' : 
        # if curr = "0", curr -> "1"
        if l == 1 : 
            input_field.set(number)
            return
        # if curr is "143*0", it will "143*1"
        if curr[l-2] in '+-*/' : 
            input_field.set(curr[0:l-1] + number)
            return
    
    input_field.set(curr + number)

def add_operator(op) : 
    curr = input_field.get()
def equalCalled() : 
    curr = input_field.get()

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator GUI")

input_field = tk.StringVar()
inputEntry = tk.Entry(root,width=40,textvariable=input_field,justify='right',font=('arial',20),state='readonly')
input_field.set("")
inputEntry.pack(padx=10,pady=(20,10),fill='x')

output_field = tk.StringVar()
outputEntry = tk.Entry(root,width=40,textvariable=output_field,justify='right',font=('arial',20),state='readonly')
output_field.set("")
outputEntry.pack(padx=10,pady=10,fill='x')

buttonFrame = tk.Frame(root,bg='lightgrey')

buttons = []
button_defs = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('00', 3, 0), ('0', 3, 1), ('=', 3, 2), ('/', 3, 3)
]

btn_style = {'font':('arial',20), 'bd':2, 'relief':'raised', 'bg':'white', 'fg':'black'}

for (text,row,col) in button_defs : 
    if text == '0' : 
        btn = tk.Button(buttonFrame,text=text,command=lambda:add_zero(),**btn_style)
    elif text == '00' : 
        btn = tk.Button(buttonFrame,text=text,command=lambda:add_doubleZero(),**btn_style)
    elif text >= '1' and text <= '9' : 
        btn = tk.Button(buttonFrame,text=text,command=lambda t=text:add_number(t),**btn_style)
    elif text in "+-*/" : 
        btn = tk.Button(buttonFrame,text=text,command=lambda t=text:add_operator(t),**btn_style)
    else : 
        btn = tk.Button(buttonFrame,text=text,command=lambda : equalCalled(),**btn_style)
    btn.grid(row=row,column=col,sticky='nsew')
    buttons.append(btn)


for i in range(4) : 
    buttonFrame.columnconfigure(i,weight=1)
    buttonFrame.rowconfigure(i,weight=1)
buttonFrame.pack(padx=10,pady=10,fill='both',expand=True)

root.mainloop()