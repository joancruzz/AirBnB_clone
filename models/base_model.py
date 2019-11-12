#!/usr/bin/python3


"""
This is a BaseModel module for base class
"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """Represents a base class"""

    def __init__(self, *args, **kwargs):
        """ initialize an instance potentially with a dictionary argument"""
        if kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime
                            (v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()
        if not kwargs or len(kwargs) == 0:
            models.storage.new(self)

    def __str__(self):
        """ overwrite string special method """
        out = "[{}] ({}) {}".format(type(self).__name__, self.id,
                                    self.__dict__)
        return out

    def save(self):
        """Updates 'updated_at' with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict
