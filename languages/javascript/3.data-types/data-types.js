// DATA TYPES


// 1. Primitive Types
console.log("== 1. Primitive Types ==");
// string
let text = "Ini string"; // pake ""
console.log(text);
let text2 = 'Ini string juga pake kutip 1'; // pake '
console.log(text2);
let text3 = `Ini string juga pake backtick`; // pake `
console.log(text3);



// number
let num = 10;
console.log(num);

// bigint
let bigNumber = 9007199254740991n;
console.log(bigNumber);

// boolean
let isBool = true;
console.log(isBool);

// undefined
let notAssigned;
console.log(notAssigned);

// null
let emptyValue = null;
console.log(emptyValue);

// symbol (nilai unik)
let sym1 = Symbol("id");
let sym2 = Symbol("id");
console.log(sym1, sym2);
console.log(sym1 === sym2);



// 2. Object
console.log("\n\n== 2. Object ==");
// Kumpulan properti (key-value) 
let user = {
  name: "user name",
  age: 10,
  isStudent: false
}
console.log("\nObject:", user);



// 3. Object Prototype (bisa di skip dahulu bila sulit dipahami)
console.log("\n\n== 3. Object Prototype ==");
// semua object di JS punya prototype
console.log(user.toString()); // dari prototype
console.log(Object.getPrototypeOf(user));



// 4. Prototypal Inheritance (bisa di skip dahulu bila sulit dipahami)
console.log("\n\n== 4. Prototypal Inheritance ==");
// object bisa mewarisi properti/method dari object lain
let animal = {
  eats: true
}
let dog = Object.create(animal);
dog.barks = true;
console.log(dog.eats); // diwarisi dari object animal
console.log(dog.barks);



// 5. Built-In Objects
console.log("\n\n== 5. Built-In Objects ==");
// javascript punya banyak object bawaan
console.log(Math.PI);
console.log(new Date());
console.log(Math.random());
console.log(new String(123));



// 6. Typeof Operator
console.log("\n\n== 6. Typeof Operator ==");
// digunakan untuk mengecek tipe data
console.log(typeof "hello");        // string
console.log(typeof 123);            // number
console.log(typeof true);           // boolean
console.log(typeof undefined);      // undefined
console.log(typeof null);           // object (bug historis)
console.log(typeof {});             // object
console.log(typeof []);             // object
console.log(typeof function(){});   // function
let exampleVar = "123"
console.log(typeof exampleVar); // mengecek type dari variabel













