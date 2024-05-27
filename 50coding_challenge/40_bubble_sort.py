# 40. Implement the bubble sort algorithm for an array of numbers
ar = [4,1,2,3,99, 23,33,1,1]
result = []
lenght = len(ar) - 1
mayor = 0
print(f'Antes: {ar}')
for x in range(lenght):
    # print(f'xX: {ar[x]}, {x}')
    for y in range(lenght):
        if ar[y] > ar[y+1]:
            mayor = ar[y]
            ar[y] = ar[y+1] 
            ar[y+1] = mayor
            # print(f'X:{x}, (x):{ar[x]}, (y):{ar[y]}, (y-1):{ar[y+1]}')

print(f'Despues: {ar}')
