# FUNCTIONS
# def namafungsi():
#   blok kode


# FUNGSI TANPA PARAMETER
def greet():
  print("Hello!")


# FUNGSI DENGAN PARAMETER
def greet2(name):
  print(f"Hello {name}")


# FUNGSI YANG MENGEMBALIKAN (RETURN) VALUE
def greet3(name):
  return f"Hello, {name}"


# CARA PEMANGGILAN
greet()
greet2()
print(greet3("Nama"))


# DEFAULT PARAMETER
def greet4(name = "Guest"):
  print(f"Hello {name}")
greet4()


# MULTIPLE RETURN VALUES
def get_user():
  return "Pythonia", 25
name, age = get_user()
print(name, age)


# KEYWORD ARGUMENT
# Panggil function dengan menamai param
def say(name, age):
  print(name, age)
say(age=25, name="Pythonia")


# VARIADIC ARGUMENTS
# *args
# Seperti rest operator kalau di JS (...args)
def sum_all(*numbers):
  return sum(numbers)

print(sum_all(1,2,3,4)) # 10


# KEYWORD VARIADIC
# **kwargs
# Mirip object rest
def user_info(**data):
  print(data)

user_info(name="Pythonia", age=25, active=True)
# Output
# {'name': 'Fikri', 'age': 25, 'active': True}


# PASSING FUNCTION AS ARGUMENT
# Kalau di JS disebut callback
def apply(func, value):
  return func(value)

def square(x):
  return x * x

print(apply(square, 5))


# INNER FUNCTIONS
# Fungsi didalam fungsi
def outer():
  def inner():
    print("Inside inner")
  inner()


# LAMBDA FUNCTIONS
# Anonymous Function
# Seperti arrow function kalau di JS. const square = x => x * x
square = lambda x: x * x
print(square(5))


# BEBERAPA BUILT IN FUNCTION YANG SERING DIPAKAI
"""
| Function   | Penjelasan       |
| ---------- | ---------------- |
| print()    | tampilkan output |
| len()      | hitung panjang   |
| type()     | cek tipe         |
| int()      | cast ke int      |
| float()    | cast ke float    |
| str()      | cast ke string   |
| sum()      | jumlahkan list   |
| max()      | nilai terbesar   |
| min()      | nilai terkecil   |
| sorted()   | sorting          |
| range()    | generate angka   |
| abs()      | absolute         |
| round()    | pembulatan       |
| input()    | ambil input user |
"""