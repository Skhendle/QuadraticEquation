import pytest
from app.quadratic_equation.service import QuadraticEquation
from app.quadratic_equation.input import QuadraticEquationModel
# Valid input case one.
def test_quadratic_equation_one():
    # set a = 1, b = -4, c = 3.
    # Excepect output.
    x1 = 3.0
    x2 = 1.0
    obj = QuadraticEquation(QuadraticEquationModel(a=1, b=-4, c=3))
    assert obj.quadratic_equation() == (x1, x2)

# Invalid input case two.
def test_quadratic_equation_two():
    # set a = 1, b = -4, c = 5.
    # Excpected output.
    output = "No Real Solution"
    obj = QuadraticEquation(QuadraticEquationModel(a=1, b=-4, c=5))
    assert obj.quadratic_equation() == output

# Invalid input case three.
def test_quadratic_equation_three():
    # set a = 0, b = -4, c = 3.
    # Excpected output. 
    output = "Undefined Expression"
    obj = QuadraticEquation(QuadraticEquationModel(a=0, b=-4, c=3))
    assert obj.quadratic_equation() == output