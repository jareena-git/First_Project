from config import  config
import psycopg2
def dbConnect():
    con = None
    try:
        params = config()
        con = psycopg2.connect(**params)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    return con
dbConnect()