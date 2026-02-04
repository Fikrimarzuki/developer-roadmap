// STRICT MODE

"use strict"; // aktifkan strict mode

console.log("=== STRICT MODE ===\n");

/*
  Strict Mode?
  Mode khusus JS yang:
  - Mencegah kesalahan umum
  - Menghilangkan fitur berbahaya
  - Membuat error lebih jelas

  Strict Mode penting karena:
  - Menghindari bug diam-diam
  - Membantu engine optimize
  - Wajib di ES modules (otomatis strict)
*/


// 1. VARIABEL TANPA DECLARATION
try {
  x = 10; // ❌ error di strict mode
} catch (err) {
  console.log("Error:", err.message);
}



// 2. TIDAK BOLEH DUPLIKAT PARAMETER
try {
  eval(`
    function test(a, a) {
      return a;
    }
  `);
} catch (err) {
  console.log("Duplicate parameter error:", err.message);
}



// 3. this TIDAK OTOMATIS GLOBAL
function showThis() {
  console.log("this =", this);
}
showThis(); // undefined (bukan global object)



// 4. TIDAK BISA DELETE VARIABLE
let a = 5;
try {
  delete a; // ❌ error
} catch (err) {
  console.log("Delete variable error:", err.message);
}



// 5. RESERVED WORDS TIDAK BOLEH DIPAKAI
try {
  eval(`let package = "test";`);
} catch (err) {
  console.log("Reserved word error:", err.message);
}



// 6. ARGUMENTS TIDAK TERHUBUNG DENGAN PARAMETER
function changeValue(a) {
  a = 100;
  console.log("arguments[0]:", arguments[0]); // tetap nilai awal
}

changeValue(5);



