#!/usr/bin/python3
"""
Start model class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__= 'states'
    id = Column(Integer, Primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
