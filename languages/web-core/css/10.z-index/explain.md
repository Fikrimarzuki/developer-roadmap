# 


## 1. Z-Index / Stacking Content
mengatur urutan layer ketika elemen bertumpuk.
```css
.box { position: absolute; z-index: 2; }
```
Catatan penting:
- `z-index` hanya bekerja pada elemen yang punya position selain static (relative/absolute/fixed/sticky).

### Stacking Context (kenapa z-index besar kadang kalah)
Elemen hanya "bertarung" dengan elemen lain dalam **stacking context** yang sama.

Contoh yang membuat stacking context baru:
- position + z-index
- opacity < 1
- transform
- filter

Jika parent membentuk stacking context, `z-index` anak yang besar hanya berlaku di dalam context itu.



## 2. CSS Specificity
specificity menentukan rule mana yang menang ketika konflik

Urutan umum:
- Inline style: 1000
- ID selector #id: 100
- Class/attr/pseudo-class .class [attr] :hover: 10
- Element selector div: 1

Jika specificity sama -> rule yang ditulis paling bawah menang.



## 3. Tables
Styling table biasanya butuh:
- border-collapse: collapse;
- `padding` di `th`, `td`
- zebra rows dengan `nth-child`
```css
table { border-collapse: collapse; }
th, td { padding: 10px; border: 1px solid #000; }
tbody tr:nth-child(even) { background: #fafafa; }
```



## 4. Lists
UL / OL
- list-style-type untuk bentuk bullet/angka
- padding-left untuk indent

Custom list (modern UI)
- matikan bullet:
```css
ul { list-style: none; padding-left: 0; }
```
Lalu buat item jadi "card" dengan border/padding.



## 5. Images
Tips responsif:
```css
img { max-width: 100%; height: auto; }
```
Untuk crop rapih:
```css
img { width: 200px; height: 150px; object-fit: cover; }
```



## 6. Filters
memberi efek visual:
```css
img { filter: grayscale(100%); }
img { filter: blur(2px); }
img { filter: contrast(140%); }
img { filter: brightness(110%) contrast(120%) saturate(140%); }
```




