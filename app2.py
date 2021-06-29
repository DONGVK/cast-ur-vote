# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 10:38:33 2021

@author: pierr
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, ForeignKey
"""
MYSQL_HOST = "172.17.0.2"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "secret"
MYSQL_DB = "users"
 
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER,
MYSQL_PWD,
MYSQL_HOST,
MYSQL_PORT,
MYSQL_DB)
 
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
 
session = Session()
 
Base = declarative_base()
"""
class Candidate(Base):
 
__tablename__ = "candidate"
 
email = Column(String(120), unique=True, nullable=False, primary_key=True)
nom = Column(String(80), nullable=False)
prenom = Column(String(80), nullable=False)
ville = Column(String(80), nullable=False)
birth_date = Column(String(80), nullable=False)
 
def add_candidate(email, nom, prenom, ville, birth_date):
try:
user = User(email=email,
nom=nom,
prenom=prenom,
ville=ville,
birth_date=birth_date)
session.add(candidate)
session.commit()
 
return True
 
except Exception as e:
print(e)
 
return False
 
def get_candidate_by_id(email):
try:
result = session.query(Candidate).filter_by(email=email).first()
return result
except Exception as e:
print(e)
return False
 
def get_all_candidate():
try:
result = session.query(Candidate).filter_by()
 
return result
except Exception as e:
print(e)
return False
 
def delete_candidate_by_id(email):
try:
candidate_to_delete = get_candidate_by_id(email)
if candidate_to_delete :
session.delete(candidate_to_delete)
session.commit()
return True
else:
return False
except Exception as e:
print(e)
return False
