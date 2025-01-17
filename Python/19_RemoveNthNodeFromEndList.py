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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
    
        return dummy.next

s = Solution()

testCases = [
    {"vals": [1,2,3,4,5], "n": 2, "expected": [1,2,3,5]},
    {"vals": [1], "n": 1, "expected": []},
    {"vals": [1,2], "n": 1, "expected": [1]}
]

for i, testcase in enumerate(testCases):
    ll = convertListToLinkedList(testcase["vals"])
    ll = s.removeNthFromEnd(ll, testcase["n"])
    output = convertLinkedListToList(ll)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
