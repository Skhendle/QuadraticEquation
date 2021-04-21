# import pytest
# from app.quadratic_equation.service import quadratic_equation

# # Valid input case one.
# def test_quadratic_equation_one():
#     # set a = 1, b = -4, c = 3.
#     # Excepect output.
#     x1 = 3.0
#     x2 = 1.0
#     assert quadratic_equation(a=1, b=-4, c=3) == (x1, x2)

# # Invalid input case two.
# def test_quadratic_equation_one():
#     # set a = 1, b = -4, c = 5.
#     # Excpected output.
#     output = "No Real Solution"
#     assert quadratic_equation(a=1, b=-4, c=5) == output

# # Invalid input case three.
# def test_quadratic_equation_one():
#     # set a = 1, b = -4, c = 3.
#     # Excpected output. 
#     output = "Undefined Expression"
#     assert quadratic_equation(a=0, b=-4, c=3) == output