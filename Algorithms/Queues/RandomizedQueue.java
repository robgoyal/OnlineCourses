/* Name: RandomizedQueue.java
   Author: Robin Goyal
   Last-Modified: May 31, 2017
   Purpose: Implement a queue that enqueues elements and 
            dequeues elements randomly from an array
*/

import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {

    // Instance variables
    private Item[] queue;
    private int size;

    // Construct an queue of size 2
    public RandomizedQueue() {
        queue = (Item[]) new Object[2];
        size = 0;
    }

    // Resize array with size capacity
    private void resize(int capacity) {
        Item[] temp = (Item[]) new Object[capacity];

        for (int i = 0; i < size; i++) {
            temp[i] = queue[i];
        }

        queue = temp;
    }

    // Return true if queue is empty
    public boolean isEmpty() {
        return (size == 0);
    }

    // Return size of array
    public int size() {
        return size;
    }

    // Add item to end of queue
    public void enqueue(Item item) {
        if (item == null) throw new java.lang.NullPointerException();

        // Double array size if max size is reached
        if (size == queue.length) {
            resize(queue.length * 2);
        }

        queue[size] = item;
        size++;
    }

    // Return and remove a random element from queue
    public Item dequeue() {
        if (isEmpty()) throw new java.util.NoSuchElementException();

        int index = StdRandom.uniform(size);
        Item item = queue[index];

        // Shift elements left for removed element
        for (int i = index; i <= size - 2; i++) {
            queue[i] = queue[i + 1];
        }

        size--;

        // Resize array if a 1/4 of array length is used 
        if (size > 0 && size == queue.length/4) {
            resize(queue.length/2);
        }

        return item;

    }

    // Randomly return an element from queue
    public Item sample() {
        if (isEmpty()) throw new java.util.NoSuchElementException();
        int index = StdRandom.uniform(size);

        return queue[index];
    }

    // Returns an iterator over queue items in completely random order
    public Iterator<Item> iterator() {
        return new RandomizedQueueIterator();
    }

    private class RandomizedQueueIterator implements Iterator<Item> {
        private int iter;

        private Item[] iteratorArray =  (Item[]) new Object[size];

        // Copy items from queue to temporary array
        public RandomizedQueueIterator() {
            for (int i = 0; i < size; i++) {
                iteratorArray[i] = queue[i];
            }   

            StdRandom.shuffle(iteratorArray);   
            iter = 0;
        }

        public boolean hasNext() {
            return iter < size;
        }

        public void remove() {
            throw new java.lang.UnsupportedOperationException();
        }

        public Item next() {
            if (isEmpty()) throw new java.util.NoSuchElementException();
            
            return iteratorArray[iter++];
        }
    }

    // Test client
    public static void main(String[] args) {
        RandomizedQueue<Integer> test = new RandomizedQueue<Integer>();

        test.enqueue(5);
        test.enqueue(15);
        test.enqueue(22);

        for (Integer s: test) {
            System.out.println(s);
        }
        test.dequeue();


        for (Integer s: test) {
            System.out.println(s);
        }
    }


}