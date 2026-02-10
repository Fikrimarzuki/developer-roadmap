# REPOSITORY INITIALIZATION

agar project bisa dikenali Git. Folder di lokal akan menjadi Git Repository setelah ini.

## git init
perintah untuk mengangktifkan Git di sebuah folder.
- buat folder kalau belum ada. Bisa dengan buat langsung atau menggunakan terminal
  ```
  mkdir new_project
  ```
- masuk ke folder
  ```
  cd new_project
  ```
- setelah masuk, ubah folder menjadi folder git
  ```
  git init
  ```
- sekarang di dalam folder akan ada folder tersembunyi
  ```
  .git/
  ```
Folder `.git` ini adalah otak Git. Jika dihapus bisa kehilangan history dari projectnya.

Isi folder `.git` adalah:
- History commit
- Branch info
- Config repo
- Tracking file changes

Jadi dengan melakukan `git init` seperti mulai sekarang perubahan di folder itu akan direkam.



## git config
mengatur identitas dan pengaturan Git.

karena setiap commit akan tercatat seperti ini:
```
Author: Nama Author `<author@email.com>`.
```
Maka Git perlu tahu:
- siapa authornya
- email author
- setting lain

### Cara setting nama dan email
```
git config --global user.name "Nama Author"
git config --global user.email "author@email.com"
```
Tanpa config, commit bisa dianggap anonymous.

### Cara melihat konfig
```
git config --list
```


## Local vs Global Config
konfig global - semua project di device dan menjadi default identitas
konfig lokal - hanya 1 repo di folder `.git` dan dipakai di project khusus

### Global Config
```
git config --global user.name "Nama Author"
```
artinya: semua project Git di device akan pakai nama ini

### Local Config
Kalau ada di dalam repo:
```
git config user.name "Nama Author Office"
```
artinya: hanya repo ini yang pakai nama ini

Konfig lokal ini dipakai kalau:
- Akun kerja beda email
- Open source pakai email lain
- Project klien berbeda identitas


## Urutan Prioritas
kalau ada konflik maka urutan prioritasnya
```
Local Config > Global Config > System Config
```


