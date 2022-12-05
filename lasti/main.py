from fastapi import FastAPI, HTTPException, Depends
import models,database
from database import engine, get_db
from logging import Handler
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from sqlalchemy import orm
from sqlalchemy.orm import Session

import uvicorn
import schemas
import hashing

app=FastAPI()

models.Base.metadata.create_all(engine)



@app.get("/")
# root, mnampilkan pesan selamat datang di aplikasi mantra
def welcome():
        return {"message": "Selamat datang di aplikasi MANTRA"}

@app.post("/register", tags=["Requester Account Management"])
# registrasi akun requester
def register(request:schemas.Requester,db:Session=Depends(get_db)):
        new_requester=models.Requester(password=hashing.Hash.bcrypt(request.password),nama=request.nama,NIK=request.NIK)
        db.add(new_requester)
        db.commit()
        db.refresh(new_requester)
        return new_requester

@app.post("/login", tags=["Requester Account Management"])
# melakukan login sesuai dengan akun requester
def login(request:schemas.Login,db:Session=Depends(database.get_db)):
        requester=db.query(models.Requester).filter(models.Requester.nama==request.nama).first()
        if hashing.Hash.verify(requester.password,request.password):
                print("password salah")
        return requester

@app.get("/API", tags=["Publisher","Provider"])
# mengambil seluruh data api
def get_all_api():
        pass

@app.get("/API/katalog", tags=["Requester"])
# mengambil seluruh data api yang sudah dipublikasi (is_published == true)
def get_published_api():
        pass

@app.post("/API", tags=["Provider"])
# menambahkan data API baru ke database
def add_api():
        pass

@app.put("/API/publish/{id_api}", tags=["Publisher"])
# mempublikasikan api dengan mengubah kolom is_published pada salah satu data pada tabel API dengan id_api=id_api
def publish_api():
        pass

@app.get("/API/{id_api}", tags=["Requester"])
# mengambil data API yang sudah diberikan aksesnya 
# (dicek pada tabel req_penggunaan_api untuk kolom status_akses == true)
def get_api():
        pass

@app.post("{id_requester}/request/penyediaan_API", response_model=schemas.Req_penyediaan_API, tags=["Requester"])
# menambahkan data req_penyediaan_API sesuai dengan id requester
def add_request_penyediaan_api(
        id_requester: int,
        Req_penyediaan_API: schemas.Req_penyediaan_API,
        db: orm.Session = Depends(get_db)
):
        db_requester = db.query(models.Requester).filter(models.Requester.id_requester == id_requester).first()
        if db_requester is None:
                raise HTTPException(status_code=404, detail="this requester account does not exist")
        Req_penyediaan_API = models.Req_penyediaan_API(**Req_penyediaan_API.dict(), requseter = id_requester)
        db.add(Req_penyediaan_API)
        db.commit()
        db.refresh(Req_penyediaan_API)
        return Req_penyediaan_API

@app.put("/konfirmasi/penyediaan_API/{id_req_penyediaan_API}", response_model=schemas.Req_penyediaan_API, tags=["Provider"])
# mengubah kolom status_konfirmasi pada tabel req_penyediaan_API jadi true
def konfirmasi_request_penyediaan_api(
        id_req_penyediaan_API: int,
        db: orm.Session = Depends(get_db)
):
        db_req = db.query(models.Req_penyediaan_API).filter(models.Req_penyediaan_API.id_req_penyediaan_API == id_req_penyediaan_API).first()
        db_req.status_konfirmasi = True
        db.commit()
        db.refresh(db_req)
        return db_req

@app.post("{id_requester}/request/penggunaan_API", tags=["Requester"])
# menambahkan data req_penggunaan_API sesuai dengan id requester
def add_request_penggunaan_api():
        pass

@app.put("/konfimasi/request/penggunaan_API/{id_req_penggunaan_API}", tags=["Publisher"])
# mengubah kolom status_akses pada tabel req_penggunaan_API jadi true
def konfirmasi_request_penggunaan_api():
        pass

@app.post("{id_requester}/request/publikasi_API", response_model=schemas.Req_publikasi_API, tags=["Publisher"])
# menambahkan data req_publikasi_API sesuai dengan id requester
def add_request_publikasi_api(
        id_publisher: int,
        Req_publikasi_API: schemas.Req_publikasi_API,
        db: orm.Session = Depends(get_db)
):
        db_publisher = db.query(models.Publisher).filter(models.Publisher.id_publisher == id_publisher).first()
        if db_publisher is None:
                raise HTTPException(status_code=404, detail="this publisher account does not exist")
        Req_publikasi_API = models.Req_publikasi_API(**Req_publikasi_API.dict(), requseter = id_publisher)
        db.add(Req_publikasi_API)
        db.commit()
        db.refresh(Req_publikasi_API)
        return Req_publikasi_API

@app.put("/konfirmasi/publikasi_API/{id_req_publikasi_API}", response_model=schemas.Req_publikasi_API, tags=["Provider"])
# mengubah kolom status_akses pada tabel req_publikasi_API jadi true
def konfirmasi_request_publikasi_api(
        id_req_publikasi_API: int,
        db: orm.Session = Depends(get_db)
):
        db_req = db.query(models.Req_publikasi_API).filter(models.Req_publikasi_API.id_req_publikasi_API == id_req_publikasi_API).first()
        db_req.status_akses = True
        db.commit()
        db.refresh(db_req)
        return db_req

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)