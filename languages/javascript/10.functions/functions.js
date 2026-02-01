// FUNCTIONS



// 1. Function Declaration & Parameters
console.log("== 1. Function Declaration & Parameters ==");
// Cara Declare
// - buat keyword function
// - diikuti nama function yang mau dibuat
// - diikuti (), bisa diisi parameter apabila ada
// - diikuti {}, yang didalamnya berisi aksi/intruksi yang akan berjalan 
function namaFungsi() {
  // instruksi
  console.log("fungsi dipanggil");
}
// Cara Panggil
// - tulis nama function
// - diikuti (), bisa diisi dengan argumen apabila ada
namaFungsi();

// Dengan parameter
function namaFungsiParameter(parameterPertama, parameterKedua) {
  // intruksi
  console.log(parameterPertama, parameterKedua);
}
namaFungsiParameter("argumen pertama", "argumen kedua")

// Return di parameter
function jumlah(a, b) {
  return a + b
}
console.log(jumlah(10, 5));

// Default Parameters
function greet(name = "Guest") { // default param
  return "Hello " + name;
}
console.log(greet("User 5"));
console.log(greet()); // pakai default



// 2. Rest Parameters
console.log("\n\n== 2. Rest Parameters ==");
// mengumpulkan sisa argumen jadi array
function sum(...numbers) {
  console.log(numbers);
  return numbers.reduce((acc, n) => acc + n, 0);
}
console.log("Sum:", sum(1, 2, 3, 4));



// 3. Arrow Function
console.log("\n\n== 3. Arrow Function ==");
// lebih ringkas, tidak punya "this" sendiri
const multiply = (a, b) => a * b;
console.log("Multiply:", multiply(3, 4));



// 4. IIFE (Immediately Invoked Function Expression)
console.log("\n\n== 4. IIFE ==");
// langsung dijalankan setelah dibuat
(function () {
  console.log("IIFE dijalankan langsung");
})();



// 5. Arguments Object
console.log("\n\n== 5. Arguments Object ==");
function showArguments() {
  console.log("arguments:", arguments);
  console.log(arguments[0]);
  console.log(arguments[1]);
}
showArguments(1, "test", true);



// 6. Scope & Function Stack
console.log("\n\n== 6. Scope & Function Stack ==");
// lexical scoping
let outer = "Outside";
function lexicalExample() {
  let inner = "Inside";
  console.log(outer); // bisa akses
  console.log(inner);
}
lexicalExample();

// closures
function counter() {
  let count = 0;
  return function () {
    count++;
    return count;
  };
}
const myCounter = counter();
console.log("Counter:", myCounter());
console.log("Counter:", myCounter());

// recursion
// memanggil function itu sendiri
function factorial(n) {
  if (n === 0) return 1; // butuh untuk memberhentikan recursion
  return n * factorial(n - 1);
}
console.log("Factorial 5:", factorial(5));



// 7. Built In Functions
console.log("\n\n== 7. Built In Functions ==");
console.log("parseInt:", parseInt("10px"));
console.log("isNaN:", isNaN("hello"));
console.log("setTimeout example:");
setTimeout(() => {
  console.log("Dijalankan setelah 1 detik");
}, 1000);


