# # from functions import square
# # print(square(2))

# # math
# # import math 
# # print(math.sqrt(16))
# # print(math.factorial(5))
# # print(math.pi)
# # # random
# # import random
# # print(random.randint(99999,999999))

# # print(random.choice([500,5,100,1000]))

# # target = random.randint(1,3)
# # finds = int(input("Enter the Surprise Number:"))
# # if target==finds:
# #     print("Tresure hunted")
# # else:
# #     print("vada poche")
# # dateandtime
# # import datetime
# # today = datetime.date.today()
# # print(today)
# # os
# import os
# print(os.getcwd())
# print(os.listdir())
# # sys
# import sys
# print(sys.version)
# print(sys.platform)

# # time
# import time
# print("start")
# time.sleep(2)
# print("end")
# # json
# person = {
#     "name":"arun",
#     "age":25
# }

# print(person)
# import json
# jsonData = json.dumps(person)
# print(jsonData)
# print(type(jsonData))

# data = json.loads(jsonData)
# print(data)
# # request

# re-> regular expression
import re 

text = "python123"
res = re.findall("[0-9]",text)
print(res)

# statistics
# import statistics

# data = [10,20,30,40,50]
# print(statistics.mean(data))

# collections
# from collections import  Counter

# data = ["a","b","a","a","c","b","c","a"]
# print(Counter(data))


# import string
# print(string.ascii_lowercase)

import re

password = input("Enter the Password:")

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$"

if re.match(pattern,password):
    print("Strong Password")
else:
    print("weak Password")