/** Name: dictionary.c
    Author: Robin Goyal
    Last-Modified: May 15, 2017
    Purpose: Implements a dictionary's functionality.
 */

#include "dictionary.h"

// Number of words loaded into dictionary
int dict_size = 0;

// Dictionary loaded
bool loaded = false;
/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    // Len of input word to check
    int len = strlen(word);
    
    // len of input word + 1 for null terminator character
    char word_check[len + 1];
    
    // lowercase all input characters
    for (int i = 0; i < len; i++) {
        word_check[i] = tolower(word[i]);
    }
    
    // Append null terminator character
    word_check[len] = '\0';

    // Find index of word to look for
    int index = hash(word_check);
    
    // Set cursor to head of linked list 
    node *cursor = hashtable[index];
    
    // Iterate through linked list till end and check if strings are same at node
    while (cursor != NULL) {
        if (strcasecmp(cursor->word, word) == 0) {
            return true;
        }
        else {
            cursor = cursor -> next;
        }
    }
    // TODO
    return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{   
    // Open dictionary and check if NULL pointer
    FILE *fp = fopen(dictionary, "r");
    if (fp == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        unload();
        return 1;
    }
    
    // Hold word from dictionary
    char word[LENGTH+1];
    
    // Iterate through dictionary strings
    while (fscanf(fp, "%s", word) != EOF) {
        
        // Create new node for word
        node *new_word = malloc(sizeof(node));
        if (new_word == NULL) {
            unload();
            return false;
        }
        
        // Initialize node values
        strcpy(new_word -> word, word);
        new_word -> next = NULL;
        
        // Get hash table index
        int index = hash(word);
        
        // If index in hashtable is empty, set index to new node
        if (hashtable[index] == NULL) {
            hashtable[index] = new_word;
        }
        
        // Set new node's next to current head, set head to new node
        else {
            new_word -> next = hashtable[index];
            hashtable[index] = new_word;
        }
        
        dict_size++;
    }  
    
    // Close file pointer
    fclose(fp);
    loaded = true;
    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    if (loaded) {
        return dict_size;
    }
    
    else {
        return 0;
    }
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{   
    // Iterate through hashtable to free each linkedlist
    for (int i = 0; i <= HASHTABLE_SIZE; i++) {
        
        // Create cursor pointer to point to head of linked list
        node *cursor = hashtable[i];
        
        // Free each node till end of linked list
        while (cursor != NULL) {
            node *temp = cursor;
            cursor = cursor -> next;
            free(temp);
        }
    }
    
    loaded = false;
    return true;
}

// Hashing function provided by user delipity's husband from r/cs50
int hash(const char* needs_hashing) {
    
    unsigned int hash = 0;

    for (int i = 0, n = strlen(needs_hashing); i < n; i++) {
        hash = (hash << 2) ^ needs_hashing[i];
    }
    
    // Moduolo HASHTABLE_SIZE so doesn't go out of bounds
    return hash % HASHTABLE_SIZE;
}