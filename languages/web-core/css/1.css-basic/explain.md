# CSS Basics
CSS (Cascading Style Sheets) digunakan untuk mengatur tampilan halaman HTML seperti warna, ukuran, layout, dan lain-lain.


## 1. Inline CSS
CSS ditulis langsung di dalam elemen HTML menggunakan atribut style.
```html
<p style="color: red;">This is red text</p>
```
Karakteristik:
- Berlaku hanya untuk 1 elemen
- Prioritas paling tinggi
- Tidak cocok untuk project besar
- Sulit di-maintain



## 2. Internal CSS
CSS ditulis di dalam tag `<style>` di bagian `<head>`.
```html
<style>
  p {
    color: green;
  }
</style>
```
Karakteristik:
- Berlaku untuk 1 halaman HTML
- Cocok untuk demo kecil
- Tidak reusable antar halaman



## 3. External CSS
CSS ditulis di file terpisah dan dihubungkan dengan HTML.
```html
<link rel="stylesheet" href="style.css">
```
Isi file style.css.
```css
p {
  color: blue;
}
```
Karakteristik:
- Digunakan di project nyata
- Bisa dipakai banyak halaman
- Lebih rapi dan mudah di-maintain
- Best practice untuk development



## 4. Cascading Order (Prioritas CSS)
CSS punya sistem prioritas ketika ada aturan yang konflik. Urutan prioritas dari yang paling kuat:
```
Inline CSS > Internal CSS > External CSS > Browser Default
```
Contoh konflik:
```
/* Inline */
<p style="color: red;">Text</p>
```
```
/* Internal */
p { color: green; }
```
```
/* External */
p { color: blue; }
```
Hasil akhir: **Merah** karena Inline menang.

---

### Kenapa cascading (bertingkat/mengalir)?
karena style menerapkan aturan gaya berdasarkan hierarki prioritas, di mana aturan yang lebih spesifik atau ditulis terakhir akan menimpa aturan sebelumnya. Aturannya dipilih berdasarkan:
1. Origin (inline, internal, external)
2. Specificity
3. Order penulisan
4. !important

