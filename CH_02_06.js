const userName = "Jake";
const credits = 2.2;
const itemsInCart = ["Jeans", "Shoes", "Socks"];

function getFirstItem(user, credits, items) {
  return `first item: ${items[0]} user: ${user} credits left: ${credits}`;
}

console.log(getFirstItem(userName, credits, itemsInCart));
