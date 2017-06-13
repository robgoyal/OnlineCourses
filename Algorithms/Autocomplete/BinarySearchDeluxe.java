/* Name: BinarySearchDeluxe.java
   Author: Robin Goyal
   Last-Modified: June 13, 2017
   Purpose: Perform binary search for key in data
*/
import java.util.Comparator;
import java.util.Arrays;

public class BinarySearchDeluxe {

    // Returns the index of the first key in a[] that equals
    // the search key or -1 if no such key
    public static <Key> int firstIndexOf(Key[] a, Key key, Comparator<Key> comparator) {
        checkNull(a, key, comparator);

        // Initialize low and high endpoints
        int lo = 0;
        int hi = a.length - 1;

        // Loop until endpoints cross
        while (hi >= lo) {

            // Calculate midpoint
            int mid = (hi + lo)/2;

            // Check if first element in array matches key
            if (comparator.compare(a[0], key) == 0) return 0;

            // Check if mid element matches with prefix
            if (comparator.compare(key, a[mid]) == 0) {

                // Continue searching for first element matching with prefix
                if (comparator.compare(key, a[mid-1]) == 0) {
                    hi = mid - 1;
                }  

                // Return first occurrence of match
                else {
                    return mid;
                }
            }

            // Look through second half
            else if (comparator.compare(key, a[mid]) > 0) {
                lo = mid + 1;
            }

            // Search through first half 
            else if (comparator.compare(key, a[mid]) < 0) {
                hi = mid - 1;
            }
        }

        // Return -1 if no match found
        return -1;

    }

    // Returns the index of the last key in a[] that equals the
    // search key, or -1 if no such key
    public static <Key> int lastIndexOf(Key[] a, Key key, Comparator<Key> comparator) {
        checkNull(a, key, comparator);

        // Initialize low and high endpoints
        int lo = 0;
        int hi = a.length - 1;

        // Loop until endpoints cross
        while (hi >= lo) {

            // Calculate midpoint
            int mid = (hi + lo)/2;

            // Check if first element in array matches key
            if (comparator.compare(a[0], key) == 0) return 0;

            // Check if mid element matches with prefix
            if (comparator.compare(key, a[mid]) == 0) {

                // Continue searching for last element matching with prefix
                if (comparator.compare(key, a[mid+1]) == 0) {
                    lo = mid + 1;
                }  

                // Return last occurrence of match
                else {
                    return mid;
                }
            }

            // Look through second half
            else if (comparator.compare(key, a[mid]) > 0) {
                lo = mid + 1;
            }

            // Search through first half 
            else if (comparator.compare(key, a[mid]) < 0) {
                hi = mid - 1;
            }
        }

        // Return -1 if no match found
        return -1;
    }


    // Check if any argument is null
    private static <Key> void checkNull(Key[] a, Key key, Comparator<Key> comparator) {
        if (a == null || key == null || comparator == null) {
            throw new java.lang.NullPointerException();
        }
    }
}