# LIST COMPREHENSION

# Cara singkat, cepat, dan pythonic untuk membut list baru dari iterable (list, range, string, dsb)
# Tanpa list comprehension
result = []
for x in range(5):
  result.append(x)

# Dengan list comprehension
result = [x for x in range(5)]

# Expression di list comprehension
squares = [x*x for x in range(6)]
print(squares)

# Conditional if di list comprehension
evens = [x for x in range(10) if x % 2 == 0]

# Conditional if else di list comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]


# Nested list comprehension
# Tanpa
pairs = []
for x in range(3):
  for y in range (3):
    pairs.append((x, y))

# Pakai
pairs = [(x, y) for x in range(3) for y in range(3)]


# Transformasi string / data
# lowercase
texts = ["Hello", "WORLD"]
normalized = [t.lower() for t in texts]

# filter + transform
emails = ["python@example.com", "invalid", "budi@mail.com"]
valid = [e for e in emails if "@" in e]


# Flatten list
# Tanpa
result = []
for row in matrix:
  for item in row:
    result.append(item)

# Pakai
flat = [x for row in matrix for x in row]


# Contoh real case: extract data from dictionary
users = [
  { "name": "Pythonia", "age": 25 },
  { "name": "Budi", "age": 30 },
  { "name": "Alex", "age": 22 }
]
# Ambil nama
names = [u["name"] for u in users]

# Filter age
older = [u for u in users if u["age"] > 25]

# 1 liner untuk processing JSON
# import json
# data = json.load(open("users.json"))
# emails = [u["email"] for u in data if u["active"]]

# Machine Learning example
# words = [w.lower() for sentence in corpus for w in sentence.split()]

# List comprehension with functions
def square(x):
  return x*x

nums = [square(x) for x in range(6)]


# Performance
# - Lebih cepat
# - Lebih memory efficient
# - Lebih pythonic
# - Cocok untuk transform/filter


