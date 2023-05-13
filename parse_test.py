import json

with open('forecast.json', 'r') as file:
    json_str = file.read()

# parse the JSON string
json_obj = json.loads(json_str)

# function to recursively parse nested objects and arrays
def parse_json(json_obj):
    # loop through all the items in the object or array
    for key, value in json_obj.items() if isinstance(json_obj, dict) else enumerate(json_obj):
        if isinstance(value, (dict, list)):
            # if the value is a nested object or array, call the function recursively
            parse_json(value)
        else:
            # if the value is a primitive type (string, number, boolean), print it
            print(key, value)

# call the function with the parsed object
parse_json(json_obj)
