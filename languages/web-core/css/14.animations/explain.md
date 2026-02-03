# ANIMATIONS


## 1. Transforms
mengubah bentuk/posisi elemen tanpa merusak layout
```css
transform: translateX(50px);
transform: rotate(45deg);
transform: scale(1.2);
transform: skew(10deg);
```
beberapa fungsi:
- translate - menggeser
- rotate - memutar
- scale - men-zoom
- skew - memiringkan



## 2. Transitions
transisi halus dari satu state ke state lain ( biasanya saat hover)
```css
.box {
  transition: all 0.3s ease;
}

.box:hover {
  background: blue;
  transform: scale(1.1);
}
```
format:
```
transition: property duration timing-function delay;
```



## 3. Keyframe Animations
animasi otomatis tanpa interaksi user
```css
@keyframes name {
  from { }
  to { }
}
```
```css
animation: name duration infinite;
```
contoh:
```css
@keyframes move {
  from { transform: translateX(0); }
  to { transform: translateX(200px); }
}

.box {
  animation: move 2s infinite alternate;
}
```



