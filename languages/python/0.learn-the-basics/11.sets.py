# SETS

# Struktur data yang berbeda dari list dan tuple
# Sering dipakai untuk operasi matematika (union, intersection, dll)

# tidak punya index dan tidak mengizinkan duplikasi

# Sets
numbers = {1, 2, 3, 4}

# TIDAK PUNYA INDEX
# numbers[0] akan error
# Apabila ingin ambil elemen pertama bisa convert ke list dahulu

# OTOMATIS HILANGKAN DUPLIKASI
nums = {1, 2, 2, 3, 3, 3}
print(nums)
# output:
# {1, 2, 3}


# MEMBUAT SET
# cara biasa
s = {1, 2, 3}
# dari list
s = set([1, 2, 2, 3])


# TAMBAH DATA KE SET
# add()
s.add(10)

# HAPUS DATA DARI SET
# remove()
# akan error jika data tidak ada
s.remove(2)
# s.remove(12) # Error

# discard()
# tidak error jika data tidak ada
s.discard(12) # tidak error

# pop()
# hapus elemen acak
s.pop()
# Karena set tidak punya index dan tidak memiliki urutan pasti
q = {10,20,30}
print(q.pop()) # hasil bisa 10, atau 20 atau 30
# ambil value + hilangkan
s2 = {10, 20, 30}
val = s2.pop()
print(val)
print(s2)


# CEK VALUE ADA DI SET
if 3 in s:
  print("ada")


# LOOPING SET
for item in s:
  print(item)


# OPERASI MATEMATIKA SET
# Union (gabung)
a = {1,2,3}
b = {3,4,5}
print(a | b)
# Output
# {1,2,3,4,5}

# Intersection (irisan)
print(a & b)
# Output
# {3}

# Difference
# hanya ada di a
print(a - b)
# Output
# {1,2}

# hanya ada di b
print(b - a)
# Output
# {4,5}

# Symmetric Difference (selain gabungan yang sama)
print(a ^ b)
# Output
# {1,2,4,5}


# CONVERT LIST - SET(REMOVE DUPLICATES)
nums = [1,2,2,3,3,4]
unique = set(nums)
print(unique)
# Output:
# {1,2,3,4}


# CONVERT SET - LIST (KALAU MAU DIURUTKAN)
nums = list(set([3,1,2,3,2,1]))
print(sorted(nums))
# Output
# [1,2,3]

# Dengan mengubah ke list jadi punya index juga
print(nums[0])


# UNTUK AMBIL ELEMENT TANPA HAPUS
s = {10,20,30}
val = next(iter(s))
print(val)
# Output bisa salah satu dari 10,20,30


