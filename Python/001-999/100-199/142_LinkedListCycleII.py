from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                start = head
                while start != slow:
                    slow = slow.next
                    start = start.next
                return slow
        return 
        
    
s = Solution()

# CREATE CYCLE LIST
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head = node1
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(s.detectCycle(head))

# CREATE NON CYCLE LIST
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

head = node1
head.next = node2
node2.next = node3
print(s.detectCycle(head))