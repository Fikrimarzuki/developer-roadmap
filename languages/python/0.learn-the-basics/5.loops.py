# LOOPS

# FOR LOOP DASAR
# menggunakan in dan : untuk for loop
for n in [1,2,3]:
  print(n)
"""
Output:
1
2
3
"""


# LOOP PAKAI RANGE
# range()
range(5) # 0,1,2,3,4
range(1,5) # 1,2,3,4
range(1,10,2) # 1,3,5,7,9



# WHILE LOOP
# menggunakan while dan :
i = 0
while i < 5:
  print(i)
  i += 1


# LOOPING STRING
for char in "python":
  print(char)


# LOOPING LIST
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
  print(fruit)


# LOOPING DICT
# Looping keys (default)
user = {"name": "John", "age": 25 }
for key in user:
  print(key)
"""
Output:
name
age
"""

# Looping values
for value in user.values():
  print(value)
"""
Output:
John
25
"""

# Looping key + value
for key, value in user.items():
  print(key, value)


# LOOPING WITH INDEX
for index, fruit in enumerate(fruits):
  print(index, fruit)


# BREAK & CONTINUE
# break
for n in range(10):
  if n == 5:
    break
  print(n)

# continue
for n in range(10):
  if n % 2 == 0:
    continue
  print(n)


# ELSE DI LOOP
# else berjalan jika loop tidak break
for i in range(5):
  print(i)
else:
  print("Loop selesai")


# LOOP COMPEREHENSION
numbers = [1,2,3,4]
squares = [n * n for n in numbers]
print(squares)