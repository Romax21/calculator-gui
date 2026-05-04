from utils.constants import ZERO_DIVISION_MESSAGE

def format_result(result) -> str: 
    num = float(result)
    
    #limit upto 10 digits after decimal to remove floating noise
    formatted = f"{num:.10f}"
    
    # remove trailing zeroes and unnecessary decimal point
    formatted = formatted.rstrip('0').rstrip('.')
    
    return formatted

def calculate_expresion(expression) -> str : 
    # if the expression is empty
    if not expression : return ""
    
    negative = False
    # remove the negative but store it
    if(expression[0] == '-') : 
        negative = True
        expression = expression[1:]
    
    # if expression is empty
    if not expression : return ""
    
    # if the last char is decimal, just remove it
    if expression[len(expression)-1] == '.' : 
        expression = expression[:-1]
    result = 0.0
    operator = '$'
    index = 0
    
    for op in "*/%+-" : 
        if op in expression : 
            operator = op
            index = expression.find(op)
            break
    
    # it implies there is no operator
    if operator == '$' : 
        # if the number was negative and not zero, add the negative
        if negative and expression != "0" : 
            expression = '-' + expression
        return format_result(expression)
    
    firstNumber = float(format_result(expression[:index]))
    if(negative) : firstNumber *= -1
    
    s = expression[index+1:]
    # all these cases, there is no second number, so just return the second number
    if not s : return format_result(str(firstNumber))
    if len(s) == 1 and s[0] == '-' : return format_result(str(firstNumber))
    
    secondNumber = float(format_result(expression[index+1:]))
    
    match operator : 
        case '+' : 
            result = firstNumber + secondNumber
        case '-' : 
            result = firstNumber - secondNumber
        case '*' : 
            result = firstNumber * secondNumber
        case '/' : 
            if secondNumber == 0 : 
                return ZERO_DIVISION_MESSAGE
            result = firstNumber/secondNumber
        case '%' : 
            if secondNumber == 0 :
                return ZERO_DIVISION_MESSAGE
            result = firstNumber % secondNumber
            if abs(result) < 1e-10 : 
                result = 0.0
            if abs(result - abs(secondNumber)) < 1e-10 : 
                result = 0.0
        case _: 
            result = None
    result = format_result(str(result))
    
    if result == '-0' : 
        result = '0'
    return result