# 최대 K만큼의 무게만을 넣을 수 있는 배낭에
# 무게 Weight와 가치 Value를 가지는 N개의 물건이 있다
# 배낭에 넣을 수 있는 물건들의 가치의 최대값 찾기 

def knapsack(weight, value, k):
    n = len(value)
    # DP 테이블 초기화 
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, k+1):
            # 물건의 무게 w 가 현재 배낭의 무게 weight[i-1] 이하일 경우 
            # 물건을 넣지 않고 그대로 가져가기 dp[i-1][w]
            # 물건을 넣고 남은 배낭 용량에 계산한 값을 더하기 중 큰 값을 선택한다 
            if weight[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][k]

if __name__ == '__main__':
    # 물건 개수와 배낭 무게 입력 받기 
    n, k = map(int, input().split())

    weight = [] 
    value = [] 

    # 각 물건의 무게와 가치 입력 받기 
    for i in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    # n, k = 3, 5
    # weight = [2, 3, 4]
    # value = [3, 4, 5]

    max_value = knapsack(weight, value, k)
    print(max_value)