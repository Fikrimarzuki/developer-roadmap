# ARRAYS AND LINKED LIST

# Python biasa menggunakan list karena lebih fleksibel dan bisa menampung tipe data apapun
# List sebenarnya adalah dynamic array yang fleksibel

# ARRAY DI PYTHON
# Hanya boleh satu tipe data
# Digunakan untuk low-level memory optimization 
from array import array
arr = array("i", [1,2,3])
# tapi biasanya programmer python menggunakan list


# LIST VS ARRAY
"""
| Feature        | Python List   | Python Array        |
| -------------- | ------------- | ------------------- |
| Mixed types    | ✔ bisa        | ✖ tidak            |
| Ukuran dinamis | ✔             | ✔                  |
| Kecepatan      | Cepat         | Lebih cepat         |
| Memory         | Besar         | Lebih kecil         |
| Kegunaan       | General       | Numeric-heavy apps  |
| Implementasi   | Dynamic array | Compact typed array |
"""
# Jadi list sudah dianggap "array" oleh kebanyakan developer python



# LINKED LIST
# Linked List adalah struktur data yang terdiri dari elemen-elemen yang disebut Node.

# Setiap Node punya 2 bagian
# value -> data
# next -> pointer (alamat) ke node berikutnya

# Diagram
# [ value | next ] -> [ value | next ] -> [ value | next ] -> None


# Berbeda dengan list
"""
✔ List (Python)
- Data berurutan di memory

Index: 0  1  2  3
Value:10 20 30 40
- Akses cepat (O(1)) => arr[2] langsung tau posisinya
- Insert/delete di tengah lambat (O(n)) => harus geser elemen lain

✔ Linked List
- Tiap node punya pointer ke node berikutnya

[10] -> [20] -> [30] -> [40] -> None
- Akses lambat (O(n))
- Insert/delete cepat di awal/tengah (O(1))

"""
# SKEMANYA
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
# tiap node punya value dan next yang pointing ke node berikutnya

# Buat Linked List (apply)
class LinkedList:
  def __init__(self):
    self.head = None
  
  # tambah data
  def append(self, value):
    new_node = Node(value)

    if self.head is None:
      self.head = new_node
      return

    current = self.head
    while current.next:
      current = current.next

    current.next = new_node

  # print data
  def print_list(self):
    current = self.head
    while current:
      print(current.value, end=" -> ")
      current = current.next
    print("None")

  # get data
  def get(self, index):
    current = self.head
    count = 0

    while current:
      if count == index:
        return current.value
      current = current.next
      count += 1
    
    return None

  # insert data
  def insert_after(self, target, value):
    current = self.head
    while current:
      if current.value == target:
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        return
      current = current.next

  # delete data
  def delete(self, value):
    current = self.head

    if current.value == value:
      self.head = current.next
      return

    while current.next:
      if current.next.value == value:
        current.next = current.next.next
        return
      current = current.next


# Cara Pakai
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
# akan terbentuk [10] -> [20] -> [30] -> None

# Cara print
ll.print_list()


# Akses lambat karena jika mau akses node ketiga (value=30), tidak bisa langsung list[2]
# Harus berjalan satu per satu
# Start → [10] -> [20] -> [30]

print(ll.get(2))
# index 0 → 10
# index 1 → 20
# index 2 → 30  ← ketemu


# INSERT CEPAT
# Kalau list
# [10, 20, 30] # insert 15 akan menggeser semua elemen

# Kalau linked list cukup ubah pointer
# [10] -> [20] -> [30]
# 10.next = 15
# 15.next = 20
# menjadi
# [10] -> [15] -> [20] -> [30]
ll.insert_after(10, 15)
ll.print_list()


# DELETE
# [10] -> [20] -> [30]
# 10.next = 30
# menjadi
# [10] -> [30]
ll.delete(15)
ll.print_list()

