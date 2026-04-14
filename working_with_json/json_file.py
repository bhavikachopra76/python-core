import json

# Load JSON file into a python object
with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'] , state['abbreviation'])

marks = {
    "people" : [
        {
            "name" : "John",
            "chemistry" : 85,
            "physics" : 90,
            "maths" : 78
         },
        {
            "name" : "Jane",
            "chemistry" : 95,
            "physics" : 85,
            "maths" : 90
        },
        {
            "name" : "Bob",
            "chemistry" : 75,
            "physics" : 90,
            "maths" : 80
        }
    ]
}

with open('marks.json', 'w') as f:
    json.dump(marks , f, indent = 4)

