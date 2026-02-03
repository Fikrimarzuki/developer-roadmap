# BOX MODEL & CSS UNITS


## 1. Box Model
tiap elemen HTML adalah kotak.

struktur box model:
- Margin
  - Border
  - Padding
  - Content

### Content
Isi elemen (teks, gambar)

### Padding
Jarak antara content dan border
```css
padding: 20px;
```

### Border
Garis pembatas
```css
border: 2px solid black;
```

### Margin
jarak antar elemen
```css
margin: 30px;
```

### Width & Height
```css
width: 200px;
height: 100px;
```
Default box model:
```
Total width = width + padding + border
```
gunakan
```css
box-sizing: border-box;
```
agar padding dan border masuk ke width

### Outline
mirip border tapi tidak mempengaruhi layout dan tidak menambah ukuran elemen
```css
outline: 3px dashed red;
```

### Box Shadow
memberi bayangan
```css
box-shadow: 5px 5px 10px rgba(0,0,0,0.3);
```
format:
```
x-offset y-offset blur color
```



## 2. CSS Units
### Absolute Units
| Unit       | Arti                              |
| ---------- | --------------------------------- |
| px         | Pixel                             |
| cm, mm, in | Ukuran fisik (jarang dipakai web) |

### Relative Units
| Unit | Relative to           |
| ---- | --------------------- |
| %    | Parent                |
| em   | Font-size parent      |
| rem  | Font-size root (html) |
| vw   | Viewport width        |
| vh   | Viewport height       |

### Units with Functions
```css
width: calc(100% - 50px);
```
fungsi lain:
- min()
- max()
- clamp()








