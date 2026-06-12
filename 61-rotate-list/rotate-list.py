# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        # 1. Base cases
        if not head or not head.next or k == 0:
            return head
        
        # 2. Find the length and the tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
            
        # 3. Calculate effective rotations
        k = k % n
        if k == 0:
            return head
            
        # 4. Form a circular linked list
        tail.next = head
        
        # 5. Find the new tail (which is n - k - 1 steps from the original head)
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next
            
        # 6. Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head