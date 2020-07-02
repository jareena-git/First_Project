from sqlalchemy import (Column,ForeignKey,Integer,Table,Sequence,String,MetaData)
from sqlalchemy.orm import relationship,mapper
from userMixin import(UserMixin)
import userMixin
from sqlalchemy.ext.declarative import declarative_base
from UserMixinModule import Serializer



class User(Serializer):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % ( self.name, self.fullname, self.password)

    def serialize(self):
        d=Serializer.serialize(self)
        return d
