# PSEUDO CLASSES

Pseudo-class diawali dengan `:` dan dipakai untuk:
- State user (hover, focus)
- Posisi elemen (first-child)
- Kondisi form (checked, disabled)

Contoh:
```css
a:hover {
  color: red;
}
```

## 1. User Action
- `:hover` - saat mouse di atas elemen
- `:active` - saat elemen diklik
- `:focus` - saat elemen aktif (input)


## 2. Link States
- `:link` - link belum dikunjungi
- `:visited` - link sudah dikunjungi


## 3. Form States
- `:checked` - checkbox / radio aktif
- `:disabled` - input tidak aktif
- `:enabled` - input aktif


## 4. Structural
- `:first-child` - anak pertama
- `:last-child` - anak terakhir
- `:nth-child(n)` - anak ke-n
- `:nth-child(even)` - genap
- `:nth-child(odd)`- ganjil


## 5. Negation
- `:not`
contoh
```css
p:not(.special) { }
```
memilih elemen yang tidak punya class tersebut




