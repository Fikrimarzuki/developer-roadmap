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
}
