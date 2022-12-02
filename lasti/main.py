from fastapi import FastAPI
import models
from database import engine
from logging import Handler

app=FastAPI()

models.Base.metadata.create_all(engine)




@app.get("/")
def welcome():
        return {"message": "Selamat datang di aplikasi MANTRA"}