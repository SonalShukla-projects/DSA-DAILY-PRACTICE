#TO FIND THE LONGEST INCREASING SUBARRAY
a=[1,2,3,2,3,4,5,6]
n=len(a)
max_len=1
curr_len=1
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        curr_len+=1
    else:
        max_len=max(max_len,curr_len)
        curr_len=1

max_len=max(max_len,curr_len)
print("Length of longest substring:",max_len)