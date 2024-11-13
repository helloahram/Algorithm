#include <stdio.h>
#include <stdlib.h>

int main()
{
    char **word = (char **)malloc(sizeof(char *) * 5);
    int i, j;
    for (i = 0; i < 5; i++)
    {
        word[i] = (char *)malloc(sizeof(char) * 16);
    }

    for (i = 0; i < 5; i++)
    {
        scanf("%s", word[i]);
    }

    for (j = 0; j < 16; j++)
    {
        for (i = 0; i < 5; i++)
        {
            if (word[i][j] != 0)
                printf("%c", word[i][j]);
            else
                printf("");
        }
    }
    for (i = 0; i < 5; i++)
        free(word[i]);
    free(word);
    return 0;
}