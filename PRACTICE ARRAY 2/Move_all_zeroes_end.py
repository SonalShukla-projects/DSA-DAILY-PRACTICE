#TO MOVE ALL ZEROES AT THE END OF ARRAY
from numpy import *
a=[1,0,2,0,3,0,4]
n=len(a)
b=[]
count=0 # to count no of zeroes
for i in range(0,n):
    if a[i]==0:
        count+=1
    else:
        b.append(a[i])

for i in range(count):
    b.append(0)
print(b)