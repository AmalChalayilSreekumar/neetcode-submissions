# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def validBST(root, left, right):
            if not root:
                return True

            if not left < root.val or not right > root.val:
                return False

            return validBST(root.left, left, root.val) and validBST(root.right, root.val, right)

        return validBST(root, float('-inf'), float('inf'))
