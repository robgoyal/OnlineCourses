/* Name: BinarySearchDeluxe.java
   Author: Robin Goyal
   Last-Modified: June 13, 2017
   Purpose: Perform binary search for key in data
*/
import java.util.Comparator;

public class BinarySearchDeluxe {

    // Testing binary search with an integer comparator
    private static class IntComp implements Comparator<Integer> {
        public int compare(Integer a, Integer b) {
            return a.compareTo(b);
        }
    }


    // Returns the index of the first key in a[] that equals
    // the search key or -1 if no such key
    public static <Key> int firstIndexOf(Key[] a, Key key, Comparator<Key> comparator) {
        checkNull(a, key, comparator);

        int lo = 0;
        int hi = a.length - 1;

        while (hi >= lo) {

            int mid = (hi + lo)/2;

            System.out.println("Low: " + lo + "  High: " + hi);
            if (comparator.compare(key, a[mid]) == 0) {

                if (key == a[mid-1]) {
                    hi = mid - 1;
                }
                else {
                    return mid;
                }
            }

            else if (comparator.compare(key, a[mid]) > 0) {
                lo = mid + 1;
            }


            else if (comparator.compare(key, a[mid]) < 0) {
                hi = mid - 1;
            }
        }

        return -1;

    }

    // Returns the index of the last key in a[] that equals the
    // search key, or -1 if no such key
    public static <Key> int lastIndexOf(Key[] a, Key key, Comparator<Key> comparator) {
        checkNull(a, key, comparator);

        int lo = 0;
        int hi = a.length - 1;

        while (hi >= lo) {

            int mid = (hi + lo)/2;

            System.out.println("Low: " + lo + "  High: " + hi);
            if (comparator.compare(key, a[mid]) == 0) {

                if (key == a[mid+1]) {
                    lo = mid + 1;
                }
                else {
                    return mid;
                }
            }

            else if (comparator.compare(key, a[mid]) > 0) {
                lo = mid + 1;
            }


            else if (comparator.compare(key, a[mid]) < 0) {
                hi = mid - 1;
            }
        }

        return -1;
    }


    // Check if any arguments are null
    private static <Key> void checkNull(Key[] a, Key key, Comparator<Key> comparator) {
        if (a == null || key == null || comparator == null) {
            throw new java.lang.NullPointerException();
        }
    }
    
    // Unit Testing
    public static void main(String[] args) {

        Comparator<Integer> intComp = new IntComp();

        String[] arr = {"Robin", "Vanessa", }
        BinarySearchDeluxe test = new BinarySearchDeluxe();


        System.out.println(test.lastIndexOf(arr, 30, intComp));
    }
}