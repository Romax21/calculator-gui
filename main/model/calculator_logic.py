from main.utils import constants

def format_result(result) -> str: 
    num = float(result)
    
    #limit upto 10 digits after decimal to remove floating noise
    formatted = f"{num:.10f}"
    
    # remove trailing zeroes and unnecessary decimal point
    formatted = formatted.rstrip('0').rstrip('.')
    
    if formatted == "-0" : 
        formatted = "0"
    
    return formatted

def verifyNumber(number) : 
    # Rules - Number can be empty or negative
    # Number cannot contains space
    # Number cannot contain more than one decimal
    # Other than decimal, it should only have numbers
    # Number cannot be just '.'
    
    if not number or number == "-" : return
    if number[0] == '-' : 
        number = number[1:]
    
    if number == '.' : raise ValueError(constants.JUST_A_DECIMAL_ERROR)
    
    if ' ' in number : 
        raise ValueError(constants.NUMBER_SPACE_ERROR)
    
    decimal = False
    for c in number : 
        if '0' <= c <= '9' : continue
        if c == '.' : 
            if decimal : raise ValueError(constants.MULTIPLE_DECIMALS_ERROR)
            decimal = True
        else : 
            raise ValueError(constants.INVALID_INPUT_ERROR)

def verifyOperator(oper) : 
    # Operator can be empty
    # Operator can only be +,-,*,/ or %
    
    if not oper : return
    if len(oper) > 1 : raise ValueError(constants.MULTIPLE_OPERATOR_ERROR)
    
    if oper not in '+-*/%' : raise ValueError(constants.INVALID_INPUT_ERROR)

def verifyInputs(opA,oper,opB) : 
    verifyNumber(opA)
    verifyOperator(oper)
    verifyNumber(opB)

def calculate_expression(opA,oper,opB) -> str : 
    
    verifyInputs(opA,oper,opB)
    
    #if opA is empty or opA == "-", just return it
    if not opA or opA == "-" : return ""
    
    # if oper is empty or opB is empty or opB is just negative, we need to return opA
    if not oper or not opB or opB == "-" : 
        result = format_result(opA)
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
            result = firstNumber/secondNumber
        case '%' : 
            result = firstNumber % secondNumber
            if abs(result) < 1e-10 : 
                result = 0.0
            if abs(result - abs(secondNumber)) < 1e-10 : 
                result = 0.0
    result = format_result(str(result))
    return result