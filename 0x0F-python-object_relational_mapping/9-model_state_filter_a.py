#!/usr/bin/python3
"""lists state objects that contain letter a in them"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    username, password, database = argv[1], argv[2], argv[3]

    host = "localhost"
    port = 3306
    url_mysql = f"mysql+mysqldb://{username}:{password}@{host}:\
              {port}/{database}"
    engine = create_engine(url_mysql, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        with_letter = session.query(State).order_by(State.id)\
                .filter(State.name.like("%a%")).all()
        if with_letter:
            for state in with_letter:
                print(f"{state.id}: {state.name}")
