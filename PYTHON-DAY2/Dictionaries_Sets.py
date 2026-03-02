# # #DICTIONARIES
# # dict={
# #     "name":"sonal",
# #     "cgpa":"8.89",
# #     "marks":[95,67,79]
# # }
# # print(dict)
# # dict["marks"]=[34,55,65]
# # print(dict)
# # print(dict["name"])
# # print(list(dict.keys()))#only keys
# # print(list(dict.values()))#only values
# # print(dict.items())#as tuples
# # print(dict.update({"age":"12"}))
# # print(dict)


# #SETS-mutable
# collection={1,2,3,4,2,"hello","hello"}
# print(collection)
# print(type(collection))
# c={}#empty dict
# cc=set()#empty set

# collection.add(5)
# print(collection)
# collection.remove(2)
# print(collection)
# print(len(collection))
# print(collection.pop())
# # print(collection.clear())

# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print(set1)

# print(set1.intersection(set2))

dict={
    "table":{"a piece of furniture",
             "list of facts and figures"
            },
    "cat":"a small animal"
}
print(dict)

classroom={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(classroom)

dict2={}
dict2["phy"]=[96]
dict2["chem"]=[98]
dict2["bio"]=[100]
print(dict2)

s={9,"9.0"}
s1={
    ("float",9.0),
    ("int",9)
}
print(s)
print(s1)