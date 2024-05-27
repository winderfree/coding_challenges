# 33. Calculate the sum of numbers received in a comma delimited string
comma_delimited_str = "1,2,3,2,34"
suma=0
array_nums = comma_delimited_str.split(",")
for x in array_nums:
    suma+=int(x)
print(suma)