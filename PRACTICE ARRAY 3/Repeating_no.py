#TO FIND A NUMBER WHICH IS REPEATED MORE THAN ONCE
from numpy import *
a=[1,2,2,3,4,5]
n=len(a)

found=False
for i in range(0,n):
    count=0
    for j in range(i+1,n):
        if a[i]==a[j]:
          print("Repeating number is :",a[i],"count :",count)
          found=True
          break
    if found:
       break
    if not found:
       print("not found")
 

   
    
    

