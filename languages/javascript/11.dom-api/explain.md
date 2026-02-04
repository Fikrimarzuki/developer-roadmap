# DOM APIs

DOM (Document Object Model) adalah representasi struktur HTML dalam bentuk objek JavaScript.  
Dengan DOM API, JavaScript bisa **membaca**, **mengubah**, **menambah**, dan **menghapus** elemen di halaman web.



## 1. Selecting Elements
digunakan untuk mengambil elemen HTML
- `document.getElementById()` - ambil elemen berdasarkan ID
- `document.getElementByClassName()` - ambil berdasarkan class (HTMLCollection)
- `document.querySelector()` - ambil elemen pertama yang cocok dengan CSS selector
- `document.querySelectorAll()` - ambil semua elemen (NodeList)



## 2. Modifying Content (Mengubah Isi)
- `textContent` - mengubah teks
- `innerHTML` - mengubah isi HTML

```js
element.textContent = "Hello";
element.innerHTML = "<b>Hello</b>";
```



## 3. Changing Attributes
- `setAttribute()` - menambah/mengubah atribut
- `getAttribute()` - mengambil nilai atribut
- `removeAttribute()` - menghapus atribut



## 4. Styling Element
- style
- class
```js
element.style.color = "red" // ganti style warna teks
element.classList.add("active") // tambah class
element.classList.remove("dark") // hapus class
element.classList.toggle("visible") // jika ada akan menghapus, jika ada akan menambah class
element.classList.replace("foo", "bar") // mengganti class
```



## 5. Creating and Adding Elements
```js
const div = document.createElement("div");
div.textContent = "New Element";
document.body.appendChild(div);
```



## 6. Removing Element
```js
element.remove();
```



## 7. Event Listeners (Interaksi)
digunakan agar halaman bisa merespon aksi user
```js
button.addEventListener("click", () => {
  alert("Clicked!");
});
```



## 8. Event Object
setiap event membawa informasi
```js
document.addEventListener("mousemove", (event) => {
  console.log(event.clientX, event.clientY);
});
```




