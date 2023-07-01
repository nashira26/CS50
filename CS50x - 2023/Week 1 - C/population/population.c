#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // start size n
    int n;
    do
    {
        n = get_int("Start size: ");
    }
    while (n < 9);

    // end size m
    int m;
    do
    {
        m = get_int("End size: ");
    }
    while (m < n);

    // TODO: Calculate number of years until we reach threshold
    int count = 0;
    int pop = n;
    while (pop < m)
    {
        count++;
        pop = pop + (pop / 3) -(pop / 4);

    }
    // TODO: Print number of years
    printf("Years: %i\n", count);
}
