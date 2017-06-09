#!/usr/bin/python3
import uuid
import json

'File storage module'


class FileStorage:
    'FileStorage class'
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        'Returns __objects'
        return self.reload()

    def new(self, obj):
        'adds an object to the instance'
        from models.base_model import BaseModel
        import uuid

        class_name = str(obj.__class__.__name__)
        obj_id = str(obj.id)
        obj_str = class_name + "." + obj_id
        FileStorage.__objects[obj_str] = obj

    def save(self):
        'serializes __objects to JSON file'
        from models.base_model import BaseModel
        new_dict = {}

        for keys in self.__objects.keys():
            value = self.__objects[keys]
            if isinstance(value, (dict, tuple, set)):
                new_dict[keys] = BaseModel.to_json(value)
                if type(value) is dict:
                    for keys1 in value.keys():
                        value1 = value[keys1]
                        if isinstance(value1, (dict, tuple, set)):
                            new_dict[keys1] = BaseModel.to_json(value1)
                        else:
                            new_dict[keys1] = BaseModel.to_json(value1)
            else:
                new_dict[keys] = BaseModel.to_json(value)
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        'deserializes the JSON file to __objects'
        from models.base_model import BaseModel
        print("above try")
        try:
            print(self.__file_path)
            print("in try")
            with open('file.json', "r", "utf-8") as f:
                print("hey")
                reloaded = json.load(f)
                print("reloaded: {} ".format(reloaded))
                for k in reloaded.key():
                    self.__objects[k] = BaseModel(**reloaded[k])
                print(self.__objects)
                return self.__objects
        except:
            print("FAIL")
            return {}
