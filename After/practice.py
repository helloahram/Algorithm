import math
import sys 

def eratosthenes(m):
    n = m*2
    is_prime = [False, False] + [True]*(n+1)

    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    count = 0
    for i in range(m+1, n+1):
        if is_prime[i]:
            count += 1

    return count 

if __name__ == '__main__':
    result = []
    while(True):
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        result.append(str(eratosthenes(n)))
    sys.stdout.write('\n'.join(result)+'\n')