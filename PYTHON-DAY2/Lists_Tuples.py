#LISTS-mutable
marks1=25
marks2=50
marks3=95
marks4=79

marks=[30,45,50,65,75,80] #lists 

print(marks)
print(type(marks))
print(marks[3])
print(len(marks))

student=["sonal",90,"nagpur"]
print(student)

student[0]=45
print(student)

# print(student[3]) # error 

print(marks[1:4])

list=[2,1,3]
list.append(4) #mutating
print(list)
list.sort() # doesn't return anything # sort in ascending order
print(list)
list.sort(reverse=True) # reverse the string in descending order
print(list)
print(list.insert(0,35)) #inserted 35 at 0 position
print(list)
print(list.reverse()) # reverse the string
print(list)

l=[2,1,3,1]
l.pop(2)
print(l)


#TUPLES- immutable
tup=(43,23,32,24)
print(tup[0])
print(tup)
tup1=(1,)
print(tup1)
print(tup[1:3])


# movies=[]
# mov1=str(input("Enter movie names :"))
# mov2=str(input("Enter movie names :"))
# mov3=str(input("Enter movie names :"))
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

l=['m','a','d','a','m']
l2=l.copy()
l2.reverse()
if l==l2:
    print("Palindrome")
else:
    print("Not")

grade=("C","D","A","A","B","A")
print(grade.count("A"))

list=["C","D","A","A","B","A"]
list.sort()
print(list)