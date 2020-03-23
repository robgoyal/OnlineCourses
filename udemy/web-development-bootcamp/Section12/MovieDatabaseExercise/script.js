/* Name: script.js
   Author: Robin Goyal
   Last-Modified: March 9, 2018
   Purpose: Implement a movie database
*/

// Movie objects with each movie containing a
// title, rating and hasWatched properties
var movies = [
    {
        title: "Harry Potter",
        rating: 4.5,
        hasWatched: true
    },
    {
        title: "The Godfather Part II",
        rating: 5,
        hasWatched: false
    }
];

// Print out contents of movies
movies.forEach(function(movie) {
    var str = "You have ";
    if (movie.hasWatched) {
        str += "watched ";
    }
    else {
        str += "not seen ";
    }

    str += "\"" + movie.title + "\" - " + movie.rating + " stars";

    console.log(str);
});
