# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, main_root: Optional[TreeNode]) -> bool:
        self.res = True
        def helper(root: TreeNode) -> int:
            if not root:
                return 0
            
            left_depth = helper(root.left)
            right_depth = helper(root.right)

            print(root.val, left_depth, right_depth)

            if abs(left_depth - right_depth) > 1:
                self.res = False
            
            return 1 + max(left_depth, right_depth)
   
        helper(main_root)
        
        return self.res

            