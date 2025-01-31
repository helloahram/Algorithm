import sys
import math 

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def find_next_prime(n):
    while not is_prime(n):
        n += 1
    return n

result = []

x = int(input())
for i in range(x):
    n = int(sys.stdin.readline().strip())
    result.append(str(find_next_prime(n)))

sys.stdout.write("\n".join(result)+"\n")
