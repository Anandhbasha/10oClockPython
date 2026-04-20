# print("hello welcome",end="-")
# print("hello","Welcome",sep="-")
# hello-welcome

# # "This python Base Class"
#                 # -python

# print("This python Base Class")
# print("\t\tPython")
# # apple/orange/banana

# print("apple","orange","banana",sep="/")

# a=10
# print(a)
# # left side a is called as variable
# # = called as assignment opeartor
# # 10 value
# # print(a)
# # print(a)
# b=20
# a=20.2
# print(a)
# # type
# print(type(a))


# a=10
# b=20
# c=30
# a=20  b=30 c=10
# temp = a
# a=b
# b=c
# c= temp
# print(a,b,c)

# a,b,c = 10,20,30
# c,a,b = a,b,c
# print(a,b,c)

# String
# name ='a'
# print(type(name))
# bool
# todayClass = True
# print(type(todayClass))

userName = "I love python"
# index
# index 0 =I
# index 1 =
# index 2 =l
# index 3 =o
# last index =-1
# slicing
# [startpoint:end point:increment]
# startpoint
# end point

# I love pytho
# # Io t
# print(userName[::3])
# # nohtyp evol I
# # nhy vli 
# print(userName[-1::-2])


# s = "abcdefg"
# # gfedcbaabcdefg

# res = s[::-1]+s
# print(res)

# PythonProgramming → reverse only first half
# nohtypProgramming
# s="PythonProgramming"

# mid = len(s)//2

# # # pythonpr
# # # res = s[:mid][::-1]+s[mid:]
# # res = s[:mid]+s[mid:][::-1]
# # print(res)
# # # 12. `"PythonProgramming"` → reverse only second half


# # # 1234567890 get even index numbers
# # # 0123456789
# # values="1234567890"
# # # # print(values[2::2])
# # # print(values[1::2])

# # print(values[1:-1])

# # list
# list = [10,30,20,40,10,40,30] 
# # index = 0,1,2,3
# # length = 4
# list[1] = 60
# print(list[1:2])
# print(list[::-1])
# print(list[1])
# # tuple
# newValue = (100,200,300,400,500)
# # newValue[1] = 424
# # print(newValue)
# print(newValue[::-1])
# # set
# newSets = {101,101,101,102,102,103,108,105,104,106,107}

# print(newSets)
# res = tuple(list)
# print(res)
# dictionary
# newData = {
#     "studentName":"Arun",
#     "studentAge":30,
#     "studentCity":"CBE",
#     "studentCourse":"Python",
#     "studentCompletedCourses":{
#         "course1":"Java",
#         "course2":"HTML",
#         "course3":"Data Science"
#     }
# }

# print(newData["studentCompletedCourses"]["course1"])

# person = {
#     "name":"ajay",
#     "age":30,
#     "city":"CBE",
#     "family":{
#         "father":"Raja",
#         "mother":"Lakshmi",
#         "siblings":{
#             "brothers":["Arun","Vijay","Ravi"],
#             "sister":"kala"
#         }
#     }
# }
# print(person["family"]["siblings"]["brothers"])

persons = [
{
    "name":"ajay",
    "age":30,
    "city":"CBE",
    "family":{
        "father":"Raja",
        "mother":"Lakshmi",
        "siblings":{
            "brothers":["Arun","Vijay","Ravi"],
            "sister":"kala"
        }
    }
},
{
    "name":"vijay",
    "age":30,
    "city":"CBE",
    "family":{
        "father":"Muthu",
        "mother":"Kamala",
        "siblings":{
            "brothers":["Bala","arun","Rahul"],
            "sister":"Deepa"
        }
    }
}
]


print(persons[1]["family"]["siblings"]["brothers"])

# json