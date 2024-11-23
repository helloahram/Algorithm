# https://www.acmicpc.net/problem/2231

# 자연수 N 의 분해합은 N 과 N 을 이루는 각 자리수의 합을 의미한다 
# 어떤 자연수 M 의 분해합이 N 인 경우, M 을 N 의 생성자라 한다 
# 자연수 N 이 주어졌을 때, N 의 가장 작은 생성자를 구해내는 프로그램을 작성하시오 
# 생성자가 없는 경우에는 0 을 출력한다 

# 백의자리 + 십의자리 + 일의자리 + 원래숫자 = n 인 조합을 찾기 
# 반복문을 어디서부터 어디까지 돌려야할까? -> n - (자리수 * 9) 부터 n 까지
# 각 자리 수의 최대값이 9니까 자리수 * 9 만큼 빼 준 값에서 시작하면 된다 

n = int(input())

# n 이 작은 수일 수 있으니 max 로 1 과 n - (자리수 * 9) 와 비교 
start = max(1, n - len(str(n)) * 9)

for m in range(start, n):
    # str 으로 m 을 문자열로 변환하고, 
    # map 으로 str 이 된 m 의 각 문자를 int 로 변환한다 
    digit_m = m + sum(map(int, str(m)))

    if n == digit_m:
        print(m)
        break

# 생성자가 없다면 0 출력 
else:
    print(0)


# a = n // 100 # 백의 자리
# b = (n % 100) // 10 # 십의 자리
# c = n % 10 # 일의 자리 

