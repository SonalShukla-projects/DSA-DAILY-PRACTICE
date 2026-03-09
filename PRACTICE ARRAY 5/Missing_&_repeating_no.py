#TO FIND A MISSING NUMBER AND A REPEATING NUMBER
a=[4,5,6,2,1,1]
a.sort()
n=len(a)
miss=0
repeat=0

for i in range(0,n-1):
    if a[i]==a[i+1]:
        repeat=a[i]
        break
actual_sum=sum(set(a))
expected=(n*(n+1))//2
miss=expected-actual_sum
    
    
print(miss)
print(repeat)