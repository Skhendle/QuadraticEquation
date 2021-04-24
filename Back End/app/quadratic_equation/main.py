import json, logging
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:8000/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.quadratic_equation import route
app.include_router(route.router)


@app.get("/")
async def root():
    return {"message": "Quadratic Equation"}