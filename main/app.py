from main.model.calculator_engine import CalculatorEngine
from main.controller.calculator_controller import CalculatorController
from main.view.calculator_view import CalculatorView

if __name__ == "__main__" : 
    engine = CalculatorEngine()
    controller = CalculatorController(engine)
    view = CalculatorView(controller)
    view.run()