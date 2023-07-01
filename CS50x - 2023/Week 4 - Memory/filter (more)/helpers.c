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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    int Gx[3][3] ={{-1, 0, 1},{-2, 0, 2},{-1, 0, 1}};
    int Gy[3][3] ={{-1, -2, -1},{0, 0, 0},{1, 2, 1}};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int GxRed = 0;
            int GxGreen = 0;
            int GxBlue = 0;
            int GyRed = 0;
            int GyGreen = 0;
            int GyBlue = 0;

            for (int a = i-1; a < i+2; a++)
            {
                for (int b = j-1; b < j+2; b++)
                {
                    if (a < 0 || a > height - 1 || b < 0 || b > width - 1)
                    {
                        continue;
                    }
                    GxRed += (Gx[a-(i-1)][b-(j-1)] * image[a][b].rgbtRed);
                    GxGreen += (Gx[a-(i-1)][b-(j-1)] * image[a][b].rgbtGreen);
                    GxBlue += (Gx[a-(i-1)][b-(j-1)] * image[a][b].rgbtBlue);
                    GyRed += (Gy[a-(i-1)][b-(j-1)] * image[a][b].rgbtRed);
                    GyGreen += (Gy[a-(i-1)][b-(j-1)] * image[a][b].rgbtGreen);
                    GyBlue += (Gy[a-(i-1)][b-(j-1)] * image[a][b].rgbtBlue);
                }
            }

            int red = round(sqrt(GxRed * GxRed + GyRed * GyRed));
            int blue = round(sqrt(GxBlue * GxBlue + GyBlue * GyBlue));
            int green = round(sqrt(GxGreen * GxGreen + GyGreen * GyGreen));

            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            copy[i][j].rgbtRed = red;
            copy[i][j].rgbtBlue = blue;
            copy[i][j].rgbtGreen = green;
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
