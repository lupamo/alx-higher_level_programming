#!/usr/bin/python3

"""module that prints cities in a database"""

from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = 3306
    mysql_url = f"mysql+mysqldb://{username}:{password}@{host}:\
        {port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_state = State(name="California",
                          cities=[City(name="San  Francisco")])
        session.add(new_state)
        session.commit()
