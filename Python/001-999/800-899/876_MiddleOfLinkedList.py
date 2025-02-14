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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow



s = Solution()

testCases = [
    {"head": [1,2,3,4,5], "expected": [3,4,5]},
    {"head": [1,2,3,4,5,6], "expected": [4,5,6]}
]

for i, testcase in enumerate(testCases):

    head = convertListToLinkedList(testcase["head"])
    output = s.middleNode(head)
    result = convertLinkedListToList(output)

    
    if result == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {result}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {result}")
