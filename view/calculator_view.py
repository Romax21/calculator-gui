import tkinter as tk
from controller import calculator_controller

cc = calculator_controller.calculator_controller()

def buttonPressed(text) : 
    expression,result = cc.buttonPressed(text)
    input_field.set(expression)
    output_field.set(result)
    return

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

resetBtn = tk.Button(root,text = 'Reset',command=lambda t='Reset':buttonPressed(t), **btn_style)
resetBtn.pack(padx = 10,pady=5,fill = 'x')

buttonFrame = tk.Frame(root,bg='lightgrey')
buttons = []
button_defs = [
    ('%', 0, 0), ('1/x', 0, 1), ('x^2', 0, 2), ('<=', 0, 3),
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text,row,col) in button_defs : 
    btn = tk.Button(buttonFrame,text=text,command=lambda t=text:buttonPressed(t),**btn_style)
    btn.grid(row=row,column=col,sticky='nsew')
    buttons.append(btn)


for i in range(4) : 
    buttonFrame.columnconfigure(i,weight=1)
for i in range(5) : 
    buttonFrame.rowconfigure(i,weight=1)

buttonFrame.pack(padx=10,pady=10,fill='both',expand=True)

root.mainloop()