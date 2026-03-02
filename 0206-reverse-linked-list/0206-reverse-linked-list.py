class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next   # store next
            current.next = prev        # reverse link
            prev = current             # move prev
            current = next_node        # move current
        
        return prev