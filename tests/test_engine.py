import pytest
from main.model.calculator_engine import calculator_engine

@pytest.fixture
def engine_object() : 
    return calculator_engine()

def test_expression1(engine_object) : 
    assert engine_object.addNumber('0') == "0"
    assert engine_object.addNumber('2') == "2"
    assert engine_object.addNumber('3') == "23"