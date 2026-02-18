class calculator_engine : 
    def __init__(self):
        self.opA = ""
        self.opB = ""
        self.oper = ""
        self.justEvaluated = False
    
    def inputResult(self) -> str : 
        return (self.opA + self.oper + self.opB)
    
    def addZero(self) -> str : 
        if self.justEvaluated : 
            self.justEvaluated = False
            self.opA = "0"
            return self.inputResult()
        
        # if oper is empty
        if not self.oper : 
            if self.opA == "0" or self.opA == "-0" : 
                return self.inputResult()
            self.opA = self.opA + '0'
            return self.inputResult()
        
        # oper is not empty
        if self.opB == "0" or self.opB == "-0" : 
            return self.inputResult()
        self.opB = self.opB + '0'
        return self.inputResult()
        