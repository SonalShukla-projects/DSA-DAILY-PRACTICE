# #WHILE LOOPS
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# i=1
# while i<=5:
#     print("Hello")
#     i+=1
# print(i)

#print numbers from 1 to 10
# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=5
# while i>0:
#     print(i)
#     i-=1

#print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

#print numbers from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

# #print multiplication table of a number n
# num=int(input("Enter a number:"))
# i=1
# while i<=10:
#     print(i*num)
#     i+=1

# #print elements of list [1,4,9,16,25,36,49,64,81,100] using a loop
# list1=[1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx < len(list1):
#     print(list1[idx])
#     idx+=1

# # #search for a number x in this tuple using loop
# t=(1,4,9,16,25,36,49,64,81,100)
# x= int(input("Enter element to search:"))
# idx=0
# flag=0
# while idx < len(t):
#     if(t[idx]==x):
#         flag=1
        
#     idx+=1

# if flag==1:
#     print("Found")
# else:
#     print("Not found")

# #break and continue keywords
# t=(1,4,9,16,25,36,49,64,81,100)
# x= int(input("Enter element to search:"))
# idx=0
# flag=0
# while idx < len(t):
#     if(t[idx]==x):
#         flag=1
#         break
#     idx+=1

# if flag==1:
#     print("Found")
# else:
#     print("Not found")

# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1    

# # #FOR LOOPS
# list1=[1,2,3,4]
# for el in list1:
#     print(el)

# tup=(1,2,3,4,5,6)
# for t in tup:
#     print(t)

# str="sonal"
# for char in str:
#     print(char)
#     if(char=='o'):
#         print("Found")

# #print elements [1,4,9,16,25,36,49,64,81,100]
# list2=[1,4,9,16,25,36,49,64,81,100]
# for el in list2:
#     print(el)

# t=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("Search this :"))
# for el in t:
#     if(x==el):
#         print("Found")
#         break
    
# #Range
# for el in range(5):#0-5
#     print(el)

# for el in range(1,6):#1-5
#     print(el)

# for el in range(0,11,2):#even -0,2,4,6,8,10
#     print(el)

# for el in range(1,11,2):
#     print(el)

# #print 1-100
# for i in range(1,101,1):
#     print(i)

# #print 100-1
# for i in range(100,0,-1):
#     print(i)

# #multiplication of n
# num=int(input("Enter number:"))
# for i in range(1,11,1):
#     print(num*i)

# #pass use
# for el in range(5):
#     pass
# print("Some code")

# n=int(input("Enter value :"))
# sum=0
# i=0
# for i in range(1,n+1):
#     sum+=i

# print(sum)



# #find factorial
# n=3
# fact=1
# for i in range(1,n+1,1):
#     if n==0:
#         print(1)
#         break
#     else:
#         fact=fact*i
#         i+=1
# print(fact)

