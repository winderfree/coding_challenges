result = []
li = set()
li.add(1)
li.add(11)
print(li.__contains__(1))

# # print(set([2,1,3,3,]))
# # buble sort
# ar = [12,7,3,8,9,1]
# min = 0
# for y in range(len(ar)-1):
#     for x in range(len(ar)-1):
#         if ar[x] > ar[x+1]:
#             min = ar[x+1]
#             ar[x+1] = ar[x]
#             ar[x] = min
#         print(ar[x])
#         print(ar[x+1])
# print(ar)