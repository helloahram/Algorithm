# 트리 노드들을 저장할 딕셔너리
tree = {}

# 전위 순회 (Preorder Traversal)
def preorder(node):
    if node != '.':
        print(node, end='')  # 루트 출력
        preorder(tree[node][0])  # 왼쪽 자식 방문
        preorder(tree[node][1])  # 오른쪽 자식 방문

# 중위 순회 (Inorder Traversal)
def inorder(node):
    if node != '.':
        inorder(tree[node][0])  # 왼쪽 자식 방문
        print(node, end='')  # 루트 출력
        inorder(tree[node][1])  # 오른쪽 자식 방문

# 후위 순회 (Postorder Traversal)
def postorder(node):
    if node != '.':
        postorder(tree[node][0])  # 왼쪽 자식 방문
        postorder(tree[node][1])  # 오른쪽 자식 방문
        print(node, end='')  # 루트 출력

# 입력 처리
n = int(input())  # 노드의 개수 입력
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)  # 노드와 그 자식들을 딕셔너리에 저장

# 출력
preorder('A')
print()
inorder('A')
print()
postorder('A')


'''
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self):
        result = [self.value]
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def inorder(self):
        result = []
        if self.left:
            result += self.left.inorder()
        result.append(self.value)
        if self.right:
            result += self.right.inorder()
        return result

    def postorder(self):
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.value)
        return result

# 입력 처리
n = 7
nodes = {}

# 예시 입력
inputs = [
    "A B C",
    "B D E",
    "C . F",
    "D . .",
    "E . .",
    "F . ."
]

for line in inputs:
    root, left, right = line.split()
    # 노드가 처음 생성될 때만 인스턴스를 생성하기 
    if root not in nodes:
        nodes[root] = Node(root)
    # '.' 가 아닌 경우 (자식 노드가 있는 경우)
    # 새로운 노드를 생성하고 자식으로 연결하기 
    if left != '.':
        nodes[left] = Node(left)
        nodes[root].left = nodes[left]
    if right != '.':
        nodes[right] = Node(right)
        nodes[root].right = nodes[right]

# 출력
print(''.join(nodes['A'].preorder()))   # 전위 순회
print(''.join(nodes['A'].inorder()))    # 중위 순회
print(''.join(nodes['A'].postorder()))  # 후위 순회
