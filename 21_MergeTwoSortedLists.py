# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

class LinkedList:
    def __init__(self, head=None) :
        self.head = head

    def __repr__(self):
        return f"{self.head}"

    def add_node(self, val, next=None):
        new_node = ListNode(val, next)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        ll = []
        is_head = self.head
        while is_head:
            ll.append(is_head)
            is_head = is_head.next
        print (ll)


class Solution:
    def __init__(self) -> None:
        pass

    def mergeTwoLists(self, list1: LinkedList, list2: LinkedList) -> LinkedList:
        res = LinkedList()

        current1, current2 = list1.head, list2.head

        while current1 and current2:
            if current1.val <= current2.val:
                res.add_node(current1.val)
                current1 = current1.next
            else:
                res.add_node(current2.val)
                current2 = current2.next

        while current1:
            res.add_node(current1.val)
            current1 = current1.next
        
        while current2:
                res.add_node(current2.val)
                current2 = current2.next
        
        res.print_list()

s = Solution()

# Test Case 1
LL1a, LL1b = LinkedList(), LinkedList()
list1a, list1b= [1,2,4], [1,3,4]
[LL1a.add_node(x) for x in list1a] 
[LL1b.add_node(x) for x in list1b]


print("Test Case 1")
LL1a.print_list()
LL1b.print_list()
s.mergeTwoLists(LL1a, LL1b)
print()

# Test Case 2
LL2a, LL2b = LinkedList(), LinkedList()
list2a, list2b = [], []
[LL2a.add_node(x) for x in list2a] 
[LL2b.add_node(x) for x in list2b]

print("Test Case 2")
LL2a.print_list()
LL2b.print_list()
s.mergeTwoLists(LL2a, LL2b)
print()

# Test Case 3
LL3a, LL3b = LinkedList(), LinkedList()
list3a, list3b = [], [0]
[LL3a.add_node(x) for x in list3a] 
[LL3b.add_node(x) for x in list3b]

print("Test Case 3")
LL3a.print_list()
LL3b.print_list()
s.mergeTwoLists(LL3a, LL3b)
print()


# Test Case 4
LL4a, LL4b = LinkedList(), LinkedList()
list4a, list4b = [1,3,4,6,8,9,12,84,560], [2,7,8,9,10]
[LL4a.add_node(x) for x in list4a] 
[LL4b.add_node(x) for x in list4b]

print("Test Case 4")
LL4a.print_list()
LL4b.print_list()
s.mergeTwoLists(LL4a, LL4b)
print()