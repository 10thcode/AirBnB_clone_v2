#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if (environ.get("HBNB_TYPE_STORAGE", "na") == "db"):
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(ForeignKey("states.id"),
                          nullable=False)
    else:
        name = ""
        state_id = ""
