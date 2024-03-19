#!/usr/bin/python3

"""listing city objects from database"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

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
        qry_rslt = session.query(State, City).filter(
                City.state_id == State.id).order_by(City.id).all()
        for row in qry_rslt:
            print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))

    session.close()
