# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # dfs 1 : building  pre-order traversal list

        nodes = []

        myStack = []
        myStack.append(p)

        while myStack:
            node = myStack.pop()
            if node:
                nodes.append(node.val)
                myStack.append(node.right)
                myStack.append(node.left)
            else:
                nodes.append(None)
            
        length = len(myStack)


        # dfs 2: pre-order traversal of second tree

        nodes2 = []

        myStack2 = []
        myStack2.append(q)

        i = 0

        while myStack2:
            node = myStack2.pop()

            if node:
                if node.val != nodes[i]:
                    return False
                myStack2.append(node.right)
                myStack2.append(node.left)
            else:
                if nodes[i] != None:
                    return False

            i += 1
        
        return True


        