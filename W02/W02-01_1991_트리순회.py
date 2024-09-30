# 이진 트리를 입력 받아, 전위 순회 Preorder, 중위 순회 Inorder,
# 후위 순회 Postorder Traversal 한 결과를 출력하는 프로그램을 작성하시오
# 전위 순회 - 루트 - 왼쪽 자식 - 오른쪽 자식
# 중위 순회 - 왼쪽 자식 - 루트 - 오른쪽 자식
# 후위 순회 - 왼쪽 자식 - 오른쪽 자식 - 루트 

# 이진 트리 노드의 개수 1 <= N <= 26
# 입력 순서는 각 노드와 왼쪽 자식 노드, 오른쪽 자식 노드 순
# 노드 이름은 A 부터 차례대로 알파벳 대문자로 매겨지고
# 항상 A 가 루트 노드, 자식 노드가 없는 경우 . 으로 표현 

class Node:
    def __init__(self, value):
        # 노드 값 저장, Left/ Right 는 초기화
        self.value = value
        self.left = None
        self.right = None

    # Preorder Root L R 
    def preorder(self):
        result = [self.value] # 현재 노드를 먼저 추가 
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    # Inorder L Root R
    def inorder(self):
        result = [] # 결과 리스트를 빈 리스트로 초기화 
        if self.left:
            result += self.left.inorder()
        result.append(self.value) # 현재 노드 추가 
        if self.right:
            result += self.right.inorder()
        return result

    # Postorder L R Root
    def postorder(self):
        result = [] # 결과 리스트를 빈 리스트로 초기화 
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.value) # 현재 노드 추가 
        return result
    
if __name__ == '__main__':
    # 트리의 각 노드를 저장하는 딕셔너리
    # 노드 이름을 Key 키로, Node 객체를 Value 값으로 저장 
    nodes = {}

    # 노드의 개수 
    n = int(input())

    # 각 노드와 자식 노드 정보 입력 
    for _ in range(n):
        root, left, right = input().split()
        # root 노드가 아직 nodes 에 없으면
        # 새롭게 Node 객체를 생성하여 저장
        if root not in nodes:
            nodes[root] = Node(root)
        # '.' 가 아닌 경우 (자식 노드가 있는 경우)
        # 새로운 노드를 생성하고 root 의 자식으로 연결하기 
        if left != '.':
            nodes[left] = Node(left)
            nodes[root].left = nodes[left]
        if right != '.':
            nodes[right] = Node(right) # 새로운 노드 생성 
            nodes[root].right = nodes[right] # 루트의 자식으로 연결 

    # 루트 노드 A 를 기준으로 pre/ in/ postorder 결과 출력 
    print(''.join(nodes['A'].preorder()))   # 전위 순회
    print(''.join(nodes['A'].inorder()))    # 중위 순회
    print(''.join(nodes['A'].postorder()))  # 후위 순회
