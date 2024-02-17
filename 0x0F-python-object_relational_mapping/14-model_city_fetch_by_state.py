#!/usr/bin/python3
''' query state.name city.id and city.name '''
import sys
from model_state import Base, State
from model_cities import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    all_city = session.query(State.name, City.id,
                             City.name).filter(State.id == City.state_id)
    for each in all_city:
        print('{}: ({}) {}'.format(each[0], str(each[1]), each[2]))
