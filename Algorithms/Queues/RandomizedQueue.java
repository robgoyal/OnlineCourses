
import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {

    private Item[] queue;
    private int size;

    public RandomizedQueue() {
        queue = (Item[]) new Object[2];
        size = 0;
    }

    private void resize(int capacity) {
        Item[] temp = (Item[]) new Object[capacity];

        for (int i = 0; i < size; i++) {
            temp[i] = queue[i];
        }

        queue = temp;
    }

    public boolean isEmpty() {
        return (size == 0);
    }

    public int size() {
        return size;
    }

    public void enqueue(Item item) {
        if (item == null) throw new java.lang.NullPointerException();

        if (size == queue.length) {
            resize(queue.length * 2);
        }

        queue[size] = item;
        size++;
    }

    public Item dequeue() {
        if (isEmpty()) throw new java.util.NoSuchElementException();

        int index = StdRandom.uniform(size);
        Item item = queue[index];

        for (int i = index; i <= size - 2; i++) {
            queue[i] = queue[i + 1];
        }

        size--;

        if (size > 0 && size == queue.length/4) {
            resize(queue.length/2);
        }

        return item;

    }

    public Item sample() {
        if (isEmpty()) throw new java.util.NoSuchElementException();
        int index = StdRandom.uniform(size);

        return queue[index];
    }

    public Iterator<Item> iterator() {
        return new RandomizedQueueIterator();
    }

    private class RandomizedQueueIterator implements Iterator<Item> {
        private int iter;

        private Item[] iteratorArray =  (Item[]) new Object[size];

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