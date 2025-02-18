# https://www.acmicpc.net/problem/28279

# 정수를 저장하는 덱을 구현한 다음
# 입력으로 주어지는 명령을 처리하는 프로그램 

# 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
# 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
# 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 
#    없다면 -1을 대신 출력한다.
# 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 
#    없다면 -1을 대신 출력한다.
# 5: 덱에 들어있는 정수의 개수를 출력한다.
# 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
# 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 
#    없다면 -1을 대신 출력한다.
# 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 
#    없다면 -1을 대신 출력한다.

# 시간 초과 떴음 

from collections import deque
import sys

queue = deque()

n = int(input())
for _ in range(n):
    c = sys.stdin.readline().split()

    if c[0] == '1':
        queue.appendleft(int(c[1]))
    elif c[0] == '2':
        queue.append(int(c[1]))
    elif c[0] == '3':
        print(queue.popleft() if queue else -1)
    elif c[0] == '4':
        print(queue.pop() if queue else -1)
    elif c[0] == '5':
        print(len(queue))
    elif c[0] == '6':
        print(0 if queue else 1)
    elif c[0] == '7':
        print(queue[0] if queue else -1)
    elif c[0] == '8':
        print(queue[-1] if queue else -1)