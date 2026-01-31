fn main() {
  println!("Hello, world!");
  
  // ===== VARIABLES =====
  // default immutable
  let x = 10;
  // x = 20; error

  // use mut for mutable
  let mut y = 10;
  println!("before reassign: {y}");
  y = 20;

  // shadowing
  let z = 5;
  let z = z + 1; // new variable

  // data types
  let a: i32 = 10;
  let b: f64 = 3.14;
  let c: bool = true;
  let d: char = 'R';

  // constants
  const MAX_USERS: u32 = 100;

  println!("{x} {y} {z}");
  println!("{a} {b} {c} {d}");
  println!("{MAX_USERS}");



  // CONTROL FLOW
  let number = 7;

  // if (expression, not statement)
  let result = if number > 5 { "big" } else { "small" };

  // loop
  let mut count = 0;
  loop {
    count += 1;
    if count == 3 {
      break;
    }
  }

  // while
  let mut n = 3;
  while n > 0 {
    n -= 1;
  }

  // for
  for i in 0..3 {
    println!("i = {}", i);
  }

  // match
  match number {
    1 => println!("one"),
    2..=5 => println!("between 2 and 5"),
    _ => println!("other"),
  }

  println!("Result: {}", result);



  // FUNCTIONS AND METHODS SYNTAX
  greet("Rustania");

  let sum = add(2, 3);
  println!("Sum: {}", sum);

  let user = User {
    name: String::from("Rustacean"),
    age: 20,
  };

  user.say_hello();




  // PATTERN MATCHING AND DESTRUCTURING
  // match
  let number = 3;
  match number {
    1 => println!("one"),
    2 | 3 => println!("two or three"),
    4..=10 => println!("range"),
    _ => println!("other"),
  }

  // destructuring tuple
  let tup = (1, "hello");
  let (_x, _y) = tup;

  // destructuring struct
  let point = Point { x: 10, y: 20 };
  let Point { x, y } = point;

  // if let
  let maybe = Some(5);
  if let Some(value) = maybe {
    println!("Value = {}", value);
  }

  println!("{x} {y}");
}

// FUNCTIONS AND METHODS SYNTAX
// function
fn greet(name: &str) {
  println!("Hello, {}", name);
}

// function return value
fn add(a: i32, b: i32) -> i32 {
  a + b // no semicolon = return
}

// struct + method
struct User {
  name: String,
  age: u8,
}

impl User {
  fn say_hello(&self) {
    println!("Hi, my name is {}", self.name);
    println!("My age is {}", self.age);
  }
}

struct Point {
  x: i32,
  y: i32,
}