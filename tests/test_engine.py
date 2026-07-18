import pytest
from main.model.calculator_engine import CalculatorEngine
import main.utils.constants as const

@pytest.fixture
def engine_object() : 
    return CalculatorEngine()

def test_expression(engine_object) : 
    assert engine_object.addNumber('0') == "0"
    assert engine_object.addNumber('2') == "2"
    assert engine_object.addNumber('3') == "23"
    assert engine_object.addOperator('+') == "23+"
    assert engine_object.addDecimal() == "23+0."
    assert engine_object.addNumber('9') == "23+0.9"
    
    expression,result = engine_object.equalCalled()
    assert expression == ""
    assert result == "23.9"

def test_expression_with_exception(engine_object) : 
    engine_object.addOperator('-')
    engine_object.addNumber('2')
    engine_object.addNumber('5')
    engine_object.addOperator('*')
    assert engine_object.inputResult() == "-25*"
    
    with pytest.raises(ValueError) as exec : 
        engine_object.addNumber('25')
    assert str(exec.value) == const.MORE_NUMBER_ERROR

def tes_reciprocal_expression(engine_object) : 
    engine_object.addOperator('-')
    engine_object.addNumber('2')
    engine_object.addNumber('5')
    
    ex,result = engine_object.reciprocal()
    assert ex == ""
    assert result == "-0.04"

def test_decimal_value(engine_object) : 
    engine_object.addMinus() == '-'
    engine_object.addDecimal() == '-0.'
    engine_object.addDecimal() == '-0.'
    engine_object.backspace() == '-0'
    engine_object.addDecimal() == '-0.'

def test_operator_error(engine_object) : 
    engine_object.addOperator('-')
    engine_object.addNumber('2')
    engine_object.addNumber('5')
    
    assert engine_object.inputResult() == "-25"
    assert engine_object.backspace() == "-2"
    engine_object.addNumber('5')
    
    ex,result = engine_object.square()
    assert ex == ""
    assert result == "625"
    
    with pytest.raises(ValueError) as exce : 
        engine_object.addOperator('/*')
    assert str(exce.value) == const.SINGLE_OPERATOR_ERROR
