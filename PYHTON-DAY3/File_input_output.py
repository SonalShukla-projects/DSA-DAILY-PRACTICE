#FILE INPUT AND OUTPUTS
# f=open("C:/Users/DELL/OneDrive/Desktop/DSA-DAILY-PRACTICE/PYHTON-DAY3/sample.txt","r")


# # line1=f.readline()

# # print(line1)


# # f.close()

# f=open("C:/Users/DELL/OneDrive/Desktop/DSA-DAILY-PRACTICE/PYHTON-DAY3/sample.txt","w")
# f.write("This is new line")


# f=open("C:/Users/DELL/OneDrive/Desktop/DSA-DAILY-PRACTICE/PYHTON-DAY3/sample.txt","a")
# f.write("This is new line")
# f.close()

#WHEN USING WITH WE DONT NEED TO CLOSE
# with open("C:/Users/DELL/OneDrive/Desktop/DSA-DAILY-PRACTICE/PYHTON-DAY3/sample.txt","r") as f:
#     data=f.read()
#     print(data)

# #DELETING A FILE 
# import os 
# os.remove("C:/Users/DELL/OneDrive/Desktop/DSA-DAILY-PRACTICE/PYHTON-DAY3/sample.txt")

#to install
#pip install tensorflow
#to install a external module

# #practice
# with open("C:/Users/DELL/OneDrive/Desktop/DSA-DAILY-PRACTICE/PYHTON-DAY3/practice.txt") as f:
#     data=f.read()
#     new=data.replace("java","python")
#     print(data)
#     print(new)

#     word="learning"
#     if (data.find(word)!= -1):
#         print("Found")
#     else:
#         print("Not found")

#     word1="learning"
#     new=f.readline()

def check_for_line():
    word="t"
    data=True
    line_no=1
    with open("C:/Users/DELL/OneDrive/Desktop/DSA-DAILY-PRACTICE/PYHTON-DAY3/practice.txt") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
check_for_line()