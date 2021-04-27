import json, logging
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    
    "http://localhost:3000",
    "localhost:3000"
    
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
    return {"message": "Web Server Application!"}

