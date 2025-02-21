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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        ltx = ListNode()
        gtx = ListNode()

        ltx_curr = ltx
        gtx_curr = gtx
        
        while head:
            if head.val < x:
                ltx_curr.next = head
                ltx_curr = ltx_curr.next
            elif head.val >= x:
                gtx_curr.next = head
                gtx_curr = gtx_curr.next
            head = head.next
        
        gtx_curr.next = None
        ltx_curr.next = gtx.next
        return ltx.next

s = Solution()

testCases = [
    {"head": [1,4,3,2,5,2], "x": 3, "expected": [1,2,2,4,3,5]},
    {"head": [2,1], "x": 2, "expected": [1,2]},
    {"head": [2,1], "x": -1, "expected": [2,1]},
    {"head": [2,1], "x": 3, "expected": [2,1]}
]

for i, testcase in enumerate(testCases):
    ll = convertListToLinkedList(testcase["head"])
    ll = s.partition(ll, testcase["x"])
    output = convertLinkedListToList(ll)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
