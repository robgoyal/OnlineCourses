/* Name: Term.java
   Author: Robin Goyal
   Last-Modified: June 13, 2017
   Purpose: A class representing autocompleting a term
*/

public class Term implements Comparable<Term> {

    // Initialized a term with the given query string and weight
    public Term(String query, long weight) {

    }

    // Compares the two terms in descending order by weight
    public static Comparator<Term> byReverseWeightOrder() {

    }

    // Compares the two terms in lexicographic order but using only the
    // first r characters of each query
    public static Comparator<Term> byPrefixOrder(int r) {

    }

    // Compares the two terms in lexicographic order by query
    public int compareTo(Term that) {

    }

    // Returns a string representation of this term in the following
    // format: the weight, followed by a tab, followed by the query
    public String toString() {

    }

    // Unit Testing
    public static void main(String[] args) {

    }

}