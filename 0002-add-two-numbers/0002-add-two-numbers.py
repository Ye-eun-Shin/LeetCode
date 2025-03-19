# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 2->4->3 => 342 라는 뜻.

        def add_two(l1, l2):
            if l1.next is None and l2.next is None:
                if l1.val+l2.val>=10:
                    return ListNode(l1.val+l2.val-10, next=ListNode(1))
                return ListNode(l1.val+l2.val)
            
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            
            if l1.val+l2.val<10:
                p = l1.val+l2.val
            else:
                p = l1.val+l2.val-10
                if l1.next is not None:
                    l1.next.val+=1
                elif l2.next is not None:
                    l2.next.val+=1
                else:
                    return ListNode(p, next = ListNode(1))

            return ListNode(p, next=add_two(l1.next, l2.next))
        
        return add_two(l1, l2)
        