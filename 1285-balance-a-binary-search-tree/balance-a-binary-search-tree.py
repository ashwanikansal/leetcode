# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_list = []

        def createSortedList(node):
            if not node:
                return
            
            createSortedList(node.left)
            sorted_list.append(node.val)
            createSortedList(node.right)
        
        createSortedList(root)

        def createBalancedTree(l, r):
            if l>r:
                return None

            m = (l+r)//2
            head = TreeNode(sorted_list[m], None, None)
            head.left = createBalancedTree(l, m-1)
            head.right = createBalancedTree(m+1, r)

            return head

        return createBalancedTree(0, len(sorted_list)-1)
            


            

        