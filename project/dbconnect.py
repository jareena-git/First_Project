from config import  config
import psycopg2
def dbConnect():
    con = None
    try:
        #reading config file
        params = config()
        # connect method is used to connect to the database
        con = psycopg2.connect(**params)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    return con
dbConnect()