// DATA STRUCTURES


// 1. Structured Data (JSON)
console.log("== 1. Structured Data (JSON) ==");
// JSON = JavaScript Object Notation
// format teks untuk representasi data terstruktur
// beda dengan object
//  - object: bisa punya function, undefined, symbol, dll
//  - JSON: hanya tipe data tertentu (string, number, boolean, null, array, object)
const user = {
  id: 1,
  name: "javasciprt",
  roles: ["admin", "editor"],
  profile: { country: "Indonesia", city: "Jakarta" }
} // ini object 

const jsonString = JSON.stringify(user);
console.log("Object -> JSON string:", jsonString);
console.log("typeof jsonString:", typeof jsonString);

const parsedBack = JSON.parse(jsonString);
console.log("JSON string -> Object:", parsedBack);
console.log("typeof parsedBack:", typeof parsedBack);

// Catatan: JSON tidak bisa menyimpan undefined / function
const weirdObj = {
  a: 1,
  b: undefined,
  c: function () {},
};
console.log(JSON.stringify(weirdObj));
// b dan c akan hilang/diabaikan (function diabaikan, undefined diabaikan)



// 2. Keyed Collections
console.log("\n\n== 2. Keyed Collections ==");
console.log("Map");
// Map
// - mirip object
// - key bisa tipe apa saja (object, function, dll)
// - menjaga urutan insert
// - punya size, method jelas (get/set/has/delete)
const map = new Map();
map.set("name", "Javascriptia");
map.set(1, "one");
const objKey = { key: "objectKey" };
map.set(objKey, "value for object key");

console.log("Map size:", map.size);
// console.log(map.name); // undefined
console.log("Map get('name'):", map.get("name"));
console.log("Map get(1):", map.get(1));
console.log("Map get(objKey):", map.get(objKey));
console.log("Map has('name'):", map.has("name"));

console.log("Iterate Map entries:");
for (const [k, v] of map.entries()) {
  console.log("  ", k, "=>", v);
}


// Weakmap
console.log("\nWeakmap");
// - key harus object
// - tidak bisa di-iterate (no entries(), no size)
// - cocok untuk "private data" / metadata object
// - key yang sudah tidak direferensikan bisa di-GC (garbage collected)
const weakMap = new WeakMap();
const sessionUser = { id: 10, name: "UserA" };

weakMap.set(sessionUser, { token: "abc123", lastLogin: Date.now() });
console.log("WeakMap has sessionUser:", weakMap.has(sessionUser));
console.log("WeakMap get sessionUser:", weakMap.get(sessionUser));

// Hapus reference object → secara teori bisa dibersihkan GC
// sessionUser = null; // kalau pakai let, bisa diset null


// Set
console.log("\nSet");
// koleksi nilai unik (tidak ada duplikat)
const set = new Set();
set.add(1);
set.add(1); // duplikat, tidak masuk
set.add(2);
set.add("2"); // 2 dan "2" beda
set.add({ a: 1 }); // object dianggap beda referensi

console.log("Set size:", set.size);
console.log("Set has(2):", set.has(2));
console.log("Set values:");
for (const v of set.values()) {
  console.log("  ", v);
}


// Weakset
console.log("\nWeakset");
// - hanya menyimpan object
// tidak bisa diiterasi, tidak ada size
// object yang tidak direferensikan bisa di GC
const weakSet = new WeakSet();
const obj1 = { name: "temp1" };
const obj2 = { name: "temp2" };

weakSet.add(obj1);
weakSet.add(obj2);

console.log("WeakSet has obj1:", weakSet.has(obj1));
console.log("WeakSet has obj2:", weakSet.has(obj2));



// 3. Indexed Collections
console.log("\n\n== 3. Indexed Collections ==");
// - arrays
// - typed arrays

console.log("Array");
const arr = [10, 20, 30];
console.log("Array:", arr);
console.log("arr[0]:", arr[0]);
console.log("length:", arr.length);

// operasi umum
arr.push(40); // tambah di akhir
console.log("push 40:", arr);
arr.pop(); // kurang di akhir
console.log("pop:", arr);
arr.unshift(0) // tambah di awal
console.log("unshift 0:", arr);
arr.shift(); // kurang di awal
console.log("shift:", arr);
// hati-hati saat penggunaannya, karena flownya di push/pop/shift/unshift dulu baru dipakai valuenya
// console.log(arr.push(50)) // yang muncul lengthnya bukan arraynya
// console.log(arr.pop()); // yang muncul nilai yang dibuang
// console.log(arr.unshift(10)); yang muncul lengthnya bukan arraynya
// console.log(arr.shift()); // yang muncul nilai yang dibuang

// contoh built in array
// map, filter, slice, reduce, reverse, sort, ...
const doubled = arr.map((x) => x * 2);
console.log("map x2:", doubled);

const filtered = arr.filter((x) => x >= 20);
console.log("filter >=20:", filtered);

const sum = arr.reduce((acc, x) => acc + x, 0);
console.log("reduce sum:", sum);


// Typed Arrays
// array khusus untuk data numerik dengan ukuran fixed dan performa lebih baik
// Contoh: Uint8Array, Int16Array, Float32Array, dll
// Biasa dipakai untuk
// - binary data
// - audio/video processing
// - webgl
// - performance-critical tasks
console.log("\nTyped Arrays");
// buffer 8 bytes
const buffer = new ArrayBuffer(8);
console.log("ArrayBuffer byteLength:", buffer.byteLength);

// view sebagai Uint8Array (0-255)
const uint8 = new Uint8Array(buffer);
uint8[0] = 255;
uint8[1] = 128;

console.log("Uint8Array:", uint8);
console.log("Uint8Array[0]:", uint8[0]);

// view sebagai Int16Array (2 bytes per item)
const int16 = new Int16Array(buffer);
int16[1] = 32767;

console.log("Int16Array:", int16);
console.log("Int16Array[1]:", int16[1]);




