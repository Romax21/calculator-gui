**A Calculator Project using Python tkinter**

**It is an MVC(model-view-controller) style project**

**Project Structure -**
Calculator
    **-> model**
        -> calculator_engine.py
        -> calculator_logic.py
    **-> view**
        -> calculator_view.py
   **-> controller**
        -> calculator_controller.py
    **-> utils**
        -> constants
    **app.py**

1. app.py starts the whole project.
2. view - Makes the whole UI of the calculator(all the buttons,input, output, etc)
3. When a button is pressed, it send that to controller
4. Controller sends it to engine's specific based on what button was pressed and receives a new input expression and output expression
5. calculator_engine get the input from controller and changes its input variables(two operator and a operator)
6. It call calculator_logic when an output button such as =, etc is called

**Features -**
1. The layout is like a phone calculator. The buttons have to pressed to put an input
2. The operators - +,-,*,/,% (modulus)
3. The decimal are allowed, so floating point operations are possible
4. Takes care of near floating errors
5. In addition, also include x^2(for square), 1/x (for reciprocal)
6. Also contains a backspace(<=) and a Reset Button
7. The operation can continue from previous operations output
8. Takes care of division by zero error

**Limitations/Future Improvement -**
1. A Very simple UI
2. Only allows one operator between two operands at a time
3. Doesn't consider very large inputs so may give error
4. Input cannot be pasted, have to write it one by one
5. Keyboard buttons are not allowed, only calculator buttons are allowed

Note - since root is Calculator
-> Run it using python -m main.app