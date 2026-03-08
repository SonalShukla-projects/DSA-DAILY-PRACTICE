# TO PERFORM KADANE'S ALGORITHM (MAXIMUM SUBARRAY SUM)
a=[-2,1,-3,4,-1,2,1,-5,4]
n=len(a)
sub=[]
max_so_far=a[0]
current_streak=a[0]

for i in range(1,n):
    current_streak=max(a[i],current_streak+a[i])
    max_so_far=max(current_streak,max_so_far)
    print("i: ",i,"element:",a[i],"current : ",current_streak,"max : ",max_so_far)
    
print("Maximum subarray sum : ",max_so_far)
