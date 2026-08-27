# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #building list of Subroot

        original_subTree = []
        original_subTree_vals = []
        original_subTree.append(subRoot)

        while original_subTree:

            node3 = original_subTree.pop()

            if node3:
                if node3.left:
                    original_subTree.append(node3.left)
                if node3.right:
                    original_subTree.append(node3.right)

                original_subTree_vals.append(node3.val)
            else: 
                original_subTree_vals.append(None)

            

        #finding subRoot in root using DFS
        myStack = []

        myStack.append(root)

        while myStack:

            subTree = []
            node = myStack.pop()
            if node.left:
                myStack.append(node.left)
            if node.right:
                myStack.append(node.right)

            
            if node.val == subRoot.val:

                myStack2 = []
                node2 = node
                myStack2.append(node2)

                while myStack2:

                    if node2:
                        node2 = myStack2.pop()
                        subTree.append(node2.val)

                        if node2.left:
                            myStack2.append(node2.left)
                        if node2.right:
                            myStack2.append(node2.right)
                    else:
                        subTree.append(None)

                    

                if subTree == original_subTree_vals:
                    return True
        
        return False

            