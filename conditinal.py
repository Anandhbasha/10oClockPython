# if
# if condition:
#     # code to execute if condition is true      
age = 15
# if age >= 18:
#     print("You are an adult.")
# # if else
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

if age <=13:
    print("You are a child.")
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# elif
if age <=13:
    print("You are a child.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# nested if
state = "TN"
locality = "Salem"

if age>=18:
    if state == "TN":
        if state == "TN":
            if locality == "Salem":
                print("You can vote in Salem, TN.")
            else:
                print("You cannot vote in Salem.")
        else:
            print("You cannot vote in TN.")
    else:
        print("You are not eligible to vote.")