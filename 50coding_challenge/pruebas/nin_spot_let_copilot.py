def foo(var1, var2):
    result = var2 - var1
    return result
    
puntos = (1,2)
print(foo(*puntos))
print(*puntos)
print(puntos[0])