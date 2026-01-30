# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = defaultdict(int)
        temp = head
        while temp:
            if m[temp] > 1:
                return True
            m[temp] += 1
            temp = temp.next

        return False

        