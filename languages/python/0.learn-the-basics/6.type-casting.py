# TYPE CASTING

# Dalam operasi tipe, python tidak sebebas JS
# "5" + 5 akan ERROR


# CONVERT KE INTEGER
age = "25"
age = int(age)
print(age) # 25
print(type(age)) # <class 'int'>

# kalau string tidak berisi angka akan error
# int("abc") # ValueError


# CONVERT KE FLOAT
pi = "3.14"
pi = float(pi)
print(pi) # 3.14


# CONVERT KE STRING
num - 99
text = str(num)
print(text) # "99"

# biasa digunakan seperti ini
print("Age: " + str(25))
# print("Age: " + 25) # ERROR


# CONVERT KE LIST
text = "python"
arr = list(text)
print(arr) # ['p','y','t','h','o','n']


# CONVERT KE TUPLE
items = [1, 2, 3]
t = tuple(items)
print(t)  # (1, 2, 3)


# CONVERT KE SET
numbers = [1,1,2,2,3]
unique = set(numbers)
print(unique)  # {1,2,3}


# CONVERT LIST DAN STRING JOIN
names = ["alex", "andi", "budi"]
result = ", ".join(names)
print(result)  # "alex, andi, budi"


# CONVERT LIST (STRING NUMBER) KE LIST (NUMBER)
arr = ["1", "2", "3"]
nums = [int(x) for x in arr]
print(nums)  # [1,2,3]


# BOOLEAN CASTING
print(bool(""))   # False
print(bool("hi")) # True
print(bool(0))    # False
print(bool(1))    # True


# CASTING INPUT
age = int(input("Your age: "))
height = float(input("Your height: "))


