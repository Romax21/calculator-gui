# from model.calculator_engine import calculator_engine
class calculator_controller : 
    def __init__(self,engine):
        self.expression = ""
        self.result = ""
        self.engine = engine
    
    def buttonPressed(self,text) : 
        self.expression = ""
        self.result = ""
        if text in '1234567890': 
            self.expression = self.engine.addNumber(text)
        elif text == '.' : 
            self.expression = self.engine.addDecimal()
        elif text in '+-*/%' : 
            self.expression = self.engine.addOperator(text)
        elif text == '1/x' : 
            self.result = self.engine.reciprocal(text)
        elif text == 'x^2' : 
            self.result = self.engine.square(text)
        elif text == '<=' : 
            self.expression = self.engine.backspace()
        elif text == '=' : 
            self.result = self.engine.equalCalled()
        
        return (self.expression,self.result)