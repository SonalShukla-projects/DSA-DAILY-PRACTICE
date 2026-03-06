#FIND SECOND LARGEST ELEMENT IN AN ARRAY

from numpy import *

a=[2,3,7,9,1]

if a[0]>a[1]:
    first=a[0]
    second=a[1]
else:
    first=a[1]
    second=a[0]

for i in range(2,len(a)):
    if a[i]>first:
        second=first
        first=a[i]
    elif a[i]>second and a[i]!=first:
        second=a[i]
print(second)