// https://modoocode.com/18#google_vignette
#include <stdio.h>

int main()
{
    int guess = 5;
    int prime[20];
    int i;
    int ok;
    int index = 1;

    prime[0] = 2;
    prime[1] = 3;

    for (;;)
    {
        ok = 0;
        for (i = 0; i <= index; i++)
        {
            if (guess % prime[i] != 0)
            {
                ok++;
            }
            else
            {
                break;
            }
        }
        if (ok == (index + 1))
        {
            index++;
            prime[index] = guess;
            printf(" 소수 %2d ; %d \n", i, prime[index]);
            if (index == 10)
                break;
        }
        guess += 2;
    }
    return 0;
}