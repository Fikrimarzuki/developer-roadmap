# RECURSION

# fungsi yang memanggil dirinya sendiri
"""
def hello():
  print("Hello")
  hello()
"""
# ini akan infinite recursion -> akan error


# Struktur
# Punya base case - kondisi untuk berhenti
# Punya recursive case - bagian yang memanggil fungsi lagi
def countdown(n):
  if n == 0:          # base case
    print("Done")
    return
  print(n)
  countdown(n - 1)    # recursive case

# Jadi misal countdown(3)
# Maka akan jalan lalu didalamnya memanggil countdown(3 - 1) sehingga countdown(2)
# Maka akan jalan lalu didalamnya memanggil countdown(2 - 1) sehingga countdown(1)
# Maka akan jalan lalu didalamnya memanggil countdown(1 - 1) sehingga countdown(0)
# Karena n === 0 maka akan return


# Untuk mengerti recursion
# Mencari base casenya, dimana ujungnya atau tempat berhentinya
# Bagaimana cara menuju base case di tiap stepnya
"""
Misalnya:
countdown(5)
- base: n=0 (berhenti)
- recursive: countdown(n-1)
factorial(5)
- base: 1
- recursive: n * factorial(n-1)
tree traversal
- base: node = None
- recursive: call left, then call right
"""

# Contoh lain - faktorial
def factorial(n):
  if n == 1:         # base case
    return 1
  return n * factorial(n - 1)


# Contoh traverse folder
"""
root
 ├── a.txt
 ├── img
 │   ├── 1.png
 │   └── 2.png
 └── docs
     └── notes.txt
"""
import os

def walk(path):
  for item in os.listdir(path):
    full = os.path.join(path, item)
    if os.path.isdir(full):
      walk(full)
    else:
      print(full)


# Contoh binary tree
def inorder(node):
  if not node:
    return
  inorder(node.left)
  print(node.value)
  inorder(node.right)


# Recursion = DFS
# graph DFS menggunakan recursion secara alami
def dfs(node, visited):
  if node in visited:
    return
  visited.add(node)
  for neighbor in graph[node]:
    dfs(neighbor, visited)


# Contoh backtracking
# [1,2] → [[], [1], [2], [1,2]]
def subsets(nums):
  result = []

  def backtrack(path, index):
    result.append(path[:])

    for i in range(index, len(nums)):
      path.append(nums[i])
      backtrack(path, i + 1)
      path.pop()

  backtrack([], 0)
  return result


# Recursion vs Loop
"""
| Task                  | Recursion  | Loop             |
| --------------------- | ---------  | ---------------- |
| Tree/Graph traversal  | ⭐ mudah   | sulit            |
| Counting              | bisa       | ⭐ mudah         |
| Sorting (merge/quick) | ⭐ alami   | rumit            |
| Directory traversal   | ⭐ simple  | rumit            |
| Fibonacci             | natural    | loop lebih cepat |
"""


# Dalam masalah nyata recursion dipakai di
# - Processing folder/file (backup system, file manager)
# - HTML DOM traversal
# - JSON traversal
# - Graph / network crawling
# - AI search (minimax)
# - Server routing tree
# - Compiler parsing







