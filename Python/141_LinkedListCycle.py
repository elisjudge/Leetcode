# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"
    
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True    

        return False
    
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

print(s.hasCycle(head))

# CREATE NON CYCLE LIST
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

head = node1
head.next = node2
node2.next = node3
print(s.hasCycle(head))

