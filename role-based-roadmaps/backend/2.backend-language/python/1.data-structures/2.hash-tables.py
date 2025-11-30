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
...
...
...



