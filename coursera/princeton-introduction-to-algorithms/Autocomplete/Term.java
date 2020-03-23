/* Name: Term.java
   Author: Robin Goyal
   Last-Modified: June 13, 2017
   Purpose: A class representing autocompleting a term
*/

import java.util.Comparator;

public class Term implements Comparable<Term> {

    private final String query;
    private final long weight;

    // Initialized a term with the given query string and weight
    public Term(String query, long weight) {

        // Check for errors
        if (query == null) {
            throw new java.lang.NullPointerException();
        }

        if (weight < 0) {
            throw new java.lang.IllegalArgumentException();
        }

        // Initialize instance variables
        this.query = query;
        this.weight = weight;
    }

    // Compares the two terms in descending order by weight
    public static Comparator<Term> byReverseWeightOrder = new Comparator<Term>() {
        
        @Override
        public int compare(Term a, Term b) {
            if (a.weight == b.weight) return 0;
            return (a.weight > b.weight) ? -1 : 1;
        }
    };

    // Compares the two terms in lexicographic order but using only the
    // first r characters of each query
    public static class byPrefixOrder implements Comparator<Term> {

        private int r;

        public byPrefixOrder(int r) {
            if (r < 0) throw new IllegalArgumentException();

            this.r = r;
        }

        public int compare(Term a, Term b) {

            // Normal compareTo on queries of size less than r
            if (a.query.length() <= r && b.query.length() <= r) {
                return a.query.compareTo(b.query);
            }

            // One query is greater than other
            else if (a.query.length() > r && b.query.length() <= r) {
                return a.query.substring(0, r).compareTo(b.query);
            }

            else if (a.query.length() <= r && b.query.length() > r) {
                return a.query.compareTo(b.query.substring(0, r));
            }

            // Both queries are greater than r
            else {
                return a.query.substring(0, r).compareTo(b.query.substring(0, r));
            }
        }
    }

    // Compares the two terms in lexicographic order by query
    @Override
    public int compareTo(Term that) {
        return this.query.compareTo(that.query);
    }

    // Returns a string representation of this term in the following
    // format: the weight, followed by a tab, followed by the query
    public String toString() {
        return this.weight + "\t" + this.query;
    }

}