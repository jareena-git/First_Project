# from sqlalchemy.ext.declarative import declared_attr
# from sqlalchemy import Column,Integer,ForeignKey
# from sqlalchemy.orm import relationship
#
# class FkMixin(object):
#     @declared_attr
#     def user_id(cls):
#         return Column(Integer,ForeignKey('users.id'))
#     @declared_attr
#     def relation_to(cls):
#         # return relationship("User", backref="salaries",primaryjoin="User.id == Post.user_id")