from model import calculator_logic
class calculator_engine : 
    def __init__(self):
        self.opA = ""
        self.opB = ""
        self.oper = ""
        self.justEvaluated = False
    
    def inputResult(self) -> str : 
        return (self.opA + self.oper + self.opB)
    
    def addNumber(self,number) -> str : 
        # new calculation
        if self.justEvaluated : 
            self.justEvaluated = False
            self.opA = number
            return self.inputResult()
        
        # if oper is empty, we will add the number to operand A
        if not self.oper : 
            if self.opA == "0" or self.opA == "-0" : 
                self.opA = self.opA[:-1]
            self.opA = self.opA + number
            return self.inputResult()
        
        # oper is not empty, we will add the number to operand B
        if self.opB == "0" or self.opB == "-0" : 
            self.opB = self.opB[:-1]
        self.opB = self.opB + number
        return self.inputResult()
    
    def addDecimal(self) -> str : 
        # continuing previous calculation
        if self.justEvaluated : 
            self.justEvaluated = False
            if '.' not in self.opA : 
                self.opA = self.opA + "."
            return self.inputResult()
        
        # if operator is empty, we will add the decimal in opA
        if not self.oper : 
            # check if the decimal is present or not
            if '.' not in self.opA : 
                if not self.opA or self.opA == "-": 
                    self.opA = self.opA + "0"
                self.opA = self.opA + "."
            return self.inputResult()
        
        # otherwise, we will add it in opB
        if '.' not in self.opB : 
            if not self.opB or self.opB == "-" : 
                self.opB = self.opB + "0"
            self.opB = self.opB + "."
        return self.inputResult()
    
    def addMinus(self) -> str : 
        # continuing previous calculation
        if self.justEvaluated : 
            self.oper = "-"
            return self.inputResult()
        
        # if opA is empty or opA is "-", opA will remain "-"
        if not self.opA or self.opA == "-": 
            self.opA = "-"
            return self.inputResult()
        
        # if oper is empty or oper is "+" or "-", we will set it to -
        if not self.oper or self.oper == "+" or self.oper == "-" : 
            self.oper = "-"
            return self.inputResult()
        
        # if opB is empty, it will be set to "-"
        if not self.opB : 
            self.opB = "-"
        return self.inputResult()
    
    def addOperator(self,op) -> str : 
        if op == "-" : 
            return self.addMinus()
        
        # continuing previous calcuation
        if self.justEvaluated : 
            self.oper = op
            return self.inputResult()
        
        # if opA is empty or "-", we will do nothing
        if not self.opA or self.opA == "-" : 
            return self.inputResult()
        
        # if oper is empty, set it to op
        # if opB is empty, we will change oper
        if not self.oper or not self.opB: 
            self.oper = op
        return self.inputResult()
    
    def resetScreen(self) : 
        self.opA = ""
        self.opB = ""
        self.oper = ""
        self.justEvaluated = False
        return (self.inputResult(),"")
    
    def backspace(self) -> str : 
        if self.opB : 
            self.opB = self.opB[:-1]
            return self.inputResult()
        
        if self.oper : 
            self.oper = ""
            return self.inputResult()
        
        if self.opA : 
            self.opA = self.opA[:-1]
        
        return self.inputResult()
    
    def equalCalled(self) : 
        result = calculator_logic.calculate_expresion(self.inputResult())
        if result != calculator_logic.ZERO_DIVISION_MESSAGE : 
            self.justEvaluated = True
        else : 
            self.justEvaluated = False
        
        self.opA = ""
        self.opB = ""
        self.oper = ""
        return (self.inputResult(),result)