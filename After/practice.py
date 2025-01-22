import math
from functools import reduce

n = int(input())
m = [int(input()) for _ in range(n)]

distances = [m[i+1] - m[i] for i in range(n-1)]

gcd = reduce(math.gcd, distances)

trees_to_add = sum((dist//gcd-1) for dist in distances)

print(trees_to_add)