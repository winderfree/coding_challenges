'''
    min_spot_to_letters
'''
def min_spot_to_letters(palabra, target):
    array_position = [ x for x in range(len(palabra)) if palabra[x] == target]
    array_position.append(len(palabra))
    for letra in range(len(array_position)):
        if letra == 0:
            for i in range(array_position[0]):
                pos = array_position[0] - i
                print(pos)
        elif letra < array_position.index(len(palabra)) :
            calc_array = array_position[letra] - array_position[letra-1] 
            for m in range(calc_array):            
                prom_calc_array = calc_array // 2
                if m > prom_calc_array:
                    cal = calc_array -  m
                    print(cal)
                elif m < prom_calc_array:
                    print(m)
                else:
                    print(prom_calc_array)
        else:
            array_position.pop()
            calc_dist = len(palabra) - array_position[-1]
            for x in range(calc_dist):
                print(x)
    return "Lo que quieras devolver"
                
print(min_spot_to_letters('deddddeffffegfgeggegehhhelol', 'e'))