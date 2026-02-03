# ATTRIBUTE SELECTORS
Memilih elemen berdasarkan atribut HTML

### Sintaks Dasar
```css
element[attribute] { }
element[attribute="value"] { }
```

### Jenis attribute selector
| Selector        | Arti                      |
| --------------- | ------------------------- |
| `[attr]`        | Elemen yang punya atribut |
| `[attr="val"]`  | Atribut sama persis       |
| `[attr*="val"]` | Mengandung kata           |
| `[attr^="val"]` | Dimulai dengan            |
| `[attr$="val"]` | Diakhiri dengan           |
contoh:
```css
input[type="text"] { }
a[href*="google"] { }
```






