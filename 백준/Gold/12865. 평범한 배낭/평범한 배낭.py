# 최대 K만큼의 무게만을 넣을 수 있는 배낭에
# 무게 Weight와 가치 Value를 가지는 N개의 물건이 있다
# 배낭에 넣을 수 있는 물건들의 가치의 최대값 찾기 

def knapsack(weight, value, k):
    n = len(value) # dp 배열, 반복문에서 간단하게 사용하기 위해 변수 생성 
    # DP 테이블 초기화 
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    # dp[i][w] 는 i번째 물건까지 고려 && 남은 용량 w 일 때의 최대 가치
    # weight, value 는 0부터 시작, dp index 는 i-1, w-weight[i-1] 로 계산
    for i in range(1, n+1):
        for w in range(1, k+1):
            # 현재 물건 weight[i-1] 을 배낭에 넣을 수 있을 때 
            # 현재 물건을 넣지 않은 경우 이전 단계 dp[i-1][w] 그대로
            # 물건을 넣었을 때 남은 배낭 용량 + 현재 물건의 가치 
            if weight[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])
            else:
                # 물건을 넣을 수 없으면 그대로 이전 값 
                dp[i][w] = dp[i-1][w]

    return dp[n][k]

if __name__ == '__main__':
    # 물건 개수와 배낭 무게 입력 받기 
    n, k = map(int, input().split())

    weight = [] 
    value = [] 

    # 물건의 무게와 가치 입력 받고 긱 배열에 추가해주기 
    for i in range(n):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)

    # n, k = 4, 7
    # weight = [2, 3, 4, 5]
    # value = [3, 4, 5, 8]

    # 최대 가치 출력 
    max_value = knapsack(weight, value, k)
    print(max_value)