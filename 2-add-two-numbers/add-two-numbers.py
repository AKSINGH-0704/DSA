class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_int(node):
            num = 0
            multiplier = 1
            while node:
                num += node.val * multiplier
                multiplier *= 10
                node = node.next
            return num
            
        total = to_int(l1) + to_int(l2)
        
        dummy = ListNode(0)
        curr = dummy
        for digit in str(total)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
            
        return dummy.next