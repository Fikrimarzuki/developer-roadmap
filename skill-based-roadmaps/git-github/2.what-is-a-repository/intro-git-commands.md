# INTRO TO GIT COMMANDS

Git bekerja dalam 3 area utama
```
Working Directory -> Staging Area -> Repository (Commit)
```

## Working Directory
ini biasanya setelah inisiasi git di folder atau kloning repo ke lokal device.

Di state ini
- membuat file
- edit file
- hapus file

semua perubahan di state ini belum direkam Git.

untuk mengecek perubahan yang terjadi
```
git status
```

## Staging Area
ini adalah tempat seleksi perubahan sebelum disimpan permanen.

kalau dianalogikan seperti memilah barang yang akan dimasukan ke kardus sebelum paket dikirim. kalau ini memilih file mana yang akan di commit.

cara menambahkan file
```
git add namaFile
```
misal
```
git add index.html
```

jika ingin semua file maka
```
git add .
```


## Commit (Repository)
menyimpan snapshot project ke dalam history Git.

ini seperti mensolatip kardus dan menuliskan catatannya. jadi seperti tombol save permanen ditambah catatan perubahan.

cara commit perubahan beserta tambahan catatannya
```
git commit -m "catatan perubahan"
```
Hasilnya:
- Git menyimpan versi file
- Memberi ID unik (hash)
- Mencatat author dan waktu


## Alur Kerja
jadi biasanya alur kerja yang terjadi seperti ini
```
# 1. Cek perubahan
git status

# 2. Masukkan ke staging
git add .

# 3. Simpan ke history
git commit -m "Update fitur login"
```


## Status File di Git
- Untracked - file baru, belum dikenal Git
- Modified - File diubah
- Staged - siap di commit
- Commited - sudah commit
