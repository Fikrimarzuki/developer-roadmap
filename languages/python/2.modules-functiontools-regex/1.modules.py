# MODULES

# Module
# File python yang bisa berisi fungsi, class, variabel, logika yang di import ke file lain.

# Builtin Modules
# module yang sudah disediakan python
# Contoh:
"""
| Module        | Fungsi               |
| ------------- | -------------------- |
| math          | matematika           |
| os            | mengakses filesystem |
| sys           | sistem interpreter   |
| json          | serialize JSON       |
| datetime      | waktu dan tanggal    |
| re            | regex                |
| random        | RNG                  |
| collections   | deque, Counter       |
"""


# Cara import
# Memakai math
import math
print(math.sqrt(16))   # 4.0
# Memakai datetime
from datetime import datetime
print(datetime.now())


# Custom module - buatan sendiri
# Buat file calculator.py
# karena file sejajar dengan file yang dijalankan maka
import calculator
print(calculator.add(10,5))
# atau bisa import spesifik
from calculator import add
print(add(10,4))
# atau bisa dibuat alias
import calculator as calc
print(calc.add(1,3))

# Modules digunakan untuk
# - Memecah file menjadi lebih terstruktur
# - Membuat helpers (utils.py)
# - Mengorganisir API / route
# - Reuse fungsi di berbagai file


