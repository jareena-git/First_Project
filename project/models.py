from sqlalchemy.ext.declarative import declarative_base
from userMixin import(UserMixin)
from Usercls import user
# from examplesmodel import example_model
# from Salary_module import salary


base=declarative_base(cls=UserMixin)
class User(base,user):
    pass


# class ExampleModel(base,example_model):
#     pass
#
# class Salary(base,salary):
#     pass


