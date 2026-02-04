// EXPRESSIONS & OPERATORS


// 1. Arithmetic Operators
console.log("== 1. Arithmetic Operators ==");
// + - * / % **
let a = 10;
let b = 3;

console.log("a + b =", a + b);
console.log("a - b =", a - b);
console.log("a * b =", a * b);
console.log("a / b =", a / b);
console.log("a % b =", a % b);
console.log("a ** b =", a ** b); // pangkat



// 2. Assignment Operators
console.log("\n\n== 2. Assignment Operators ==");
// = += -= *= /= %= **= <<= >>= >>>= &= ^= |= &&= ||= ??=
let x = 5;
x += 2;  // x = x + 2
x *= 3;  // x = x * 3
x -= 1;
x /= 4;
console.log("x =", x);



// 3. Comparison Operators
console.log("\n\n== 3. Comparison Operators ==");
// > < >= <= == === != !==
console.log("5 > 3:", 5 > 3);
console.log("5 < 3:", 5 < 3);
console.log("5 >= 5:", 5 >= 5);
console.log("5 === '5':", 5 === "5");
console.log("5 == '5':", 5 == "5");
console.log("5 != '5':", 5 != "5");
console.log("5 !== '5':", 5 !== "5");



// 4. Logical Operators
console.log("\n\n== 4. Logical Operators ==");
// && || !
console.log("true && false:", true && false);
console.log("true || false:", true || false);
console.log("!true:", !true);



// 5. Conditional (Ternary) Operator
console.log("\n\n== 5. Conditional (Ternary) Operators ==");
// kondisi ? kondisi true : kondisi false
let age = 20;
let status = age >= 18 ? "Adult" : "Minor";
console.log("Status:", status);



// 6. Unary Operators
console.log("\n\n== 6. Unary Operators ==");
let n = 5;
console.log("++n:", ++n);
console.log("--n:", --n);
console.log("typeof n:", typeof n);
console.log("delete example:");

let obj = { a: 1 };
delete obj.a;
console.log(obj);



// 7. Comma Operator
console.log("\n\n== 7. Comma Operators ==");
// - Menjalankan beberapa ekspresi, ambil hasil terakhir
let c = (1, 2, 3);
console.log("c =", c); // 3



// 8. String Operator
console.log("\n\n== 8. String Operators ==");
let first = "Hello";
let second = "World";
console.log(first + " " + second);
let third = "Hello"
third += " World"



// 9. Bitwise Operators
console.log("\n\n== 9. Bitwise Operators ==");
console.log("5 & 1 =", 5 & 1); // AND
console.log("5 | 1 =", 5 | 1); // OR
console.log("5 ^ 1 =", 5 ^ 1); // XOR
console.log("~5 =", ~5); // NOT
console.log("5 << 1 =", 5 << 1); // LEFT SHIFT
console.log("5 >> 1 =", 5 >> 1); // RIGHT SHIFT
console.log("5 >>> 2 =", 5 >>> 2); // ZERO-FILL RIGHT SHIFT




// 10. Bigint Operators
console.log("\n\n== 10. Bigint Operators ==");
let big1 = 10n;
let big2 = 3n;
console.log("big1 + big2 =", big1 + big2);
console.log("big1 * big2 =", big1 * big2);


