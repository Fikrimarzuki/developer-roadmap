// LOOPS AND ITERATIONS

// notes: untuk stop infinite loop: ctrl + c

// Why?
// contoh simpel, butuh log 5 kali
// cara standar tanpa loop
console.log("Tanpa Loop");
console.log("Hello World!");
console.log("Hello World!");
console.log("Hello World!");
console.log("Hello World!");
console.log("Hello World!");
// menggunakan loop
console.log("\nMenggunakan Loop");
for (let i = 0; i < 5; i++) {
  console.log("Hello World!");
}
// - lebih simple
// - lebih mudah apabila ada perubahan
// - ...dll



// 1. For Loop
console.log("\n\n== 1. For Loop ==");
/*
  for (inisialisasi; kondisi; eksekusi) {
    // aksi
  }
*/
for (let i = 0; i < 3; i++) {
  console.log("i =", i);
}
let vocal = "aiueo"
for (let i = 0; i < vocal.length; i++) {
  console.log("huruf vokal kecil: ", vocal[i]);
  console.log("huruf vokal besar: ", vocal[i].toLocaleUpperCase());
}



// 2. While Loop
console.log("\n\n== 2. While Loop ==");
/*
  while (kondisi) {
    // aksi
  }
*/
let count = 0;
while (count < 3) {
  console.log("count = ", count);
  count++
}



// 3. Do... While Loop
console.log("\n\n== 3. Do While Loop ==");
// Minimal menjalankan 1 kali meskipun kondisi false
let num = 0;
do {
  console.log("num = ". num);
  num++
} while(num < 2)



// 4. Break & Continue
console.log("\n\n== 4. Break & Continue ==");
// break - menghentikan loop
for (let i = 0; i < 10; i++) {
  if (i === 4) {
    console.log("Break at", i);
    break;
  }
  console.log("i =", i);
}

// continue - lompat ke iterasi berikutnya
for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue; // lewati angka 2
  }
  console.log("continue i =", i);
}



// 5. For... Of Loop
console.log("\n\n== 5. For... Of Loop ==");
// untuk iterasi Value dari iterable (array, string, dll)
const fruits = ["apple", "banana", "mango"];

for (const fruit of fruits) {
  console.log("fruit:", fruit);
}

const word = "html";
for (const char of word) {
  console.log("char:", char);
}



// 6. For...In Loop
console.log("\n\n== 5. For... In Loop ==");
// untuk iterasi Key (property name) dari object
const user = {
  name: "Javascriptia",
  age: 25,
  country: "Indonesia",
};

for (const key in user) {
  console.log(key, "=>", user[key]);
}

// For in vs For of di array
const animals = ["cat", "dog", "bee"];
for (const animal of animals) {
  console.log(animal, "=>", animal);
}
for (const index in animals) {
  console.log(index, "=>", animals[index]);
}


