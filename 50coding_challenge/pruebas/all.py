
# 1. Rad to Degree Conversion
# Craft a Python function that accepts a single numeric argument, 
# representing an angle in radians. This function converts radians into 
# degrees and returns the degree value.
# Formula::multiply the number of radians by 180/π.

# def rad_deg(ang_rad):
#     pi = 3.14159265359
#     con = (ang_rad * 180/pi)
#     return con

# print(rad_deg(3))

# 2. List Sorting

# Idear -Devise a Python function taking a list of numbers and 
# a second parameter with options: "asc", "desc", or "none". If "asc", 
# return numbers in ascending order; if "desc", in descending order; if "none", 
# return the list as is.
# lista = []
# def my_func(lista, opt):
#     if opt == "desc":
#         lista.sort(reverse=True)
#     elif opt == "asc":
#         lista.sort(reverse=False)
#     elif opt == "none":
#         lista
#     return lista

# print(my_func([2,1,3,4,12], "desc"))

# 7. Duplicate Characters
# Create a function taking strings as input. 
# Output a string with each character doubled. 
# For instance, input "now" rendimiento -yields "nnooww". 

# def my_func(cadena):
#     new_cadena = ""
#     for x in cadena:
#         new_cadena += f"{x}{x}"
#     return new_cadena

# print(my_func("now"))

# 6. Extract Integers from Mixed List
# Shape a Python function, "get_integers," which sifts -colar
# integers from a mixed list of non-negative integers and strings. 
# Return the filtered integers, maintaining the original order.
# var = 4
# print(type(int))

# def get_integers(lista):
#     for li in lista:
#         if type(li) == int:
#             print(f'{li} int' )
#         elif type(li) == str:
#             print(f'{li} str' )


# get_integers(["mundo",2,3,6,"hola"]) 

# 4. Counting String Vowels
# Construct a Python function that tallies vowels in a word. 
# Iterate through each character using a loop, 
# checking for vowels (uppercase/lowercase). Return the count of vowels found.

def my_func(word):
    cont = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for letter in word:
        # print(letter)
        for vowel in vowels:
            if letter == vowel:
                cont += 1
            # print(f'{letter} letras, {vowel} vocales.')      
    return cont           

print(my_func('HoOlaaa'))