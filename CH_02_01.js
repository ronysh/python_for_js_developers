const myName = "Ronnie";

function sayHi(name) {
  return `Hi ${name} 👋!`;
}

class Pet {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const mona = new Pet("Mona", 6);

console.log(sayHi(myName));
