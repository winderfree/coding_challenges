# 1.	Write a function named 'format_number' 
# that takes a non-negative number as its only parameter. 
# Your function should convert the number to a string 
# and add commas as a thousand separators. For example, 
# calling format_number(1000000) should return "1,000,000". 
# cadena = "doald"
# new_cadena:str = ""
# for x in cadena:
#     new_cadena+=x
#     print(x)
# print(new_cadena)
def format_number(non_negative:int):
    str_number:str = str(non_negative)
    new_cadena:str = ""
    cont = 0
    # convert number to str
    for x in str_number[::-1]:
        new_cadena+=x
        cont+=1
        if  cont % 3 == 0:
            new_cadena+=","
    nc = new_cadena[::-1].lstrip(",")
    return nc
print(format_number(1000000000))


# 1.	Find the largest and the smallest number in a given array.
# a = [3,-1,23,9,2, -19]
# a.sort(reverse=False)
# if a[0]>=0 or a[0]<0:
#     print(a[0],"menor")
# if a[-1]:
#     print(a[-1],"mayor")
# print(a)

# 2.	Find the second largest number in the integer array.
# int_ar = [2,2,8,7,6,9,12]
# int_ar.sort()
# # print(int_ar)
# # print(int_ar[-2])

# # 3.	Print array in reverse order.
# int_ar = [2,2,8,7,6,9,12]
# int_ar.sort(reverse=True)
# print(int_ar)

# 4.	Insert an element at the end of an array.
# int_ar.append(21)
# print(int_ar)

# 5.	Merge two sorted arrays into a single sorted array.
# int_ar1 = [2,2,8,7,6,9,12]
# int_ar.sort()
# int_ar2 = [2,2,8,7,6,9,12]
# int_ar.sort()
# sin_ar = int_ar1+int_ar2
# sin_ar.sort()
# print(sin_ar)