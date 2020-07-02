from sqlalchemy import (Column,ForeignKey,Integer,Table,Sequence,String)

class UserMixin(object):
    id = Column(Integer,primary_key=True)
    name = Column(String(25),nullable=False)
    def get_id(self):
        return  id
    def get_name(self):
        return name

