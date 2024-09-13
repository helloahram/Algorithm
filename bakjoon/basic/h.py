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

def recur(n: int) -> int:
    if n>0:
        recur(n-1)
        print(n)
        recur(n-2)

recur(4)