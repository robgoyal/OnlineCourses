/* Name: Autocomplete.java
   Author: Robin Goyal
   Last-Modified: June 13, 2017
   Purpose: Perform autocomplete for a given set of strings
            and string weights
*/

import edu.princeton.cs.algs4.*;
import java.util.Arrays;

public class Autocomplete {

    public Term[] terms;
    public Term[] results;

    // Initialized the data structure from the given array of terms
    public Autocomplete(Term[] terms) {

        if (terms == null) {
            throw new java.lang.NullPointerException();
        }

        this.terms = terms;
        Arrays.sort(this.terms);

    }

    // Returns all terms that start with the given prefix,
    // in descending order of weight
    public Term[] allMatches(String prefix) {
        Term temp = new Term(prefix, 0);
        Term.byPrefixOrder comparator = new Term.byPrefixOrder(prefix.length());

        int firstIndex = BinarySearchDeluxe.firstIndexOf(terms, temp, comparator);
        int lastIndex = BinarySearchDeluxe.lastIndexOf(terms, temp, comparator);

        //System.out.println(Arrays.toString(terms));
        //System.out.println(firstIndex + "   " + lastIndex);
        //results = new Term[lastIndex-firstIndex];
        results = Arrays.copyOfRange(terms, firstIndex, lastIndex + 1);

        //System.out.println(Arrays.toString(results));
        Arrays.sort(results, Term.byReverseWeightOrder);
        return results;
        // for (int i = 0; i < results.length; i++) {
        //     results[i] = terms[firstIndex + i];
        // }
    }

    // Returns the number of terms that start with the given prefix
    /*public int numberOfMatches(String prefix) {
        
    }*/

    // Unit Testing
    public static void main(String[] args) {
        String filename = args[0];
        In in = new In(filename);

        int N = in.readInt();
        Term[] terms = new Term[N];

        for (int i = 0; i < N; i++) {
            long weight = in.readLong();
            in.readChar();
            String query = in.readLine();
            terms[i] = new Term(query, weight);
        }

        int k = Integer.parseInt(args[1]);
        Autocomplete autocomplete = new Autocomplete(terms);

        while(StdIn.hasNextLine()) {
            String prefix = StdIn.readLine();
            Term[] results = autocomplete.allMatches(prefix);
            for (int i = 0; i < Math.min(k, results.length); i++) {
                StdOut.println(results[i]);
            }
        }
    }   
}