import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(20), nullable=False)
    edad = Column(Integer, nullable=True)
    correo = Column(String(80), unique=True, nullable=False)
    foto_perfil = Column(String(200), nullable=True)
    password = Column(String(20), nullable=False)
    biografia = Column(String(200), nullable=True)

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(200), nullable=False)
    foto = Column(String(200), nullable=True)
    tipo = Column(String(15), nullable=False)
    fecha = Column(String(15), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=True)

class Mensajes(Base):
    __tablename__ = 'mensajes'
    id = Column(Integer, primary_key=True)
    texto = Column(String(200), nullable=False)
    tipo = Column(String(15), nullable=False)
    fecha = Column(String(15), nullable=False)
    id_emisor = Column(String(200), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=True)

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    texto = Column(String(200), nullable=False)
    fecha = Column(String(15), nullable=False)
    id_publicacion = Column(Integer, ForeignKey('publicacion.id'), nullable=True)

class Me_Gusta(Base):
    __tablename__ = 'me_gusta'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(15), nullable=False)
    id_publicacion = Column(Integer, ForeignKey('publicacion.id'), nullable=True)

class Seguidores(Base):
    __tablename__ = 'seguidores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(20), nullable=False)
    foto_perfil = Column(String(200), nullable=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=True)

class Siguiendo(Base):
    __tablename__ = 'siguiendo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(20), nullable=False)
    foto_perfil = Column(String(200), nullable=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=True)

class Bloqueados(Base):
    __tablename__ = 'bloqueados'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=True)

class Solicitud_Seguimiento(Base):
    __tablename__ = 'solicitud_seguimiento'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
