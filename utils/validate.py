import re

def not_empty(input):
    if not input:
        raise ValueError("Input Cannot be Empty")
    return True

def validate_length(input, expected_length):
    if(len(input) < expected_length):
        raise ValueError("Input needs more characters")
    elif(len(input) > expected_length):
        raise ValueError("Input is too long")
    else:
        return True

def validateAlphaNumeric(input):
    pattern = r"^[a-zA-Z0-9]+$"  # alphanumeric characters only

    if not re.match(pattern, input):
        raise ValueError("Input does not match required pattern")
    return True

def validateString(input):
    if not isinstance(input, str):
        raise ValueError("Input must be a String")
    return True

def validateFloat(input):
    if not isinstance(input, float):
        raise ValueError("Input must be a Float")
    return True

def validateInt(input):
    if not isinstance(input, int):
        raise ValueError("Input must be a Integer")
    return True