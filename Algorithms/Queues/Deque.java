/* Name: Deque.java
   Author: Robin Goyal
   Last-Modified: May 18, 2017
   Purpose: Implement a double ended queue
            using a linked list
*/

import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Deque<Item> implements Iterable<Item> {

    // Instance variables
    private Node first;
    private Node last;
    private int size;

    // Node class
    private class Node {
        Item item;
        Node next;
    }

    // Construct an empty deque 
    public Deque() {
        size = 0;
        last = first;
    }

    // Returns if the deque is empty
    public boolean isEmpty() {

        return (size == 0);
    }

    // Returns the number of items on the deque
    public int size() {

        return size;
    }

    // Adds an item to the front
    public void addFirst(Item item) {
        if (item == null) throw new java.lang.NullPointerException();

        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;

        if (isEmpty()) {
            last = first;
        }
        size++;
    }

    // Adds an item to the end
    public void addLast(Item item) {
        if (item == null) throw new java.lang.NullPointerException();

        Node oldlast = last;
        last = new Node();
        last.item = item;
        oldlast.next = last;

        if (isEmpty()) {
            first = last;
        }
        size++;
    }

    // Removes and returns the item at the front
    public Item removeFirst() {
        if (isEmpty()) throw new java.util.NoSuchElementException();

        Item item = first.item;
        first = first.next;
        size--;

        return item;
    }

    // Removes and returns the item at the end
    public Item removeLast() {
        if (isEmpty()) throw new java.util.NoSuchElementException();

        Item item = last.item;
        size--;
        return item;
    }

    // Returns an iterator over items in order from front to end
    public Iterator<Item> iterator() {
        return new DequeIterator();
    }

    private class DequeIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public void remove() {
            throw new java.lang.UnsupportedOperationException();
        }

        public Item next() {
            if (isEmpty()) throw new java.util.NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String args[]) {
        Deque<Integer> test = new Deque<Integer>();
        for (int i = 0; i <= 25; i++) {
            test.addFirst(i);
        }

        for (int i = 0; i <= 25; i++) {
            System.out.println(test.removeFirst());
        }
    }
}