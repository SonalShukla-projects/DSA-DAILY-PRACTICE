#LEADER=USKE BAAD SARE CHOTE ELEMENTS HO
#TO FIND LEADERS IN AN ARRAY

a=[16,17,4,3,5,2]
n=len(a)
leader=[]

current_max=a[n-1]
leader.append(current_max)

for i in range(n-2,-1,-1):
    if a[i]>current_max:
        leader.append(a[i])
        current_max=a[i]

print("leaders :",leader[::-1])

