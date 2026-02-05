# HASH TABLES

# Hash table adalah struktur data yang menyimpan data dalam bentuk:
# key -> value

# Key diubah menjadi index oleh fungsi hash()
# "name" --hash--> 192817281 --mod--> index 3

# Hash Table bekerja
# Contoh misal ada array internal ukuran 5:
"""
Index:   0      1      2      3      4
Value:  [ ]    [ ]    [ ]   [ ]    [ ]

lalu mau simpan

key: "name" value: "Budi"
"""

# Prosesnya
# 1. Hitung hash
# hash("name") = 292818273

# 2. Konversi ke index array
# 292818273 % 5 = 3

# 3. Simpan ke index 3
"""
Index:   0      1      2      3               4
Value:  [ ]    [ ]    [ ]   ["name":"Budi"] [ ]
"""


# COLLISION
# Jika dua key menghasilkan index yang sama
# Contoh:
# hash("name") % 5 = 3
# hash("email") % 5 = 3

# Cara python mengatasi ini
# Python menggunakan chaining
"""
Index 3:
["name":"pythonia"] -> ["email":"pythonia@email.com"] -> None
Bentuknya seperti Linked List di dalam Hash Table
"""


# IMPLEMENTASI HASH TABLE (SECARA MANUAL)
# Step 1: buat bucket array
class HashTable:
  def __init__(self):
    self.size = 10
    self.table = [[] for _ in range(self.size)]

# Step 2: hash function
def _hash(self, key):
  return hash(key) % self.size

# Step 3: insert key-value
def insert(self, key, value):
  index = self._hash(key)
  bucket = self.table[index]

  for i, (k, v) in enumerate(bucket):
    if k == key:
      bucket[i] = (key, value)
      return

  bucket.append((key, value))

# Step 4: retrieve value
def get(self, key):
  index = self._hash(key)
  bucket = self.table[index]

  for k, v in bucket:
    if k == key:
      return v

  return None

# Demo
ht = HashTable()
ht.insert("name", "Pythonia")
ht.insert("age", 25)

print(ht.get("name"))  # Pythonia
print(ht.get("age"))   # 25


# HASH TABLE DIGUNAKAN DALAM
# Python dictionary
# {"name": "Pythonia"}

# JSON
# JSON → convert ke dictionary di Python.

# Cache (Redis uses Hash Table)
# "user:10" → {name:"Pythonia", age:25}

# Routing table
# API endpoint
# "/api/login" → function_login

# Database Indexing
# B-Tree & Hash Index.

# Counting frequency
freq = {}
for word in list_of_words:
    freq[word] = freq.get(word, 0) + 1


# BIG O Time Complexity
"""
| Operasi | Average | Worst                  |
| ------- | ------- | ---------------------- |
| Insert  | O(1)    | O(n) (collision parah) |
| Get     | O(1)    | O(n)                   |
| Delete  | O(1)    | O(n)                   |

Worst terjadi jika semua key masuk di index yang sama, tapi hal ini jarang karena hashing modern bagus.
"""

# Dibanding struktur lain
"""
| Struktur    | Akses   | Insert  | Delete  |
| ----------- | ------  | ------  | ------  |
| Array       | O(1)    | O(n)    | O(n)    |
| Linked List | O(n)    | O(1)    | O(1)    |
| Hash Table  | ⭐O(1) | ⭐O(1)  | ⭐O(1)  |
"""

