def calculate_expresion(expression) : 
    negative = False
    # remove the negative but store it
    if(expression[0] == '-') : 
        negative = True
        expression = expression[1:]
    
    # if expression is empty
    if not expression : return
    result = 0
    operator = '$'
    index = 0
    
    for op in "*/+-" : 
        if op in expression : 
            operator = op
            index = expression.find(op)
            break
    
    # it implies there is no operator
    if operator == '$' : 
        # if the number was negative, add the negative
        if negative : 
            expression = '-' + expression
        return expression
    
    firstNumber = int(expression[:index])
    if(negative) : firstNumber *= -1
    
    s = expression[index+1:]
    if not s : return firstNumber
    if len(s) == 1 and s[0] in '*/+-' : return firstNumber
    if len(s) == 2 and s[0] in '*/+-' and s[1] == '-' : return firstNumber
    
    secondNumber = int(expression[index+1:])
    
    match operator : 
        case '+' : 
            result = firstNumber + secondNumber
        case '-' : 
            result = firstNumber - secondNumber
        case '*' : 
            result = firstNumber * secondNumber
        case '/' : 
            if secondNumber == 0 : 
                return "ZeroDivision"
            result = firstNumber//secondNumber
        case _: 
            result = None
    
    return str(result)

print(calculate_expresion("-66"))