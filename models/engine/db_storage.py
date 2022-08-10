#!/usr/bin/python3
"""DBStorage module"""

import MySqldb
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from models.engine.FileStorage import classes
import os
from models.base_models import Base
USER = os.environ.get('HBNB_MYSQL_USER')
PWD = os.environ.get('HBNB_MYSQL_PWD')
HOST = os.environ.get('HBNB_MYSQL_HOST')
DB = os.environ.get('HBNB_MYSQL_DB')
ENV = os.environ.get('HBNB_ENV')

Class DBStorage():
    """Class DBStorage"""

    __engine = None
    __session = None

    __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(USER, PWD, HOST, DB), pool_pre_ping=True)
        if ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """List from database"""
        if cls:
            objs = self.__session.query(self.classes()[cls])
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()

	dic = {}
	        for obj in objs:
	            k = '{}.{}'.format(type(obj).__name__, obj.id)
        	    dic[k] = obj
        return dic
    def new(self, obj):
        """"""
        self.__session.add(obj)
    def save(self):
        """Commits changes of current session"""
        self.__session.commit()

    def delete(self, obj=None)
        """Deletes object from current DB session if obj not None"""
        if obj:
            self.__session.delete(obj)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Reloads current db session from engine"""
        from models.state import state
        from models.city import city
        from models.user import user
        from models.review import review
        from models.amenity import amenity
        from models.place import place

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      exire_on_commit=False)
        Session = scoped_session(self.session)
        self.__session = Session()
