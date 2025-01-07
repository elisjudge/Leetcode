# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val %= 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    
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

s = Solution()

list1a, list1b = [2,4,3], [5,6,4]
ll1a, ll1b = list_to_linked_list(list1a), list_to_linked_list(list1b)
sum1 = s.addTwoNumbers(ll1a, ll1b)
print(s.print_list(sum1))

list2a, list2b = [2,9,1], [5,3]
ll2a, ll2b = list_to_linked_list(list2a), list_to_linked_list(list2b)
sum2 = s.addTwoNumbers(ll2a, ll2b)
print(s.print_list(sum2))

list3a, list3b = [2,9,1,1], [5,3]
ll3a, ll3b = list_to_linked_list(list3a), list_to_linked_list(list3b)
sum3 = s.addTwoNumbers(ll3a, ll3b)
print(s.print_list(sum3))

list4a, list4b = [2,4,9], [5,6,4,9]
ll4a, ll4b = list_to_linked_list(list4a), list_to_linked_list(list4b)
sum4 = s.addTwoNumbers(ll4a, ll4b)
print(s.print_list(sum4))