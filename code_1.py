import math

def add(a,b):
    return a+b
def subtrack(a,b):
    return a-b
def mltply(a,b):
    return a*b
def divide(a,b):
    return a/b
user_example = input()
if "+" in user_example:
   user_example = user_example.split("+")
   for i in range(0, len(user_example)):
       user_example[i] = float (user_example[i])
result = add(user_example[0], user_example[1])
print(result)
if "-" in user_example:
    user_example = user_example.split("-")
    for i in range(0, len(user_example)):
       user_example[i] = float (user_example[i])
result = subtrack(user_example[0], user_example[1])
print(result)
if "/" in user_example:
    user_example = user_example.split("/")
    for i in range(0, len(user_example)):
       user_example[i] = float (user_example[i])
result = divide(user_example[0], user_example[1])
print(result)
if "*" in user_example:
    user_example = user_example.split("*")
    for i in range(0, len(user_example)):
       user_example[i] = float (user_example[i])
result = mltply(user_example[0], user_example[1])
print(result)

# 5^2 = 25
# 25^0.5 = 5