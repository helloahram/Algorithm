#include <stdio.h>

int main()
{
    int score;
    char grade;
    scanf("%d", &score);

    if (90 <= score && score <= 100)
    {
        grade = 'A';
    }
    else if (80 <= score && score < 90)
    {
        grade = 'B';
    }
    else if (70 <= score && score < 80)
    {
        grade = 'C';
    }
    else if (60 <= score && score < 70)
    {
        grade = 'D';
    }
    else
    {
        grade = 'F';
    }
    printf("%c", grade);
    return 0;
}