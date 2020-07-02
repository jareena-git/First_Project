# from sqlalchemy import Column,Integer,Float,ForeignKey,Text
# from sqlalchemy.orm import relationship
# from salary_fk_Mixin import FkMixin
# from Serializer_module import Serializer
# class salary(FkMixin,Serializer):
#         __tablename__='salaries'
#         id = Column(Integer,primary_key=True)
#         emp_salary=Column(Float,nullable=False)
#         PositionLevel=Column(Text,nullable=False)
#         Position = Column(Text, nullable=False)
#         # user_id=Column(Integer, ForeignKey('users.id'))
#
#
#         def __init__(self,id,emp_salary,PositionLevel,Position):
#             self.id=id
#             self.emp_salary=emp_salary
#             self.PositionLevel=PositionLevel
#             self.Position=Position
#
#         def serialize(self):
#             d = Serializer.serialize(self)
#             return d
#
#
