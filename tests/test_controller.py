import pytest
from main.controller.calculator_controller import CalculatorController
from main.model.calculator_engine import CalculatorEngine
import main.utils.constants as const

@pytest.fixture
def engine_object() : 
    return CalculatorEngine()

@pytest.fixture
def controller_object(engine_object) : 
    return CalculatorController(engine_object)

def test_addition(controller_object) : 
    controller_object.buttonPressed('2')
    controller_object.buttonPressed('1')
    controller_object.buttonPressed('+')
    controller_object.buttonPressed('3')
    expression,result = controller_object.buttonPressed('4')
    
    assert expression == '21+34'
    expression,result = controller_object.buttonPressed('=')
    assert result == '55'
    
def test_subtraction(controller_object) : 
    controller_object.buttonPressed('2')
    controller_object.buttonPressed('1')
    controller_object.buttonPressed('-')
    controller_object.buttonPressed('3')
    expression,result = controller_object.buttonPressed('4')
    
    assert expression == '21-34'
    expression,result = controller_object.buttonPressed('=')
    assert result == '-13'

def test_backspace(controller_object) : 
    controller_object.buttonPressed('2')
    controller_object.buttonPressed('1')
    controller_object.buttonPressed('-')
    controller_object.buttonPressed('3')
    ex,result = controller_object.buttonPressed('4')
    assert ex == '21-34'
    
    ex,result = controller_object.buttonPressed('<=')
    assert ex == '21-3'
    ex,result = controller_object.buttonPressed('<=')
    assert ex == '21-'
    ex,result = controller_object.buttonPressed('<=')
    assert ex == '21'
    ex,result = controller_object.buttonPressed('<=')
    assert ex == '2'
    
    ex,result = controller_object.buttonPressed('x^2')
    assert ex == ''
    assert result == '4'

def test_notText_error(controller_object) : 
    ex,result = controller_object.buttonPressed('')
    assert result == const.INPUT_EMPTY_ERROR
    
    ex,result = controller_object.buttonPressed('abc')
    assert result == const.INVALID_INPUT_ERROR
    
    ex,result = controller_object.buttonPressed('+-')
    assert result == const.SINGLE_OPERATOR_ERROR
    
    ex,result = controller_object.buttonPressed('12')
    assert result == const.MORE_NUMBER_ERROR
    
    controller_object.buttonPressed('1')
    controller_object.buttonPressed('/')
    controller_object.buttonPressed('0')
    
    ex,result = controller_object.buttonPressed('=')
    assert result == const.ZERO_DIVISION_ERROR