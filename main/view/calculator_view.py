import tkinter as tk
# from main.model.calculator_engine import calculator_engine
# from controller.calculator_controller import calculator_controller

class CalculatorView : 
    def __init__(self,controller) : 
        self.controller = controller
        self.root = tk.Tk()
        self.root.geometry("400x600")
        self.root.title("Calculator GUI")
        
        self.input_field = tk.StringVar()
        self.inputEntry = tk.Entry(self.root,width=40,textvariable=self.input_field,justify='right',font=('arial',20),state='readonly')
        self.input_field.set("")
        self.inputEntry.pack(padx=10,pady=(20,10),fill='x')
        
        self.output_field = tk.StringVar()
        self.outputEntry = tk.Entry(self.root,width=40,textvariable=self.output_field,justify='right',font=('arial',20),state='readonly')
        self.output_field.set("")
        self.outputEntry.pack(padx=10,pady=10,fill='x')
        
        self.btn_style = {'font':('arial',20), 'bd':2, 'relief':'raised', 'bg':'white', 'fg':'black'}
        
        self.resetBtn = tk.Button(self.root,text = 'Reset',command=lambda t='Reset':self.buttonPressed(t), **self.btn_style)
        
        self.resetBtn.pack(padx = 10,pady=5,fill = 'x')

        self.buttonFrame = tk.Frame(self.root,bg='lightgrey')
        self.buttons = []
        self.button_defs = [
            ('%', 0, 0), ('1/x', 0, 1), ('x^2', 0, 2), ('<=', 0, 3),
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
        ]
        
        for (text,row,col) in self.button_defs : 
            self.btn = tk.Button(self.buttonFrame,text=text,command=lambda t=text:self.buttonPressed(t),**self.btn_style)
            self.btn.grid(row=row,column=col,sticky='nsew')
            self.buttons.append(self.btn)

        for i in range(4) : 
            self.buttonFrame.columnconfigure(i,weight=1)
        for i in range(5) : 
            self.buttonFrame.rowconfigure(i,weight=1)

        self.buttonFrame.pack(padx=10,pady=10,fill='both',expand=True)

    def buttonPressed(self,text) : 
        expression,result = self.controller.buttonPressed(text)
        self.input_field.set(expression)
        self.output_field.set(result)
        return
    
    def run(self) : 
        self.root.mainloop()