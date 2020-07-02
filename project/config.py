# from configparser import ConfigParser
# def config(filename = "database.ini", session = 'postgresql'):
#     db = {}
#     parser = ConfigParser()
#     parser.read(filename)
#     if parser.has_section(session):
#         params = parser.items(session) # parser returns list of tuples
#         for param in params:  # iterate list of tuples and get each tuple one by one
#             db[param[0]] = param[1] # store into dictionary
#     else:
#         raise Exception("session not found{0}{1}".format(filename,session))
#
#
#     return db
#
#
# config()