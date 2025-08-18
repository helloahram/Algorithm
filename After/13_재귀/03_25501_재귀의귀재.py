# https://www.acmicpc.net/problem/25501

# 팰린드롬은, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열
# 문자열 S 를 isPalindrome 함수의 인자로 전달했을 때
# 팰린드롬 여부인 반환값과 Recursion 함수의 호출 횟수를 계산하는 문제


def isPalindrome(s):
    result = recursion(s, 0, len(s) - 1)
    return result


def recursion(s, l, r, counter=1):
    if l >= r:
        return 1, counter
    elif s[l] != s[r]:
        return 0, counter
    else:
        return recursion(s, l + 1, r - 1, counter + 1)


t = int(input().strip())
for _ in range(t):
    s = input().strip()
    result, cnt = isPalindrome(s)
    print(result, cnt)
