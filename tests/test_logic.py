import pytest
from model.calculator_logic import calculate_expresion
from utils.constants import ZERO_DIVISION_MESSAGE

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("2+3","5"),
        ("7-4","3"),
        ("6*5","30"),
        ("8/2","4"),
        ("4.2%3","1.2")
    ]
)
def test_basicOperations(expression,expected) : 
    result = calculate_expresion(expression)
    assert result == expected

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("2.5+1.5","4"),
        ("5.5-2.2","3.3"),
        ("3.2*2","6.4"),
        ("7.5/2.5","3"),
        ("0.1+0.2","0.3")
    ]
)
def test_decimalOperations(expression,expected) : 
    result = calculate_expresion(expression)
    assert result == expected

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("1/0",ZERO_DIVISION_MESSAGE),
        ("23%0",ZERO_DIVISION_MESSAGE)
    ]
)
def test_zeroDivision(expression,expected) : 
    result = calculate_expresion(expression)
    assert result == expected