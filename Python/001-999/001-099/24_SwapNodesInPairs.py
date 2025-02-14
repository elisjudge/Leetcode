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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next

        while curr and curr.next:
            temp = curr.next
            prev.next = temp
            curr.next = temp.next
            temp.next = curr

            prev = curr
            curr = curr.next

        return dummy.next

s = Solution()

testCases = [
    {"head": [1,2,3,4], "expected": [2,1,4,3]},
    {"head": [], "expected": []},
    {"head": [1], "expected": [1]},
    {"head": [1,2,3], "expected": [2,1,3]}
]

for i, testcase in enumerate(testCases):
    ll = convertListToLinkedList(testcase["head"])
    ll = s.swapPairs(ll)
    output = convertLinkedListToList(ll)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")