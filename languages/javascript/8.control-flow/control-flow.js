// CONTROL FLOW


// 1. Conditional Statements
console.log("== 1. Conditional Statements ==");
/*
  if (kondisi) {
    // aksi
  }
  if (kondisi1) {
    // aksi 1
  } else if (kondisi2) {
    // aksi 2
  }
  if (kondisi1) {
    // aksi 1
  } else {
    // kondisi 1 tidak terpenuhi akan kesini 
  }
*/

// If Else
let score = 75;

if (score >= 85) {
  console.log("Grade A");
} else if (score >= 70) {
  console.log("Grade B");
} else if (score >= 60) {
  console.log("Grade C");
} else {
  console.log("Grade D");
}


// Switch
let role = "admin";

switch (role) {
  case "admin":
    console.log("Full access");
    break;
  case "editor":
    console.log("Edit access");
    break;
  case "viewer":
    console.log("Read only access");
    break;
  default:
    console.log("Unknown role");
}



// 2. Exceptional Handling
console.log("\n\n== 2. Exceptional Statements ==");
// handling error agar program tidak crash

// Throw statement
let num1 = 10
let num2 = 2
let num3 = 0
try {
  console.log(num1 / num2);
} catch (err) {
  console.log("Terjadi error:", err.message);
}
try {
  if (num3 === 0) {
    throw new Error("Tidak bisa dibagi 0")
  }
  console.log(num1 / num3); // kalau tidak divalidasi akan error
} catch (err) {
  console.log("Terjadi error:", err.message);
}


// Try / Catch / Finally
try {
  let data = JSON.parse('{"name": "FiJavascriptiakri"}');
  console.log("Parsed JSON:", data);
} catch (error) {
  console.log("JSON error:", error.message);
} finally {
  console.log("Finally selalu dijalankan");
}


// Error objects
try {
  // Akses variabel yang belum dideklarasikan
  console.log(notDefinedVar);
} catch (error) {
  console.log("Name:", error.name);
  console.log("Message:", error.message);
  console.log("Stack:", error.stack.split("\n")[0]);
}








