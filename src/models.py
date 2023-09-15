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
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    usuario = Column(String(250), nullable=False)

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    coment_text = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates = "comentario")
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates = "comentario")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates = "post")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    img = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates = "media")
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
