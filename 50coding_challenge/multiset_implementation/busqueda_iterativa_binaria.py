def busqueda_iterativa(ar, target):
    menor = 0
    mayor = len(ar)-1
    medio = menor+mayor//2
    while menor <= mayor:
        if ar[medio] == target:
            return medio
        elif ar[medio] < target:
            menor = medio + 1
        else:
            mayor = medio - 1
        medio = (menor + mayor) // 2
    return -1
ar = [2,4,5,6,7,8]
for i in range(10):
    print(i,busqueda_iterativa(ar, i))
# print(f'menor: {menor}, mayor: {mayor}, medio: {medio}')
