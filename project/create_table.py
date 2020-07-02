from dbconnect import dbConnect
import psycopg2
con = dbConnect()
# def create_tables(emp_list):
#     try:
#         if con:
#             cur = con.cursor()
#             query = "CREATE TABLE Employee(Id INTEGER PRIMARY KEY,Name VARCHAR(25) NOT NULL,City VARCHAR(20) NOT NULL)"
#             cur.execute(query)
#             cur.close()
#             con.commit()
#         else:
#             print("Connection object is None")
#     except(Exception,psycopg2.DatabaseError) as error:
#         print("Error while connnecting to database{0}".format(error))
#
# if __name__ == "__main__":
#     create_tables([(1,"Sirajunnisa","Vijayawada"),(2,"Jani","Hyderabad"),(3,"Sona","Gujarath")])

















#
# def insert_tb_data(param_list):
#     try:
#         if con:
#             #if id is auto increament
#             select = "insert into Employee VALUES(%s,%s,%s)"
#             cur = con.cursor()
#             cur.executemany(select,param_list)
#             # result = cur.rowcount()
#             # print(result)
#             cur.close()
#             con.commit()
#         else:
#             print("Connection object is None")
#     except(Exception,psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if con is not None:
#             con.close()
#
#
# if __name__ == "__main__":
#     insert_tb_data([(4,"Sirajunnisa","Vijayawada"),(8,"Jani","Hyderabad"),(6,"Sona","Gujarath")])











# def insert_tb_data(name, id):
#     try:
#         if con:
#             #if id is auto increament
#             select = "UPDATE Employee SET Name = %s WHERE Id = %s"
#             cur = con.cursor()
#             cur.execute(select,(name,id))
#             cur.close()
#             con.commit()
#         else:
#             print("Connection object is None")
#     except(Exception,psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if con is not None:
#             con.close()
#
#
# if __name__ == "__main__":
#     insert_tb_data("Siraj",1)




#
# 123	"jareena"	"vijayawada"
# 121	"jareena"	"vijayawada"
# 122	"joh"	"vijaz"
# 124	"johna"	"Guntur"
# 125	"jothi"	"Srikakulam"
# 126	"jothi"	"Srikakulam"
# 127	"jothi"	"Srikakulam"
# 2	"Jani"	"Hyderabad"
# 3	"Sona"	"Gujarath"
# 4	"Sirajunnisa"	"Vijayawada"
# 8	"Jani"	"Hyderabad"
# 6	"Sona"	"Gujarath"
# 1	"Siraj"	"Vijayawada"