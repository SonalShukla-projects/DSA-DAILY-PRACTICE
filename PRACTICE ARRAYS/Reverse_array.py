#REVERSE AN ARRAY WITHOUT USING FUNCTION
from numpy import *
a=[1,2,3,4,5]
n=len(a)
print(n)
print("\n")

for i in range(n-1,-1,-1):
    print(a[i])

