from pydantic import BaseModel
from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import declarative_base

base = declarative_base()

class RuleData(BaseModel):
    property: str
    url: str

class CreateRuleReq(BaseModel):
    rule_type: str
    priority: int
    data: list[RuleData]


class Rules(base):                    # pylint: disable=too-few-public-methods
    __tablename__ = 'rules'

    id = Column(Integer(), primary_key=True)
    rule = Column(Text())
    priority = Column(Integer())
    property = Column(Text())
    url = Column(Text())
