from typing import Optional
import heapq

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
    def mergeKListsMergeSort(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """ Performed using a merge sort algorithm """
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeSortedList(l1, l2))
            lists = merged_lists
        
        return lists[0]

    def mergeSortedList(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        """ Helper Function for the Merge Sort Algorithm """
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        while l1 or l2:
            if l1:
                tail.next = l1
                l1 = l1.next
            elif l2:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        return dummy.next
    
    def mergeKListsHeap(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            current.next = node
            current = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        return dummy.next


s = Solution()

testCases = [
    {"lists": [[1,4,5],[1,3,4],[2,6]], "expected": [1,1,2,3,4,4,5,6]},
    {"lists": [], "expected": []},
    {"lists": [[]], "expected": []}
]

for i, testcase in enumerate(testCases):
    
    lls_merge_Sort = [convertListToLinkedList(l) for l in testcase["lists"]]
    ll_merge_sort = s.mergeKListsMergeSort(lls_merge_Sort)
    output_merge_sort = convertLinkedListToList(ll_merge_sort)

    lls_heap = [convertListToLinkedList(l) for l in testcase["lists"]]
    ll_heap = s.mergeKListsHeap(lls_heap)
    output_heap = convertLinkedListToList(ll_heap)
    
    if output_merge_sort == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (Merge Sort): {output_merge_sort}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (Merge Sort): {output_merge_sort}")

    if output_heap == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (Heap): {output_heap}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (Heap): {output_heap}")