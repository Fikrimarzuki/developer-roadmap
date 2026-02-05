# FILE HANDLING

## Membuka file
Format umum
```python
f = open("file.txt", "r")
```
Tetapi cara terbaik menggunakan `context manager`
```python
with open("file.txt", "r") as f:
  data = f.read()
```
Karena:
- lebih aman dari error
- file otomatis ditutup
- lebih clean

## Mode open file
| Mode   | Arti                               |
| ------ | ---------------------------------- |
| `"r"`  | read                               |
| `"w"`  | write (overwrite)                  |
| `"a"`  | append                             |
| `"x"`  | create new (error kalau sudah ada) |
| `"b"`  | binary mode                        |
| `"t"`  | text mode (default)                |
| `"r+"` | read + write                       |

Contoh
```python
with open("file.bin", "rb") as f:
  content = f.read()

```


## Read file
Baca seluruh isi file
```python
with open("data.txt", "r") as f:
  content = f.read()
```

Baca per baris
```python
with open("data.txt") as f:
  for line in f:
    print(line.strip())
```

Baca seluruh baris sebagai list
```python
with open("data.txt") as f:
  lines = f.readlines()
```


## Write File
Overwrite file
```python
with open("output.txt", "w") as f:
  f.write("Hello world!")
```
Append
```python
with open("output.txt", "a") as f:
  f.write("\nNew line appended.")
```


## Read and Write file besar (streaming)
- Jika file sangat besar (1GB+), jangan pakai read()
- Gunakan streaming
  ```python
  with open("big.log") as f:
    for line in f:
      process(line)
  ```
Lebih memory efficient karena:
- tidak load seluruh file
- baca baris per baris


## JSON File Handling
### Baca JSON
```python
import json

with open("data.json") as f:
  data = json.load(f)

print(data)
```

### Tulis JSON
```python
with open("data.json", "w") as f:
  json.dump(data, f, indent=4)
```


## CSV File Handling
### Read CSV
```python
import csv

with open("data.csv") as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)
```

### With header
```python
with open("data.csv") as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row["name"], row["age"])
```

### Write CSV
```python
with open("out.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerow(["name", "age"])
  writer.writerow(["Pythonia", 25])
```


## Binary File (Images, Videos, PDF)
### Read Binary
```python
with open("photo.jpg", "rb") as f:
  content = f.read()
```

### Write binary
```python
with open("copy.jpg", "wb") as f:
  f.write(content)
```


## Error handling pada File
```python
try:
  with open("missing.txt") as f:
    data = f.read()
except FileNotFoundError:
  print("File tidak ditemukan.")
```
Exception umum
- FileNotFoundError
- PermissionError
- IsADirectoryError
- IOError


## Best Practice File Handling
- Selalu gunakan `with open(...)`
- Pakai encoding `utf-8`:
  ```python
  with open("file.txt", "r", encoding="utf-8"):
  ```
- Jangan pakai `.read()` untuk file besar
- Gunakan CSV/JSON module
- Gunakan pathlib untuk path modern
  ```python
  from pathlib import Path

  p = Path("data.txt")
  print(p.read_text())
  ```


## Pathlib (modern file handling)
### Pathlib lebih pythonic daripada string path
```python
from pathlib import Path

p = Path("folder/data.txt")
print(p.exists())
print(p.is_file())
```

### Read file
```python
text = Path("test.txt").read_text()
```

### Write File
```python
Path("test.txt").write_text("hello dunia")
```



