# https://www.acmicpc.net/problem/19532

# ax + by = c, dx + ey = f
# 연립방정식의 해를 구하는 문제 

# b 와 e 의 최소공배수를 구해서 y 값을 구하고 
# 그 값을 이용해서 x 값을 구하면 되지 않을까?
# 이거보다는 크래머의 규칙이나 가우스 소거법이 효율적이라고 한다 

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            exit()

# 가우스소거법 틀렸다고 해서 다른 방법을 찾아봤다 
####################### 가우스소거법 

# 첫번째 열 기준으로 두번째 행 조작 
# x 없애서 y 구하기 
# if a != 0: 
#     scale = d / a
#     d -= scale * a
#     e -= scale * b 
#     f -= scale * c

# if e != 0:
#     y = f / e
# else:
#     y = 0

# x = (c - b * y) / a

# print(int(x), int(y))

####################### 아래는 크래머의 공식
# denominator = (a * e) - (b * d)
# x = (c * e - b * f) // denominator
# y = (a * f - c * d) // denominator

# print(x, y) 