# BRANCHING BASICS

jalur kerja terpisah dalam satu project jadi bisa buat fitur baru tanpa ganggu kode utama

seperti pohon:
```
main ────●────●────●
           \
            ●──● (feature-login)
```


## Creating Branch
bikin cabang baru dari branch sekarang
```
git branch nama-branch
```
atau langsung buat dan pindah branch:
```
git checkout -b nama-branch
```

branch baru ini akan punya salinan dari titik terakhir commit.

alasan dipakai adalah
- bikin fitur baru
- eksperimen
- fix bug


## Renaming Branch
ganti nama branch
```
git branch -m nama-baru
```
contoh:
```
git branch -m feature-auth
```
biasanya digunakan kalau salah nama atau ingin nama yang lebih jelas


## Deleting Branch
hapus branch yang sudah tidak dipakai
```
git branch -d nama-branch
```
kalau Git menolak (belum di merge):
```
git branch -D feature-login
```


## Checkout Branch
pindah ke branch lain
```
git checkout nama-branch-lain
```
saat folder, isi folder akan ikut berubah sesuai branch.


## Merging Basics
menggabungkan perubahan dari branch lain

misal:
- buat fitur di branch `feature-login`
- sudah selesai
- lalu ingin dimasukan ke branch `main`

maka langkahnya
```
git checkout main
git merge feature-login
```
git akan menyatukan perubahan.


## Merge Conflict
terjadi ketika dua branch mengubah baris yang sama, maka git akan minta untuk memilih perubahan yang benar.











