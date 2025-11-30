# TUPLES

# Tuple
# Kumpulan nilai seperti list, tetapi immutable

# TUPLE VS LIST
"""
| List                     | Tuple                  |
| ------------------------ | ---------------------- |
| `[]`                     | `()`                   |
| Mutable                  | Immutable              |
| Lebih lambat             | Lebih cepat            |
| Cocok untuk data berubah | Cocok untuk data tetap |
"""

# Gunakan Tuple jika
# ✔ Data tidak akan berubah
# ✔ Mau lebih cepat dari list
# ✔ Mau return multiple values
# ✔ Mau data aman dari modifikasi

# Cara buat
person = ("Pythonia", 25, "Indonesia")


# TUPLE DENGAN 1 ITEM
# Harus pakai koma apabila hanya ada 1 item
x = (5) # dianggap integer!
y = (5,) # ini tuple


# AKSES ELEMEN SAMA SEPERTI LIST
fruits = ("apple", "banana", "orange")

print(fruits[0]) # apple
print(fruits[-1]) # orange


# TUPLE IMMUTABLE - TIDAK BISA DIUBAH
numbers = (1,2,3)
"""
numbers[0] = 10 # ERROR

Output:
TypeError: 'tuple' object does not support item assignment
"""


# TUPLE SLICING
nums = (1,2,3,4,5)
print(nums[1:4]) # (2,3,4)
print(nums[::-1]) # reverse tuple


# TUPLE UNPACKING
person = ("Pythonia", 25)
name, age = person
print(name) # Pthonia
print(age) # 25


# MULTIPLE REETURN VALUE = TUPLE
def get_user():
  return "Pythonia 2", 25

name, age = get_user()


# SEBAGAI KEY DICITIONARY
locations = {
  (1, 2): "Point A",
  (3, 5): "Point B"
}
