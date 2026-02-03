# CSS FUNCTIONS

biasa digunakan untuk
- perhitungan
- responsiveness
- warna dinamis
- transformasi

## Beberapa Fungsi
- calc()                - hitung nilai
- min()                 - pilih nilai terkecil
- max()                 - pilih nilai terbesar
- clamp()               - batas min-max fleksibel
- var()                 - pakai css variabel
- rgb()/hsl()           - warna
- translate()/rotate()  - transform


## calc()
```css
width: calc(100% - 20px);
```

## min()
```css
width: min(300px, 80%);
```

## max()
```css
width: max(300px, 50%);
```

## clamp()
```css
font-size: clamp(16px, 5vw, 32px);
```

## var()
```css
color: var(--main-color);
```

## color functions
```css
background: rgb(255,0,0);
background: hsl(200,50%,50%);
```

## transform functions
```css
transform: rotate(10deg) translateX(20px);
```



