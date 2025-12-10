# STATIC TYPING

- Python itu dynamic typed languange
- Sejak 3.5+, python mendukung optional static typing melalui type hints
- Static typing membantu:
  - mencegah bug lebih awal
  - membuat IDE auto-complete lebih pintar
  - memudahkan refactoring
  - dokumentasi code otomatis
  - membuat API besar lebih stabil

## Typing (built-in module)
- modul inti untuk membuat type annotation
Contoh
```python
def greet(name: str) -> str:
  return "Hello " + name
```
Type hint tidak mengubah cara kerja Python, tapi digunakan:
- editor (VSCode, PyCharm)
- MyPy, Pyright
- linter
- tools lainnya

### Tipe yang sering dipakai
#### List, Dict, Tuple, Set
```python
from typing import List, Dict, Tuple, Set

numbers: List[int] = [1, 2, 3]
user: Dict[str, int] = {"age": 25}
coords: Tuple[int, int] = (10, 20)
names: Set[str] = {"alex", "budi"}
```

#### Optional
```python
from typing import Optional

def find_user(id: int) -> Optional[str]:
  ...
```

#### Union
```python
from typing import Union

def load(data: Union[str, bytes]):
  ...
```
Python 3.10+ bisa
```python
def load(data: str | bytes):
  ...
```

#### Callable (fungsi sebagai parameter)
```python
from typing import Callable

def run(func: Callable[[int], int], value: int):
  return func(value)
```

#### TypedDict (struktur mirip interface)
```python
from typing import TypedDict

class User(TypedDict):
  id: int
  name: str
```

#### Generics
```python
from typing import TypeVar

T = TypeVar("T")

def first(lst: list[T]) -> T:
  return lst[0]
```


## Mypy
- Static type checker
- mypy adalah checker yang membaca file python dan memastikan semua type hint valid
- install
  ```
  pip install mypy
  ```
  Jalankan
  ```bash
  mypy app.py
  ```
  Contoh error
  ```python
  def add(x: int, y: int) -> int:
    return x + y

  add("hello", 5)
  ```
  Output
  ```go
  error: Argument 1 to "add" has incompatible type "str"; expected "int"
  ```

Kenapa Mypy penting:
- mencegah bug runtime
- memastikan API tetap stabil
- banyak dipakai di perusahaan besar


## Pyright
- Fast Type Checker
- Pyright adalah alternatif mypy
  - ditulis dalam TypeScript
  - super cepat
  - powerfull saat dipakai di VSCode
  - dipakai oleh Pylance (VSCode Python language server)

### Install
```bash
npm install -g pyright
```
Jalankan
```bash
pyright
```
Sering kali lebih cepat & lebih strict daripada mypy


## Pyre
- Meta/facebook type checker
- Kelebihan:
  - sangat cepat (ditulis dalam OCaml)
  - punya fitur profiling type coverage
  - dipakai di internal Meta (Instagram, dll)

Untuk developer biasa - pyright atau mypy lebih umum


## Pydantic
- Data validation + type enforcement
- pydantic:
  - menggunakan static typing untuk memvalidasi data runtime
  - dipakai oleh FastAPI
  - sangat digunakan dalam backend modern
  - jauh lebih strict daripada dataclass

### Contoh
```python
from pydantic import BaseModel

class User(BaseModel):
  id: int
  name: str
    age: int = 18
```
### Input
```python
u = User(id="1", name="Fikri")
print(u)
```
Pydantic otomatis konversi "1" menjadi 1.

### Jika invalid
```python
User(id="abc", name="Fikri")
```
Error:
```python
ValidationError: id must be an int
```

Pydantic sangat powerful:
- type validation
- nested models
- JSON serialization
- environment settings
- schema generation
- async validation


## Summary
| Tool         | Fungsi                     | Kapan dipakai                 |
| ------------ | -------------------------- | ----------------------------- |
| **typing**   | type hints built-in Python | selalu dipakai                |
| **mypy**     | type checker               | untuk project besar, CI/CD    |
| **pyright**  | type checker cepat         | untuk VSCode user             |
| **pyre**     | enterprise type checker    | untuk team besar (Meta style) |
| **pydantic** | runtime validation         | API, backend, data models     |


## Rekomendasi
- Untuk backend (FastAPI, microservices)
- wajib
  - typing
  - pydantic
  - pyright (lebih modern) - atau mypy
- tidak wajib
  - pyre (lebih niche)




