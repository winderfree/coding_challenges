# 37. Create a function that will convert a string in an array containing the ASCII codes of 
# each character
def convert_str_to_array_ascii_codes(string:str):
    ascii_codes = []
    for x in string:
        ascii_codes.append(ord(x))
    return f'El ascii array es: {ascii_codes}'

# print(convert_str_to_array_ascii_codes("hola pepe"))
# print(ord("w"))
# print(chr(119))
# 38. Create a function that will convert an array containing ASCII codes in a string

def array_ascii_codes_to_convert_str(ar)->str:
    convert_str = ""
    for x in ar:
        print(chr(x))
        convert_str+=chr(x)
    return f'El ascii array es: {convert_str}'
print(array_ascii_codes_to_convert_str([104, 111, 108, 97, 32, 112, 101, 112, 101]))