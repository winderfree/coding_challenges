# def tri_recursion(k):
#     return k
# print(tri_recursion(6-1))

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n + factorial(n - 1)
# print(factorial(6))

# def my_func(k):
#     print(k)