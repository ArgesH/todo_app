def my_sum():
    pass

def foo():
    my_sum()

def recursive(i):
    if i == 0:
        return 0
    print(i)
    return recursive(i-1)

print(recursive(9))

for i in range(9, -1, -1):
    print(i)

def find_factorial(i):
    if i == 1:
        return 1
    
    return i * find_factorial(i-1)

print("-----")
print(find_factorial(5))

var = 1
for i in range(1, 6):
    var = var * i
print(var)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
# 0, 1, 3, 

a = 0
b = 1
c = -1
for _ in range(8):
    c = a + b
    a = b
    b = c
print(c)

def fib(n):
    if n in [0, 1]:
        return n

    return fib(n-1) + fib(n-2)

my_dict = {}

my_dict["key"] = "value"
my_dict["next_key"] = "test"

del my_dict["key"]
my_dict["test"] = 0

print(my_dict.get("test", "PASS"))

if "test" not in my_dict or not my_dict["test"]:
    pass
    pass

0, "", False, None, [], (), {}, (,)






