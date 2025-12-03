# FUNCTIONAL TOOLS

# LAMBDAS
# Fungsi kecil yang tidak perlu nama
# Format
# lambda arg: expression

# Contoh:
square = lambda x: x * x
print(square(5))  # 25

# Contoh sorting dengan lambda:
users = [
  {"name": "fikri", "age": 25},
  {"name": "budi", "age": 30}
]
sorted_users = sorted(users, key=lambda u: u["age"])

# Contoh di filtering
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))

# Contoh di mapping
nums = [1, 2, 3]
squared = list(map(lambda x: x*x, nums))

# Lambda biasa dipakai
# Sebagai callback
# Untuk sort / filter cepat
# Saat butuh fungsi simple & inline
# Digunakan oleh banyak library Python


# DECORATORS
# Fungsi yang membungkus fungsi lain
# Digunakan untuk:
# - logging
# - authentication
# - caching
# - validate input
# - rate limiting

def my_decorator(fn):
  def wrapper():
    print("Before")
    fn()
    print("After")
  return wrapper

@my_decorator
def greet():
  print("Hello")

greet()
# Output
# Before
# Hello
# After

# Contoh untuk logging
def logger(func):
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__}")
    return func(*args, **kwargs)
  return wrapper

@logger
def greet2():
  print("Hello")

greet2()

# Contoh decorator dengan argument
def repeat(n):
  def decorator(fn):
    def wrapper(*args, **kwargs):
      for _ in range(n):
        fn(*args, **kwargs)
    return wrapper
  return decorator

@repeat(3)
def hello():
  print("Hi")
hello()

# Penggunaannya nanti bisa seperti ini
# di Router
# @app.get("/users")
# def get_users():
#   ...

# di decorator
# @requires_auth
# def dashboard():
#   ...

# di login middleware
# @app.middleware("http")
# async def log_request(request, call_next):
#   ...


# ITERATORS
# Objek yang bisa di loop
# Dalam python: list, tuple, dict, string adalah iterator atau bisa diubah menjadi iterator
nums = [1, 2, 3]
it = iter(nums)

print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3

# Custom Iterator
class Count:
  def __init__(self, max):
    self.max = max
    self.n = 0

  def __iter__(self):
    return self

  def next(self):
    return self.__next__()

  def __next__(self):
    if self.n < self.max:
      self.n += 1
      return self.n
    raise StopIteration

# Iterator dipakai untuk
# - File reading line-by-line
# - Streaming data
# - Efficient loops
# - Custom generators

# GENERATORS
# Function yang menghasilkan iterator menggunakan yield

# Contoh generator
def countdown(n):
  while n > 0:
    yield n
    n -= 1

# Kelebihan generator:
# Memory efficient (tidak simpan seluruh list)
# Bisa handle data sangat besar
# Cocok untuk data streaming

# Membaca file besar
# with open("log.txt") as f:
#   for line in f:
#     process(line)

# Generator pipeline
# def read_numbers():
#   for i in range(100000):
#     yield i

# def even(nums):
#   for n in nums:
#     if n % 2 == 0:
#       yield n

# for x in even(read_numbers()):
#   print(x)


