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
    # Implement your business logic here 
    # All the parameters are present in the options argument
    spacecraft_to_find = {
        "id": "<SpacecraftId>",
        "name": "<string>",
        "type": "<string>",
        "description": "<string>",
    }
    spacecraft_found = False
    
    for specific_spacecraft in data_base["spacecrafts"]:
        if (specific_spacecraft["id"] == int(options["spacecraftId"])):
            spacecraft_to_find = specific_spacecraft
            spacecraft_found = True
            break

    #Equivalent to: "spacecraft_found is True"
    if spacecraft_found:
        return json.dumps(spacecraft_to_find), 200
    else:
        return json.dumps(f'No spacecraft found for the provided `spacecraftId`: {options["spacecraftId"]}'), 404


def PutSpacecraftId(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["spacecraftId"]: The unique identifier of the spacecraft

    """

    # Implement your business logic here
    # All the parameters are present in the options argument
    # In our case, you cannot use PUT to update the ID of a spacecraft

    #for specific_spacecraft in data_base["spacecrafts"]:
    #    if (specific_spacecraft["id"] == int(options["spacecraftId"])):

    print(options, file = sys.stderr)



    return json.dumps({
        "description": "<string>",
        "id": "<SpacecraftId>",
        "name": "<string>",
        "type": "<string>",
    }), 200
