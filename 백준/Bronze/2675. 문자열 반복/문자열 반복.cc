#include <stdio.h>
#include <string.h>

int main()
{
    // TC 개수 t, 반복 횟수 r, 문자열 s, 새로운 문자열
    int t, r;
    char s[21], result[201][201];
    int index = 0;

    scanf("%d", &t);

    for (int k = 0; k < t; k++)
    {
        scanf("%d %s", &r, s);
        int slength = strlen(s);
        index = 0;

        for (int i = 0; i < slength; i++)
        {
            for (int j = 0; j < r; j++)
            {
                result[k][index++] = s[i];
            }
        }
        result[k][index] = '\0';
    }
    for (int k = 0; k < t; k++)
    {
        printf("%s\n", result[k]);
    }
}