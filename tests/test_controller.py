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