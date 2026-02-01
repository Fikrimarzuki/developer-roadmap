// TYPE CASTING
// proses mengubah nilai dari satu tipe data ke tipe data lain



// 1. Type Conversion vs Coercion
// conversion = normal
// coercion = otomatis oleh javascript
console.log("== 1. Type Conversion vs Coercion ==");
// Conversion (manual)
let strNumber = "123";
let convertedNumber = Number(strNumber);
console.log("str number: ", strNumber, ". typeof: ", typeof strNumber);
console.log("converted number: ", convertedNumber, ". typeof: ", typeof convertedNumber);

// Coercion (otomatis)
let result = "5" * 2; // string 5 dikali number 2 otomatis akan jadi number
console.log("otomatis diubah oleh js: ", result, ". typeof: ", typeof result);



// 2. Implicit Type Casting (Coercion)
console.log("\n\n== 2. Implicit Type Casting (Coercion) ==");
// string + number -> string
console.log("'5' + 2 =", "5" + 2);

// string - number -> number
console.log("'5' - 2 =", "5" - 2);

// boolean ke number
console.log("true + 1 =", true + 1);
console.log("false + 1 =", false + 1);

// loose comparison
console.log("'5' == 5 →", "5" == 5);   // true (coercion)
console.log("'5' === 5 →", "5" === 5); // false (no coercion)



// 3. Explicit Type Casting (Manual Conversion)
console.log("\n\n== 3. Explicit Type Casting (Manual Conversion) ==");
// String → Number
console.log("Number('123'):", Number("123"));
console.log("parseInt('10px'):", parseInt("10px"));
console.log("parseFloat('3.14'):", parseFloat("3.14"));

// Number → String
console.log("String(123):", String(123));
console.log("(123).toString():", (123).toString());

// To Boolean
console.log("Boolean(1):", Boolean(1));
console.log("Boolean(0):", Boolean(0));
console.log("Boolean(''):", Boolean(""));
console.log("Boolean('Hello'):", Boolean("Hello"));



// 4. Truthy & Falsy Values
console.log("\n\n== 4. Truthy & Falsy Values ==");
// falsy -> false, 0, "", null, undefined, NaN
let values = [false, 0, "", null, undefined, NaN, "text", 123, [], {}];
values.forEach(v => {
  console.log(v, "→", Boolean(v));
});



// 5. Type Checking
console.log("\n\n== 5. Type Checking ==");

console.log("typeof 'hello':", typeof "hello");
console.log("typeof 123:", typeof 123);
console.log("typeof true:", typeof true);
console.log("typeof undefined:", typeof undefined);
console.log("typeof null:", typeof null); // bug historis
console.log("typeof {}:", typeof {});
console.log("typeof []:", typeof []);
console.log("typeof function(){}:", typeof function(){});




