import pytest
from main.model.calculator_logic import calculate_expression
from main.utils.constants import ZERO_DIVISION_MESSAGE

@pytest.mark.parametrize(
    "opA,oper,opB,expected",
    [
        ("2","+","3","5"),
        ("7","-","4","3"),
        ("6","*","5","30"),
        ("8","/","2","4"),
        ("4.2","%","3","1.2")
    ]
)
def test_basicOperations(opA,oper,opB,expected) : 
    result = calculate_expression(opA,oper,opB)
    assert result == expected

@pytest.mark.parametrize(
    "opA,oper,opB,expected",
    [
        ("2.5","+","1.5","4"),
        ("5.5","-","2.2","3.3"),
        ("3.2","*","2","6.4"),
        ("7.5","/","2.5","3"),
        ("0.1","+","0.2","0.3")
    ]
)
def test_decimalOperations(opA,oper,opB,expected) : 
    result = calculate_expression(opA,oper,opB)
    assert result == expected

@pytest.mark.parametrize(
    "opA,oper,opB,expected",
    [
        ("1","/","0",ZERO_DIVISION_MESSAGE),
        ("23","%","0",ZERO_DIVISION_MESSAGE)
    ]
)
def test_zeroDivision(opA,oper,opB,expected) : 
    result = calculate_expression(opA,oper,opB)
    assert result == expected
    
@pytest.mark.parametrize(
    "opA,oper,opB,expected",
    [
        (".","","","The first character is a decimal"),
        ("12","+",".23","The first character is a decimal"),
        (" 12 ","+","45","Number contains space, it should not contain space!"),
        ("12a","","","The input is invalid"),
        ("12","-","8.9..","The input contains multiple decimals"),
        ("12","23","","Operator is invalid"),
        ("12","+-","","Operator must be just one letter"),
        ("","+","","The equation is not possible"),
        ("","","2","The equation is not possible"),
        ("12","","12","The equation is not possible")
    ]
)
def test_inputException(opA,oper,opB,expected) : 
    with pytest.raises(ValueError) as exc : 
        calculate_expression(opA,oper,opB)
    assert str(exc.value) == expected