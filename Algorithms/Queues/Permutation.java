
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Permutation {
    public static void main(String[] args) {

        if (args.length != 1) {
            throw new IllegalArgumentException();
        }

        RandomizedQueue<String> test = new RandomizedQueue<String>();

        for (int i = 0; i < Integer.parseInt(args[0]); i++) {
            test.enqueue(StdIn.readString());
        }

        for (String s: test) {
            StdOut.println(s);
        }
    }
}