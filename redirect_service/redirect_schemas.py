from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Rules(base):                    # pylint: disable=too-few-public-methods
    __tablename__ = 'rules'

    id = Column(Integer(), primary_key=True)
    rule = Column(Text())
    priority = Column(Integer())
    property = Column(Text())
    url = Column(Text())
