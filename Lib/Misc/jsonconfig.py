from ..Misc.logs import *
import json

def GetJSONConfig(file_path): 
    """
    Retrieve and return a JSON configuration from the specified file as a dictionary.
    
    Parameters:
    - file_path (str): The path to the JSON file.

    Returns:
    - dict: A dictionary containing the JSON configuration.

    Exceptions:
    - FileNotFoundError: Raised if the specified file is not found.
    - json.JSONDecodeError: Raised if there is an error decoding the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        return -1
    except json.JSONDecodeError:
        return -2
