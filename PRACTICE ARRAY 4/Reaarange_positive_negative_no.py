#TO REARRANGE POSITIVE AND NEGATIVE NUMBERS ALTERNATIVELY
a=[4,-1,2,-3,5,-6,7,8,-9]
n=len(a)

pos=[]
neg=[]

for x in a :
    if x>=0:
        pos.append(x)
    else:
        neg.append(x)

result=[]
m=min(len(pos),len(neg))

for i in range(m):
    result.append(pos[i])
    result.append(neg[i])
for i in range(m,len(pos)):
    result.append(pos[i])
for i in range(m,len(neg)):
    result.append(neg[i])

print(result)

