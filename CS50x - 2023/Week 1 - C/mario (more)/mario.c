#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;  //declaring a variable name for the input height
    do
    {
        h = get_int("Height: ");    //assign the input to variable
    }
    while (h < 1 || h > 8);     //acceptable range validation until the right input

    for (int i = 1; i <= h; i++)    //iterate through each new line
    {
        for (int j = 1; j <= h - i; j++)    //iterate in each line creating needed spaces in left
        {
            printf(" ");
        }
        for (int k = 1; k <= i; k++)    //iterate in each line creating # on left
        {
            printf("#");
        }
        printf("  ");   //printing the middle gap
        for (int m = 1; m <= i; m++)    //iterate in each line creating # on right
        {
            printf("#");
        }
        printf("\n");
    }
}