x,y = 1, 0
print(y)
while x < 10:
    x,y = (y, x+y)
    print(y)
    print(f'this x:{x}')
    print(f'this y:{y}')

