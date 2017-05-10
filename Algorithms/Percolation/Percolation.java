/* Name: Percolation.java
   Author: Robin Goyal
   Last Modified: May 10, 2017
   Purpose: Open sites and determine if a NxN grid percolates (a path 
            from top node to bottom node exists)
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

        // Set grid sites to blocked sites
        for (int i = 1; i <= gridSize; i++) {
            site[i] = false;
        }

        // Set virtual top and virtual bottom sites to open site
        site[0] = true;
        site[gridSize + 1] = true;
    }

    // check if row or col arguments are within grid size
    private void checkBounds(int row, int col) {
        if (row <= 0 || row > width) {
            throw new IndexOutOfBoundsException("Row index i out of bounds");
        }

        if (col <= 0 || col > width) {
            throw new IndexOutOfBoundsException("Col index j out of bounds");
        }
    }

    // return one-dimensional array index with two-dimensional array arguments
    private int xyTo1D(int i, int j) {
        int gridIndex = (i * width) - (width - j);
        return gridIndex;

    }

    // open site (row, col) if it is not opened already
    public void open(int row, int col) {
        checkBounds(row, col);
        int index = xyTo1D(row, col);

        if (site[index]) {
            return;
        }

        else {
            openSite(row, col, index);
            site[index] = true;
        }
    }

    // open surrounding sites (at most 4 union calls for a site)
    private void openSite(int row, int col, int index) {
        
        // join top index
        if (row == 1) {
            // connect to virtual top
            grid.union(0, index);
        }

        else if (isOpen(row-1, col)) {
            grid.union(index - width, index);
        }

        // join bottom index
        if (row == width) {
            // connect to virtual bottom
            grid.union(gridSize + 1, index);
        }

        else if (isOpen(row+1, col)) {
            grid.union(index + width, index);
        }

        // join left index
        if (col != 1 && isOpen(row, col - 1)) {
            grid.union(index - 1, index);
        }

        // join right index
        if (col != width && isOpen(row, col + 1)) {
            grid.union(index + 1, index);
        }
    }


    // return if a site is open
    public boolean isOpen(int row, int col) {
        checkBounds(row, col);
        int index = xyTo1D(row, col);

        return site[index];
    }

    // return if a site is full
    public boolean isFull(int row, int col) {
        checkBounds(row, col);
        int index = xyTo1D(row, col);

        // Check if site is connected to virtual top site
        return grid.connected(0, index);
    }

    // return the number of open sites
    public int numberOfOpenSites() {
        int openSites = 0;
        for (int i = 1; i <= gridSize; i++) {
            if (site[i]) {
                openSites++;
            }
        }
        return openSites;
    }

    // Check if virtual top and virtual bottom are connected
    public boolean percolates() {
        return grid.connected(0, gridSize + 1);
    }

    // Test client
/*    public static void main(String[] args) {
        Percolation test = new Percolation(4);
        test.open(1, 2);
        test.open(2, 2);
        test.open(2, 3);
        test.open(3, 3);
        System.out.println(test.numberOfOpenSites());
        boolean c = test.isFull(2, 3);
        System.out.println("Result: " + c);
    }*/
}