# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        node_map = {root.val: root}

        left_most_leaf = inorder[0]

        i = 0
        currVal = preorder[i]
        curr = root

        while currVal != left_most_leaf:
            i+=1
            currVal = preorder[i]
            new_node = TreeNode(currVal)
            curr.left = new_node
            curr = curr.left

            node_map[currVal] = curr

        # i is the last node of the left chain, so right subtrees start at i+1
        p = i + 1
        j = 0
        prev = None

        while j < len(inorder):
            if inorder[j] in node_map:
                prev = node_map[inorder[j]]
                j+=1
            else:
                start = j
                while j < len(inorder) and inorder[j] not in node_map:
                    j+=1

                size = j - start
                prev.right = self.buildTree(preorder[p:p+size], inorder[start:j])
                p += size

        return root


        
        







