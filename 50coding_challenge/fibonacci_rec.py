# 15. Create a function that will find the nth Fibonacci number using recursion
def nth_fibonacci(number):
    # base case 
    if  number == 0:
        return 0
    elif  number < 0:
        return 1
    else:
        result =  nth_fibonacci(number-1) + nth_fibonacci(number-2) 
        print(f'nth_fibonacci(number-1): {nth_fibonacci(number-1)}, nth_fibonacci(number-2): {nth_fibonacci(number-1)}')
        return result
    
print(nth_fibonacci(6))
    