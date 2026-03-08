#TO FIND MAXIMUM PRODUCT OF A SUBARRAY
a=[2,3,-2,4]
n=len(a)

max_end=a[0]
min_end=a[0]
max_so_far=a[0]

for i in range(1,n):
    if a[i]<0:
        max_end,min_end=min_end,max_end
        
    max_end=max(a[i],max_end*a[i])
    min_end=min(a[i],min_end*a[i])
    max_so_far=max(max_end,max_so_far)


print("Maximum product : ",max_so_far)