/* Name: script.js
   Author: Robin Goyal
   Last-Modified: March 6, 2018
   Purpose: Solve array exercises
*/

/* Print the contents of the array in reverse order */
function printReverse(array) {
    for (var i = array.length - 1; i >= 0; i--) {
        console.log(array[i]);
    }
}

/* Return true if all elements in the array are the same */
function isUniform(array) {
    var firstElem = array[0];

    for (var i = 1; i < array.length; i++) {
        if (array[i] !== firstElem) {
            return false;
        }
    }

    return true;
}

/* Sum all numbers in the array */
function sumArray(array) {
    var total = 0;

    array.forEach(function(number) {
        total += number;
    });

    return total;
}

/* Returns the maximum number in the array */
function max(array) {
    var currentMax = array[0];

    array.forEach(function(number) {
        if (number >= currentMax) {
            currentMax = number;
        }
    });

    return currentMax;
}
