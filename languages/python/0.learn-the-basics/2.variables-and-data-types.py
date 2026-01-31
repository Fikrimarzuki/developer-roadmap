# VARIABEL
name = "Ini adalah string"
age = 25
is_active = True


# DINAMIS
x = 10
x = "hello"
# tidak akan error


# NAMING RULES
# Boleh huruf, angka, underscore
# Tidak boleh dimulai angka atau beberapa simbol
# Case-sensitive
"""
Contoh valid

first_name = "John"
age2 = 20
__x = 100
"""
"""
Contoh error

2age = 100 # error
first-name = "Alex" # error
"""


# DATA TYPES
strDataType = "hello" # str
intDataType = 25 # int
floatDataType = 3.14 # float
boolDataType = True # bool menggunakan huruf kapital di awal True/False
listDataType = [1,2,3] # seperti array kalau di JS
dictDataType = { "name": "nama" } # seperti object kalau di JS
tupleDataType = (1,2) # seperti array tapi immutable di JS
setDataType = {1,2,3} # seperti Set di JS
noneDataType= None # seperti null kalau di JS


# CHECK TYPE
a = 10
print(type(a))
# output <class 'int'>


# MULTIPLE ASSIGNMENT
a,b,c = 1,2,3
print(a, b, c)
a, b = b, a


# CONSTANTS
# tidak punya constant, hanya convention saja, variabel dibuat kapital
MAX_USERS = 100
API_KEY = "secret"


# NONE
# Seperti null kalau di JS
val = None


# TYPE HINTING
# Optional: mirip TS tapi tidak wajib
name: str = "Budi"
age: int = 25


# NUMERIC OPERATIONS
print(1 + 1) # 2
print(1 * 2) # 2
print(10 / 3) # 3.333...
print(10 // 3) # 3 pembulatan ke bawah
print(10 % 3) # 1
print(2 ** 3) # 8 (power)

