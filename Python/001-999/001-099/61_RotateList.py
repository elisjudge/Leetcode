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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()

        curr = head
        n_nodes = 0
        while curr: 
            curr = curr.next
            n_nodes += 1
        
        # normalize k to range of length nodes
        rotations = k % n_nodes
        if not rotations:
            return head

        slow = head
        fast = head

        while rotations:
            fast = fast.next
            rotations -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        dummy.next = slow.next
        slow.next = None
        fast.next = head

        return dummy.next


s = Solution()

testCases = [
    {"head": [1,2,3,4,5], "k": 2, "expected": [4,5,1,2,3]},
    {"head": [0,1,2], "k": 4, "expected": [2,0,1]}
]

for i, testcase in enumerate(testCases):
    ll = convertListToLinkedList(testcase["head"])
    ll = s.rotateRight(ll, testcase["k"])
    output = convertLinkedListToList(ll)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
