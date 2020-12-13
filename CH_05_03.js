const friends = [
    {name: "Graham"},
    {name: "John"}, 
    {name: "Terry"}, 
    {name: "Eric"}, 
    {name: "Michael"}
  ];
  
const nameStrings = friends.map(friend => friend.name);
const namesWithH = nameStrings.filter(name => name.includes("h"));

console.log("=====nameStrings=====");
console.log(nameStrings);

console.log("=====namesWithH=====");
console.log(namesWithH);
