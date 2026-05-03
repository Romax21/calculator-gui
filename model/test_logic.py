from model.calculator_logic import calculate_expresion

def test_add_basic() : 
    result = calculate_expresion("2+3")
    assert result == "5"
    
def test_addDouble() : 
    result = calculate_expresion("23+34")
    assert result == "57"