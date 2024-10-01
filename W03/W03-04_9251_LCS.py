# LCS Longest Common Subsequence 최장 공통 부분 수열 
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제 

def lcs(A, B):
    m = len(A) # 첫번째 배열 길이 구하기
    n = len(B) # 두번째 배열 길이 구하기 

    # 빈 문자열이 있는 경우 0 리턴 
    if n == 0 or m == 0:
            return 0
    
    # 2차원 DP 배열 초기화 (m+1 x n+1 크기)
    dp = [[0] * (n+1) for _ in range(m+1)]

	# DP 배열 채우기 
    for i in range(1, m+1):
        for j in range(1, n+1):
            # 이미 모든 dp 배열을 0 으로 초기화했으므로
            # 인덱스 에러를 방지하기 위해 i, j == 0 고려하지 않음 
            # if i == 0 or j == 0: # 마진 설정
            #     dp[i][j] = 0 
            
            # dp 는 인덱스 1부터, A B 는 인덱스 0부터 시작하기 때문에
            # A[i-1] 와 B[j-1] 를 비교하여 dp[i][j] 값을 결정 
            if A[i-1] == B[j-1]: # 두 문자가 같을 경우 
                dp[i][j] = dp[i-1][j-1] + 1
            else: # 두 문자가 다를 경우 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n] # 최장 공통 부분 수열 길이 반환 

if __name__ == '__main__':
    A = input().strip()
    B = input().strip()
    
    print(lcs(A, B)) # LCS 길이 출력