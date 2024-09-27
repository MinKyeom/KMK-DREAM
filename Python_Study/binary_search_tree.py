"""
class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    #전위순회
    def preoder(self, n):
    if n != None:
        print(n.item,'',end='')
        if n.left: self.preorder(n.left)
        if n.right: self.preorder(n.right)

    #중위순회
    def inorder(self, n):
    if n != None:
        if n.left: self.inorder(n.left)
        print(n.item, '', end='')
        if n.right: self.inorder(n.right)

    #후위순회
    def postorder(self, n):
    if n != None:
        if n.left: self.postorder(n.left)
        if n.right: self.postorder(n.right)
        print(n.item, '', end='')

    #레벨순회
    def levelorder(self, root):
    q = []
    q.append(root)
    while q:
        t = q.pop(0)
        print(n.item,'',end='')
        if n.left != None: q.append(t.left)
        if n.right != None: q.append(t.right)

    #트리 높이
    def height(self, root):
        if root == None: return 0
        return max(self.height(root.left),self.height(root.right)) + 1

tree = BinaryTree()
n1=Node(10);n2=Node(20);n3=Node(30);n4=Node(40);n5=Node(50);n6=Node(60);n7=Node(70);n8=Node(80);

#트리
tree.root = n1
n1.left=n2;n1.right=n3
n2.left=n4;n2.right=n5
n3.left=n6;n3.right=n7
n4.left=n8

print('트리 높이: {}\n전위순회: {}\n중위순회: {}\n후위순회: {}\n레벨순회: {}'.format(
    tree.height(tree.root),         # 트리 높이: 4
    tree.preorder(tree.root),       # 전위 순회: 10 20 40 80 50 30 60 70
    tree.inorder(tree.root),        # 중위 순회: 20 40 80 50 10 30 60 70
    tree.postorder(tree.order),     # 후위 순회: 20 40 80 50 30 60 70 10
    tree.levelorder(tree.order)))   # 레벨 순회: 10 20 30 40 50 60 70 80
"""