# SPHINX

- Documentation generator untuk Python

Dari
- docstrings
- markdown / reStructuredText
- code annotations

Akan diubah menjadi
- website HTML
- PDF
- ePub

Cocok untuk
- Dokumentasi API
- DOkumentasi library
- Dokumentasi internal project
- User Guides
- Documentation for pip packages

Contoh project besar yang pakai sphinx
- NumPy
- Pandas
- Pydantic
- SQLAchemy
- Django docs

## Sphinx penting karena
- Auto generate docs from code
  ```python
  def add(a: int, b: int) -> int:
    """
    Add two numbers.

    :param a: first number
    :param b: second number
    :return: sum of a and b
    """
    return a + b
  ```
Sphinx bisa otomatis membuat halaman dokumentai API lengkap dari function tersebut
- Mendukung type hints
- Bisa build website docs professional
- Sangat cocok untuk library open-source
- Generate banyak format (HTML, PDF, EPUB)


## Cara install dan setup
### Install
```bash
pip install sphinx
```

### Buat skeleton docs
- Jalankan
  ```bash
  sphinx-quickstart
  ```
- Setelah itu akan ditanya
  - project name
  - author
  - versi
  - apakah pakai autodoc
  - apakah pakai type hints
  - apakah pakai napoleon (Google-style docstring)
- Setelah itu struktur foldernya
  ```
  docs/
    build/
    source/
      conf.py
      index.rst
      modules.rst
  ```

## Format dokumentasi: reStructuredText (RST)
- Sphinx default menggunakan `.rst`
  ```rst
  My Project
  ==========

  Welcome to my documentation!

  .. autofunction:: mymodule.add
  ```
Namun sekarang sphinx juga mendukung markdown via extension myst-parser

## Auto generate API docs (autodoc)
- Tambahkan extension di `conf.py`:
  ```python
  extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
  ]
  ```
- Contoh generate docs
  ```rst
  .. automodule:: myproject.module
    :members:
    :undoc-members:
  ```
- Autogenerate table
  ```bash
  sphinx-apidoc -o docs/source myproject
  ```


## Napoleon Extension (Google-style & NumPy-style-docstring)
Jika ingin docstring seperti ini
```python
def add(a, b):
  """Add 2 numbers.

  Args:
    a (int): First number
    b (int): Second number

  Returns:
    int: Sum
  """
  return a + b
```
Sphinx bisa parse format lewat
```python
extensions = [
  "sphinx.ext.napoleon",
]
```


## Build Documentation
Di dalam folder docs
```bash
make html
```
Browser output ada di
```bash
docs/build/html/index.html
```


## Contoh dokumentasi API sphinx
Docstring
```python
def multiply(a: int, b: int) -> int:
  """
  Multiply two numbers.

  :param int a: first number
  :param int b: second number
  :return: multiplication result
  :rtype: int
  """
  return a * b
```
Hasil HTML:
- Title: multiply
- Parameters section
- Return type
- Description


## Perbandingan dengan docs lain
- Sphinx vs MkDocs vs Docusaurus
| Tool           | Kelebihan                                     | Kekurangan           |
| -------------- | --------------------------------------------- | -------------------- |
| **Sphinx**     | best for Python API, autodoc, rst, pdf output | rst agak sulit       |
| **MkDocs**     | markdown, modern, mudah                       | autodoc butuh plugin |
| **Docusaurus** | bagus untuk website docs                      | tidak Python-native  |

Jika tujuannya project python maka `sphinx` lebih baik, tapi jika website docs pribadi `MkDocs` lebih enak.

