# app/main.py

from fastapi import FastAPI
from app.api.v1.endpoints import users
from app.db.database import client

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    client.close()