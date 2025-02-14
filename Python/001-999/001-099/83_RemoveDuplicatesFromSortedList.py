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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                nxt = curr.next
                while nxt and curr.val == nxt.val:
                    nxt = nxt.next
                curr.next = nxt
            else:
                curr = curr.next

        return head

s = Solution()

testCases = [
    {"head": [1,1,2,3,3], "expected": [1,2,3]},
    {"head": [1,1,2], "expected": [1,2]}
]

for i, testcase in enumerate(testCases):

    head = convertListToLinkedList(testcase["head"])
    output = s.deleteDuplicates(head)
    result = convertLinkedListToList(output)

    
    if result == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {result}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {result}")
