# SORTING ALGORITHM


# BUBBLE SORT
# Bandingkan dua elemen bersebelahan → tukar jika salah urut.
# Lakukan sampai tidak ada lagi yang perlu ditukar.
"""
Step
[5, 2, 4, 3]
[2, 5, 4, 3]
[2, 4, 5, 3]
[2, 4, 3, 5]
[2, 3, 4, 5]
"""
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr


# SELECTION SORT
# Cari elemen terkecil → pindahkan ke posisi depan.
"""
Step
[5, 2, 4, 1]
^
min = 1 -> swap ke depan
...
...
[1, 2, 4, 5]
"""
def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr


# INSERTION SORT
# Ambil satu elemen, letakkan pada posisi yang benar di bagian yang sudah terurut.
"""
Step
[5, 2, 4, 3]
[|5]   sorted part
insert 2 -> [2,5]
insert 4 -> [2,4,5]
insert 3 -> [2,3,4,5]
"""
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1

    arr[j+1] = key
  
  return arr


# MERGE SORT
# Divide and Conquer:
# - Bagi array menjadi dua
# - Sort masing-masing
# - Gabungkan kembali
"""
Step
[5, 3, 8, 4]
→ [5,3] + [8,4]
→ [3,5] + [4,8]
→ [3,4,5,8]
"""
def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])
  return result


# QUICK SORT
# Cara kerja:
# - Pilih pivot
# - Bagi array menjadi < pivot, pivot, > pivot
# - Rekursif sorting di kedua sisi
"""
Step
Pivot = 5
[3,2,8,5,4]
→ [3,2,4] + [5] + [8]
"""
def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr)//2]
  left = [x for x in arr if x < pivot]
  mid  = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quick_sort(left) + mid + quick_sort(right)


# Python built-in sort() / sorted()
# Python memakain Timsort, campuran:
# Merge Sort
# Insertion Sort


# PERBANDINGAN
"""
| Algoritma   | Best           | Avg           | Worst         | Catatan         |
| ----------- | ------------   | ------------  | ------------  | --------------- |
| Bubble      | O(n)           | O(n²)         | O(n²)         | mudah           |
| Selection   | O(n²)          | O(n²)         | O(n²)         | swap sedikit    |
| Insertion   | O(n)           | O(n²)         | O(n²)         | bagus utk small |
| Merge       | O(n log n)     | O(n log n)    | O(n log n)    | stabil          |
| Quick       | O(n log n)     | O(n log n)    | O(n²)         | cepat rata-rata |
| Python sort | ⭐ O(n log n) | ⭐ O(n log n) | ⭐ O(n log n) | terbaik         |
"""


