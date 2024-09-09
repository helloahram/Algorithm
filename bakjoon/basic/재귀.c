#include <stdio.h>

int facorial(int n)
{
    if (n == 1)
    {
        return 1;
    }
    return n * facorial(n - 1);
}

int main()
{
    int num;
    printf(" Enter the number ; ");
    scanf("%d", &num);

    if (num < 1)
    {
        printf(" Greater than or equal to 1 ");
    }
    else
    {
        printf(" Facorial of %d is %d \n", num, facorial(num));
    }
}
