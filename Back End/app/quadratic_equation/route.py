import json, logging
from fastapi import APIRouter, Depends

# Importing input_models, that will be used route paramaters
from app.quadratic_equation.input import QuadraticEquationModel

# Import the service for the route
from app.quadratic_equation.service import QuadraticEquation

router = APIRouter()

@router.post("/quadratic_equation", tags=["equations"])
async def quadratic_equation(input_model: QuadraticEquationModel):
    return QuadraticEquation(inputs = input_model ).quadratic_equation()