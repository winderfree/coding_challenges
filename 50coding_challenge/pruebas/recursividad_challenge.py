def tri_recursion(k):
  if(k>0):
    print(f'k={k}, tri_recursion(k-1)={tri_recursion(k-1)}')
    print("se suma k + tri_recursion(k-1) \n",k+tri_recursion(k-1))
    result = k+tri_recursion(k-1)
    print("se imprime result\n")
    print(result)
  else:
    "Not k>0: result = 0\n"
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6) 