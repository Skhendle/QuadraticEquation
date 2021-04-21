from pydantic import BaseModel
from typing import List, Optional


class QuadraticEquationModel(BaseModel):
    a: int
    b: int
    c: int