#!/usr/bin/python3

"""
a module that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = 3306
    mysql_url = f"mysql+mysqldb://{username}:{password}\
            @{host}:{port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        added_state = State(name="Louisiana")
        session.add(added_state)
        session.commit()
        print(added_state.id)
