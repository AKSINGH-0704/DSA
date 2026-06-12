from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
            
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        
        while count >= k:
            curr = prev_group_tail.next
            prev = None
            
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                
            tail = prev_group_tail.next
            tail.next = curr
            prev_group_tail.next = prev
            prev_group_tail = tail
            
            count -= k
            
        return dummy.next