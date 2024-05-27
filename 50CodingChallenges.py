# 1. Print numbers from 1 to 10
# print([x for x in range(1,11)])
# 2 print odd numbers impares
# odd_numbers = [x for x in range(0,100) if x%2==1]
# print(odd_numbers) 
# 3. Print the multiplication table with 7
# num = 7
# for x in range(12):
#     print(f'la tabla de 7\n {num} * {x} = {num*x}')
# 4. Print all the multiplication tables with numbers from 1 to 10
# for x in range(1,11):
#     print("La tabla del ", x)
#     for y in range(1,11):
#         print(f'{x} * {y} = {x*y}')
# 5. Calculate the sum of numbers from 1 to 10
# suma=0
# for x in range(1,11):
#     print(f'x:{x}, suma:{suma}')
#     suma += x
# print(suma)
# 6. Calculate 10!
# multi=1
# for x in range(1,11):
#     print(f'x:{x}, multi:{multi}')
#     multi *= x
# print(multi)
# 7. Calculate the sum of even numbers greater than 10 and less than 30
# suma:int = 0
# for x in range(30):
#     if x > 10 and x < 30:
#         suma += x
#         # print(suma)
# print(suma)

# 8. Create a function that will convert from Celsius to Fahrenheit
# Grados Fahrenheit = (grados centígrados × 9/5) +32.
# def cel_to_far(cel):
#     far = (cel * 9/5)+32
#     return far
# print(cel_to_far(60))

# 9. Create a function that will convert from Fahrenheit to Celsius

# 10. Calculate the sum of numbers in an array of numbers
# cont = 0
# for x in [1,2,3,6]:
#     cont+=x
# print(cont)

# 11. Calculate the average of the numbers in an array of numbers
# cont = 0
# ar = [5,6,4,5,6,7]
# for x in ar:
#     cont+=x
# print(cont/len(ar))

# 12. Create a function that receives an array of numbers as argument and returns an 
# array containing only the positive numbers
# def posite_numbers(ar):
#     result_ar = [x for x in ar if x >= 0 ]
#     return result_ar
# print(posite_numbers([1,-1,3,7,-10,9]))

# 13. Find the maximum number in an array of numbers
# cont = 0
# ar_num = [0,3,23,43,12,77]
# for x in ar_num:
#     if x > cont:
#         cont = x
# print(cont)

# 14. Print the first 10 Fibonacci numbers without recursion
# x, y = 0, 1
# for z in range(10):
#     print(f'x = {x}'"\n")
#     x, y = y, x+y
#     print(f'y = {y}')

# 15. Create a function that will find the nth Fibonacci number using recursion

# 16. Create a function that will return a Boolean specifying if a number is prime
# def is_prime(number):
#     for x in range(2,number):
#         if number % x==0:
#             print(f'Es primo tiene {x} como divisor')
#             return False
#     return True
# print(is_prime(96))

# 17. Calculate the sum of digits of a positive integer number
# num_positive = int(input("insertar un número entero positivo:"))
# if num_positive > 0:
#     suma = 0
#     for x in str(num_positive):
#         suma += int(x)
#         print(x)
#     print("la suma es:",suma)
# else:
#     print("ïnsertar valores positivos")

# 18. Print the first 100 prime numbers
# cont = 0
# numero = 11
# texto = ""
# lista_resultado = []
# for y in range(1, 100):
#     for x in range(2,y):
#         if y % x==0:
#             texto = f"el {y} es par"
#             lista_resultado.append(texto)
#             # print(f'{numero} par tiene numero: {numero} con {x} como divisor')
#             cont+=1
#             texto = " "
#         elif y >= x:
#             texto = f"el {y} es impar"
#             lista_resultado.append(texto)
#             cont=0
#             texto=" "
#             # print(f' numero: {numero}, no par cont {x} como divisor')
#         if cont > 0:
#             texto = " "
#         else:
#             texto = " "
        
# # print(f'result {texto}')
# print(lista_resultado)
# def es_primo(num, n=2):
    # if n >= num:
    #     print("Es primo")
    #     return True
    # elif num % n != 0:
    #     return es_primo(num, n + 1)
    # else:
    #     print("No es primo", n, "es divisor")
    #     return False
# new_ar = []
# for x in range(2,100):
#     for numero in range(2,numero):
#         if x % numero == 0 :
#             print(f'firtnum{x} num:{numero}')
#         else:print(x)
# print(new_ar)
# 19. Create a function that will return in an array the first “p” prime numbers 
# greater than “n”
# 20. Rotate an array to the left 1 position
# 21. Rotate an array to the right 1 position
# 22. Reverse an array
# 23. Reverse a string
# 24. Create a function that will merge two arrays and return the result as a new 
# array
# 25. Create a function that will receive two arrays of numbers as arguments and 
# return an array composed of all the numbers that are either in the first array 
# or second array but not in both
# 26. Create a function that will receive two arrays and will return an array with 
# elements that are in the first array but not in the second

# 27. Create a function that will receive an array of numbers as argument and will return a 
# new array with distinct elements
# 28. Calculate the sum of first 100 prime numbers and return them in an array
# 29. Print the distance between the first 100 prime numbers
# 30. Create a function that will add two positive numbers of indefinite size. The numbers 
# are received as strings and the result should be also provided as string.
# 31. Create a function that will return the number of words in a text
# 32. Create a function that will capitalize the first letter of each word in a text
# 33. Calculate the sum of numbers received in a comma delimited string
# 34. Create a function that returns an array with words inside a text. 
# 35. Create a function to convert a CSV text to a “bi-dimensional” array
# 36. Create a function that converts a string to an array of characters
# 37. Create a function that will convert a string in an array containing the ASCII codes of 
# each character
# 38. Create a function that will convert an array containing ASCII codes in a string
# 39. Implement the Caesar cypher


# boleano = True
# name = "juan" if boleano == False else "Jose"
# print(name)
# lista1 = [12,3]
# lista2 = [4,3]
# resulta = lista1+lista2
# print(resulta)
# def prueba(aas:str | None=None):
#     if aas:
#         return aas
#     else:
#         return "None"

# 40. Implement the bubble sort algorithm for an array of numbers

# 41. Create a function to calculate the distance between two points defined by their x, y 
# coordinates

# 42. Create a function that will return a Boolean value indicating if two circles 
# defined by center coordinates and radius are intersecting
# 43. Create a function that will receive a bi-dimensional array as argument and a 
# number and will extract as a unidimensional array the column specified by the 
# number
# 44. Create a function that will convert a string containing a binary number into a 
# number
 

# 45. Create a function to calculate the sum of all the numbers in a jagged array 
# (contains numbers or other arrays of numbers on an unlimited number of 
# levels)
# 46. Find the maximum number in a jagged array of numbers or array of numbers
# 47. Deep copy a jagged array with numbers or other arrays in a new array
# 48. Create a function to return the longest word in a string
# 49. Shuffle an array of strings
# 50. Create a function that will receive n as argument and return an array of n 
# random numbers from 1 to n. The numbers should be unique inside the array.
# 51. Find the frequency of letters inside a string. Return the result as an array of 
# arrays. Each subarray has 2 elements: letter and number of occurrences.
# 52. Calculate Fibonacci(500) with high precision (all digits)
# 53. Calculate 70! with high precision (all digits)
