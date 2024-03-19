#!/usr/bin/python3
"""A module that deletes a state"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
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
        state_delete = session.query(State).filter(
                State.name.contains('a')).all()
        if state_delete:
            for state in state_delete:
                session.delete(state)
            session.commit()
