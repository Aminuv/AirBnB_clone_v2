#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class State(BaseModel, Base):
    """ Represents the State class """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """ getter for the cities attribute """
            from models import storage

            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
