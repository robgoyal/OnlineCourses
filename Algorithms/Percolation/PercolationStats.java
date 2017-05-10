import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.StdOut;

public class PercolationStats {

    // Instance variables
    private int size;
    private int experiments;

    // holds percolation threshold for each exeriment
    private double[] results;

    // Performs trials number of experiments independent experiments on nxn grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new java.lang.IllegalArgumentException();
        }

        size = n;
        experiments = trials;
        results = new double[experiments];

        for (int i = 0; i < experiments; i++) {
            results[i] = percolationThreshold();
        }
    }

    // Sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(results);
    }

    // Sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(results);
    }

    // Low endpoint of 95% confidence interval
    public double confidenceLo() {
        return (mean() - (1.96 * stddev())/Math.sqrt(experiments));
    }

    // High endpoint of 95% confidence interval 
    public double confidenceHi() {
        return (mean() + (1.96 * stddev())/Math.sqrt(experiments));
    }

    private double percolationThreshold() {
        Percolation trial = new Percolation(size);
        int row, col;

        while (!(trial.percolates())) {
            row = StdRandom.uniform(1, size + 1);
            col = StdRandom.uniform(1, size + 1);
            trial.open(row, col);
        }

        return trial.numberOfOpenSites()/(Math.pow(size, 2));
    }

    // Main test client
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int t = Integer.parseInt(args[0]);

        PercolationStats test = new PercolationStats(n, t);
        double trialMean = test.mean();
        double trialStdDev = test.stddev();
        double trialConfidenceLo = test.confidenceLo();
        double trialConfidenceHi = test.confidenceHi();

        StdOut.println("mean =  " + trialMean);
        StdOut.println("stddev = " + trialStdDev);
        StdOut.println("95% confidence interval = [" + trialConfidenceLo + ", " + 
                       trialConfidenceHi + "]");
    }
}