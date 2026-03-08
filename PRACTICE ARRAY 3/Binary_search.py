#TO FIND THE INDEX OF THE ELEMENT IN AN SORTED ARRAY
from numpy import *
a=[1,2,3,4,5,6]
n=len(a)
target=int(input("Search this element :"))
idx=0
flag=0 # not found
left=0
right=n-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        print("Element found at ",mid)
        found=1
        break
    elif target>a[mid]:
        left=mid+1
    else:
        right=mid-1

if not found:
    print("element not found")
          


    