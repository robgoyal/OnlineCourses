/* Name: script.js
   Author: Robin Goyal
   Last-Modified: March 1, 2018
   Purpose: Solve while loop exercises
*/

var initial;

// Print all numbers between -10 and 19
initial = -10;

while (initial <= 19) {
    console.log(initial);
    initial++;
}

// Print all even numbers between 10 and 40
initial = 10;

while (initial <= 40) {
    if (initial % 2 == 0) {
        console.log(initial);
    }

    initial++;
}

// Print all odd numbers between 300 and 333
initial = 300;

while (initial <= 333) {
    if (initial % 2 == 1) {
        console.log(initial);
    }

    initial++;
}

// Print all numbers divisible by 5 and 3 between 5 and 50
initial = 5;

while (initial <= 50) {
    if (initial % 15 == 0) {
        console.log(initial);
    }

    initial++;
}
