#!/usr/bin/python3
"""
a module that changes the name of
a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = "3306"
    mysql_url = f"mysql+mysqldb://{username}:{password}@{host}:\
        {port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        change_state = session.query(State).filter_by(id=1).first()
        change_state.name = "New Mexico"
        session.commit()
