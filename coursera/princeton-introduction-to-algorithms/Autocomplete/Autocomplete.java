/* Name: Autocomplete.java
   Author: Robin Goyal
   Last-Modified: June 13, 2017
   Purpose: Perform autocomplete for a given set of strings
            and string weights
*/

import edu.princeton.cs.algs4.*;
import java.util.Arrays;

public class Autocomplete {

    // Declare instance variables
    private Term[] terms;
    private Term[] results;

    // Initialized the data structure from the given array of terms
    public Autocomplete(Term[] terms) {

        // Check if reference to array is null
        if (terms == null) {
            throw new java.lang.NullPointerException();
        }

        this.terms = terms;
        Arrays.sort(this.terms);

    }

    // Returns all terms that start with the given prefix,
    // in descending order of weight
    public Term[] allMatches(String prefix) {

        // Create query and comparator
        Term query = new Term(prefix, 0);
        Term.byPrefixOrder comparator = new Term.byPrefixOrder(prefix.length());

        // Calculate first and last indices matching query
        int first = BinarySearchDeluxe.firstIndexOf(terms, query, comparator);
        int last = BinarySearchDeluxe.lastIndexOf(terms, query, comparator);

        // Return empty array if binary search returned nothing
        if (first == -1 || last == -1) return new Term[0];

        // Copy prefix matches to new array
        results = Arrays.copyOfRange(terms, first, last + 1);

        // Sort array by weight in decreasing order
        Arrays.sort(results, Term.byReverseWeightOrder);
        return results;
    }

    // Returns the number of terms that start with the given prefix
    public int numberOfMatches(String prefix) {

        // Create query and comparator
        Term query = new Term(prefix, 0);
        Term.byPrefixOrder comparator = new Term.byPrefixOrder(prefix.length());

        // Calculate first and last indices matching query
        int first = BinarySearchDeluxe.firstIndexOf(terms, query, comparator);
        int last = BinarySearchDeluxe.lastIndexOf(terms, query, comparator);

        // Return 0 if binary search returned nothing
        if (first == -1 || last == -1) return 0;

        // Return number of matches
        return last - first + 1;    
    }

    // Unit Testing
    public static void main(String[] args) {

        // Take filename as input
        String filename = args[0];
        In in = new In(filename);

        // Create terms array of number of elements
        int N = in.readInt();
        Term[] terms = new Term[N];

        // Loop through file and initialize terms
        for (int i = 0; i < N; i++) {
            long weight = in.readLong();
            in.readChar();
            String query = in.readLine();
            terms[i] = new Term(query, weight);
        }

        // Number of matches to look for 
        int k = Integer.parseInt(args[1]);
        Autocomplete autocomplete = new Autocomplete(terms);

        // Take prefix as input and print matches
        while(StdIn.hasNextLine()) {
            String prefix = StdIn.readLine();
            Term[] results = autocomplete.allMatches(prefix);
            for (int i = 0; i < Math.min(k, results.length); i++) {
                StdOut.println(results[i]);
            }
        }
    }   
}