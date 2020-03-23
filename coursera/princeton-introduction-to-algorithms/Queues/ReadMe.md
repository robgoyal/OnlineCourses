## Queues

### Purpose

This assignment wanted us to implement a deque and a randomized queue.

### Procedure

#### Deque

A deque is a double ended queue which allows users to remove and add elements from both the front and the back of the queue. Since the specification was to perform each operation in constant time, I had to create a doubly linked list to hold references to both the front of the queue and back of the queue. The greatest challenge with implementing the deque was properly replacing the references when adding or removing elements. It became of great help to draw out the linked list structure and keep track of pointers to the different nodes. 

#### Randomized Queue

This random queue is a basic queue but chooses to randomly remove an element from the structure. I implemented this using an array and decided to dynamically resize it instead of using a linked list. This data structure also introduced me to iterators and generics. The iterator was to return a iterable object in a random order. Whenever an element was randomly removed from the queue, I shifted all the elements over.

#### Permutation

The Permutation file used the randomized queue data structure to read in standard input and randomly remove k elements (k is a command line argument). 