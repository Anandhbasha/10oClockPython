# Arithmetic operators
# +, -, *, /, %, //, **
a=10
b=3
print(a+b) 
print(a-b)  
print(a*b) 
print(a/b) 
print(a%b)
# floor division - it gives the quotient without the remainder
print(a//b) 
# power operator - it gives the result of a raised to the power of b
# 10*10*10 = 1000
print(a**b) 

# Assignment operators
# =, +=, -=, *=, /=, %=, //=, **=
a=10
a+=5 
print(a)
a-=3
print(a)
a*=2
print(a)
a/=4 #24/4
print(a)
# a%=3 
# print(a)
a//=2
print(a)
a**=3
print(a)


# comparison operators
# ==, !=, >, <, >=, <=
a=10
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
b=10
print(a>=b)
print(a<=b)

# Logical operators
# and, or, not
a=10
b=5
print(a>5 and b<10 and a!=b and a!=10)
print(a>5 or b>10 or a==b or a!=10)
print(not(a>5 and b<10 and a!=b and a!=10))

# Bitwise operators
# &, |, ^, ~, <<, >>
a=10 # 1010 in binary
b=5  # 0101 in binary
print(a&b) # 0000   and both bits are 1 then only it gives 1 otherwise 0
print(a|b) # 1111   or if at least one of the bits is 1 then it gives 1 otherwise 0
print(a^b) # 1111   xor if the bits are different then it gives 1 otherwise 0
print(~a)  # -11    complement of a
print(a<<1) # 20    left shift - multiplies a by 2
print(a>>1) # 5     right shift - divides a by 2

# Membership operators
# in, not in    
a=[1,2,3,4,5]
print(3 in a) # True    
print(6 in a) # False
print(3 not in a) 
print(6 not in a) 

# Identity operators
# is, is not
a=10    
b=5
print(a is b) # False using is operator we can check whether a and b are the same object in memory or not
print(a is not b) # True
c=a 
print(a is c) # True
print(a is not c) # False

# Ternary operator
# condition_if_true if condition else condition_if_false
age=18
status="Eligible to Vote" if age>=18 else "Not Eligible to Vote"
print(status)

# operator preferences
print((2*3)+5/2+(3-1)**2)
# 6+5/2+2**2
# 6+2.5+4
# 12.5
# (),**,*,/,%,+,-