# TESTING

Testing memastikan
- code benar
- tidak rusak ketika di refactor
- bisa dimaintain developer lain
- mengurangi bug production
- meningkatkan confidence saat deploy


## Unittest /pyUnit
- testing built-in Python
- mirip JUnit (Java) atau NUnit (C#)

### Controh struktur data
```python
import unittest

class TestMath(unittest.TestCase):
  def test_add(self):
    self.assertEqual(1 + 1, 2)

  def test_subtract(self):
    self.assertEqual(5 - 3, 2)

if __name__ == "__main__":
  unittest.main()
```
### Kelebihan
- sudah ada di Python (tidak perlu install)
- standar sejak dulu

### Kekurangan
- syntax agak verbosa
- tidak se-modern pytest


## Pytest
- testing framework paling banyak dipakai
  - simple
  - powerful
  - banyak plugin
  - auto discovery fixtures
  - mendukung fixtures
  - cocok untuk FastAPI, Django, dsb
  - bisa test async function

### Install
```pythbashon
pip install pytest
```

### Contoh test dengan pytest
File: `test_math.py`
```python
def test_add():
  assert 1 + 1 == 2

def test_list_length():
  assert len([1, 2, 3]) == 3
```
Jalankan:
```bash
pytest
```

Lebih simple daripada unittest:
- tidak butuh class
- tidak perlu inheritance
- assertion pakai assert biasa

### Contoh Fixture
```python
import pytest

@pytest.fixture
def sample_data():
  return [1, 2, 3]

def test_sum(sample_data):
  assert sum(sample_data) == 6
```

### Contoh async test
```python
import pytest
import asyncio

@pytest.mark.asyncio
async def test_async():
  await asyncio.sleep(1)
  assert True
```


## Doctest
Membuat tes langsung dari contoh di docstring

### Contoh
```python
def add(a, b):
  """
  Add two numbers.

  >>> add(1, 2)
  3
  >>> add(5, 5)
  10
  """
  return a + b
```

### Jalankan
```bash
python -m doctest app.py
```

- Kalau output tidak sama maka tes gagal.
- Cocok untuk:
  - library kecil
  - util function
  - dokumentasi API
  - contoh kecil
- Tidak cocok untuk testing besar


## Tox
- multi environment testing
- digunakan untuk menjalankan tes di berbagai environment
  - berbagai versi python
  - berbagai dependency
  - linting + formatting + test automation
  - CI/CD integration
- Cocok untuk
  - library open source
  - project besar yang harus support Python 3.9 - 3.12

### Install
```bash
pip install tox
```

### Contoh file tox.ini
```ini
[tox]
envlist = py39, py310, py311

[testenv]
deps = pytest
commands = pytest
```

### Jalankan
```bash
tox
```

Tox akan:
- membuat environment Python 3.9
- membuat environment Python 3.10
- membuat environment Python 3.11
- menjalankan pytest pada semuanya

Sangat power full untuk memastikan compatibility


## Perbandingan Tools
| Tool     | Kategori                          | Kapan dipakai             |
| -------- | --------------------------------- | ------------------------- |
| unittest | Built-in test                     | project kecil atau legacy |
| pytest   | Modern testing                    | semua project modern      |
| doctest  | Doc-driven test                   | contoh dalam docstring    |
| tox      | multi-version environment testing | open-source / CI/CD       |


`Pytest` paling direkomendasikan
- syntax sangat clean
- fixture system powerful
- bisa test async function
- integrasi mudah dengan FastAPI
- kompatibel dengan unittest
- otomatis mencari file test_*.py
- mendukung mocking
- memiliki banyak plugin:
- pytest-cov → coverage
- pytest-mock → mocking
- pytest-asyncio → async testing

Ini mirip Jest untuk JavaScript — modern, powerful, dan masa depan Python testing.


## Contoh testing FastAPI
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}
```
Jalankan
```
pytest
```


## Best Practice Testing
- semua file test diawali `test_`
- gunakan fixtures untuk reusable setup
- hindari test yang bergantung pada network external
- gunakan mocking untuk API/DB
- masukkan testing ke CI/CD (GitHub Actions)
- gunakan coverage analysis:
```bash
pytest --cov=yourpackage
```
