// USING (THIS) KEYWORD



// 1. this in a method
const user = {
  name: "Javascriptia",
  greet() {
    console.log("Hello, I am", this.name);
  },
};
user.greet();


// 2. this in a normal function
// - non strict mode - global object
// - strict mode - undefined
function showThis() {
  console.log("this in function:", this);
}
showThis();


// 3. using it alone
console.log("this alone:", this);


// 4. this in event handler
// ini hanya jalan di browser bukan node
// document.querySelector("button").addEventListener("click", function() {
//   console.log(this); // tombol yang diklik
// });


// 5. this in arrow function
// arrow function tidak punya this, melainkan mengambil dari luar (lexical this)
const obj = {
  value: 10,
  normal() {
    console.log("normal this:", this.value);
  },
  arrow: () => {
    console.log("arrow this:", this.value); // undefined
  },
};
obj.normal();
obj.arrow();


// 6. Function borrowing
// pinjam method dari objek lain
const person1 = {
  name: "Alice",
};
const person2 = {
  name: "Bob",
};

function sayHello() {
  console.log("Hi, I'm", this.name);
}

sayHello.call(person1);
sayHello.call(person2);


// 7. Explicit binding
// - call
// - apply
// - bind
function introduce(city, country) {
  console.log(`I'm ${this.name} from ${city}, ${country}`);
}

const dev = { name: "Javascriptia" };

// CALL → argumen satu-satu
introduce.call(dev, "Jakarta", "Indonesia");

// APPLY → argumen dalam array
introduce.apply(dev, ["Bandung", "Indonesia"]);

// BIND → mengembalikan function baru
const boundFn = introduce.bind(dev, "Surabaya", "Indonesia");
boundFn();



