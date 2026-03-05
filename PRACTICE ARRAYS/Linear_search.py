#TO PERFORM LINEAR SEARCH IN AN ARRAY
from numpy import *

a=[1,2,3,4,5]
n=len(a)
found=0 # if not element found
idx=a[0]
search=int(input("Search this element:"))
for i in range(0,n):
    if a[i]==search:
        found=1
        idx=i
        break
if found==1:
    print("Search is found: ",search,"at :",idx)
else:
    print("Not found.")