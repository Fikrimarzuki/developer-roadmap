# CSS VARIABLES

- disebut juga **custom properties**
- digunakan untuk menyimpan nilai yang bisa dipakai ulang
```css
--main-color: blue;
```
cara menggunakan variabelnya
```css
color: var(--main-color);
```
- gunakan `:root` untuk global variabel

penting karena
- theming (dark/light)
- konsistensi warna
- mudah maintenance
- mirip variabel di programming



## Scope
variabel mengikuti scope CSS
```css
.box {
  --color: red;
}
```
hanya berlaku di dalam `.box`


## Fallback
```css
color: var(--main-color, black);
```
jika variabel tidak ada maka pakai nilai kedua


















