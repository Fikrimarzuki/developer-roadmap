# LISTS

# List
numbers = [1,2,3,4]
alphabets = ["a","b","c","d"]
mixed = ["hello", 10, True, 3.14]


# INDEXING
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # apple
print(fruits[2])  # orange
print(fruits[-1]) # orange
print(fruits[-2]) # banana


# MENGUBAH ISI LIST
fruits[1] = "mango"


# TAMBAH ITEM
# append() - tambah 1 item
fruits.append("grape")
# insert() - tambah di index tertentu
fruits.insert(1, "melon")


# MENGHAPUS ITEM
# remove() - berdasarkan value
fruits.remove("banana")
# pop() - hapus berdasarkan index, dan mengembalikan value
last = fruits.pop()
print(last)
# del() - hapus item
del fruits[0]


# CEK ITEM ADA DI LIST
if "apple" in fruits:
  print("Ada apple")


# PANJANG LIST
print(len(fruits))


# LOOPING LIST
# value tanpa index
for fruit in fruits:
  print(fruit)
# value dengan index
for i, fruit in enumerate(fruits):
  print(i, fruit)


# SLICING
numbers = [1,2,3,4,5]
print(numbers[1:4]) # [2,3,4]
print(numbers[:3]) # [1,2,3]
print(numbers[::2]) # [1,3,5]
print(numbers[::-1]) # reverse list


# LIST COMPREHENSION
# contoh map apabila di JS
numbers = [1,2,3,4]
squares = [n * n for n in numbers]
# contoh filter apabila di JS
even = [n for n in numbers if n % 2 == 0]


# SORTING LIST
# Ascending
nums = [5,3,1,4]
nums.sort()
prints(nums)  # [1,3,4,5]

# Descending
nums.sort(reverse=True)

# return new list
sorted_nums = sorted(nums)
sorted_desc = sorted(nums, reverse=True)


# LIST OF LISTS (MATRIX)
matrix = [
  [1,2,3],
  [4,5,6]
]
print(matrix[1][2])  # 6
