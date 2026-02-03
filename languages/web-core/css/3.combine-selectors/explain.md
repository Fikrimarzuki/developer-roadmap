# COMBINE SELECTORS


## 1. Descendant Selector (`space`)
```css
div p {
  color: blue;
}
```
Semua `<p>` di dalam `<div>` baik langsung maupun nested
```html
<div>
  <p></p>
  <div>
    <p></p>
  </div>
</div>
```
```
div
  └─ p ✅
  └─ div
    └─ p ✅
```



## 2. Child Selector (`>`)
```css
div > p {
  color: green;
}
```
hanya `<p>` yang langsung di dalam `<div>`
```html
<div>
  <p></p>
  <span>
    <p></p>
  </span>
</div>
```
```
div
  └─ p ✅
  └─ div
    └─ p ❌

```



## 3. Adjacent Sibling Selector (`+`)
```css
h3 + p {
  color: red;
}
```
Pilih `<p>` yang sejajar dan setelah `<h3>`
```html
<div>
  <p></p>
  <h3></h3>
  <p></p>
  <p></p>
</div>
```
```
div
  └─ p ❌
  └─ h3
  └─ p ✅
  └─ p ❌
```



## 4. General Sibling Selector (`~`)
```css
h4 ~ p {
  color: purple;
}
```
Semua `<p>` setelah `<h4>` dalam parent yang sama
```html
<div>
  <h4></h4>
  <p></p>
  <div></div>
  <p></p>
</div>
```
```
h4
p ✅
div
p ✅
```



## 5. Namespace Selector (`|`)
- Selector ini sudah jarang dipakai.
- Namespace dipakai kalau dokumen punya lebih dari satu jenis bahasa markup, biasanya:
  - HTML + SVG
  - HTML + XML
  - HTML + MathML



