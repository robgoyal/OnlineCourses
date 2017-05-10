/* Name: Percolation.java
   Author: Robin Goyal
   Last Modified: May 10, 2017
   Purpose: Determine if a NxN grid percolates (a path from top node
            to bottom node)
*/
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    // Create instance variables
    private WeightedQuickUnionUF grid;
    private boolean[] site;
    private int gridSize, width;

    // create NxN grid with all sites blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new java.lang.IllegalArgumentException();
        }

        // Initialize instance variables
        gridSize = n * n;
        width = n;

        grid = new WeightedQuickUnionUF(n*n + 2);
        site = new boolean[n*n + 2];

        // Set grid sites to false
        for (int i = 1; i <= gridSize; i++) {
            site[i] = false;
        }

        // Set virtual top and virtual bottom sites to true
        site[0] = true;
        site[gridSize + 1] = true;
    }

    // Check if row or col arguments are within grid size
    private void checkBounds(int row, int col) {
        if (row <= 0 || row > width) {
            throw new IndexOutOfBoundsException("Row index i out of bounds");
        }

        if (col <= 0 || col > width) {
            throw new IndexOutOfBoundsException("Col index j out of bounds");
        }
    }

    // Open site (row, col) if it is not opened already
    public void open(int row, int col) {

    }

    // Is site (row, col) open?
    public boolean isOpen(int row, int col) {

    }

    public boolean isFull(int row, int col) {

    }

    public int numberOfOpenSites() {

    }


    public boolean percolates() {

    }
}