# 소수 decimal[] 소수개수 count 

n = int(input())
d = []
count = 0

for i in range(n):
    d.append(int(input()))

def is_prime(x):
    # 1 이하 숫자는 소수 아님
    if x <= 1: 
        return False
    # 2 는 소수 
    if x == 2:
        return True
    # 2 의 배수는 소수 아님
    if x % 2 ==0:
        return False
    # 3 이상부터 제곱근 계산 
    for i in range(3, int(x** 0.5) +1, 2):
        if x % i == 0:
            return False
    return True 

for n in d:
    if is_prime(n):
        count += 1

print(count)