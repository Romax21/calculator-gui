import pytest
from main.model.calculator_engine import calculator_engine
from main.utils.constants import ZERO_DIVISION_MESSAGE

@pytest.fixture
def engine_object() : 
    return calculator_engine()

def test_expression1(engine_object) : 
    assert engine_object.addNumber('0') == "0"
    assert engine_object.addNumber('2') == "2"
    assert engine_object.addNumber('3') == "23"
    assert engine_object.addOperator('+') == "23+"
    assert engine_object.addDecimal() == "23+0."
    assert engine_object.addNumber('9') == "23+0.9"
    
    expression,result = engine_object.equalCalled()
    assert expression == ""
    assert result == "23.9"

def test_expression2(engine_object) : 
    engine_object.addOperator('-')
    engine_object.addNumber('2')
    engine_object.addNumber('5')
    engine_object.addOperator('*')
    engine_object.addOperator('-')
    engine_object.addNumber('2')
    engine_object.addNumber('5')
    
    assert engine_object.inputResult() == "-25*-25"
    
    ex,result = engine_object.equalCalled()
    assert ex == ""
    assert result == "625"

def test_expression3(engine_object) : 
    engine_object.addOperator('-')
    engine_object.addNumber('2')
    engine_object.addNumber('5')
    
    ex,result = engine_object.reciprocal()
    assert ex == ""
    assert result == "-0.04"