# SYNTAX BASIC


## 1. Rules
```css
selector {
  property: value;
}
```
Penjelasan:
- Selector - menentukan elemen yang ingin diberi style
- Property - style yang mau diubah (color, font-size, dll)
- Value - nilai dari property

Contoh:
```css
p {
  color: red;
}
```
Semua elemen `<p>` akan mempunyai teks warna merah.



## 2. Comments
digunakan untuk memberi catatan dan tidak dijalankan.
```css
/* This is a CSS comment */
```
Bisa dipakai untuk:
- Penjelasan
- Debugging
- Menonaktifkan sementara kode



## 3. Simple Selectors
Selector adalah cara kita memilih `elemen HTML`.
### Element Selector
Memilih berdasarkan nama tag.
```css
p {
  color: green;
}
```
Semua elemen `<p>` akan mempunyai teks warna hijau 

### Class Selector
Memilih elemen dengan atribut `class`. Menggunakan simbol titik (`.`) sebelum nama class.
```css
.box {
  border: 1px solid black;
}
```
```html
<div class="box"></div>
```
Semua elemen yang mempunyai class **box** akan mempunyai border.

### ID Selector
Memilih elemen dengan atribut `id`. Menggunakan simbol (`#`) sebelum nama id. Id harus unik, tidak boleh ada lebih dari 1 dalam 1 halaman.
```css
#header {
  background-color: yellow;
}
```
```html
<div id="header"></div>
```

### Universal Selector
Memilih semua elemen.
```css
* {
  font-family: Arial;
}
```

### Grouping Selector
Menggabungkan beberapa selector.
```css
h1, p {
  color: green;
}
```
Semua elemen `h1` dan `p` akan mempunyai teks berwarna hijau.




