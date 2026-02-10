# INSTALLING GIT LOCALLY

## References
- [Git - Downloads](https://git-scm.com/install/)
- [Install Git](https://github.com/git-guides/install-git)

## Install Git
### Windows
- Download dari: [LINK](https://git-scm.com)
- Install
- Setelah selesai buka `Git Bash`
- Cek
  ```
  git --version
  ```
  Muncul versi dari git

### macOS
- Biasanya sudah ada, cek:
  ```
  git --version
  ```
- Kalau belum ada
  ```
  brew install git
  ```

### Linux
```
sudo apt install git
```

## Initial Setup
Set identitas kamu:
```
git config --global user.name "Nama Kamu"
git config --global user.email "emailkamu@example.com"
```
agar Git mencatat siapa yang commit

