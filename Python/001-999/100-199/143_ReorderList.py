from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertListToLinkedList(vals: list, head = None) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def convertLinkedListToList(head: ListNode) -> list:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find middle point of LL
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # Beginning of second half of LL
        slow.next = None # Breaks LL into two
        
        ## Reverse second half of LL
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge two halves of list
        h1, h2 = head, prev
        while h2: # Use second half as it may be shorter
            temp1, temp2 = h1.next, h2.next
            h1.next = h2
            h2.next = temp1
            h1, h2 = temp1, temp2

s = Solution()

testCases = [
    {"vals": [1,2,3,4], "expected": [1,4,2,3]},
    {"vals": [1,2,3,4,5], "expected": [1,5,2,4,3]},
    {"vals": [1,2], "expected": [1,2]},
    {"vals": [1,2,3,4,5,6], "expected": [1,6,2,5,3,4]},
    {"vals": [1,2,3,4,5,6,7], "expected": [1,7,2,6,3,5,4]},
    {"vals": [1], "expected": [1]}
]

for i, testcase in enumerate(testCases):
    ll = convertListToLinkedList(testcase["vals"])
    s.reorderList(ll)
    output = convertLinkedListToList(ll)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")

