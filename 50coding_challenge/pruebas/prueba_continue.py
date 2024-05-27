ar = []
ar_new=[]
for index in range(1, 15):
    if index % 2 == 0:
        ar.append(index)
    if index % 2 == 1:
        continue
    ar_new.append(ar[:])
    ar.pop()
    print(ar)
    print(ar_new)
print('final array:',ar)