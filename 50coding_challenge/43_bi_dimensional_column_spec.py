# 43. Create a function that will receive a bi-dimensional array as argument and a 
# number and will extract as a unidimensional array the column specified by the 
# number
import numpy as np
def bidimensional_as_unidimensional_columns(*args):
    try:   
        column = int(input("Inserte número:"))
        print(np.array(args))
        for x in range(len(args)):
            print(args[x][column])
    except IndexError:
        print('El Index de la columna esta fuera de rango')
        print(f'error: {IndexError}')
    # return np.array(args)
print(bidimensional_as_unidimensional_columns([1,2,3],[3,2,4],[23,22,11]))
# A = np.array([[0,1,2],[2,3,4,],[4,5,6]])
# # print(A)
# # print(A[[1],[0]])
# try:   
#     column = int(input("Inserte número:"))
#     print(A)
#     for x in range(len(A)):
#         print(A[x][column])
# except IndexError:
#     print('El Index de la columna esta fuera de rango')
#     print(f'error: {IndexError}')
        # print(f'filas: {x}, columnas: {y}')
# print(bi_ar) 
# def ()