#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, event, DDL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
import psycopg2
import time

database_host="postgresql"
database_port=""
#Use for local test
#database_host="localhost"
#database_port=":5432"
database_uri=f"postgres://postgres:secret@{database_host}{database_port}/postgres"


Base = declarative_base()

class History(Base):
    __tablename__ = 'History'
    #comment __table_args__ if you are going to use sqlite
    __table_args__ = {'schema': 'sqlalchemyqueenspuzzle'}
    id = Column(Integer, primary_key=True)
    result = Column(String)
    number_row = Column(String)

    def __repr__(self):
        return "<History(result='%s', number_row='%s')>" % (self.result, self.number_row)


def check_database_exist():
    while(check_postgres_database_conection()==False):
        print("The postgres is not up yet")
        time.sleep (5000.0 / 1000.0);
    check_postgres_database_exist()
    

def check_postgres_database_conection():
    try:
        conn = psycopg2.connect(f"user='postgres' host='{database_host}' password='secret' connect_timeout=1 ")
        conn.close()
        return True
    except:
        return False

def check_postgres_database_exist():
    db = create_engine(database_uri)
    try:
        db.connect()
        db.execute('SELECT * FROM History')
    except Exception:
        # Switch database component of the uri
        print("Create New postgres database")
        event.listen(Base.metadata, 'before_create', DDL("CREATE SCHEMA IF NOT EXISTS sqlalchemyqueenspuzzle"))
        db = create_engine(database_uri)
        Base.metadata.create_all(db)


def insert_result_queens_puzzle(number_row,result): 
    db = create_engine(database_uri)
    Base.metadata.bind = db
    DBSession = sessionmaker(bind=db)
    session = DBSession()
    new_History=History(result=result,number_row=number_row)
    session.add(new_History)
    session.commit()

def show_results_queens_puzzle():
    db = create_engine(database_uri)
    Base.metadata.bind = db
    DBSession = sessionmaker(bind=db)
    session = DBSession()
    for instance in session.query(History).order_by(History.id):
        print("-----------------------------------------------------------------")
        print(instance.result+" Size:"+ instance.number_row)