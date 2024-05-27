# import string
# # print(cadena_minuscula)
# 3-0=3
# 3-1=2
# 3-2=1
# 3-3=0
# 5-4=1
# 5-5=0
# 6-6=0
# 11-7=4
# 11-8=3
# 11-9=2
# 11-10=1

cadena = "mkteneetkybekkkkkke"
lenght = len(cadena) - 1
var = "e"
cont = 0
palabra_resulta = ""
numeros_arreglo = [x for x in range(len(cadena)) if cadena[x] == var]
# numeros_arreglo.insert(0, 0)
for letter in range(len(cadena)):
    
    palabra_resulta += str(letter)
    print(letter)
    print(letter)
print(numeros_arreglo)
print(palabra_resulta)
