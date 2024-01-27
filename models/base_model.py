#!/usr/bin/python3
"""
"""
from datetime import datetime
import uuid
class BaseModel:
    """this is a class that defines all common attributes of other classes"""
    def __init__(self):
        """method used to assign uuid when an instance is created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    def save(self):
        """updates the current time an instance was saved"""
        self.updated_at = datetime.utcnow()
    def to_dict(self):
        """return a dictionary containing keys and values"""
        inst_dict = self.__dict__.copy()
        inst_dict["class"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict
    def __str__(self):
        """prints the class nam, id and the dictionary"""
        class_name = self.__class__.__name__
        return "[{}] ({}) [{}]".format(class_name,self.id,self.__dict__)
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
       print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


