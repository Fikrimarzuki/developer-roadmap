# HEAPS, STACKS, QUEUES

# STACKS
# LIFO - Last In, First Out
# struktur data di mana elemen terakhir yang dimasukkan adalah elemen pertama yang dikeluarkan
"""
Operasi Dasar:
| Operasi   | Arti                              |
| --------- | --------------------------------- |
| push(x)   | masukkan ke atas                  |
| pop()     | keluarkan elemen paling atas      |
| peek()    | lihat elemen atas tanpa menghapus |
| isEmpty() | apakah stack kosong               |
"""
# Implementasi
stack = []
stack.append(10)  # push
stack.append(20)
stack.append(30)

print(stack.pop())  # 30
print(stack[-1]) # peeking

# Contoh Stack
# Undo/Redo di editor (VSCode, Word)
# Call Stack (fungsi rekursi)
# Parsing (cek kurung (){}[])
# Depth First Search (DFS)
# Browser navigation (back/forward)


# QUEUES
# FIFO - First In, First Out
# antrian, elemen pertama yang masuk adalah yang pertama keluar.
"""
Operasi dasar:
| Operasi    | Arti               |
| ---------- | ------------------ |
| enqueue(x) | tambah ke belakang |
| dequeue()  | ambil dari depan   |
| peek()     | lihat elemen depan |
| isEmpty()  | apakah kosong      |
"""
# Implementasi
from collections import deque

queue = deque()

queue.append(10)    # enqueue
queue.append(20)
queue.append(30)

print(queue.popleft())  # dequeue

# Contoh queue
# Task scheduling (OS scheduler)
# Job queues (RabbitMQ, Redis queue, Celery)
# Breadth First Search (BFS)
# Server request handling
# Messaging system


# HEAP
# struktur data yang digunakan untuk priority queue.
# Elemen dengan nilai terkecil atau terbesar akan keluar terlebih dahulu (tergantung jenis heap).

# implementasi
import heapq

nums = [5, 3, 8, 1]
heapq.heapify(nums)

print(nums)  # menjadi heap (urutan internal tidak berurutan)

# pop elemen prioritas tertinggi (paling kecil)
print(heapq.heappop(nums))  # 1

# push elemen
heapq.heappush(nums, 2)

# Contoh heap
# Priority queue (misalnya ambulan → prioritas tinggi)
# Shortest path algorithms (Dijkstra)
# Event simulation
# CPU scheduling
# Data stream (cari top K element)




# REVIEW WITH CODE
# Stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())  # 3
print(stack)        # [1,2]

# Queue
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())  # 1
print(queue)            # deque([2,3])

# Heap
import heapq

pq = []
heapq.heappush(pq, (1, "urgent"))
heapq.heappush(pq, (5, "normal"))
heapq.heappush(pq, (3, "medium"))

print(heapq.heappop(pq))  
# (1, "urgent")




