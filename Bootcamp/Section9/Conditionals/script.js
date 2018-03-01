/* Name: script.js
   Author: Robin Goyal
   Last-Modified: March 1, 2018
   Purpose: Solve conditional exercises
*/

var age = 25;

// Check if age is negative
if (age < 0) {
    console.log("Age cannot be negative");
}

// 21 years old
if (age === 21) {
    console.log("happy 21st birthday!!");
}

// Odd age
if (age % 2 == 1) {
    console.log("Your age is odd!");
}

// Perfect square
if (Number.isInteger(Math.sqrt(age))) {
    console.log("perfect square!");
}
