# POSITION


## 1. Static
```css
position: static;
```
- Default semua elemen
- Tidak bisa pakai top, left, dll



## 2. Relative
```css
position: relative;
top: 10px;
left: 20px;
```
- Bergerak relatif dari posisi aslinya
- Masih mengambil ruang awalnya



## 3. Absolute
```css
position: absolute;
top: 0;
left: 0;
```
- Keluar dari flow normal
- Diposisikan relatif ke parent terdekat yang punya `position` selain static



## 4. Fixed
```css
position: fixed;
bottom: 10px;
right: 10px;
```
- Menempel di layar (viewport)
- Tidak ikut scroll



## 5. Sticky
```css
position: sticky;
top: 0;
```
- Awalnya seperti relative
- Saat scroll melewati batas, jadi fixed


