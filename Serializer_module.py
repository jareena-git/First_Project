from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

class Serializer(object):
    # @declared_attr
    # def salary_relation(cls):
    #     return relationship("salary",backref="users")

    def serialize(self):
        return {
                    c: getattr(self, c) for c in inspect(self).attrs.keys()
               }

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

    # @declared_attr
    # def user_relation(self):
    #     return relationship('salary', backref='users')
