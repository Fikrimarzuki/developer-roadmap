# PSEUDO ELEMENTS

## 1. `::before`
menambahkan konten sebelum elemen
```css
div::before {
  content: "★";
}
```


## 2. `::after`
menambahkan konten setelah elemen
```css
div::after {
  content: "✓";
}
```


## 3. `::first-letter`
menstyle huruf pertama
```css
p::first-letter {
  font-size: 30px;
}
```


## 4. `::first-line`
menstyle baris pertama
```css
p::first-line {
  color: blue;
}
```


## 5. `::selection`
style saat teks diseleksi user
```css
::selection {
  background: black;
  color: white;
}
```


## 6. `::placeholder`
style placeholder input
```css
input::placeholder {
  color: gray;
}
```


## 7. `::marker`
style bullet/number list
```css
li::marker {
  color: red;
}
```






