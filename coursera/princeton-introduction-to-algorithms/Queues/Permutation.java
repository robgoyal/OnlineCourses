/* Name: Permutation.java
   Author: Robin Goyal
   Last-Modified: May 31, 2017
   Usage: java-algs4 Permutation k
   Purpose: Read k strings from input 
            and randomly output the strings
*/

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
    
// Main client
public class Permutation {
    public static void main(String[] args) {

        // Check to make sure only a single command line arg
        if (args.length != 1) {
            throw new IllegalArgumentException();
        }

        // Create a randomized queue data structure
        RandomizedQueue<String> permutation = new RandomizedQueue<String>();

        // Read in k strings
        for (int i = 0; i < Integer.parseInt(args[0]); i++) {
            test.enqueue(StdIn.readString());
        }

        // Randomly print strings
        for (String s: test) {
            StdOut.println(s);
        }
    }
}