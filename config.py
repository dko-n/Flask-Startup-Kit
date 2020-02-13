'''
    name: config.py
    description: Application configuratin file.
    author: On Kato
'''

DATABASE_CONFIG = {
    "ENGINE" : "mysql+pymysql",
    "USER" : "root",
    "PASSWORD" : "",
    "HOST": "localhost",
    "DATABASE_NAME" : "test",
    "CHARSET" : "utf-8"
}

# DATABASE URL
SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}/{}?charset={}".format(
    DATABASE_CONFIG["ENGINE"], 
    DATABASE_CONFIG["USER"], 
    DATABASE_CONFIG["PASSWORD"], 
    DATABASE_CONFIG["HOST"], 
    DATABASE_CONFIG["DATABASE_NAME"], 
    DATABASE_CONFIG["CHARSET"]
)

SQLALCHEMY_TRACK_MODIFICATIONS = False