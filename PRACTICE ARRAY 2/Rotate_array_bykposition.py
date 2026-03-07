#TO ROTATE AN ARRAY BY K POSITIONS

from numpy import *
a=[1,2,3,4,5]
n=len(a)
k=int(input("Enter how many positions to move:"))
k=k%n
a[-k:]
a[:-k]
rotated=a[-k:]+a[:-k]
print(rotated)

