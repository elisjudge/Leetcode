# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass

    def isPalindrome(self, head: ListNode) -> bool:
        """
        This will use a two pointer algorithm but with a slow moving pointer and a
        fast moving pointer. The fast pointer will move at twice the speed of the 
        slow pointer, which if both pointers begin at the beginning, the fast pointer
        will hit the end of the list and the slow pointer will be in the middle.

        Then, to solve in O(1) space, using the slow pointer, we will reverse the 
        linked list starting from the middle to the end.

        Then, a simple value check between the beginning and end points of the linked list
        moving back towards the middle will be enough to determine whether the linked list
        is a palindrome or not.
        """
        
        fast = head
        slow = head

        # find the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # begin reversing from the middle
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # start checking from both ends of the linked list
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True


# Define a function to load in some test cases and convert them to linked lists

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for i in lst[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head


head1 = [1,2,2,1]
head1 = list_to_linked_list(head1)
head2 = [1,2]
head2 = list_to_linked_list(head2)

s= Solution()
print(s.isPalindrome(head1))
print(s.isPalindrome(head2))
