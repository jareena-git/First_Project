from flask import Flask,request,jsonify
# from flask import
from flask.blueprints import Blueprint
from BlueprintRount import userBluePrint as userBluePrint_20
from BluePrint21 import addressBluePrint as addressBluePrint_21
# from . import pscons
import os

app=Flask(__name__)

# db = SQLAlchemy(app)

app.register_blueprint(userBluePrint_20,url_prefix='/2.0')
app.register_blueprint(addressBluePrint_21,url_prefix='/2.1')


basedir=os.path.abspath(os.path.dirname(__file__))

# DB_URL = 'postgresql+psycopg2://postgres:Saleem!123@127.0.0.1:5432/Employees'
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning







@app.route('/2.1')
@app.route('/2.0')
def index():
    return 'hello jareena'


# run server
if __name__=="__main__":
    app.run(debug=True)
