# 1번 문제 2579 계단 오르기 

def stair_up(n, stairs):
    # 누적 점수 선언하기 
    dp = [0] * (n+10)

    # 1번 계단과 2번 계단은 다 오를 수 밖에 없다 
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    # 1) 직전 계단을 오른 경우 3개 연속은 안 되니 그 전전 계단을 올랐음
    # 그 전전 계단 dp[n-3], 직전 계단 stairs[n-1], 현재 계단 stairs[n]
    # 2) 직전 계단을 오르지 않고 전전 계단을 오른 경우 
    # 전전 계단 dp[n-2], 현재 계단 stairs[n]
    # 둘 중 값이 더 큰 경우를 dp 배열에 저장 
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    # 누적 점수 반환하기
    return dp[n]


if __name__ == '__main__':
    # 계단 개수를 n 으로 입력 받기
    n = int(input())

    # 계단 점수를 stairs 배열로 선언 및 초기화하고 입력 받기 
    stairs = [0] * (n+10)
    for i in range(1, n+1):
        stairs[i] = int(input())

    # # 아래를 쓰면 0부터 시작이라 for 문 사용 
    # stairs = [list(map(int, input().split())) for _ in range(n)]

    # 결과 구하기 
    print(stair_up(n, stairs))