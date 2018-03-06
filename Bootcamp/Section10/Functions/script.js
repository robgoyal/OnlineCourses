/* Name: script.js
   Author: Robin Goyal
   Last-Modified: March 3, 2018
   Purpose: Solve function exercises
*/


/* Return True iff a number is even */
function isEven(num) {
    return (num % 2 == 0);
}

/* Return the factorial of a number */
function factorial(num) {
    var total = 1;
    for (var i = num; i > 0; i--) {
        total *= i;
    }

    return total;
}


/* Convert a kebab-cased string argument to
   a snake_cased version */
function kebabToSnake(str) {

    // Replaces all occurrences of -
    return str.replace(/[-]/g, '_');
}
