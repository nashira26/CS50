#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

bool only_digits(string k);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    //error message if there's not a single input for the key
    if (argc != 2)
    {
        printf("Usage: ./ceasar key\n");
        return 1;
    }
    //error message if the input k is not an intger value
    else if (only_digits(argv[1]) == 0)
    {
        printf("Usage: ./ceasar key\n");
        return 1;
    }
    //proceeding with a valid key value
    else
    {
        //key value transformed to integer and saved in betwee the range
        int k = atoi(argv[1]);
        if (k > 26)
        {
            k = k % 26;
        }
        //plaintext taken as input
        string plaintext = get_string("plaintext:  ");

        //ciphertext printed out by iterating through each character rotating.
        printf("ciphertext: ");
        for (int i = 0; i < strlen(plaintext); i++)
        {
            printf("%c", rotate(plaintext[i], k));
        }

        printf("\n");
        return 0;
    }
    return 0;
}
//fuunction to check if a string is only digits
bool only_digits(string k)
{
    int j = strlen(k);
    for (int i = 0; i < j; i++)
    {
        if (!isdigit(k[i]))
        {
            return 0;
        }
    }
    return 1;
}
//function to decrypt to cipher language
char rotate(char c, int k)
{
    if (c >= 65 && c <= 90)
    {
        c = (((c - 65) + k) % 26) + 65;
        return c;
    }
    else if (c >= 97 && c <= 122)
    {
        c = (((c - 97) + k) % 26) + 97;
        return c;
    }
    else
    {
        return c;
    }
}

