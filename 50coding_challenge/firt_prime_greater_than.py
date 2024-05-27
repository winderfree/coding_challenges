# 19. Create a function that will return in an array the first “p” prime numbers 
# greater than “n”
def prime_numbers_greater_than(first_p, n):
    return_array = []
    for numero in first_p:
        for x in range(2,numero):
            if numero % x == 0:
                print(f'numero no primo {numero}')            
            
            print(f'numero primo: {numero}, x: {x}')
              
            
prime_numbers_greater_than([2,3,5,4,7,13,11,6,1], 3)
        