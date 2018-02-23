/* Name: dictionary.c
   Author: Robin Goyal and CS50
   Last-Modified: February 22, 2018
   Purpose: Implement a dictionary's functionality
*/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

#include "dictionary.h"

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Creates variable to copy word
    int n = strlen(word);
    char lower_copy[n + 1];

    // Converts word to lowercase
    for (int i = 0; i < n; i++)
    {
        if (isalpha(word[i]))
        {
            lower_copy[i] = tolower(word[i]);
        }
        else
        {
            lower_copy[i] = word[i];
        }
    }

    // Null terminating character to copy
    lower_copy[n] = '\0';

    // Index for hashing
    int index = hash(lower_copy);

    node *cursor = hashtable[index];

    // Traverse until reaching end of linked list
    while (cursor != NULL)
    {
        // Compare word in node and word to check
        if (strcmp(cursor->word, lower_copy) == 0)
        {
            return true;
        }

        cursor = cursor->next;
    }

    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Open file for reading
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    // Initialize word to store words from dictionary
    char word[LENGTH + 1];

    // Index for hashing
    int index;

    // node
    node *temp_node;

    // Loop until reaching EOF
    while (fscanf(file, "%s", word) != EOF)
    {
        // Create temporary node
        temp_node = malloc(sizeof(node));
        if (temp_node == NULL)
        {
            printf("Could not allocate memory for node.\n");
            unload();
            return false;
        }

        // Initialize fields for node
        strcpy(temp_node->word, word);
        temp_node->next = NULL;

        // Store word at hashed index in hashtable
        index = hash(word);

        // Check if hashtable at index contains no nodes
        if (!hashtable[index])
        {
            hashtable[index] = temp_node;
        }

        // Insert node at front of linked list
        else
        {
            temp_node->next = hashtable[index];
            hashtable[index] = temp_node;
        }
    }

    // Close file
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int word_count = 0;
    node *cursor;

    // Iterate over all linked lists in hashtable
    for (int i = 0; i < HASHTABLE_SIZE; i++)
    {
        cursor = hashtable[i];

        // Increment number of words in linked list
        while (cursor != NULL)
        {
            word_count++;
            cursor = cursor->next;
        }
    }

    return word_count;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // Pointer to traverse through nodes
    node *cursor = NULL;
    node *temp;

    // Iterate over all linked lists in hashtable
    for (int i = 0; i < HASHTABLE_SIZE; i++)
    {
        cursor = hashtable[i];

        // Free all nodes in linked list
        while (cursor != NULL)
        {
            temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}

// Returns index to for a hashed string
// https://www.reddit.com/r/cs50/comments/1x6vc8/pset6_trie_vs_hashtable/
int hash(char *word)
{
    unsigned int count = 0;

    //
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        count = (count << 2) ^ word[i];
    }
    return count % HASHTABLE_SIZE;
}