# DICTIONARIES

# Kumpulan data key -> value
# Mirip seperti object kalau di JS

# Dictionary
user = {
  "name": "Budi",
  "age": 25,
  "city": "Jakarta"
}


# AKSES VALUE
print(user["name"])
print(user["age"])


# UBAH VALUE
user["age"] = 26


# TAMBAH KEY
user["job"] = "Developer"


# HAPUS DATA
# del()
del user["city"]

# pop()
job = user.pop("job")
print(job) # developer

# popitem()
# hapus item terakhir
key, value = user.popitem()


# CEK ADA KEY
if "name" in user:
  print("key name ada")


# MENDAPATKAN KEY, VALUE, ITEMS
print(user.keys()) # dict_keys([...])
print(user.values()) # dict_values([...])
print(user.items()) # dict_items([...])

for key, value in user.items():
  print(key, value)

# Output
# name Budi
# age 25


# NESTED DICTIONARY (JSON STYLE)
user = {
  "name": "Alex",
  "address": {
    "city": "Bogor",
    "country": "Indonesia"
  }
}
print(user["address"]["city"])


# LOOPING DICTIONARY
# Key
for key in user:
  print(key)

# Key + value
for key, value in user.item():
  print(f"{key}: {value}")


# COPY DICTIONARY (AVOID REFERENCE)
new_user = user.copy()


# MERGE DICTIONARIES
# Python 3.9+
# merged = dict1 | dict2
# merged = {**dict1, **dict2}


# GET VALUE TANPA ERROR - get()
# print(user["age2"]) # ERROR
# agar tidak error
print(user.get("age2", "not found"))
# not found


