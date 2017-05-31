/* Name: Deque.java
   Author: Robin Goyal
   Last-Modified: May 31, 2017
   Purpose: Implement a double ended queue
            using a linked list
*/

import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {

    // Instance variables
    private Node first;
    private Node last;
    private int size;

    // Node class
    private class Node {
        private Item item;
        private Node next;
        private Node prev;
    }

    // Construct an empty deque 
    public Deque() {
        size = 0;
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

        if (isEmpty()) {
            first = new Node();
            first.item = item;
            last = first;
        }

        else {
            Node oldFirst = first;
            Node node = new Node();

            node.item = item;
            node.next = oldFirst;
            node.prev = null;
            oldFirst.prev = node;

            first = node;
        }
        size++;
    }

    // Adds an item to the end
    public void addLast(Item item) {
        if (item == null) throw new java.lang.NullPointerException();

        if (isEmpty()) {
            last = new Node();
            last.item = item;
            first = last;
        }

        else {
            Node oldlast = last;
            Node node = new Node();

            node.item = item;
            node.next = null;
            node.prev = oldlast;
            oldlast.next = node;

            last = node;
        }
        size++;
    }

    // Removes and returns the item at the front
    public Item removeFirst() {
        if (isEmpty()) throw new java.util.NoSuchElementException();

        Item item = first.item;
        first = first.next;
        size--;

        if (isEmpty()) {
            last = first;
        }

        else {
            first.prev = null;
        }

        return item;
    }

    // Removes and returns the item at the end
    public Item removeLast() {
        if (isEmpty()) throw new java.util.NoSuchElementException();

        Item item = last.item;
        last = last.prev;

        size--;

        if (isEmpty()) {
            first = last;
        }
        else {
            last.next = null;
        }

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

    public static void main(String[] args) {
        Deque<Integer> test = new Deque<Integer>();
        for (int i = 0; i <= 10; i++) {
            test.addFirst(i + 5);
            test.addLast(i + 15);
        }

        for (int i = 0; i <= 10; i++) {
            test.removeLast();
            test.removeFirst();
        }

        for (Integer s: test) {
            System.out.print(s + " ");
        }
    }
}