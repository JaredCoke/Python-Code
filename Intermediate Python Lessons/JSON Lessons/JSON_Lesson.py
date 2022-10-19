"""
JSON: Lighweight data format used for data exchange. Heavily used in web application
JSON: Javascript Object Notation
Serialization | Encoding = converting from python to JSON
Deserialization | Decoding = converting from JSON to python
"""

### [Serialization] Convert python Object (nested list) into a JSON object
import json

# define the python nested list
person = {"name":"Jamal", "age":30, "city":"New York", "hasChildren":False, "titles":["engineer","programmer"]} #create a nested list

# convert to JSON object
personJSON = json.dumps(person)
print('This is the unmodified default python-JSON format:')
print(personJSON)

print('')


### [Serialization] Convert python nested list into a JSON object using Default JSON format:
import json

# define the python nested list
personA = {"name":"Jamal", "age":30, "city":"New York", "hasChildren":False, "titles":["engineer","programmer"]} #create a nested list

# convert to JSON object
personJSONA1 = json.dumps(personA, indent=4, separators=(': ', '= ')) # here's a decent way to format | dumps a string
personJSONA = json.dumps(personA, indent=4, sort_keys=True) #preferred way to format | dumps a string
print('This is the modified decent python-JSON format:')
print(personJSONA1)
print('This is the modified best python-JSON format:')
print(personJSONA)

print('\n')


### [Serialization] Converting & Dumping to a File
import json

# define the python nested list
personB = {"name":"Jamal", "age":30, "city":"New York", "hasChildren":False, "titles":["engineer","programmer"]} #create a nested list

# convert to JSON object
personJSONB = json.dumps(personA, indent=4, sort_keys=True) #preferred way to format
print('This is the modified best python-JSON format:')
print(personJSONB)

with open('person.json','w') as file:
    #json.dump(person, file) # default un JSON format write
    json.dump(person, file, indent=4) #JSON format write

print('\n')



### Deserialization | Decoding: Converting JSON data to Python object

## Loading from a JSON string
import json

personB1 = {"name":"Jamal", "age":30, "city":"New York", "hasChildren":False, "titles":["engineer","programmer"]} #create a nested list
personJSONB1 = json.dumps(personA, indent=4, sort_keys=True) #preferred way to format

personB1 = json.loads(personJSONB1) # loads from a string and converts to a Python nested list
print(personB1)

print('')


## Loading from a JSON file
import json

personB2 = {"name":"Jamal", "age":30, "city":"New York", "hasChildren":False, "titles":["engineer","programmer"]} #create a nested list
personJSONB2 = json.dumps(personA, indent=4, sort_keys=True) #preferred way to format

with open('person.json','r') as file:
    personB2 = json.loads(personJSONB2) # loads from a string and converts to a Python dictionary
    print('This is JSON data converted back to a Python object')
    print(personB2)