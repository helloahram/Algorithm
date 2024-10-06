def knapsack(items, K):
    dp = [0] * (K + 1)

    # 역순으로 처리해주는 이유는 현재 아이템을 사용할 때, 
    # 이전의 dp배열을 수정하지 않기 위해서이다.
    for weight, value in items:
        for j in range(weight, K+1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[K]

import sys
input = lambda: sys.stdin.readline().strip()

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

print(knapsack(items, K))