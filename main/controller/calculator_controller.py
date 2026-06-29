from main.utils import constants

class CalculatorController : 
    def __init__(self,engine):
        self.expression = ""
        self.result = ""
        self.engine = engine
    
    def buttonPressed(self,text) : 
        self.expression = ""
        self.result = ""
        try : 
            if not text : 
                raise ValueError(constants.INPUT_EMPTY_ERROR)
            elif text.isdigit() : 
                self.expression = self.engine.addNumber(text)
            elif text == '.' : 
                self.expression = self.engine.addDecimal()
            elif text in '+-*/%' : 
                self.expression = self.engine.addOperator(text)
            elif text == '1/x' : 
                self.expression,self.result = self.engine.reciprocal()
            elif text == 'x^2' : 
                self.expression,self.result = self.engine.square()
            elif text == '<=' : 
                self.expression = self.engine.backspace()
            elif text == '=' : 
                self.expression,self.result = self.engine.equalCalled()
            elif text == 'Reset' : 
                self.engine.resetScreen()
            else : 
                raise ValueError(constants.INVALID_INPUT_ERROR)
        except (ValueError,ZeroDivisionError) as e : 
            self.engine.resetScreen()
            self.result = str(e)
        return (self.expression,self.result)