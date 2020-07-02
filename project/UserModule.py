from sqlalchemy import (Column,ForeignKey,Integer,Table,Sequence,String,MetaData)
from sqlalchemy.orm import relationship,mapper
from sqlalchemy.ext.declarative import declarative_base
from UserMixinModule import Serializer
base=declarative_base()



class user(Serializer):
    __tablename__= "users"
    id = Column(Integer,primary_key=True,nullable=False)
    name= Column(String(20),nullable=False)
    full_name=Column(String(20),nullable=False)

    def __init__(self,id,name,full_name):
        self.id=id
        self.name=name
        self.full_name
