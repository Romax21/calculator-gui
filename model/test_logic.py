import pytest
from model.calculator_logic import calculate_expresion

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("2+3","5"),
        ("7-4","3"),
        ("6*5","30"),
        ("8/2","4")
    ]
)
def test_basicOperations(expression,expected) : 
    result = calculate_expresion(expression)
    assert result == expected