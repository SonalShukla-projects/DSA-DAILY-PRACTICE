#TO FIND SUBARRAY WITH THE GIVEN SUM
a=[1,2,3,7,5]
n=len(a)
target=int(input("Enter sum to find subarray:"))

current_sum=0
start=0

for i in range(n):
    current_sum+=a[i]
    while current_sum>target:
        current_sum-=a[start]
        start+=1
    if current_sum==target:
        print(start,i)
        break

