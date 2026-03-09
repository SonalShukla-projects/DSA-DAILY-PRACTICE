#TO FIND THREE SUM - UNIQUE TRIPLETS WHOSE SUM=0
a=[-1,0,1,2,-1,-4]
a.sort()
n=len(a)
result=[]


for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]==0:
                triplet=sorted([a[i],a[j],a[k]])
                if triplet not in result:
                    result.append(triplet)

print(result)