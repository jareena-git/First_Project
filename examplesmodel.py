# from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
# from sqlalchemy.ext.declarative import declarative_base
#
#
#
#
# class example_model():
#     """Data model example."""
#     __tablename__ = "example_table"
#     __table_args__ = {"schema": "example"}
#
#     id = Column(Integer,
#                 primary_key=True,
#                 nullable=False)
#     name = Column(String(100),
#                   nullable=False)
#     description = Column(Text,
#                          nullable=True)
#     join_date = Column(DateTime,
#                        nullable=False)
#     vip = Column(Boolean,
#                  nullable=False)
#     number = Column(Float,
#                     nullable=False)
#     data = Column(PickleType,
#                   nullable=False)
#
#     def __repr__(self):
#         return '<Example model {}>'.format(self.id)
