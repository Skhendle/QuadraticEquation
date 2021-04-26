from pydantic import BaseModel
from typing import List, Optional


class QuadraticEquationModel(BaseModel):
    a: float
    b: float
    c: float