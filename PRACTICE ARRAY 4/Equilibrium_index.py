#TO FIND EQUILIBRIUM INDEX OF AN ARRAY
a=[1,3,3,2,2]
n=len(a)

for i in range(n):
    left_sum=sum(a[:i])
    right_sum=sum(a[i+1:])
    if left_sum==right_sum:
        print("equilibrium index:",i)
        break

