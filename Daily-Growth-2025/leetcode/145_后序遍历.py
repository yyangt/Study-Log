# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node,ans):
            if node is not None:
                return helper(node.left,ans)+helper(node.right,ans)+[node.val]
            return []
        return helper(root,[])