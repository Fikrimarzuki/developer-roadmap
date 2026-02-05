# OBJECT ORIENTED PROGRAMMING

# Dalam OOP, buat objek dalam class
# class = blueprint
# object = hasil cetakan

# OOP penting karena
# - membuat struktur kode rapi
# - mudah diperbesar (scalable)
# - dipakai di project besar
# - cocok untuk API, database models, services
# - konsep yang sama di Java, C#, PHP, JavaScript (class terbaru)


# CLASS
# nama class biasa diawali dengan kapital
class Person:
  pass

# Buat class dengan tribut & constructor
# __init__ -> constructor (dipanggil ketika object dibuat)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Pythonia", 25)
print(p1.name)
print(p1.age)


# METHOD (fungsi dalam class)
class Person:
  def __init__(self, name):
    self.name = name
  
  def greet(self):
    print(f"Hello, my name is {self.name}")

p = Person("Pythonia")
p.greet()

# self adalah reference ke object itu sendiri
# di JS biasanya menggunakan this


# Class variable vs instance variabel
# Instance variable (tiap object punya nilai)
# self.name

# Class variable (shared oleh semua object)
class Person:
  species = "Human"


# METHODS (Instance, Class, Static)
# Instance methods
# def greet(self):
# cara pakai
# obj.greet()

# Class methods
# dipanggil tanpa bikin object
# menggunakan decorator @classmethod
class Person:
  count = 0

  @classmethod
  def increment(cls):
    cls.count += 1

# Static methods
# tidak butuh self atau cls
class Math:
  @staticmethod
  def add(a, b):
    return a + b
# dipanggil
Math.add(5, 10)


# DUNDER METHODS (MAGIC METHODS)
# Dunder = Double Underscore
"""
contoh
__init__
__str__
__repr__
__add__
__len__
__getitem__
__iter__

digunakan untuk custom behavior object
"""

# __str__
# tampilkan object jadi string
class Person:
  def __init__(self, name):
    self.name = name
  
  def __str__(self):
    return f"Person(name={self.name})"

print(Person("Pythonia"))

# __len__
class Team:
  def __init__(self, members):
    self.members = members
  
  def __len__(self):
    return len(self.members)

# __add__
class Money:
  def __init__(self, amount):
    self.amount = amount
  
  def __add__(self, other):
    return Money(self.amount + other.amount)



# INHERITANCE
# inheritance = class bisa mewarisi sifat class lain
class Animal:
  def speak(self):
    print("Animal speaking")

class Dog(Animal):
  def speak(self):
    print("Woof!")

# cara pakai
d = Dog()
d.speak()


# Gunaka super untuk panggil parent
class Animal:
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)  # panggil constructor parent
    self.breed = breed


# MULTIPLE INHERITANCE
class A:
  pass

class B:
  pass

class C(A, B):
  pass


# Contoh OOP dalam real project
# FastAPI / Flask router
# class UserService:
#   def get_user(self, id):
#     ...

# Database Model (ORM)
# class User(Base):
#   id = Column(Integer, primary_key=True)
#   username = Column(String)

# Payment Gateway wrapper
# class PaymentGateway:
#   def pay(self):
#     pass


# SUMMARY OOP
"""
| Konsep      | Fungsi                          |
| ----------- | ------------------------------- |
| Classes     | blueprint object                |
| Methods     | fungsi dalam class              |
| Dunder      | custom behavior (str, len, add) |
| Inheritance | mewarisi class lain             |
| super()     | memanggil parent constructor    |
"""


