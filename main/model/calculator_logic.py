from main.utils.constants import ZERO_DIVISION_MESSAGE

def format_result(result) -> str: 
    num = float(result)
    
    #limit upto 10 digits after decimal to remove floating noise
    formatted = f"{num:.10f}"
    
    # remove trailing zeroes and unnecessary decimal point
    formatted = formatted.rstrip('0').rstrip('.')
    
    if formatted == "-0" : 
        formatted = "0"
    
    return formatted

def calculate_expression(opA,oper,opB) -> str : 
    #if opA is empty or opA == "-", just return it
    if not opA or opA == "-" : return ""
    
    # if oper is empty or opB is empty or opB is just negative, we need to return opA
    if not oper or not opB or opB == "-" : 
        result = format_result(opA)
        if result == "-0" : result = "0"
        return result
    
    result = 0.0
    
    firstNumber = float(format_result(opA))
    secondNumber = float(format_result(opB))
    
    match oper : 
        case '+' : 
            result = firstNumber + secondNumber
        case '-' : 
            result = firstNumber - secondNumber
        case '*' : 
            result = firstNumber * secondNumber
        case '/' : 
            if secondNumber == 0.0 : 
                return ZERO_DIVISION_MESSAGE
            result = firstNumber/secondNumber
        case '%' : 
            if secondNumber == 0.0 : 
                return ZERO_DIVISION_MESSAGE
            result = firstNumber % secondNumber
            if abs(result) < 1e-10 : 
                result = 0.0
            if abs(result - abs(secondNumber)) < 1e-10 : 
                result = 0.0
        case _: 
            result = None
    result = format_result(str(result))
    return result