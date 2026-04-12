from model import calculator_engine
class calculator_controller : 
    def __init__(self):
        self.expression = ""
        self.result = ""
        self.ce = calculator_engine.calculator_engine()
    
    def buttonPressed(self,text) : 
        self.expression = ""
        self.result = ""
        if text in '1234567890': 
            self.expression = self.ce.addNumber(text)
        elif text == '.' : 
            self.expression = self.ce.addDecimal()
        elif text in '+-*/%' : 
            self.expression = self.ce.addOperator(text)
        elif text == '1/x' : 
            self.result = self.ce.reciprocal(text)
        elif text == 'x^2' : 
            self.result = self.ce.square(text)
        elif text == '<=' : 
            self.expression = self.ce.backspace()
        elif text == '=' : 
            self.result = self.ce.equalCalled()
        
        return (self.expression,self.result)