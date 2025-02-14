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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev_node = dummy

        while True:
            kth = self.getKth(group_prev_node, k)
            if not kth:
                break
            group_next_node = kth.next

            prev, curr = kth.next, group_prev_node.next

            while curr != group_next_node:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev_node.next
            group_prev_node.next = kth
            group_prev_node = temp
        
        return dummy.next

    def getKth(self, curr:ListNode, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr        

s = Solution()

testCases = [
    {"head": [1,2,3,4,5,6], "k": 3, "expected": [3,2,1,6,5,4]},
    {"head": [1,2,3,4,5], "k": 3, "expected": [3,2,1,4,5]},
    {"head": [1,2,3,4,5], "k": 2, "expected": [2,1,4,3,5]}
]

for i, testcase in enumerate(testCases):
    ll = convertListToLinkedList(testcase["head"])
    ll = s.reverseKGroup(ll, testcase["k"])
    output = convertLinkedListToList(ll)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")