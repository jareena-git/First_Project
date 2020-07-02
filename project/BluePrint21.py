from flask.blueprints import Blueprint
from flask import jsonify,request
import psqlconfigutils
from model import(base,user,address)
import json
from sqlalchemy import desc
from sqlalchemy import and_



addressBluePrint=Blueprint('addressBluePrint21',__name__)

# @userBluePrint.route('/',methods=['GET'])
# def get():
#     records = psqlconfigutils.session.query(User).all()
#     return json.dumps(User.serialize_list(records))

@addressBluePrint.route('/address',methods=['POST'])
def create_record():
    id=request.json['id']
    email_address=request.json['email_address']
    adds=address(id=id,email_address=email_address)
    psqlconfigutils.session.add(adds)
    psqlconfigutils.session.commit()
    return "address added successfully"

@addressBluePrint.route('/get_address_records',methods=['GET'])
def get_addresses():
    all_addresses=psqlconfigutils.session.query(address).all()
    return json.dumps(address.serialize_list(all_addresses))

@addressBluePrint.route('/userrecord',methods=['POST'])
def create_user_record():
    id=request.json['id']
    name=request.json['name']
    full_name=request.json['fullname']
    password = request.json['password']
    newUser=user(id=id,name=name,fullname=full_name,password=password)
    psqlconfigutils.session.add(newUser)
    psqlconfigutils.session.commit()
    return "user created successfully"

@addressBluePrint.route('/getUserRecord/<id>', methods=['GET'])
def get_user_record(id):
    user_record=psqlconfigutils.session.query(user).get(id)

    # change password of the trived object
    user_record.password="up_pass"
    print("Updated password of this user: {0}, password {1}".format(user_record.name,user_record.password))

    #add fake user to the users table
    fake_user=psqlconfigutils.session.add(user(id=11,name="fake",fullname="fakeuser",password="fake_pass"))

    get_list_users_by_names=psqlconfigutils.session.query(user).filter(user.name.in_(["Sirajunnisa","fake","Jani"])).all()
    print("The list of users filter by name {0}".format(json.dumps(user.serialize_list(get_list_users_by_names))))




    #role back changes which we made before
    # psqlconfigutils.session.rollback()

    # retrive record based on name is Saleem
    get_record_by_name=psqlconfigutils.session.query(user).filter_by(name='Saleem').first()
    print("Get single user by using name, userid is : {0},username is : {1},userfullname is : {2}".format(get_record_by_name.id,get_record_by_name.name,get_record_by_name.fullname))

    #Get instances of the user class in desc order
    get_all_user_desc=psqlconfigutils.session.query(user).order_by(desc(user.id))
    print("Get all instances of the user in desceding order:{0}".format(json.dumps(user.serialize_list(get_all_user_desc))))

    get_all_user_asc=psqlconfigutils.session.query(user).order_by(user.id)
    print("Get all instances of the user in ascending order:{0}".format(json.dumps(user.serialize_list(get_all_user_asc))))

    for name,fullname,password in psqlconfigutils.session.query(user.name,user.fullname,user.password):
        print("All users are {0},{1},{2}".format(name,fullname,password))

    for row,lab in  psqlconfigutils.session.query(user,user.name.label('user_name')).all():
        print("labeld colums{0}:{1}:{2}{3}".format(row.name,row.fullname,row.password,lab.user_name))




    return json.dumps(user.serialize(user_record))

@addressBluePrint.route('/getAllUserRecords', methods=['GET'])
def get_user_records():
    all_users=psqlconfigutils.session.query(user).all()
    for name,fullname in psqlconfigutils.session.query(user,user.fullname):
        print(name,fullname)

    # label the name to the column
    for name in psqlconfigutils.session.query(user.name.label('nick_name')):
        print(name.nick_name)

    for row in psqlconfigutils.session.query(user).order_by(desc(user.id))[0:5]:
        print(row)

    # get jani from user instance
    for fullname, in psqlconfigutils.session.query(user.fullname).\
            filter_by(name='Jani'):
        print(fullname)

    for fullname, in psqlconfigutils.session.query(user.fullname).\
            filter(user.name=='Saleem'):
        print(fullname,)

    # retrive record by name
    for row in psqlconfigutils.session.query(user).\
            filter(user.name=="Jani").\
            filter(user.fullname=="Janee Shaik"):
        print("my name is {0}".format(row))
    # print(named_tuple)

    user_expected=psqlconfigutils.session.query(user).\
            filter(and_(user.name=='Saleem',user.fullname=='Saleem Syed')).\
            order_by(user.id).one()
    print("one fetch all the rows if single object found it will give otherwise throw error for")

    return json.dumps(user.serialize_list(all_users))











































# full_name=request.json['full_name']
    # newUser=User(id=id,name=name,full_name=full_name)
    # psqlconfigutils.session.add(newUser)
    # psqlconfigutils.session.commit()
    # return None

