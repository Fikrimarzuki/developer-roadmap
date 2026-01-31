# PACKAGE MANAGER

## PIP
- Python Package Installer
- Package manager default python
- Kalau di bahasa lain
| Bahasa     | Package Manager   |
| ---------- | ----------------- |
| JavaScript | npm / pnpm / yarn |
| Python     | pip               |
| PHP        | composer          |
| Java       | maven / gradle    |
| Go         | go modules        |
pip digunakan untuk:
- install package
- uninstall package
- freeze dependency

### Command di pip
#### Install Package
```bash
pip install requests
```

#### Cek Package
```bash
pip list
```

#### Uninstall package
```bash
pip uninstall requests
```

#### Freeze dependencies (buat requirements.txt)
```bash
pip freeze > requirements.txt
```

#### Install dari requirements.txt
```bash
pip install -r requirements.txt
```


## CONDA
- Environment + package manager

### Biasa Digunakan untuk
- Data science
- Machine learning
- Managemment library yang butuh C/C++ binary
- Multiple python version

### Contoh library yang berat untuk pip
- numpy
- scipy
- tensorflow
- pytorch
<br/>

### Command Conda
#### Buat environment
```bash
conda create -n myenv python=3.12
```

#### Aktifkan
```bash
conda activate myenv
```

#### Install package
```bash
conda install numpy
```


## UV
- package manager modern berbasis Rust
- pip -> lama
- uv -> sangat cepat (20-100x lebih cepat)

<br/>
Fitur uv
- install packet super cepat
- environment virtual manager
- kompatibel dengan pip & PyPI
- mendukung pyproject.toml
- mirip pnpm / bun di ekosistem JS

### Command UV
#### Install uv
```bash
pip install uv
```

#### Install package
```bash
uv pip install fastapi
```

#### Run environment
```bash
uv venv
source .venv/bin/activate
```


## Poetry
- Modern python dependency & env manager
- Poetry banyak dipakai di project besar
- Sama seperti npm + package.json, Poetry memakai
```bash
pyproject.toml
```

### Poetry menyelesaikan masalah pip
- dependency conflict
- virtual environment
- version lock
- build & publish package

### Command
#### Install poetry
```bash
pip install poetry
```

#### Buat project baru
```bash
poetry new myproject
```

#### Install package
```bash
poetry add fastapi
```

#### Jalankan env
```bash
poetry shell
```

### File penting
- pyproject.toml — seperti package.json


### Poetry digunakan untuk
- Backend web apps
- ML pipeline
- Library development
- Production-level packaging


## PDM
- Python Development Master
- Mirip poetry tapi lebih ringan

Pdm
- Menggunakan pyproject.toml
- Dependency resolver cepat
- Mirip npm (tanpa virtualenv manual)
- Mendukung PEP modern
- Banyak dipakai python developer yang suka style JS/npm

### Command
#### Install
```bash
pip install pdm
```

#### Inisiasi Project
```bash
pdm init
```

#### Install package
```bash
pdm add fastapi
```

Running environment otomatis di .venv


## Perbandingan Singkat
| Tool       | Fungsi            | Kelebihan               | Kekurangan                   |
| ---------- | ----------------- | ----------------------- | ---------------------------- |
| **pip**    | install package   | simple, default         | dependency kadang bermasalah |
| **PyPI**   | registry library  | semua library ada       | bukan tool                   |
| **conda**  | env + package     | best untuk data science | berat                        |
| **uv**     | pip-superfast     | sangat cepat            | masih baru                   |
| **Poetry** | env + dependency  | best for production     | agak rumit untuk pemula      |
| **PDM**    | modern dependency | mirip npm, cepat        | belum sepopuler poetry       |


## Package manager dan beberapa contoh biasa dipakai
### Backend Web/API (FastAPI, Flask)
- Poetry atau uv
(alternatif pip + virtualenv)

### Machine Learning / Data Science
- Conda

### Library development (publish ke PyPI)
- Poetry

### Pemula
- pip + virtualenv

### Developer modern yang suka npm style
- PDM





