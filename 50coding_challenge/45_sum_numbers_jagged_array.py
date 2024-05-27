# 45. Create a function to calculate the sum of all the numbers in a jagged array 
# (contains numbers or other arrays of numbers on an unlimited number of 
# levels)
from itertools import chain
ar = [[3,2,[8,7,[3,6]]],[2,23],[1,2]]
print(list(chain(*ar)))
# ar = [1,2, [3,[2,23,[1,2]],100],12]
# print([y for x in ar for y in x])