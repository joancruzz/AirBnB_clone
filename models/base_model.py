#!/usr/bin/python3


"""
This is a BaseModel module for base class
"""


import models
import uuid
import datetime


class BaseModel:
    """Represents a base class"""

    def __init__(self, *args, **kwargs):
        """Initiate class constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def  __str__(self):
        """Return class name, id, dict"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.to_dict)

    def save(self):
        """Updates 'updated_at' with current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__"""
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__items():
            if isinstance(value, datetime) is True:
                value = value.isoformat()
            my_dict[key] = value    
        return my_dict
