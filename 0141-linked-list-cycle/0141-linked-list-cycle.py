# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        head.val = 100001
        now = head
        while True:
            if now.next is None:
                return False

            now.val = 100001
            now = now.next
            
            if now.val==100001:
                return True
        
        #return False