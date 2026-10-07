# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder dfs

        values = []

        def getValues(node):
            if not node:
                return
            
            getValues(node.left)
            values.append(node.val)
            getValues(node.right)
        
        getValues(root)
        return values[k - 1]

        