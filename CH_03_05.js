const friends = [
  {name: "Graham"}, // use a string for key "name" in Python
  {name: "John"}, 
  {name: "Eric"}, 
  {name: "Terry"}, 
  {name: "Michael"}
]; // extra credit: why did I choose these names ;)

friends.forEach((friend) => {
  if (friend.name.includes("a")) {
    console.log(`Hey ${friend.name}!`);
  }
});

