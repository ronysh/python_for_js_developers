const literalSoup = {
  vegies: ["tomatoes", "onions", "carrots", "brocholi"],
  coock () {
      setTimeout(() => {
        console.log("literally ready");
      }, 1000);
  }
};

function SoupConstructor() {
  this.vegies = ["tomatoes", "onions", "carrots", "brocholi"];
  this.coock = function() {
        setTimeout(() => {
        console.log("constructed ready");
      }, 2000);
  };
};

class SoupClass {
  constructor() {
    this.vegies = ["tomatoes", "onions", "carrots", "brocholi"];
  }
  coock () {
    setTimeout(() => {
        console.log("classy ready");
    }, 3000);
  } 
}

new SoupConstructor().coock();
new SoupClass().coock();
literalSoup.coock();