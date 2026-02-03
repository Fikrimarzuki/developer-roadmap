# RESPONSIVENESS

- membuat website adaptif di semua ukuran layar.
- website berubah layout/ukuran berdasarkan:
  - lebar layar
  - ukuran container
  - ukuran font


## 1. Media Queries
digunakan untuk ubah style berdasarkan **viewport**
```css
@media (max-width: 600px) {
  body {
    background: lightyellow;
  }
}
```
jika layar <= 600px maka style aktif



## 2. Container Queries
lebih modern dari media query, berdasarkan **ukuran parent**, bukan layar.
```css
.container {
  container-type: inline-size;
}

@container (max-width: 300px) {
  .card {
    background: pink;
  }
}
```
dipakai kalau komponen dipakai di banyak layout



## 3. Responsive Typography
unit relatif
- rem - berdasarkan root font
- em - berdasarkan parent
- vw - berdasarkan lebar layar

teknik modern:
```css
font-size: clamp(16px, 4vw, 32px);
```
artinya
- minimum 16px
- maksimum 32px
- fleksibel di tengah


###
biasanya:
- rem & clamp untuk font
- media query untuk breakpoint besar
- container query untuk komponen reusable


