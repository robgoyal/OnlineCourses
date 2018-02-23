/* Name: dictionary.h
   Author: Robin Goyal and CS50
   Last-Modified: February 22, 2018
   Purpose: Implement a dictionary's functionality
*/

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45
#define HASHTABLE_SIZE 32768

// Node for Linked List
typedef struct _node
{
    // Precondition that no word in dictionary is greater than 45 characters
    char word[LENGTH + 1];
    struct _node* next;
} node;

// Initialize hashtable
static node* hashtable[HASHTABLE_SIZE];
// Prototypes
bool check(const char *word);
bool load(const char *dictionary);
unsigned int size(void);
bool unload(void);
int hash(char *word);

#endif // DICTIONARY_H
