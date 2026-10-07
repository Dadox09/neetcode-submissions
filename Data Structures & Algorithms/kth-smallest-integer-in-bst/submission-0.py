# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #1-indexed begin 1
        #build the values list, order the list and return kth index - 1
        #build with BFS
        #cost build list O(n), order O(nlogn), return O(1)

        values = []
        q = deque([root])

        while q:
            for _ in range(len(q)):  
                node = q.popleft()  
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                values.append(node.val)
        
        values.sort()
        return values[k - 1]

