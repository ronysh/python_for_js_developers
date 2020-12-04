const addNumbers = (a, b) => {
    const result = a + b; // demonstrating scope
    return result;
}

function sayHi(name) {
    const greeting = `Hey ${name}`;
    return greeting;
}


console.log(addNumbers(1, 2))
