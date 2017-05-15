/**
 * Declares a dictionary's functionality.
 */

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <ctype.h>

// maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// Max hashtable size
#define HASHTABLE_SIZE 65536

/**
 * Define the node struct for linked lists in hash table
 */
typedef struct node {
    char word[LENGTH + 1];
    struct node *next;
} node;

// Create array of node structures with size HASHTABLE_SIZE
node *hashtable[HASHTABLE_SIZE];

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word);

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary);

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void);

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void);

/**
 * Computes hash table index
 */
int hash(const char* needs_hashtag);

#endif // DICTIONARY_H
