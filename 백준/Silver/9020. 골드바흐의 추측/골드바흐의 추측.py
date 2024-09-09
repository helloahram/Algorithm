def estostenes(num):
    isPrime = [True] * (num+1)

    isPrime[0] = isPrime[1] = False
    for i in range(2, int(num**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, num+1, i):
                isPrime[j] = False
    # isPrime 반환 
    return isPrime

def goldenbach(n, isPrime):
    # 가장 가까운 소수들의 합을 구하는 것이니 n//2 부터 1 까지 
    # isPrime[i] 과 isPrime[n-i] 이 소수인지 확인 
    for i in range(n//2, 1, -1):
        if isPrime[i] and isPrime[n-i]:
            return i, n-i
    return None

# 에라토스테네스의 체를 사용하여 10000 까지 소수 여부 판별해놓기 
isPrime = estostenes(10000)

# Test Case 개수 입력 받기 
T = int(input())

# Test Case 개수만큼 n 을 입력 받고 각 n 에 대한 골든바흐 파티션 구하기

# 골든바흐 파티션 결과를 저장할 배열 선언 
result = []

for _ in range(T):
    n = int(input())
    a, b = goldenbach(n, isPrime)
    result.append(f"{a} {b}")

print('\n'.join(result))
    