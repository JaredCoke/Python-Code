"""
JSON: Lighweight data format used for data exchange. Heavily used in web application
JSON: Javascript Object Notation
"""

### Deserialization | Decoding: Converting JSON data to Python object

## Loading a Custom Python object from a JSON file
import json

class User:

    def __int__(self,name,age): # create a custom method
        self.name = name
        self.age = age

user = User('Max',27)

def encode_user(o): #create a custom encoding function to handle JSON-python data/objects
    if isinstance(o,User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__:True}
    else:
        raise TypeError('Whoa - Object of type User is not JSON serializable.')

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,User):
            return {'name':o.name, 'age':o.age, o.__class__.__name__:True}
        return JSONEncoder.default(self,o)

userJSON = json.dumps(user, cls= UserEncoder)
print(userJSON)