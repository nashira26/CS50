#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all pixels to greyscale
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        if (width % 2 == 0)
        {
            for (int j = 0; j < width / 2; j++)
            {
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - j - 1];
                image[i][width - j - 1] = temp[i][j];
            }
        }
        else
        {
            for (int j = 0; j < width / 2; j++)
            {
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - j - 1];
                image[i][width - j - 1] = temp[i][j];
            }
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sumRed = 0;
            float sumGreen = 0;
            float sumBlue = 0;
            float count = 0;

            for (int a = i-1; a < i+2; a++)
            {
                for (int b = j-1; b < j+2; b++)
                {
                    if (a < 0 || a > height - 1 || b < 0 || b > width - 1)
                    {
                        continue;
                    }
                    else
                    {
                        sumRed += image[a][b].rgbtRed;
                        sumGreen += image[a][b].rgbtGreen;
                        sumBlue += image[a][b].rgbtBlue;
                        count++;
                    }
                }
            }
            copy[i][j].rgbtRed = round(sumRed / count);
            copy[i][j].rgbtBlue = round(sumBlue / count);
            copy[i][j].rgbtGreen = round(sumGreen / count);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
        }
    }
    return;
}

