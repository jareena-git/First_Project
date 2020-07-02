import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os.path import expanduser
import os
from userMixin import(UserMixin)
from model import(address,user,base)
# from Usercls import(user)
# from models import(User,base)
# from UserModule import(user,base)


# engine = create_engine(url)
# Session = sessionmaker(bind=engine)
# session = Session()
# Session.configure(bind=engine)
# base.metadata.create_all(engine)
#


url='postgresql://postgres:Saleem!123@127.0.0.1:5432/CollegeDB'
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
Session.configure(bind=engine)
base.metadata.create_all(engine)
