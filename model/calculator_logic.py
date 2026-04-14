from utils.constants import ZERO_DIVISION_MESSAGE

def removeTrailingZeroes(expression) : 
    if '.' not in expression : return expression
    index = len(expression)-1
    while index >= 0 and expression[index] == '0' : 
        index -= 1
    if expression[index] != '.' : return expression[:index+1]
    return expression[:index]

def calculate_expresion(expression) : 
    # if the expression is empty
    if not expression : return
    
    negative = False
    # remove the negative but store it
    if(expression[0] == '-') : 
        negative = True
        expression = expression[1:]
    
    # if expression is empty
    if not expression : return
    
    # if the last char is decimal, just remove it
    if expression[len(expression)-1] == '.' : 
        expression = expression[:-1]
    result = 0.0
    operator = '$'
    index = 0
    
    for op in "*/+-%" : 
        if op in expression : 
            operator = op
            index = expression.find(op)
            break
    
    # it implies there is no operator
    if operator == '$' : 
        # if the number was negative, add the negative
        if negative : 
            expression = '-' + expression
        return removeTrailingZeroes(expression)
    
    firstNumber = float(removeTrailingZeroes(expression[:index]))
    if(negative) : firstNumber *= -1
    
    s = expression[index+1:]
    # all these cases, there is no second number, so just return the second number
    if not s : return removeTrailingZeroes(str(firstNumber))
    if len(s) == 1 and s[0] == '-' : return removeTrailingZeroes(str(firstNumber))
    
    secondNumber = float(removeTrailingZeroes(expression[index+1:]))
    
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
            result = (firstNumber/secondNumber) * 100
        case _: 
            result = None
    result = removeTrailingZeroes(str(result))
    
    if result == '-0' : 
        result = '0'
    return result