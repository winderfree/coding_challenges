# 36. Create a function that converts a string to an array of characters
def string_to_array(cadena:str):
    chars = []
    for x in cadena:
        chars.append(x)
    return chars
print(string_to_array("Hola mundo"))