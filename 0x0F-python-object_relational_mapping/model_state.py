#!/usr/bin/python3
"""
model state
"""

from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

mt_data = MetaData()
Base = declarative_base(metadata=mt_data)


class State(Base):
    """
    Class that define state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
