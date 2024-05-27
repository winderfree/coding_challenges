arr = [1,2,3,4,5,6,7,8,9,10]
arr1 = []
arr2 = []
# count para saber cuantos elementos se repiten 
media = len(arr)/2
# prueba = len(arr) % 2
# print(prueba)
# print(media)
if len(arr) % 2 == 0:
    print(f'{media} int')
    for x in arr:
        if x <= media:
            arr1.append(x)
            print(f'{x} estos son del primer arreglo.')
        else:
            arr2.append(x)
            print(f'{x} ultimos')

else:
    print(f'{media}, float - {int(media)} vuelta a int')

print(f'arr1 = {arr1}, arr2 = {arr2}')