# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root,largest):

            if root is None:
                return None
            
            if root.val>=largest: 
                self.ans+=1
                largest = root.val
            
            dfs(root.right,largest)
            dfs(root.left, largest)
        
        if root:
            dfs(root,root.val)

        return self.ans

            
