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

for (text,row,col) in button_defs : 
    btn = tk.Button(buttonFrame,text=text,font=('arial',20),bd=2,relief='raised',bg='white',fg='black',command=lambda t=text:add_number(t))
    btn.grid(row=row,column=col,sticky='nsew')
    buttons.append(btn)


for i in range(4) : 
    buttonFrame.columnconfigure(i,weight=1)
    buttonFrame.rowconfigure(i,weight=1)
buttonFrame.pack(padx=10,pady=10,fill='both',expand=True)

root.mainloop()