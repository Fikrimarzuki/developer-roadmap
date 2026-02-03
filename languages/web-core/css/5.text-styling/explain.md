# TEXT STYLING


## 1. Color
atur warna teks
```css
p { color: #0b57d0; }
```
value bisa berupa
- hex: #FF0000 atau #FF000080
- rgb: rgb(255, 0, 0)
- rgba: ada alpha channel untuk transparansi
- hsl: hue, saturation, lightness
- hsla



## 2. Direction
atur arah penulisan, biasanya untuk bahasa RTL (right to left) seperti Arab/ibrani
```css
.rtl { direction: rtl; }
```
catatan: untuk demo agar terlihat, kadang dibantu `unicode-bidi`
```css
.rtl { direction: rtl; unicode-bidi: bidi-override; }
```



## 3. Text Alignment
atur perataan teks
```css
.left   { text-align: left; }
.center { text-align: center; }
.right  { text-align: right; }
.justify{ text-align: justify; }
```



## 4. Text Decoration
atur dekorasi teks
```css
a { text-decoration: none; }
.strike { text-decoration: line-through; }
```
Beberapa properti modern yang sering dipakai
- text-decoration-line
- text-decoration-style
- text-decoration-thickness



## 5. Text Transform
ubah tampilan huruf(kapital, kapital, capslock) tanpa mengurab teks asli
```css
.upper { text-transform: uppercase; }
.lower { text-transform: lowercase; }
.cap   { text-transform: capitalize; }
```



## 6. Text Spacing
atur jarak antar huruf dan kata
```css
.space {
  letter-spacing: 2px;
  word-spacing: 10px;
}
```
beberapa tambahan yang sering dipakai
```css
.indent { text-indent: 28px; }
```



## 7. Line Height
atur jarak antar baris
```css
.tight { line-height: 1.1; }
.normal{ line-height: 1.6; }
.loose { line-height: 2.2; }
```



## 8. Text Shadows
memberi bayangan pada teks
```css
.title {
  text-shadow: 2px 2px 0 rgba(0,0,0,0.25);
}
```
formatnya: `text-shadow: offset-x offset-y blur color;`



## 9. Fonts

### Font Family
menentukan font utama dan cadangan
```css
font-family: Arial, sans-serif;
```
Browser pilih font pertama, kalau tidak ada pakai cadangan.

### Font Style
```css
font-style: italic;
```

### Font Size
```css
font-size: 16px;
```

### Font Weight
```css
font-weight: bold; /* atau 700 */
```

### Font Variant
```css
font-variant: small-caps;
```

### Font Shorthand
Gabungan semua properti font dalam 1 baris
```css
font: italic bold 16px Arial, sans-serif;
```
urutannya
```
font-style -> font-weight -> font-size -> font-family
```

### Google Fonts
Tambahkan di HTML
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
```
lalu di css
```css
font-family: 'Poppins', sans-serif;
```
