from fastapi import FastAPI
import models
from database import engine
from routers import toko,user,authentication
from logging import Handler

app=FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(user.router)


@app.get("/")
def welcome():
        return {"message": "Selamat datang di aplikasi MANTRA"}