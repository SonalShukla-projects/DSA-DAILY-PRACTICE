#REMOVE DUPLICATES FROM AN ARRAY

from numpy import *
a=[1,2,3,4,4,5,5]
n=len(a)
flag=1 # if  sorted
duplicate=[]

#To check first if the array is sorted or not
for i in range(0,n-1):
    if a[i]>a[i+1]:
        flag=0
        break
if flag==1:
    print("Array is sorted.")
else:
    print("Not Sorted.")

print("\n")

print("Array before removing duplicates:")
for x in a:
    print(x)
print("\n")

for i in range(0,n-1):
    for j in range(i+1,n-1):
        if a[i]==a[j]:
            duplicate.append(a[j])
            a.remove(a[j])

print("Duplicates :",duplicate)
print("\n")

print("Array after removing duplicates:")
for x in a:
    print(x)
        