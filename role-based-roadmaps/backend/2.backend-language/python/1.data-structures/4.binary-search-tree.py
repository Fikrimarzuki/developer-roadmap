# BINARY SEARCH TREE

# Struktur BST Node
# Satu node punya: value, left child, right child
"""
     10
    /  \
   5    20
  / \   / \
 3   7 15  25
"""
# Setiap node
# left child < node value
# right child > node value

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


# Untuk buat BST buat class utama
class BST:
  def __init__(self):
    self.root = None


# Insert ke BST
# Aturan insert
# Jika nilai lebih kecil -> masuk ke left
# Jika nilai lebih besar -> masuk ke right
def insert(self, value):
  if self.root is None:
    self.root = Node(value)
    return

  current = self.root
  while True:
    if value < current.value:
      if current.left:
        current = current.left
      else:
        current.left = Node(value)
        return
    else:
      if current.right:
        current = current.right
      else:
        current.right = Node(value)
        return

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(15)
bst.insert(25)

"""
Visual diagramnya
      10
     /  \
    5    20
         / \
       15   25
"""


# Search di BST
def search(self, value):
  current = self.root

  while current:
    if value == current.value:
      return True
    elif value < current.value:
      current = current.left
    else:
      current = current.right

  return False

bst.search(15)  # True
bst.search(8)   # False


# Untuk delete node dalam BST
# Case 1: Node tanpa child
"""
  15
    \
    [20]  <- hapus daun
"""

# Case 2: Node punya 1 child
"""
    10
   /
  [5] <- hapus ini yang punya child
 /
3
"""
# delete 5 → 3 naik ke posisi 5.

# Case 3: Node punya 2 child
"""
     10
    /  \
   5   [20] <- hapus ini
       / \
      15  25
"""
# akan cari pengguna yang sesuai
# delete 20:
# penggantinya adalah 25, maka ganti 20 jadi 25

# Implementasi
def delete(self, value):
  self.root = self._delete_node(self.root, value)

def _delete_node(self, node, value):
  if not node:
    return node

  if value < node.value:
    node.left = self._delete_node(node.left, value)
  elif value > node.value:
    node.right = self._delete_node(node.right, value)
  else:
    # Case 1: no child
    if not node.left and not node.right:
        return None
    
    # Case 2: one child
    if not node.left:
        return node.right
    if not node.right:
        return node.left
    
    # Case 3: two children
    successor = self._min_value(node.right)
    node.value = successor.value
    node.right = self._delete_node(node.right, successor.value)

  return node

def _min_value(self, node):
  while node.left:
    node = node.left
  return node


# Traversal - cara baca BST
# In order (Left -> Node -> Right)
def inorder(self, node):
  if node:
    self.inorder(node.left)
    print(node.value)
    self.inorder(node.right)

# Pre-order (Node -> left -> right)

# Post-order (Left -> right -> Node)


# BST cepat karena?
# Jika tree seimbang
# Height = log(n)
# artinya
# insert -> O(log n)
# search -> O(log n)
# delete -> O(log n)

# Contoh
# 1 juta node:
# log2(1000000) = 20
# cuma perlu 20 langkah


# BST dipakai
# Database indexing (B-Tree = versi tree untuk disk)
# File system (folder tree)
# HTML DOM tree
# Compilers
# Routing table
# Search autocomplete


# Perbandingan BST dengan struktur lain
"""
| Struktur     | Search   | Insert   | Delete   | Notes                   |
| ------------ | -------- | -------- | -------- | ----------------------- |
| List (array) | O(n)     | O(n)     | O(n)     | lambat                  |
| Hash Table   | O(1)     | O(1)     | O(1)     | tidak urut              |
| BST          | O(log n) | O(log n) | O(log n) | data otomatis terurut   |
| Sorted list  | O(log n) | O(n)     | O(n)     | insert lambat           |
| Heap         | O(n)     | O(log n) | O(log n) | prioritas, bukan search |
"""
# BST unggul karena:
# - struktur terurut
# - operasi logaritmik
# - representasi pohon yang natural


# Bagaimana jika value sama?
# tidak ada aturan umum tapi bisa menggunakan salah satu pilihan

# Value sama -> masuk ke kanan
"""
    10
   /  \
  5    20
         \
          20
"""

# Value sama -> masuk ke kiri
"""
     10
    /  \
   5    20
        /
      20
"""

# Value sama tidak ditulis ulang
"""
    10
   /  \
  5    20
"""
# pilihannya bisa di ignore 
# if value == current.value:
#   return  # ignore

# atau pilihan lainnya menyimpan count
# Node:
# value = 20
# count = 3


# Implementasi value sama
# Masuk kanan
def insert(self, value):
  if self.root is None:
    self.root = Node(value)
    return
  
  current = self.root

  while True:
    if value < current.value:
      if current.left:
        current = current.left
      else:
        current.left = Node(value)
        return
    else:  # value >= current.value
      if current.right:
        current = current.right
      else:
        current.right = Node(value)
        return

# Masuk ke kiri
if value <= current.value:
  # left
else:
  # right

# Menggunakan count
if value == current.value:
  current.count += 1
  return

class Node:
  def __init__(self, value):
    self.value = value
    self.count = 1
    self.left = None
    self.right = None


