from flask.blueprints import Blueprint
from flask import jsonify,request
import psqlconfigutils
from models import(User,base)
import json



userBluePrint=Blueprint('userBluePrint20',__name__)

@userBluePrint.route('/',methods=['GET'])
def get():
    records = psqlconfigutils.session.query(User).all()
    return json.dumps(User.serialize_list(records))





@userBluePrint.route('/user',methods=['POST'])
def create_record():
    id=request.json['id']
    name=request.json['name']
    full_name=request.json['full_name']
    newUser=User(id=id,name=name,full_name=full_name)
    psqlconfigutils.session.add(newUser)
    psqlconfigutils.session.commit()
    return None


@userBluePrint.route('/ViewUser')
def view_user():
    return 'view user'


@userBluePrint.route('/PostSalary',methods=['POST'])
def create_salary():
    id = request.json['id']
    name= request.json['name']
    emp_salary = request.json['emp_salary']
    PositionLevel = request.json['PositionLevel']
    Position = request.json['Position']
    fk_declrative = request.json['fk_declrative']

    new_salary_record=Salary(id=id,name=name,emp_salary=emp_salary,PositionLevel=PositionLevel,Position=Position,fk_declrative=fk_declrative)
    print(Salary.__table__)
    psqlconfigutils.session.add(new_salary_record)
    psqlconfigutils.session.commit()
    return 'Success'


# @userBluePrint.route('/PostSalary',methods=['POST'])
# def get_salary(id):




# @userBluePrint.route('/StudentTb',methods=['POST'])
# def create_student():
