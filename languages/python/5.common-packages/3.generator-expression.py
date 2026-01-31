# GENERATOR EXPRESSION

# Versi lazy dari list comprehension
# List comprehension
[x * x for x in range(5)]
# membuat seluruh list di memory

# Generator expression
(x * x for x in range(5))
# tidak membuat list, tapi menghasilkan nilai satu persatu saat dibutuhkan

# Analogi
# List comprehension - memasak semua makanan sekaligus
# Generator expression - memasak hanya saat orang pesan


# Degan generator expression
# - Lebih hemat memory
# - Cepat untuk streaming data
# - Scalable untuk jutaan data
# - Ideal untuk file besar

# Contoh extreme
nums = (x for x in range(10_000_000))
# tidak memakai memory besar karena datanya tidak disimpan

# Contoh basic
gen = (x * 2 for x in range(5))
print(gen)
# output
# <generator object ... >
# ambil nilainya
print(next(gen))
print(next(gen))


# Looping generator
gen = (x*x for x in range(5))
for value in gen:
  print(value)
# 0
# 1
# 4
# 9
# 16


# Generator hanya bisa digunakan sekali
# jika sudah selesai looping - tidak bisa dipakai lagi
gen = (x for x in range(3))
for (v in gen):
  print(v)

for (v in gen):
  print(v) # tidak keluar apa-apa


# List comprehension vs generator expression
# list comp
# data = [x*2 for x in range(1_000_000)]
# memory besar - bisa crash

# generator
data = (x*2 for x in range(1_000_000))
# memory hanya beberapa bytes


# Filter + transform
evens = (x for x in range(10) if x % 2 == 0)


# Generator di pipeline]
# data panjang
gen = (line.strip() for line in open("logs.txt"))
# filter
errors = (line for line in gen if "ERROR" in line)
# lalu proses
for err in errors:
  print(err)


# Generator + sum(), any(), max(), min()
# bisa langsung dipakai
total = sum(x*x for x in range(10))
# tidak perlu disimpan di list
sum([x*x for x in range(10)])
# lebih hemat memory


# Real world FastAPI / async processing
# generator bisa dipakai untuk streaming response
async def generate_numbers():
  for i in range(5):
    yield str(i)
    await asyncio.sleep(1)


# Generator expression vs function generator
# Generator expression
(x*x for x in range(10))
# simple, inline

# Generator function
def mygen():
  for x in range(10):
    yield x*x
# fleksibel, bisa punya banyak logic, bisa handle kondisi kompleks


# Nested generator expression
gen = (x+y for x in [1,2] for y in [10,20])


# Generator exhaustion
g = (x forx in range(3))
print(list(g)) # [0,1,2]
print(list(g)) # []


# Kesalahan umum
# Membuat generator tapi butuh list
nums = (x for x in range(10))
# len(nums) # Error

# Solusi
nums = list(x for x in range(10))


# Kesimpulan Besar
"""
| Fitur       | List Comprehension     | Generator Expression      |
| ----------- | ---------------------- | ------------------------- |
| Memory      | besar                  | kecil / hemat             |
| Speed       | cepat untuk data kecil | scalable untuk data besar |
| Output      | list langsung          | nilai satu per satu       |
| Reusability | bisa dipakai ulang     | hanya sekali              |
| Use case    | transform data kecil   | streaming / big data      |
"""


# Contoh real use case
# analisa file besar 10GB
"""
lines = (line for line in open("bigfile.log"))
errors = (l for l in lines if "ERROR" in l)

for e in errors:
  print(e)
"""
# tidak ada list besar - tidak ada memory error






