# 7.	Write a code in Python to find out whether 
# a given string S is a valid regex or not.


# 5.	Write a function in Python to parse a string 
# such that it accepts a parameter- an encoded string. 
# This encoded string will contain a first name, 
# last name, and an id. You can separate the values 
# in the string by any number of zeros. The id will 
# not contain any zeros. The function should return 
# a Python dictionary with the first name, last name, 
# and id values. For example, if the input would be "John000Doe000123". 
# Then the function should return: 
# { "first_name": "John", "last_name": "Doe", "id": "123" }
# first_name , last_name, id = "Juan" , "Casado", "123" 
# encode_str = f'{first_name}{last_name}{id}'
def parse_string(encode_str:str):
    enc = encode_str.split("0") 
    enc_new = []
    new_ar = {}
    for x in enc:
        if x != "":
            enc_new.append(x)
    new_ar.update({
                "first_name": enc_new[0],
                "last_name": enc_new[1],
                "id": enc_new[2]
            })
    print(*enc_new)
    print(new_ar)
print(parse_string("0000Juan000Casado00000123"))


# 4.	Write a function to find the domain name 
# from the IP address. The function will accept 
# an IP address, make a DNS request, and return 
# the domain name that maps to that IP address 
# while using records of PTR DNS. 
# You can import the Python socket library.

# import socket
# # print([x for x in socket.gethostname()])

# print([(f"{x}") for x in socket.getaddrinfo("127.0.0.1","8080")])
# def domain_name(IP_address):
#     #make a DNS request
#     var_domain_name = ("129.0.0.1")
#     return var_domain_name





# 3.	Write a function to detect 13th Friday. 
# The function can accept two parameters, and 
# both will be numbers. The first parameter will 
# be the number indicating the month, and the 
# second will be the year in four digits. Your 
# function should parse the parameters, and 
# it must return True when the month contains
# a Friday with the 13th, else return False. 
# import time
# import calendar
# def detect_13_friday(month:int, year:int):    
#     for x in calendar.Calendar.itermonthdates(calendar.Calendar(),year,month):
#         print(x.strftime("%d"), x.strftime("%w"))
#         if x.strftime("%d") == "13" and x.strftime("%w") == "5": 
#             print(f'{x.strftime("%a")}-{x.strftime("%w")} - dia:{x.strftime("%d")} - {x.strftime("%B")}:{x.strftime("%Y")} ')
#             return True
#             # break
#     return False
# print(detect_13_friday(11,2025))
# print([calendar.Calendar(2024).firstweekday == 1])



# 1.	Write a function in Python to check
# duplicate letters. It must accept a string, 
# i.e., a sentence. The function should 
# return True if the sentence has any word 
# with duplicate letters, else return False. 

# def duplicate_letters(s):
#     var = False
#     for letter in s:
#         if s.count(letter) > 1:
#             var = True
#             return var
#             # break
#     return var

# print(duplicate_letters("hoa"))