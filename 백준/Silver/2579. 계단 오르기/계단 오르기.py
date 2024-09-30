# 계단에 쓰여 있는 점수가 주어질 때 점수의 최댓값 구하기

# 1. 한 번에 한 계단 또는 두 계단씩 오를 수 있다
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다
# 3. 마지막 도착 계단은 반드시 밟아야 한다 

# 직전 계단을 밟고 올라온 경우 그 이전 계단은 n-3 번째
# dp[i-3] + stair[i-1] + stair[i]
# 두 칸 전 계단을 밟고 올라온 경우
# dp[i-2] + stair[i]

n = int(input())
stair = [0] * 301 # 계단 점수를 저장하는 배열
dp = [0] * 301 # 누적 최대값을 저장하는 배열 

for i in range(1, n+1):
    stair[i] = int(input()) # 점수 입력 받기 

# 계단이 두 개 밖에 없는 경우 두 개 다 밟아야 하니
# n 이 1 과 2 일 때 기본값 생성 
dp[1] = stair[1] 
if n > 1:
    dp[2] = stair[1] + stair[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

print(dp[n])