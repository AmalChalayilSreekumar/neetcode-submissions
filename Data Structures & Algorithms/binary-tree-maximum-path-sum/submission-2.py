# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.best_path = root.val

        def findPath(root, path_current):
            if not root: 
                return 0
            
            
            left = max(findPath(root.left,path_current),0)
            right = max(findPath(root.right,path_current),0)

            path_current = max(left,right) + root.val


            self.best_path = max(self.best_path, left+right+root.val)

            return path_current

        findPath(root, 0)

        return self.best_path
            


