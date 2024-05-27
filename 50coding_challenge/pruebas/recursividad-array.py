def recursivo(k):
    ar_result = []
    if k > 0:
        # print("recursivo(k-1):",recursivo(k-1))
        result = k + recursivo(k-1)
        print(f'valor k: {k}')
        # print(f'valor recursivo(k-1): {recursivo(k-1)}')
        # print(f'valor result = k + recursivo(k-1): {result}')
        ar_result.append(result)
        print(result)
        print("---------------------------------------")
        print(ar_result)
        print("---------------------------------------")
    else:
        result = 0
    print("array_result:",ar_result)
    return result

print("\n\nRecursion Example Results")
print(recursivo(6))