from fastapi import FastAPI
import models
from database import engine, get_db
from logging import Handler

import uvicorn
import schemas as sc

app=FastAPI()

models.Base.metadata.create_all(engine)




@app.get("/")
# root, mnampilkan pesan selamat datang di aplikasi mantra
def welcome():
        return {"message": "Selamat datang di aplikasi MANTRA"}

@app.post("/register")
# registrasi akun requester
def register():
        pass

@app.get("/login")
# melakukan login sesuai dengan akun requester
def login():
        pass

@app.get("/API")
# mengambil seluruh data api
def get_all_api():
        pass

@app.get("/API/katalog")
# mengambil seluruh data api yang sudah dipublikasi (is_published == true)
def get_published_api():
        pass

@app.post("/API")
# menambahkan data API baru ke database
def add_api():
        pass

@app.put("/API/publish/{id_api}")
# mempublikasikan api dengan mengubah kolom is_published pada salah satu data pada tabel API dengan id_api=id_api
def publish_api():
        pass

@app.get("/API/{id_api}")
# mengambil data API yang sudah diberikan aksesnya 
# (dicek pada tabel req_penggunaan_api untuk kolom status_akses == true)
def get_api():
        pass

@app.post("{id_requester}/request/penyediaan_API")
# menambahkan data req_penyediaan_API sesuai dengan id requester
def add_request_penyediaan_api():
        pass

@app.put("/konfirmasi/penyediaan_API/{id_req_penyediaan_API}")
# mengubah kolom status_konfirmasi pada tabel req_penyediaan_API jadi true
def konfirmasi_request_penyediaan_api():
        pass

@app.post("{id_requester}/request/penggunaan_API")
# menambahkan data req_penggunaan_API sesuai dengan id requester
def add_request_penggunaan_api():
        pass

@app.put("/konfimasi/request/penggunaan_API/{id_req_penggunaan_API}")
# mengubah kolom status_akses pada tabel req_penggunaan_API jadi true
def konfirmasi_request_penggunaan_api():
        pass

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)