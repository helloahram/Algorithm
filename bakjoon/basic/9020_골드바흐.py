# Test Case 개수 T 짝수 n 소수 a, b

# 소수 배열 만들기
# 에라토스테네스의 체 
def eratosthenes(num):
    isPrime = [True] * (num+1)
    
    if num < 2: return False
    for i in range(2, int(num**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, num+1, i):
                isPrime[j] = False
    return isPrime

# 골드바흐 파티션 만들기 
# 차이가 가장 작은 것을 확인하기 위해 n//2 부터 시작함 
def goldbach(n, isPrime):
    for i in range(n//2, 1, -1):
        if isPrime[i] and isPrime[n-i]:
            return i, n-i

# 소수를 미리 구해놓기 
limit = 10000
isPrime = eratosthenes(10000)

T = int(input())
for _ in range(T):
    n = int(input())
    a, b = goldbach(n, isPrime)
    print(a, b)
