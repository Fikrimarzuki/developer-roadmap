# CODE FORMATTING

## Tujuannya
- Membuat kode Python rapi, konsisten, mudah dibaca dan otomatis diformat tanpa perlu bingung dengan style


## Black
- Paling populer
- "Formatting is not a matter of opinion"
- Dengan black, maka:
  - Memberi style yang konsisten
  - auto-fix indent, spacing, quotes
  - mengubah code menjadi standar PEP8
  - sangat cepat
  - dipakai oleh perusahaan besar & open-source

### Install
```bash
pip install black
```

### Format satu file
```bash
black app.py
```

### Format seluruh folder
```bash
black .
```

### Contoh black
#### Sebelum
```python
def add( a,b ):
  return a+b
```
#### Setelah
```python
def add(a, b):
  return a + b
```

### Alasan disukai
- tanpa konfigurasi
- standar industri
- stabil
- sangat cocok dengan Pyright, Mypy, Ruff, Poetry


## YAPF
- Yet Another Python Formatter
- Formatter by Google
- "Write code as if a human would format it"
- Dengan YAPF:
  - lebih fleksibel dari Black
  - bisa dikustomisasi sesuai style
  - cocok jika ingin kontrol lebih banyak

### Install
```bash
pip install yapf
```

### Format file
```bash
yapf -i app.py
```

### Format folder
```bash
yapf -r -i .
```

### Konfigurasi di .style.yapf
```ini
[style]
based_on_style = pep8
column_limit = 88
```

### Yang menggunakan YAPF
- Internal google
- Tim yang ingin custom formatting


## RUFF
- The new all-in-one Python linter + formatter
- Tool baru yang sangat cepat
- Fungsinya
  - linter
  - import sorter
  - formatter (Black-compatible model)
  - rules seperti flake8, pylint, isort, pycodestyle
  - sangat cepat (10-100x lebih cepat)

### Install
```bash
pip install ruff
```

### Pakai pipx
```bash
pipx install ruff
```

### Format
```bash
ruff format .
```

### Lint code
```bash
ruff check .
```

### Auto-fix
```bash
ruff check . --fix
```

### Konfigurasi (pyproject.toml)
```toml
[tool.ruff]
lline-length = 88
select = ["E", "F", "W"]
```


## Perbandingan
| Tool      | Type               | Strength                            |
| --------- | ------------------ | ----------------------------------- |
| **Black** | Formatter          | Standar industri, tanpa konfigurasi |
| **YAPF**  | Formatter          | Bisa custom style                   |
| **Ruff**  | Linter + formatter | Super cepat, modern, recommended    |


## Contoh konfigurasi pyproject.toml
```toml
[tool.black]
line-length = 88

[tool.ruff]
line-length = 88
select = ["E", "F", "W", "I"]
fix = true

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```


