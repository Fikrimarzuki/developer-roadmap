# METHODOLOGIES


## 1. BEM (Block Element Modifier)
struktur penamaan class
```
block__element--modifier
```


## 2. SASS (CSS Preprocessor)
bahasa CSS yang punya fitur tambahan
```scss
$primary: blue;

.card {
  color: $primary;

  &:hover {
    color: red;
  }
}
```
fitur utama:
- Variables
- Nesting
- Mixins
- Functions


## 3. PostCSS
tool untuk memproses CSS. Contoh plugin:
- Autoprefixer
- CSS Nesting
- Minifier
```css
display: flex;
```
bisa diubah otomatis jadi kompatibel browser lama


## 4. CSS Modules
scoped CSS, biasanya di React/Next.js
```css
.button {
  color: red;
}
```
di komponen
```js
import styles from "./button.module.css";

<button className={styles.button}></button>
```
class jadi unik
```
button__3f82a
```


## 5. CSS-in-JS
CSS ditulis di JavaScript. Contoh (styled-components):
```js
const Button = styled.button`
  background: blue;
  color: white;
`;
```
kelebihan:
- scoped
- dynamic styling
- theming mudah



