#!/usr/bin/python3

"""
    This module defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ The Base Model class """
    def __init__(self, *args, **kwargs):
        """ This method initializes an instance of a model """
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(val,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(val,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'id':
                    self.id = val
                else:
                    setattr(self, key, val)
        else:
            from models import storage                       
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ This method defines a custom string method 
            Returns a string representation of the instance
        """
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ This method updates the "updates_at" with the current datetime """
        from models import storage        
        self.updated_at = datetime.now()
        storage.save()
        

    def to_dict(self):
        """ returns a dictionary containing
            all keys/values of __dict__ of the instance
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        result_dictionary = {}
        result_dictionary['__class__'] = self.__class__.__name__
        result_dictionary.update(self.__dict__)
        return result_dictionary
