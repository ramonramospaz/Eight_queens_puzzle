#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

database_uri="sqlite:///sqlalchemyQueensPuzzle.db"
    
Base = declarative_base()

class History(Base):
    __tablename__ = 'History'
    id = Column(Integer, primary_key=True)
    result = Column(String)
    number_row = Column(String)

    def __repr__(self):
        return "<History(result='%s', number_row='%s')>" % (self.result, self.number_row)

def check_database_exist():
    db = create_engine(database_uri)
    try:
        db.connect()
        db.execute('SELECT * FROM History')
    except Exception:
        # Switch database component of the uri
        print("Create New database")
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
        print(instance.result, instance.number_row)