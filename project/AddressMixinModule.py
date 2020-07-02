from sqlalchemy import ForeignKey,Column,Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

class AddressMixin(object):
    @declared_attr
    def user_id(cls):
        return Column(Integer, ForeignKey('users.id'))

    @declared_attr
    def user(cls):
        relationship("User", back_populates="addresses")



