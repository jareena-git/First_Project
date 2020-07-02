from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from AddressMixinModule import AddressMixin
from Serializer_module import Serializer




class Address(AddressMixin,Serializer):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)

    def __init__(self,id,email_address):
        self.id = id
        self.email_address = email_address

    def serialize(self):
        d=Serializer.serialize(self)
        return d


