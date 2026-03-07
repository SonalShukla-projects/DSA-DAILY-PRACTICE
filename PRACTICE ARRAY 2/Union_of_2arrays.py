#TO FIND UNION OF TWO ARRAYS
from numpy import *

a=[1,2,3,4]
b=[2,3,5,6]
union=[]
for x in a:
    union.append(x)

for y in b:
    if y not in union:
        union.append(y)

print("Union:",union)