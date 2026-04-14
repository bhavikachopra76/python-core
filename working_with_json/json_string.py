import json

# JSON string
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "email": null,
            "has_license": true
        }
    ]
}
'''

# Converting JSON string to python object
data = json.loads(people_string)
# Easily using the JSON string as a python object to loop through it
for people in data['people']:
    del people['phone']

# Converting python object back to JSON string
json_string = json.dumps(data , indent = 4)
print(json_string)

