import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


# Cada usuario puede tener un personaje favorito y una nave favorita.

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites_starship = Column(Integer, ForeignKey('starship.id'))
    favorite_character = Column(Integer, ForeignKey('character.id'))

    def to_dict(self):
        return {}


# Cada personaje puede tener varias naves y pertenecer a un planeta

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    planet = Column(Integer, ForeignKey('planets.id'))
    starships = relationship('Starship')
    users = relationship('User')

    def to_dict(self):
        return {}


# Cada nave pertenece a un personaje

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    size = Column(Integer, nullable=False)
    max_speed = Column(Integer, nullable=False)
    acceleration = Column(Integer, nullable=False)
    users = relationship('User')
    owner = Column(Integer, ForeignKey('character.id'))

    def to_dict(self):
        return {}


# Cada planeta puede tener varios personajes

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    population = relationship('Character')

    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
