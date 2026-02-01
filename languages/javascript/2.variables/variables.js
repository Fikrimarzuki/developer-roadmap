// ALL ABOUT VARIABLES


// 1. Variable Declarations
console.log("== 1. Variable Declarations ==");
// cara lama, sudah jarang dipakai pada saat development karena bisa dideklarasi ulang
var nameVar = "Varname"
console.log(nameVar);
var nameVar = "Varname 2" // masih jalan, hal ini akan menimbulkan error pada saat development
console.log(nameVar);
nameVar = "Varname 3" // bisa reassign juga
console.log(nameVar);

// let - bisa diubah nilainya tapi tidak bisa dideklarasi ulang
let nameLet = "Letname"
console.log(nameLet);
// let nameLet = "Letname 2" // hal ini akan error
nameLet = "Letname 2" // tapi bisa reassign
console.log(nameLet);

// const - tidak bisa diubah nilainya sama sekali\
const nameConst = "Constname";
console.log(nameConst);
// const nameConst = "Constname 2"; // akan error
// nameConst = "Constname 2"; // akan error juga
const PI = 3.14; // biasanya nama variabel capital
console.log(PI);



// 2. Hoisting
console.log("\n\n== 2. Hoisting ==");
// deklarasi variable diangkat ke atas scope
console.log(hoistingVar); // tidak error karena var di hoist, tapi nilainya undefined
var hoistingVar = "Hoisting var"

// console.log(hoistingLet); // akan error
let hoistingLet = "Hoisting let"

// console.log(hoistingConst); // akan error
const hoistingConst = "Hoisting const"



// 3. Variable Naming Rules
console.log("\n\n== 3. Variable Naming Rules ==");
// Beberapa karakter yang diperbolehkan
// - huruf, angka, _, $
// - tidak boleh diawali angka
// - case sensitive

// best practice adalah camel case, kata pertama kecil, kata berikutnya diawali dengan kapital
let camelCase = "Camel Case"
let _underscore = "Underscore"
let $dollarPrice = 10000
console.log(camelCase, _underscore, $dollarPrice);

// let 1name = "test" // akan error
// let user-name = "test" // akan error



// 4. Variable Scopes
console.log("\n\n== 4. Variable Scopes ==");
// area variabel bisa diakses

// Global Scope
let globalVariable = "Global";

// abaikan fungsi ini untuk sekarang
function fungsi1() {
  console.log(globalVariable);
}
fungsi1();

// Function Scope
function fungsiScope() {
  let functionLet = "Let dalam function"
  var functionVar = "Var dalam function"
  console.log(functionLet);
  console.log(functionVar);
  
}
fungsiScope();
// console.log(functionLet); // akan Error karena tidak bisa diakses di luar function
// console.log(functionVar); // akan Error juga


// Block scope
{
  let blockLet = "Let dalam block"
  const blockConst = "const dalam block"
  var blockVar = "var dalam block"

  console.log(blockLet);
  console.log(blockConst);
  console.log(blockVar);
}

console.log(blockVar); // masih bisa (var tidak punya block scope)
// console.log(blockLet); // akan error
// console.log(blockConst); // akan error



