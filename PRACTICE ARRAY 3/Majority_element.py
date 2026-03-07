#TO FIND THE MAJORITY ELEMENT IN AN ARRAY

from numpy import *
a=[1,2,2,2,3,4,5,5,2,2,2]
n=len(a)
candidate=None
votes=0

for num in a :
    if votes==0:
        candidate=num
    if num==candidate:
        votes+=1
    else:
        votes-=1

if a.count(candidate)> n//2:
    print("Majority is :",candidate)
else:
    print("Not found")