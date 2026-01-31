# POLYMORPHISM AND ABSTRACTION

# POLYMORPHISM
# Satu interface, banyak bentuk

# Contoh
class Dog:
  def speak(self):
    return "Woof!"

class Cat:
  def speak(self):
    return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
  print(animal.speak())

# methodnya sama speak() tapi hasilnya tergantung jenis objectnya


# POLYMORPHISM DENGAN INHERITANCE
class Animal:
  def speak(self):
    return "Some sound"

class Cow(Animal):
  def speak(self):
    return "Moo!"

class Sheep(Animal):
  def speak(self):
    return "Baa!"

for animal in [Cow(), Sheep(), Animal()]:
  print(animal.speak())


# POLYMORPHISM PADA FUNCTION
def make_sound(animal):
  print(animal.speak())

make_sound(Dog())
make_sound(Cat())

# Real case polymorphism dalam API design
class Payment:
  def pay(self):
    raise NotImplementedError

class OVO(Payment):
  def pay(self):
    return "Pay with OVO"

class Dana(Payment):
  def pay(self):
    return "Pay with DANA"

def checkout(gateway: Payment):
  print(gateway.pay())

checkout(OVO())
checkout(Dana())


# ABSTRACTION
# menyembunyikan detail internal dan hanya memperlihatkan bagian penting

# Abstraction penting karena
# - Memaksa untuk mengikuti struktur class tertentu
# - Menghindari error karena method tidak diimplementasi
# - Lebih rapi dan clean
# - Dipakai di semua framework besar (Django, FastAPI)

from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def speak(self):
    pass

# artinya setiap class yang mewarisi Animal HARUS punya method speak()

class Dog(Animal):
  def speak(self):
    return "Woof!"

# Jika lupa mengimplementasi speak(), Python error:
# Jika lupa mengimplementasi speak(), Python error:


# Contoh Real case
from abc import ABC, abstractmethod

class Database(ABC):

  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def query(self, sql):
    pass

class MySQL(Database):
  def connect(self):
    print("Connected to MySQL")

  def query(self, sql):
    print("Running:", sql)

db = MySQL()
db.connect()
db.query("SELECT * FROM users")


# POLYMORPHISM + ABSTRACTION = POWER
# Dalam project besar:
# - Abstraction = blueprint (kontrak yang harus dipenuhi)
# - Polymorphism = fleksibilitas implementasi

# Contoh BE
class Cache(ABC):
  @abstractmethod
  def set(self, key, value): pass

  @abstractmethod
  def get(self, key): pass

# Implementasi Redis
class RedisCache(Cache):
  def set(self, key, value):
    # ...

  def get(self, key):
    # ...

# Implementasi Memory Cache
class MemoryCache(Cache):
  def set(self, key, value):
    self.store[key] = value

  def get(self, key):
    return self.store.get(key)

cache: Cache = MemoryCache()
cache.set("a", 123)
print(cache.get("a"))

