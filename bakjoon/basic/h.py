# arr = [1, 2, 3, 4]

# for i in arr:
#     print(i)

# a = "Hello"
# b = "Hello"
# print(f"a is b 는 {a is b}") 
# print(f"a == b 는 {a == b}")

# # a = a + " World"
# # print(&a)

# c = ['a', 'b', 'c']
# d = ['a', 'b', 'c']
# print(f"c is d 는 {c is d}")
# print(f"c == d 는 {c == d}")

# a = "Hello"
# print(a.upper())
# print(a)

# def recur(n: int) -> int:
#     if n>0:
#         recur(n-1)
#         print(n)
#         recur(n-2)

# recur(4)

# import itertools

# chars = ['A', 'B', 'C']

# p = itertools.permutations(chars, 2)  # 순열
# c = itertools.combinations(chars, 2)  # 조합

# cr = itertools.combinations_with_replacement(chars, 2)  # 조합
# cp = itertools.product(chars, repeat=2)
# print(list(cp))
# print(list(cr))
# print(list(p))
# print(list(c))

# from typing import Any

# class Queue:
#     # def __init__(self, capacity: int) -> None:
#     #     self.no = 0
#     #     self.front = 0
#     #     self.rear = 0
#     #     self.capacity = capacity
#     #     self.que = [None] * capacity

    
#     def push(x):
#         que.append(x)


def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

if __name__ == '__main__':
    print(fibonacci(10))