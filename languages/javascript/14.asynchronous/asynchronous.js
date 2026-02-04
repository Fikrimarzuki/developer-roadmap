// ASYNCHRONOUS


// 1. Synchronous vs Asynchronouse
// synchronouse
console.log("Start Sync");
console.log(1);
console.log(2);
console.log("End Sync");
// asynchronous
console.log("Start Async");
setTimeout(() => {
  console.log("Timeout async done"); // akan muncul paling akhir
}, 0);
console.log("End Async");
// Output:
// Start Async
// End Async
// Timeout async done
// Karena setTimeout masuk ke Web API → Callback Queue → Event Loop



// 2. Event Loop
// Call Stack -> Web APIs -> Callback Queue -> Event Loop
// JS hanya punya 1 thread, jadi async butuh mekanisme ini



// 3. setTimeout & setInterval
setTimeout(() => {
  console.log("This runs after 1 second");
}, 1000);

let counter = 0;
const interval = setInterval(() => {
  console.log("Interval:", counter);
  counter++;
  if (counter === 3) {
    clearInterval(interval);
  }
}, 500);



// 4. Callback
// callback synchronous
function kali(a, b) {
  return a * b
}
function tambah(a, b) {
  return a + b
}
function kurang(a, b) {
  return a - b
}
function bagi(a, b) {
  return a / b
}
function calculator(num1, num2, cb) {
  return cb(num1, num2)
}
console.log(calculator(10, 20, kali)); // 200
console.log(calculator(15, 5, tambah)); // 20
console.log(calculator(10, 5, kurang)); // 5
console.log(calculator(50, 5, bagi)); // 10

// callback asynchronous
function fetchData(callback) {
  setTimeout(() => {
    callback("Data received");
  }, 1000);
}

fetchData((result) => {
  console.log("Callback:", result);
});



// 5. Callback Hell
setTimeout(() => {
  console.log("Step 1");
  setTimeout(() => {
    console.log("Step 2");
    setTimeout(() => {
      console.log("Step 3");
    }, 500);
  }, 500);
}, 500);



// 6. Promises
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const success = true;
    if (success) resolve("Promise success");
    else reject("Promise failed");
  }, 1000);
});

myPromise
  .then((res) => console.log(res))
  .catch((err) => console.log(err));



// 7. Async / Await
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function runAsync() {
  console.log("Async start");
  await delay(1000);
  console.log("After 1s");
  await delay(1000);
  console.log("After 2s");
}

runAsync();



