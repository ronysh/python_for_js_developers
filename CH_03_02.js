const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Pick any number:", function (number) {
  if (number < 0) {
    console.log("Don't be so negative...");
  } else if (number < 10) {
    console.log("Between 0-10. Fair enough.");
  } else if (number < 1000001) {
    console.log("Good attitude.");
  } else {
    console.log("Don't be greedy.");
  }
  process.exit(0);
});
