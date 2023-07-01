// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

//count for words in dictionary
int count = 0;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open dictionary file
    FILE *infile = fopen(dictionary, "r");
    if (infile == NULL)
    {
        return false;
    }

    //read strings from file one at a time
    char word[LENGTH+1];
    while (fscanf(infile, "%s", word) != EOF)
    {
        //create new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            free(n);
            return false;
        }
        strcpy(n->word, word);
        n->next = NULL;

        //obtain hash value
        int hash_index = hash(word);

        //insert node into hash table
        node *head = table[hash_index];
        if (head == NULL)
        {
            table[hash_index] = n;
            count++;
        }
        else
        {
            n->next = table[hash_index];
            table[hash_index] = n;
            count++;
        }
    }
    fclose(infile);
    return true;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    //obtain hash value
    int n = strlen(word);
    char word_cpy[n+1];
    for (int i = 0; i < n; i++)
    {
        word_cpy[i] = tolower(word[i]);
    }
    word_cpy[n] = '\0';
    int hash_val = hash(word_cpy);
    node *cursor = table[hash_val];
    //if word is in the dictionary
    while (cursor != NULL)
    {
        if (strcasecmp(word_cpy, cursor->word) == 0)
        {
            return true;
            break;
        }
        else
        {
            cursor = cursor->next;
        }
    }

    //not in dictionary
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *head = table[i];
        node *cursor = head;
        node *temp = cursor;
        //free linked lists
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(temp);
            temp = cursor;
        }
    }
    return true;
}
