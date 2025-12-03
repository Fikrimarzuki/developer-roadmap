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

p1 = Person("Fikri", 25)
print(p1.name)
print(p1.age)


# METHOD (fungsi dalam class)
class Person:
  def __init__(self, name):
    self.name = name
  
  def greet(self):
    print(f"Hello, my name is {self.name}")

p = Person("Fikri")
p.greet()

# self adalah reference ke object itu sendiri
# di JS biasanya menggunakan this



