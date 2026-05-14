import pytest
from main.controller.calculator_controller import calculator_controller
from main.utils.constants import ZERO_DIVISION_MESSAGE
from main.model.calculator_engine import calculator_engine

@pytest.fixture
def engine_object() : 
    return calculator_engine()

@pytest.fixture
def controller_object(engine_object) : 
    return calculator_controller(engine_object)

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