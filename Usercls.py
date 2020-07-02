from sqlalchemy import (Column,ForeignKey,Integer,Table,Sequence,String,MetaData)
from sqlalchemy.orm import relationship,mapper
from userMixin import(UserMixin)
import userMixin
from Serializer_module import Serializer
# metadata=MetaData()
#
# usertb=Table("users",metadata,Column("id",Integer,primary_key=True),Column("name",String(20),nullable=False),
# Column("full_name",String(20),nullable=False))

#userMixin.UserMixin
class user(Serializer):
    __tablename__= 'users'
    id = Column(Integer,primary_key=True,nullable=False)
    name= Column(String(20),nullable=False)
    full_name=Column(String(20),nullable=False)

    def __init__(self,id,name,full_name):
        self.id=id
        self.name=name
        self.full_name=full_name

    def serialize(self):
        d=Serializer.serialize(self)
        return d



# mapper(users,usertb)
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializable format"""
#         return {
#             'id': self.id,
#             'name': str(self.name),
#             # This is an example how to deal with Many2Many relations
#             'full_name': str(self.full_name)
#         }
#
#     @property
#     def serialize_many2many(self):
#         """
#         Return object's relations in easily serializable format.
#         NB! Calls many2many's serialize property.
#         """
#         return [item.serialize for item in self.many2many]
