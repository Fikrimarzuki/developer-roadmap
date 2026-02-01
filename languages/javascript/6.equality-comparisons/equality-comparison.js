// EQUALITY COMPARISONS


// 1. Value Comparison Operators
console.log("1. Value Comparison Operators");
// ==, ===, Object,is

// == (loose equality)
// - bisa melakukan type coercion (konversi otomatis)
// - banyak edge-case -> rawan bug
// - membandingkan nilai saja
console.log("'5' == 5", "5" == 5);
console.log("0 == false", 0 == false);
console.log("'' == false", "" == false);
console.log("null == undefined", null == undefined);

// === (strict equality)
// - Tidak melakukan coercion
// - Biasanya ini yang dipakai sehari-hari
// - membandingkan nilai dan tipe datanya
console.log("'5' === 5", "5" === 5);
console.log("0 === false", 0 === false);
console.log("null === undefined", null === undefined);
console.log("NaN === NaN", NaN === NaN);
console.log("-0 === 0", -0 === 0);

// Object.is (sameValue)
// Mirip === tapi berbeda untuk beberapa tipe data
// - NaN: Object.is(NaN, NaN) -> true (kalau === hasilnya false)
// - -0 dan 0: Object.is(-0, 0) -> false (kalau === hasilnya true)
console.log("Object.is(NaN, NaN)", Object.is(NaN, NaN));
console.log("Object.is(-0, 0)", Object.is(-0, 0));



// 2. Object / Reference Comparison
console.log("\n\n== 2. Object/Reference Comparison");
// object (termasuk array/function) dibandingkan berdasarkan referensi, bukan isi

console.log("[] === []:", [] === []); // false
console.log("{} === {}:", {} === {}); // false
const obj = {};
console.log("obj === {}:", obj === {}); // false

const a1 = { x: 1 };
const a2 = { x: 1 };
const a3 = a1;

console.log("a1 === a2:", a1 === a2); // false (beda referensi)
console.log("a1 === a3:", a1 === a3); // true (referensi sama)

const arr1 = [1, 2];
const arr2 = [1, 2];
console.log("arr1 === arr2:", arr1 === arr2); // false

// Kalau mau bandingkan isi, perlu logic sendiri (misal deepEqual)
console.log("JSON stringify compare:", JSON.stringify(arr1) === JSON.stringify(arr2)); // true (tapi ada limit)



// 3. Equality Algorithms
console.log("\n\n== 3. Equality Algoritms ==");
// - isLooselyEqual  -> ==
// - isStrictlyEqual -> ===
// - SameValueZero   -> dipakai oleh Array.prototype.includes, Set, Map key matching*
// - SameValue       -> dipakai oleh Object.is
console.log("NaN with NaN");
console.log("==:", NaN == NaN, "; ===:", NaN === NaN, "; Object.is:", Object.is(NaN, NaN));
console.log("cek isNaN dulu", Number.isNaN(NaN) && Number.isNaN(NaN));
console.log("null with null");
console.log("==:", null == null, "; ===:", null === null, "; Object.is:", Object.is(null, null));
console.log("-0 with 0");
console.log("==:", -0 == 0, "; ===:", -0 === 0, "; Object.is:", Object.is(-0, 0));
console.log('"5" with 5');
console.log("==:", "5" == 5, "; ===:", "5" === 5, "; Object.is:", Object.is("5", 5));
console.log("null with undefined");
console.log("==:", null == undefined, "; ===:", null === undefined, "; Object.is:", Object.is(null, undefined));
console.log("false with 0");
console.log("==:", false == 0, "; ===:", false === 0, "; Object.is:", Object.is(false, 0));
console.log('"" with 0');
console.log("==:", "" == 0, "; ===:", "" === 0, "; Object.is:", Object.is("", 0));






