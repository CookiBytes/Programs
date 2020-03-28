let a = "red";
let b = "blue";

// Solution A
a = "blue";
b = "red";

// Solution B
let c = a;
a = b;
b = c;

console.log(a);
console.log(b);
