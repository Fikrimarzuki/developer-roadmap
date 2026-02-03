# LAYOUTS


## 1. Flow Layout
- Block akan mengambil 1 row, sehingga turun ke bawah (vertikal)
- Inline tidak mengambil 1 row, sehingga sejajar (horizontal)
```html
<div>Block 1</div>
<div>Block 2</div>
<span>Inline 1</span>
<span>Inline 2</span>
```
hasilnya
```
===============================
| Block 1                      |
| Block 2                      |
| Inline 1Inline 2             | 
===============================
```



## 2. Float Layout
```css
float: left;
```
dulu dipakai untuk layout kolom. Sekarang sudah jarang dipakai untuk layout utama.



## 3. Multicolumn Layout
membagi teks ke beberapa kolom
```css
column-count: 3;
```



## 4. Flexbox (1D Layout)
```css
display: flex;
```
cocok untuk navbar, card row, alignment



## 5. Grid (2D Layout)
```css
display: grid;
```
cocok untuk dashboard, gallery, layout kompleks





