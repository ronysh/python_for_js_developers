const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Pick any number:", function (num) {
  if (num < 0) {
    console.log("Don't be so negative...");
  } else if (num < 10) {
    console.log("Between 0-10. Fair enough.");
  } else if (num < 1000001) {
    console.log("Good attitude.");
  } else {
    console.log("Don't be greedy.");
  }
  process.exit(0);
});
