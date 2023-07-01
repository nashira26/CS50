#include <cs50.h>
#include <stdio.h>
#include <math.h>

//declaring functions to count letters, words and sentences
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: "); //get user input and print the first output

    //calculate grade using the count of letters, words and sentences
    float L = (count_letters(text) / (float) count_words(text)) * 100;
    float S = (count_sentences(text) / (float) count_words(text)) * 100;

    float index = (0.0588 * L) - (0.296 * S) - 15.8;
    int grade = round(index);

    //printing final output as per the grade specifications
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

//declaring functions to count letters
int count_letters(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        //letters are differntiated by their ascii values
        if ((text[i] > 64 && text[i] < 91) || (text[i] > 96 && text[i] < 123) )
        {
            count++;
        }
    }
    return count;
}

//declaring function to count words
int count_words(string text)
{
    int count = 1;
    for (int i = 0; text[i] != '\0'; i++)
    {
        //letters are differntiated by the presence of a soace
        if (text[i] == 32)
        {
            count++;
        }
    }
    return count;
}

//declaring function to count sentences
int count_sentences(string text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        //letters are differntiated by the ascii values of symbols
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            count++;
        }
    }
    return count;
}

