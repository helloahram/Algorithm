#include <stdio.h>

void find_fraction(int x)
{
    int a, b, n = 0, total = 0;

    while (total < x)
    {
        total += n;
        n++;
    }

    n--;
    total -= n; // 이전대각선

    int k = x - total;

    if (n % 2 != 0)
    {
        a = n - k + 1;
        b = k;
    }
    else
    {
        a = k;
        b = n - k + 1;
    }
    printf("%d/%d\n", a, b);
}

int main()
{
    int x;
    scanf("%d", &x);

    find_fraction(x);

    return 0;
}