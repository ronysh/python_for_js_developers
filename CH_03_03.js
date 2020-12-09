const arr = [1, 2];

let i = 0;

while (i < arr.length) {
  console.log(arr[i] + " from while loop");
  i++;
}

console.log("================");

for (let i = 0; i < arr.length; i++) {
  console.log(arr[i] + " from C-style for loop");
}

console.log("================");

arr.forEach(item => console.log(item + " from forEach"));

console.log("================");

for (const i of arr) {
  console.log(i + " from for/of");
}

console.log("================");
