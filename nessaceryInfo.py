 # user = user(id=1, name="jareena", full_name="jareena shaik")
# base.metadata.create_all(engine)

    # user1 = User(id=5,name="sulthana", full_name="sulthana shaik")
    # session.add(user1)
    # session.commit()
    # qry=session.query(User).filter_by(name="jareena").first()
# for name, fullname in session.query(User.name, User.full_name):
# print(name,fullname)
    # qry=session.query(User)
    # print(qry)



    # def __init__(self):
    #     # dict_conf_args = {}
    #     # dict_conf_args['username']='postgres'
    #     # dict_conf_args['password'] = 'Saleem!123'
    #     # dict_conf_args['database'] = 'postgres'
    #     # dict_conf_args['port'] = '5432'
    #     # dict_conf_args['host'] = '127.0.0.1'
    #     # db_config_file=basedir+'/db.conf'
    #     # url='postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(user=dict_conf_args['username'],password=dict_conf_args['password'],
    #     #                                                                    host=dict_conf_args['host'],port=dict_conf_args['port'],
    #     #                                                                    dbname=dict_conf_args['database'] )

    # def create(User):
    #     base.metadata.create_all(self.engin)
    #
    #     user1=user(name="jareena",full_name="jareena shaik")
    #     session.add(user1)
    #     obj1 = self.session.query("users").all()
    #     print(obj1)

# basedir=os.path.dirname(__file__)





# return json.dump([dict(r) for r in records],default=alchemyencoder)

    # for record in records.all():
    #     record_as_dict=dict({'id' : record.id,'name':record.name,'full_name': record.full_name})
    # recordObject=[]
    # recorddict={}
    # for result in all_results:
    #     recordObject.extend({'id' : result.id,'name':result.name,'full_name': result.full_name})
    #     print(recordObject)
    #     recorddict=dict(recordObject)
    # return jsonify(record_as_dict)

    # for id,name,fullname in psqlconfigutils.session.query(User.id,User.name,User.full_name).filter_by(full_name='jareena shaik'):
    #     recordObject={'id' : id,'name':name,'full_name': fullname}
    #     return jsonify(recordObject)
