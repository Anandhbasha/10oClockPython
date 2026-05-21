class InvalidNumber(Exception):
    pass
try:
    num = input("Eneter the number:")
    if not num.isdigit():
        raise InvalidNumber("Please provide a postive number only")
except InvalidNumber as e:
    print(e)
print("Hello")