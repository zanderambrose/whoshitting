def is_all_caps(string):
    # Check if the string is not empty and contains only alphabetic characters
    if string and string.isalpha():
        # Check if the string is equal to its uppercase version
        if string == string.upper():
            return True
    return False


def is_br_element(string):
    # Check if the string is not empty and contains only alphabetic characters
    if string:
        # Check if the string is equal to its uppercase version
        if string == "<br/>":
            return True
    return False
