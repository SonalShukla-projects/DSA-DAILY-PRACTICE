#TO FIND A DUPLICATE NUMBER IN AN ARRAY
a=[1,2,3,4,5,1,1]
n=len(a)
flag=0 # Not found
duplicate=0

for i in range(0,n):
    for j in range(1,n):
        if a[i]==a[j]:
            flag=1
            duplicate=a[i]
            break

print("Duplicate element is :",duplicate)
