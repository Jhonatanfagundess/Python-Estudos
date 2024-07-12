from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# postgresql://usuario:senha@host/database
DATABASE_URI = ''

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()