# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

class Solution:
    def __init__(self) -> None:
        pass

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if not head:
            return None

        current = head
        prev = None

        while current:
            next = current.next        

            if current.val == val:
                if not prev:
                    head = next
                else:
                    prev.next = next
            else:
                prev = current
            current = next
        return head

    def print_list(self, head: ListNode) -> list:
        ll = []
        while head:
            ll.append(head)
            head = head.next
        return ll


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for i in lst[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head


head1, val1 = [1,2,6,3,4,5,6], 6
head1 = list_to_linked_list(head1)
head2, val2 = [], 1
head2 = list_to_linked_list(head2)
head3, val3 = [7,7,7,7], 7
head3 = list_to_linked_list(head3)


s = Solution()

head1 = s.removeElements(head1, val1)
print(s.print_list(head1))

head2 = s.removeElements(head2, val2)
print(s.print_list(head2))

head3 = s.removeElements(head3, val3)
print(s.print_list(head3))
