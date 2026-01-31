# CONCURRENCY

## Multiprocessing
- Menjalankan banyak proses OS secara paralel
- CPU-bound tasks - paling cocok
- Python membuat proses baru, bukan thread.
- Pro cons:
  - \+ Bisa benar-benar berjalan paralel pada banyak core CPU
  - \+ Cocok untuk perhitungan berat (machine learning, image processing, encryption)
  - \+ Memory dipisah per proses
  - \- Overhead lebih besar daripada thread
  - \- Tidak cocok untuk I/O

Contoh:
```python
from multiprocessing import Process

def work():
  print("Working in another process")

p = Process(target=work)
p.start()
p.join()
```
Dipakai saat:
- CPU-heavy tasks
- Image processing
- Data science model training
- Video encoding


## Asynchrony (async/await)
- I/O concurrency tanpa membuat banyak thread
- Cocok untuk API server, networking, DB queries
- Async= cooperative multitasking
- Tidak butuh banyak thread, hanya 1 loop event
- Pro cons:
  - \+ Sangat efisien untuk I/O
  - \+ Dipakai FastAPI, aiohttp, websockets
  - \+ Bisa handle ribuan request dengan resource kecil
  - \+ Tidak membuat CPU paralel tapi non-blocking
  - \- Butuh gaya coding berbeda
  - \- Tidak mempercepat CPU-bound jobs

Contoh
```python
import asyncio

async def hello():
  print("Hello")
  await asyncio.sleep(1)
  print("World")

asyncio.run(hello())
```
Dipakai pada saat:
- Web server (FastAPI)
- Network programming (sockets)
- HTTP Requests (httpx)
- Database async engine


## GIL (Global Interpreter Lock)
- Kunci yang membuat hanya 1 thread Python bis eksekusi bytecode pada suatu waktu
- GIL = alasan Python therading tidak bisa paralel pada CPU, kecuali untuk operasi C-level (numpy, I/O)

Intinya
- Threading tidak bisa mempercepat CPU tasks
- Threading tetap bagus untuk I/O tasks
- Multiprocessing adalah solusi untuk CPU-bound concurrency
- Asyncio menghindari blocking I/O tanpa thread

Kenapa Python butuh GIL:
- mempermudah memory management
- aman untuk single-threaded scripting
- sejarah dari CPython implementation


## Threading
- Banyak thread dalam 1 proses
- Terpengaruh GIL - tidak paralel untuk CPU tasks
- Tapi tetap sangat berguna untuk I/O-bound tasks:
  - reading/writing files
  - networking
  - SQL queries
  - HTTP requests

Contoh
```python
import threading

def work():
  print("Working in thread")

t = threading.Thread(target=work)
t.start()
t.join()
```
Dipakai saat:
- I/O concurrency
- Background tasks
- Simple parallelism tanpa async


# PERBANDINGAN
| Model               | Paralel?            | Terpengaruh GIL?                | Best for                   |
| ------------------- | ------------------- | ------------------------------- | -------------------------- |
| **Multiprocessing** | Ya                  | Tidak                           | CPU-bound                  |
| **Threading**       | Tidak (karena GIL)  | Ya                              | I/O-bound                  |
| **Async/await**     | Tidak (cooperative) | Tidak pakai thread              | I/O-bound high concurrency |
| **GIL**             | —                   | Mengunci eksekusi thread Python | Memengaruhi threading      |


# REAL CASE
## FastAPI menggunakan async concurrency
```python
@app.get("/items")
async def read_items():
  data = await fetch_data()
  return data
```
Non-blocking - super cepat untuk banyak request

## CPU-bound (must use multiprocessing)
```python
from multiprocessing import Pool

def compute(n):
  return n * n

with Pool() as p:
  print(p.map(compute, range(10_000)))
```

## I/O-bound using threading
```python
import requests
from threading import Thread

def fetch(url):
  print(requests.get(url).status_code)

urls = ["https://google.com", "https://github.com"]

threads = [Thread(target=fetch, args=(u,)) for u in urls]

for t in threads: t.start()
for t in threads: t.join()
```


## SUMMARY
- Threading → I/O tasks, affected by GIL
- Multiprocessing → CPU tasks, bypass GIL
- Async/await → high performance I/O concurrency
- GIL → alasan thread tidak paralel CPU

