# #USING ARRAY MODULE
import array as a
# from array import *

val=a.array('i',[10,20,30,40,50,60,90,100])
print(val)

print("\n")

for el in range(0,len(val)):
    print(val[el])

print("\n")

for i in range(0,len(val)):
    print(val[i] ,end=" ")

print("\n")

for x in val:
    print(x)

print(val.typecode)

print("\n")

val.reverse()
for i in range(0,len(val)):
    print(val[i],end=" ")

print("\n")
val.insert(1,200)

for i in range(0,len(val)):
    print(val[i])

print("\n")

copyArray=a.array(val.typecode ,(x for x in val))

for i in range(0,len(copyArray)):
    print(copyArray[i],end=" ")

print("\n")

#POP FUNCTION
copyArray.pop(3)

for i in range(0,len(copyArray)):
    print(copyArray[i],end=" ")

print("\n")

#REMOVE FUNCTION
copyArray.remove(30)


for i in range(0,len(copyArray)):
    print(copyArray[i],end=" ")

print("\n")
#SLICING OF ARRAY
v=a.array('i',[1,2,3,4,5,6,7,8,9])
abc=v[2 : 5]

for i in range(0,len(abc)):
    print(abc[i])

print("\n")
abc=v[2 : -3]

for i in range(0,len(abc)):
    print(abc[i])
print("\n")
abc=v[ : :-1]

for i in range(0,len(abc)):
    print(abc[i])

print("\n")

# #USER SE INPUT LENA HAI
# arr=a.array('i',[])
# n = int(input("Enter size of array:"))
# for i in range(0,n):
#     arr.append(int(input('Enter next number:')))

# for x in arr:
#     print(x,end=" ")

# print("\n")

#SEARCH AN ELEMENT IN ARRAY
s=a.array('i',[1,2,3,4,5,6,7,8,9])
for i in range(0,len(s)):
    print(s[i],end=" ")

idx=s.index(50)
print("\n")
print(idx)
