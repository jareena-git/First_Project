from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship


class Serializer(object):
    # @declared_attr
    # def User_Addresses(cls):
    #     return relationship("Address", order_by=Address.id, backref="user")

    def serialize(self):
        return {
                    c: getattr(self, c) for c in inspect(self).attrs.keys()
               }

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
