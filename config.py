'''
    name: config.py
    description: Application configuratin file.
    author: On Kato
'''

import binascii
import os

# Secret key gen
SECRET_KEY = binascii.hexlify(os.urandom(36))

# DATABASE URL
DATABASE_CONFIG = {
    "ENGINE" : "mysql+pymysql",
    "USER" : "root",
    "PASSWORD" : "",
    "HOST": "localhost",
    "DATABASE_NAME" : "flask",
    "CHARSET" : "utf8"
}

SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}/{}?charset={}".format(
    DATABASE_CONFIG["ENGINE"], 
    DATABASE_CONFIG["USER"], 
    DATABASE_CONFIG["PASSWORD"], 
    DATABASE_CONFIG["HOST"], 
    DATABASE_CONFIG["DATABASE_NAME"], 
    DATABASE_CONFIG["CHARSET"]
)

# Model Files Directory Name
MODEL_DIR = "models"