#!/user/bin/python3
''' create state class that inherits methods form sqlalchamey'''


from sqlalchamy import Column, Integer, String, MetaData
from sqlalchamy.ext.orm import declarative_base

mainData = MetaData()

Base = declarative_base(metadata=mainData)


class State(Base):
    __tablename__ = 'states'
    id = column(Integer, unique=True, primary_key=True, nualleable=False)
    name = column(String(128), nualleable=False)
