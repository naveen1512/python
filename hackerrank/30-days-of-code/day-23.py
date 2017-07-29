from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        queue = deque();
        queue.append(root)

        while len(queue) > 0:
            temp = queue.popleft()
            print(temp.data, end=' ')
            if temp.left != None:
                queue.append(temp.left)

            if temp.right != None:
                queue.append(temp.right)



T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)