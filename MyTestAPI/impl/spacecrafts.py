import json


def GetSpacecraftId(options):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["spacecraftId"]: The unique identifier of the spacecraft

    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "description": "<string>",
        "id": "<SpacecraftId>",
        "name": "<string>",
        "type": "<string>",
    }), 200


def PutSpacecraftId(options, body):
    """
    :param options: A dictionary containing all the paramters for the Operations
        options["spacecraftId"]: The unique identifier of the spacecraft

    :param body: The parsed body of the request
    """

    # Implement your business logic here
    # All the parameters are present in the options argument

    return json.dumps({
        "description": "<string>",
        "id": "<SpacecraftId>",
        "name": "<string>",
        "type": "<string>",
    }), 201



