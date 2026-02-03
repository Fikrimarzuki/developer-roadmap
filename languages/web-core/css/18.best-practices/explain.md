# BEST PRACTICE

bukan cuma bikin UI bagus, tapi cepat, bisa diakses semua orang dan maintainable


## 1. Performance
### Minimalkan CSS
- hapus css tidak terpakai
- hindari selector terlalu kompleks
kurang baik:
```css
div ul li a span { }
```
baik:
```css
.nav-link { }
```

### Gunakan Class
- class lebih reusable dan ringan untuk styling

### Hindari `!important`
sebisa mungkin hindari `!important` agar lebih mudah di-maintain

### Gunakan transform dan opacity untuk animasi
lebih ringan dibanding `top/left`
```css
transform: translateX(20px);
```

### Lazy load gambar
```html
<img src="image.jpg" loading="lazy">
```

### Gunakan shorthand
```css
margin: 10px 20px;
```
jika menggunakan semua value gunakan shorthand, lebih efisien dari 4 baris



## 2. ACCESSIBILITY
website harus bisa digunakan oleh:
- keyboard-only users
- screen readers

### Kontras Warna
gunakan kontras cukup
```
WCAG minimal 4.5:1
```

### Fokus Keyboard
jangan hilangkan outline
```css
outline: none;
```
bisa pakai
```css
:focus {
  outline: 2px solid blue;
}
```

### Gunakan `:focus-visible`
```css
:focus-visible {
  outline: 3px solid red;
}
```

### Gunakan unit relatif
```css
font-size: 1rem;
```
biar bisa di zoom.

### Jangan hanya warna sebagai indikator
❌ hanya merah untuk error
✅ tambah icon / teks

### Gunakan HTML semantik
```html
<button>Submit</button>
```
bukan:
```html
<div>Submit</div>
```




