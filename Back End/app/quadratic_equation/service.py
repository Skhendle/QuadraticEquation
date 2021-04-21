from app.quadratic_equation.input import QuadraticEquationModel
import math

class QuadraticEquation:
    
    def __init__(self, inputs: QuadraticEquationModel):
        self.__inputs = inputs

    def quadratic_equation(self):
        value = math.pow(self.__inputs.b,2)-4*self.__inputs.a*self.__inputs.c

        if value < 0:
            return "No Real Solution"

        q = 2*self.__inputs.a

        if q == 0:
            return "Undefined Expression"

        delta = math.sqrt(value)
        
        x1 = (-self.__inputs.b + delta)/q
        x2 = (-self.__inputs.b - delta)/q

        return x1, x2
