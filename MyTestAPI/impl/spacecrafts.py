import json
import sys

# Opening our database file (database.json)
file = open("MyTestAPI\impl\database.json")

# Loading our database:
data_base = json.load(file)


def GetSpacecraftId(options):
    """
    :param options: A dictionary containing all the parameters for the Operations
        options["spacecraftId"]: The unique identifier of the spacecraft

    """
    #Just testing below
    #print(options["spacecraftId"], file=sys.stderr)


    # Implement your business logic here 
    # All the parameters are present in the options argument
    spacecraft_to_find = {
        "id": "<SpacecraftId>",
        "name": "<string>",
        "type": "<string>",
        "description": "<string>",
    }
    
    for specific_spacecraft in data_base["spacecrafts"]:
        if (specific_spacecraft["id"] == int(options["spacecraftId"])):
            spacecraft_to_find = specific_spacecraft
            break
            #print("spacecraft found", file=sys.stderr)
    
    return json.dumps(spacecraft_to_find), 200

    #This is testing
    # Returning the exact values instead of placeholders (specific_spacecraft was i) check test.py for more info.
    # return json.dumps({
    #     "description": specific_spacecraft["description"],
    #     "id": options["spacecraftId"],
    #     "name": specific_spacecraft["name"],
    #     "type": specific_spacecraft["type"],
    # }), 200


def PutSpacecraftId(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["spacecraftId"]: The unique identifier of the spacecraft

    """
    #Similar logic here just like with the get.
    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "description": "<string>",
        "id": "<SpacecraftId>",
        "name": "<string>",
        "type": "<string>",
    }), 200
