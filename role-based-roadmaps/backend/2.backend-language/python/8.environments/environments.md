# ENVIRONMENT

- Digunakan untuk:
  - memisahkan dependency antar project
  - memastikan versi Python & package konsisten
  - menghindari conflict antar library
  - membuat project lebih mudah di-deploy

## Virtualenv
- Environment dasar untuk python
- Membuat environment terpisah untuk setiap project
- Digunakan oleh pip, poetry, uv, pdm (di belakang layar)

### Cara membuat virtualenv
```bash
python -m venv .venv
```
Atau
```bash
virtualenv venv
```

### Aktifkan environment
- Windows
  ```bash
  .\venv\Scripts\activate
  ```
- Mac/Linux
  ```bash
  source venv/bin/activate
  ```
- Nonatifkan
  ```bash
  deactivate
  ```

Environment terpisah ini yang memastikan:
- Project A pakai FastAPI 0.110
- Project B pakai FastAPI 0.95

Folder `.venv` biasanya tidak ikut commit ke Git


## Pipenv
- pip + virtualenv + lockfile
- pipenv dibuat untuk menjadi npm/yarn versi python, sebelum poetry muncul

### Fitur
- otomatis membuat virtualenv
- otomatis membuat Pipfile & Pipfile.lock
- dependency management lebih rapi daripada pip biasa

### Install pipenv
```bash
pip install pipenv
```

### Buat environment + install package
```bash
pipenv install requests
```
Akan menghasilkan
```csharp
Pipfile
Pipfile.lock
```

### Masuk ke shell environment
```bash
pipenv shell
```

### Install dev dependencies
```bash
pipenv install pytest --dev
```

Kelebihan:
- lebih simple daripada pip + venv
- ada lockfile → dependency versi terkunci
- digunakan oleh banyak project lama

Kekurangan
- Outdated dibanding Poetry / PDM
- Lebih lambat
- Tidak sepopuler dulu


## Pyenv
- Version manager untuk Python
- Mirip `nvm` kalau di Node.js atau `asdf` untuk multi version tools
- digunakan untuk install & switch versi python pada satu komputer

### Install versi python tertentu
```bash
pyenv install 3.12.2
pyenv install 3.10.14
```

### Set versi global
```bash
pyenv global 3.12.2
```

### Set versi lokal untuk folder project
```bash
pyenv local 3.10.14
```
Ini akan membuat `.python-version` file.

### Penting karena
- Beda project sering butuh versi Python berbeda
- Kadang library hanya support versi tertentu
- Deployment lebih mudah jika versi konsisten
- Berguna untuk testing multi-version

pyenv tidak mengelola package - hanya mengelola versi python

untuk dependency isolation tetap pakai:
- virtualenv
- Pipenv
- Poetry
- PDM
- uv venv


## Kombinasi
| Tool           | Fungsi                                          |
| -------------- | ----------------------------------------------- |
| **pyenv**      | mengatur versi Python                           |
| **virtualenv** | membuat environment terpisah                    |
| **Pipenv**     | manage dependency + membuat virtualenv otomatis |

### Pakai pip
```
pyenv → pilih Python version  
virtualenv → buat environment  
pip → install dependencies
```

### Pakai pipenv
```
pyenv → pilih Python version  
pipenv → env + dependency manager
```

### Pakai poetry
```
pyenv → pilih Python version  
poetry → env + dependency + build system
```


## Skenario Real Project
### Project 1 - Backend FastAPI
- Install Python 3.12 via pyenv
- poetry init → automatic virtualenv
- poetry add fastapi uvicorn sqlalchemy pydantic

### Project 2 - Data Science
- Python 3.10
- pipenv or conda environment
- numpy, pandas, matplotlib

### Project 3 - Old project
- Python 3.8
- pip + virtualenv


## Visual Summary Diagram
```
    +-----------+
    |   pyenv   |   -> manage Python versions (3.8, 3.9, 3.10...)
    +-----------+
            |
+----------------------+
|   virtualenv/env    | -> isolated package environment
+----------------------+
            |
+----------------------+
| pip / pipenv/poetry | -> manage and install dependencies
+----------------------+
```








