from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Instansi(Base):
    __tablename__="Instansi"
    id_instansi=Column(Integer,primary_key=True,index=True)
    nama_instansi=Column(String)

    #one-to-many relationship dengan provider
    provider=relationship("Provider",back_populates="instansi_column")
    #one-to-many relationship dengan publisher
    publisher=relationship("Publisher",back_populates="instansi_column")

class Requester(Base):
    __tablename__="Requester"
    id_requester=Column(Integer,primary_key=True,index=True)
    password=Column(String)
    nama=Column(String)
    NIK=Column(Integer)
    # instansi=Column(String,ForeignKey("Instansi.id_instansi"))

    #one-to-one relationship dengan instansi
    # instansi_column=relationship("Instansi",back_populates="requester")

    #one-to-many relationship dengan req_penggunaan_API
    req_penggunaan=relationship("Req_penggunaan_API",back_populates="requester")
    #one-to-many relationship dengan req_penyediaan_API
    req_penyediaan=relationship("Req_penyediaan_API",back_populates="requester")

class Provider(Base):
    __tablename__="Provider"
    id_provider=Column(Integer,primary_key=True,index=True)
    password=Column(String)
    nama=Column(String)
    NIP=Column(Integer)
    instansi=Column(String,ForeignKey("Instansi.id_instansi"))

    #many-to-one relationship dengan instansi
    instansi_column=relationship("Instansi",back_populates="provider")
    #one-to-many relationship dengan API
    API=relationship("API",back_populates="provider")

class Publisher(Base):
    __tablename__="Publisher"
    id_publisher=Column(Integer,primary_key=True,index=True)
    password=Column(String)
    nama=Column(String)
    NIP=Column(Integer)
    instansi=Column(String,ForeignKey("Instansi.id_instansi"))

    #many-to-one relationship dengan instansi
    instansi_column=relationship("Instansi",back_populates="publisher")
    #one-to-many relationship dengan req_publikasi_API
    req_publikasi=relationship("Req_publikasi_API",back_populates="publisher")


class Req_publikasi_API(Base):
    __tablename__="Request_Publikasi_API"
    id_req_publikasi_API=Column(Integer,primary_key=True,index=True)
    id_publisher=Column(Integer,ForeignKey("Publisher.id_publisher"))
    id_api=Column(Integer,ForeignKey("API.id_api"))
    status_akses=Column(Boolean, default = False)
    
    #one-to-many relationship dengan publisher
    publisher=relationship("Publisher",back_populates="req_publikasi")
    #one-to-many relationship dengan API
    API=relationship("API",back_populates="req_publikasi")

class API(Base):
    __tablename__="API"
    id_api=Column(Integer,primary_key=True,index=True)
    nama_API=Column(String)
    instansi_penyedia=Column(String,ForeignKey("Provider.instansi"))
    direktori=Column(String,ForeignKey("Direktori.id_direktori"))
    keterangan=Column(String)
    alamat_akses=Column(String)
    file_adapter=Column(String)
    is_published=Column(Boolean, default = False)

    #one-to-many relationship dengan request_publikasi_api
    req_publikasi=relationship("Request_publikasi_API",back_populates="API")
    #one-to-many relationship dengan request_penggunaan_api
    req_penggunaan=relationship("Request_penggunaan_API",back_populates="API")
    #many-to-one relationship dengan direktori
    direktori=relationship("Direktori",back_populates="API")
    #many-to-one relationship dengan provider
    provider=relationship("Provider",back_populates="API")

class Direktori(Base):
    __tablename__="Direktori"
    id_direktori=Column(Integer,primary_key=True,index=True)
    nama_direktori=Column(String)

    #one-to-many relationship dengan API
    API=relationship("API",back_populates="direktori")

class Req_penggunaan_API(Base):
    __tablename__="Request_Penggunaan_API"
    id_req_penggunaan_API=Column(Integer,primary_key=True,index=True)
    id_requester=Column(Integer,ForeignKey("Requester.id_requester"))
    id_api=Column(Integer,ForeignKey("API.id_api"))
    status_akses=Column(Boolean, default = False)

    #many-to-one relationship dengan API
    API=relationship("API",back_populates="req_penggunaan")
    #many-to-one relationship dengan requester
    requester=relationship("Requester",back_populates="req_penggunaan")
    

class Req_penyediaan_API(Base):
    __tablename__="Request_Penyediaan_API"
    id_req_penyediaan_API=Column(Integer,primary_key=True,index=True)
    id_requester=Column(Integer,ForeignKey("Requester.id_requester"))
    nama_api=Column(String)
    spesifikasi=Column(String)
    status_konfirmasi=Column(Boolean, default = False)

    #many-to-one relationship dengan requester
    requester=relationship("Requester",back_populates="req_penyediaan")


