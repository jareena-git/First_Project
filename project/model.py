from sqlalchemy.ext.declarative import declarative_base
from userMixin import(UserMixin)
from UserModules import User
from AddressModule import Address
from Serializer_module import Serializer


base=declarative_base()




class user(base,User):
    pass

class address(base,Address):
    pass
