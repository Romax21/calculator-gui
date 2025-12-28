def calculate_expresion(expression) : 
    negative = False
    if(expression[0] == '-') : 
        negative = True
        expression = expression[1:]
    
    result = 0
    operator = '.'
    index = 0
    
    for op in "+-*/" : 
        if op in expression : 
            operator = op
            index = expression.find(op)
            break
    
    firstNumber = int(expression[:index])
    if(negative) : firstNumber *= -1
    print(firstNumber)
    
    secondNumber = int(expression[index+1:])
    print(secondNumber)
    
    match operator : 
        case '+' : 
            result = firstNumber + secondNumber
        case '-' : 
            result = firstNumber - secondNumber
        case '*' : 
            result = firstNumber * secondNumber
        case '/' : 
            result = firstNumber//secondNumber
        case _: 
            result = None
    
    return str(result)

print(calculate_expresion("123+568"))
print(calculate_expresion("1111/5"))