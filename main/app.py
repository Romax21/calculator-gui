from model.calculator_engine import calculator_engine
from controller.calculator_controller import calculator_controller
from view.calculator_view import calculator_view

if __name__ == "__main__" : 
    engine = calculator_engine()
    controller = calculator_controller(engine)
    view = calculator_view(controller)
    view.run()