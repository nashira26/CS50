#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage:  ./recover IMAGE");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    //buffer to store each jpg block of element
    BYTE buffer[512];

    //counter to count the number of images
    int count = 0;

    //string to store jpg filename
    char filename[8];

    //saving jpg in a file
    FILE *img = NULL;


    //Read 512 bytes into a buffer
    while (fread(buffer, sizeof(BYTE), 512, file) == 512)
    {
        //if start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            if (img != NULL)
            {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg", count);
            img = fopen(filename, "w");
            fwrite(&buffer, sizeof(BYTE), 512, img);
            count++;
        }
        //if already found jpeg
        else if (img != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, img);
        }
    }
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(file);

    return 0;
}