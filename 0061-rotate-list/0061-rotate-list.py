# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k==0:
            return head
        
        node = head
        length=1
        node_list = [node]
        while node.next: # 끝노드 발견하기&길이 측정
            node = node.next
            node_list.append(node)
            length+=1
        k = k%length
        # 1. length-1 노드의 next -> head
        # 2. head가 length-k를 가리킴
        # 3. length-k-1 노드 next는 None을 가리킴

        if length==1 or k==0:
            return head
        
        node_list[length-1].next = head
        print(k, length)
        head = node_list[length-k]
        node_list[length-k-1].next = None

        return head
            
            