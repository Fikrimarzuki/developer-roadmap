# GITIGNORE & VIEWIN COMMIT HISTORY


## .gitignore
file ini akan memberi tahu Git bahwa **File/folder ini jangan ikut disimpan ke repository**

file ini dibutuhkan karena tidak semua file harus masuk ke Git.

Beberapa file:
- terlalu besar
- otomatis dibuat sistem (contoh: node_modules, _pycache__)
- berisi rahasia (API key, password) - contoh: API Key, Third Party Key
- tidak penting untuk project - contoh: Thumbs.db

Kalau tidak di ignore maka
- repo akan berat
- file rahasia seperti Secret atau Key akan bocor
- banyak file sampah

### Contoh isi `.gitignore`
```
# Folder dependencies
node_modules/

# File environment
.env

# Log files
*.log

# Build folder
dist/

# OS files
.DS_Store
Thumbs.db
```

### Cara kerjanya adalah
- git akan mengabaikan file yang belum pernah di track
- jika sudah pernah di commit, `.gitignore` tidak langsung menghapus file tersebut

untuk menghapus file/folder dari tracking
```
git rm --cached nama_file
```

### Letak file 
ada di root project sejajar dengan folder `.git`



## Viewing Commit History
setiap commit berarti satu snapshot versi project.

### cara lihat log
```
git log
```
Output berisi:
- Commit ID (hash)
- Author
- Tanggal
- Pesan commit


### versi ringkas log
```
git log --oneline
```
lebih simple
```
a34f21b Tambah fitur login
9c31aa1 Fix bug navbar
1a2bc3d Init project
```
Beberapa opsi lain `--graph`, `--patch`, `--stat`


### Melihat perubahan detail
menampilkan perubahan pada commit terakhir
```
git show
```

### Melihat perbedaan file
Menampilkan perubahan yang belum di stage
```
git diff
```


