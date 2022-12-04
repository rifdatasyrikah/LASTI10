from typing import List
from pydantic import BaseModel

class Instansi(BaseModel):
    # __tablename__="Instansi"
    id_instansi : int
    nama_instansi : str
    
class Requester(BaseModel):
    # __tablename__="Requester"
    id_requester : int
    password : str
    nama : str
    NIK : int

    # #one-to-one relationship dengan instansi
    # instansi_column=relationship("Instansi",back_populates="requester")

    # #one-to-one relationship dengan req_penggunaan_API
    # req_penggunaan_2=relationship("Req_penggunaan_API",back_populates="requester2")
    # #one-to-one relationship dengan req_penyediaan_API
    # req_penyediaan=relationship("Req_penyediaan_API",back_populates="requester3")

class Provider(BaseModel):
    # __tablename__="Provider"
    id_provider : int
    password : str
    nama : str
    NIP : str
    instansi : str

    # #one-to-one relationship dengan instansi
    # instansi_column_2=relationship("Instansi",back_populates="provider")
    # #one-to-one relationship dengan API
    # API4=relationship("API",back_populates="provider",uselist=False)

class Publisher(BaseModel):
    # __tablename__="Publisher"
    id_publisher : int
    password : str
    nama : str
    NIP : int
    instansi : str

    # #one-to-one relationship dengan instansi
    # instansi_column_2=relationship("Instansi",back_populates="publisher")
    # #one-to-one relationship dengan req_publikasi_API
    # req_publikasi=relationship("Req_publikasi_API",back_populates="publisher",uselist=False)

class Req_publikasi_API(BaseModel):
    # __tablename__="Request_Publikasi_API"
    id_req_publikasi_API : int
    id_publisher : int
    id_api : int
    status_akses : bool

    # #one-to-one relationship dengan publisher
    # publisher=relationship("Publisher",back_populates="req_publikasi")
    # #one-to-one relationship dengan API
    # API=relationship("API",back_populates="req_publikasi2")

class API(BaseModel):
    # __tablename__="API"
    id_api : int
    nama_API : str
    instansi_penyedia : str
    direktori : str
    keterangan : str
    alamat_akses : str
    file_adapter : str
    is_published : bool

    # #one-to-one relationship dengan request_publikasi_api
    # req_publikasi2=relationship("Request_publikasi_API",back_populates="API",uselist=False)
    # #one-to-one relationship dengan request_penggunaan_api
    # req_penggunaan=relationship("Request_penggunaan_API",back_populates="API2",uselist=False)
    # #one-to-one relationship dengan direktori
    # direktori=relationship("Direktori",back_populates="API3")
    # #one-to-one relationship dengan provider
    # provider=relationship("Provider",back_populates="API4")

class Direktori(BaseModel):
    # __tablename__="Direktori"
    id_direktori : int
    nama_direktori : str

    # #one-to-one relationship dengan API
    # API3=relationship("API",back_populates="direktori",uselist=False)

class Req_penggunaan_API(BaseModel):
    # __tablename__="Request_Penggunaan_API"
    id_req_penggunaan_API : int
    id_requester : int
    id_api : int
    status_akses : bool

    # #one-to-one relationship dengan API
    # API2=relationship("API",back_populates="req_penggunaan")
    # #one-to-one relationship dengan requester
    # requester2=relationship("Requester",back_populates="req_penggunaan_2")
    

class Req_penyediaan_API(BaseModel):
    # __tablename__="Request_Penyediaan_API"
    id_req_penyediaan_API : int
    id_requester : int
    nama_api : str
    spesifikasi : str
    status_konfirmasi : bool

    # #one-to-one relationship dengan requester
    # requester3=relationship("Requester",back_populates="req_penyediaan")


