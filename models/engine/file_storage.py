s module defines a class to manage file storage for hbnb clone"""	"""This module defines a class to manage file storage for hbnb clone"""
import json	import json
class FileStorage:	class FileStorage:
    """This class manages storage of hbnb models in JSON format"""	    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'	    __file_path = 'file.json'
    __objects = {}	    __objects = {}


    def all(self):	    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""	        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects	        if cls is None:
            return FileStorage.__objects
        else:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    obj_dict[key] = value
            return obj_dict


    def new(self, obj):	    def new(self, obj):
        """Adds new object to storage dictionary"""	        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})	        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
    def save(self):	    def save(self):
        """Saves storage dictionary to file"""	        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:	        with open(FileStorage.__file_path, 'w') as f:
            temp = {}	            temp = {}
            temp.update(FileStorage.__objects)	            temp.update(FileStorage.__objects)
            for key, val in temp.items():	            for key, val in temp.items():
                temp[key] = val.to_dict()	                temp[key] = val.to_dict()
            json.dump(temp, f)	            json.dump(temp, f)
    def reload(self):	    def reload(self):
        """Loads storage dictionary from file"""	        """Loads storage dictionary from file"""
        from models.base_model import BaseModel	        from models.base_model import BaseModel
        from models.user import User	        from models.user import User
        from models.place import Place	        from models.place import Place
        from models.state import State	        from models.state import State
        from models.city import City	        from models.city import City
        from models.amenity import Amenity	        from models.amenity import Amenity
        from models.review import Review	        from models.review import Review


        classes = {	        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,	            'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,	            'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review	            'Review': Review
                  }	        }
        try:	        try:
            temp = {}	            temp = {}
            with open(FileStorage.__file_path, 'r') as f:	            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)	                temp = json.load(f)
                for key, val in temp.items():	                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)	                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:	        except FileNotFoundError:
            pass	            pass

    def delete(self, obj=None):
        """deletes an object"""
        if obj is not None:
            key = obj.__class__.__name__+'.'+obj.id
            if key in self.__objects:
                del self.__objects[key]
0 comments on commit c7d84aa
