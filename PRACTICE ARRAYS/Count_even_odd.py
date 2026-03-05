#TO COUNT EVEN AND ODD NUMBERS
from numpy import *

a=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in range(0,len(a)):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
print("Even count : ",even,"\nOdd count: ",odd)