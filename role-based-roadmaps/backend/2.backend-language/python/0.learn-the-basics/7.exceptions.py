# EXCETIONS (ERROR HANDLING)
# TRY, EXCEPT, FINALLY

# EXCEPTIONS
# Error yang terjadi saat program berjalan

"""
Contoh error umum:
- Membagi dengan 0
- Mengubah string ke int tapi string tidak valid
- Mengakses index yang tidak ada
- File tidak ditemukan
Kalau error terjadi dan tidak ditangani, program akan berhenti.
Agar tidak berhenti bisa dengan menggunakan try/except
"""

"""
Di Python, semua error adalah class, contohnya:
- ValueError
- TypeError
- KeyError
- ZeroDivisionError
"""

# BASIC TRY/EXCEPT
try:
  result = 10 / 0
except:
  print("Error terjadi!")



# MENANGKAP SPESIFIK ERROR
try:
  value = int("hello")
except ValueError:
  print("Tidak bisa convert ke integer")

try:
  items = [1, 2, 3]
  print(items[10])
except IndexError:
  print("Index tidak ditemukan")


# MULTIPLE EXCEPT
try:
  x = int("abc")
except ValueError:
  print("Value error")
except TypeError:
  print("Type error")


# AMBIL DETAIL ERROR
try:
  x = 10 / 0
except Exception as e:
  print("Error:", e)
# Error: division by zero


# FINALLY
try:
  file = open("test.txt")
except:
  print("File tidak ditemukan")
finally:
  print("Selesai dicek")


# ELSE
try:
  x = int("10")
except:
  print("Error")
else:
  print("Tidak ada error")
# Tidak ada error


# RAISE ERROR (BUAT ERROR SENDIRI)
age = -5
if age < 0:
  raise ValueError("Umur tidak valid!")
# karena line diatas tidak menggunakan try except, maka kode setelahnya tidak dijalankan karena program berhenti


# CUSTOM ERROR CLASS
"""
class CustomError(Exception):
  pass
raise CustomError("Something wrong!")
"""
class AgeError(Exception):
  pass

age = -5
if age < 0:
  raise AgeError("Umur tidak boleh negatif!")

# Output:
# Traceback...
# AgeError: Umur tidak boleh negatif!

# Contoh custom error lain dan handlingnya
class AgeError2(Exception):
  pass

try:
  age = -1
  if age < 0:
    raise AgeError2("Umur tidak valid")
except AgeError2 as e:
  print("Terjadi error:", e)
# Output:
# Terjadi error: Umur tidak valid

# Jadi bisa dibuat beda error beda penanganan
class AgeError3(Exception):
  pass

class NameErrorCustom(Exception):
  pass

try:
  name = ""
  age = -5

  if name == "":
    raise NameErrorCustom("Nama tidak boleh kosong")

  if age < 0:
    raise AgeError3("Umur harus positif")

except NameErrorCustom as e:
  print("Error Nama:", e)

except AgeError3 as e:
  print("Error Umur:", e)

# Ouput saat name string kosong
# Error Nama: Nama tidak boleh kosong
