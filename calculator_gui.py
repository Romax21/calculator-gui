import tkinter as tk
from calculator_logic import calculate_expresion

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

def op_index() : 
    curr = input_field.get()
    index = 0
    if curr[0] == '-' : index += 1
    
    l = len(curr)
    while index < l : 
        if curr[index] in '+-*/' : 
            return index
        index += 1
    return -1

def add_plus() : 
    curr = input_field.get()
    # if curr is empty, no need to add anything
    if not curr : 
        return
    l = len(curr)
    if l == 1 : 
        # if curr is only '-', it will changed to nothing
        # basically, user changed from writing a negative number to a positive number
        if curr[0] == '-' : 
            input_field.set('')
            return
        # if curr is then like '9' -> '9+'
        input_field.set(curr + '+')
        return
    
    index = op_index()
    # there is no operator so curr is like - '-34' or '342'
    if index == -1 : 
        input_field.set(curr + '+')
        return
    
    # if operator is at last index, so curr - '-786*' or '-4589-'
    if index == l-1 : 
        # we will change the op
        input_field.set(curr[:-1] + '+')
        return
    # cases like '456*-' or 'cases like 2334/-'
    if index == l-2 : 
        # we will just remove the minus
        input_field.set(curr[:-1])
        return
    # if index < l-2 -> there already a operator before, we won't add anything new
    return

def add_minus() : 
    curr = input_field.get()
    # if curr is empty, just append the minus
    if not curr : 
        input_field.set('-')
        return
    l = len(curr)
    if l == 1 : 
        # if curr is only '-', it will stay the same
        if curr[0] == '-' : return
        # if curr is then like '9' -> '9-'
        input_field.set(curr + '-')
        return
    
    index = op_index()
    # there is no operator so curr is like - '-34' or '342'
    if index == -1 : 
        input_field.set(curr + '-')
        return
    
    # if operator is at last index, so curr - '-786*' or '-4589-'
    if index == l-1 : 
        if curr[index] in '*/' : 
            # going from '-123*' to '-123*-'
            input_field.set(curr + '-')
            return
        if curr[index] == '+' : 
            # we will change the positive to negative : 
            input_field.set(curr[:-1] + '-')
            return
        # since -- is +, we will remove the minus and changed it to plus
        input_field.set(curr[:-1] + '+')
        return
    
    # cases like '456*-' or 'cases like 2334/-'
    # if index == l-2 : 
        # things will stay the same
        return
    # if index < l-2 -> there already a operator before, we won't add anything new
    return

def add_operator(op) : 
    if op == '+' : 
        add_plus()
        return
    if op == '-' : 
        add_minus()
        return
    
    # remaining op are * and /
    curr = input_field.get()
    # if curr is empty no need to add anything
    if not curr : return
    
    # starting of the negative number
    l = len(curr)
    if l == 1 and curr[0] == '-' : return
    
    index = op_index()
    if index == -1 : 
        # add the operator since there is none right now
        input_field.set(curr + op)
        return
    if index == l-1 : 
        # since the op is at last place, change it to current op
        input_field.set(curr[:-1] + op)
        return
    if index == l-2 : 
        # it is the case of curr being "123*-" or "123/-" : 
        # we will remove the last two operators and add the curr one
        input_field.set(curr[:-2] + op)
        return
    # if index < l-2, operator is already here, we will not add it.
    return

def equalCalled() : 
    expression = input_field.get()
    out = calculate_expresion(expression)
    
    # if output is empty, do nothing
    if not out : return
    # for division by zero
    if out == "ZeroDivision" : 
        output_field.set("Division by zero is not possible !!!")
        input_field.set('')
        return
    # else just set the output field
    output_field.set(out)
    return

def resetScreen() : 
    input_field.set('')
    output_field.set('')

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

btn_style = {'font':('arial',20), 'bd':2, 'relief':'raised', 'bg':'white', 'fg':'black'}

resetBtn = tk.Button(root,text = 'Reset',command = resetScreen(), **btn_style)
resetBtn.pack(padx = 10,pady=5,fill = 'x')
buttonFrame = tk.Frame(root,bg='lightgrey')

buttons = []
button_defs = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('00', 3, 0), ('0', 3, 1), ('=', 3, 2), ('/', 3, 3)
]

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