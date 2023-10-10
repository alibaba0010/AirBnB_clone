#!/usr/bin/python3

"""
    This module defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ The Base Model class """
    def __init__(self, *args, **kwargs):
        """ This method initializes an instance """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'id':
                    self.id = value
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ This method defines a custom string method """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ This method updates the "updates_at" with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing
            all keys/values of __dict__ of the instance
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        result_dict = {}
        result_dict['__class__'] = self.__class__.__name__
        result_dict.update(self.__dict__)
        return result_dict
