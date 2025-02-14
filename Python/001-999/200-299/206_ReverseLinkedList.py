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

    def add_node(self, val, next=None):
        new_node = ListNode(val, next)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse_list(self):
        """
        Iterative Solution
        """
        if self.head is None:
            print("Cannot reverse an empty list")
            return
        prev = None
        current = self.head
                
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        print (prev)

    def reverse_list_recursive(self, prev = None):
        """
        Recursive Solution
        """
        current = self.head 

        if current is None:
            self.head = prev
            print(self.head)
            return self.head
        
        self.head = current.next
        current.next = prev
        self.reverse_list_recursive(current)
            

    def print_list(self):
        ll = []
        is_head = self.head
        while is_head:
            ll.append(is_head)
            is_head = is_head.next
        print (ll)


LL = LinkedList()
inputs = [1,2,3,4,5]

for i in inputs:
    LL.add_node(i)

LL.print_list()
LL.reverse_list_recursive()
LL.print_list()


LL2 = LinkedList()
inputs2 = ["Apple", "Banana", "Carrot", "Duck", "Egg"]

for i in inputs2:
    LL2.add_node(i)
LL2.print_list()
LL2.reverse_list()
LL2.print_list()