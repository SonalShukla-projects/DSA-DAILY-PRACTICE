from numpy import *
a=[15,48,52,1,12,41,20,12]
small=a[0]
for i in range(1,len(a)):
    if a[i]<small:
        small=a[i]
    
print("Smallest element is at index :",small)
