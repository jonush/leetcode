"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2) -> ListNode:
    # given two linked lists
    # combine nodes of both linked lists getting one node from each at a time
    
    # place each linked list in a separate queue
    # alternate and get a node from each queue

    q = []
    
    while l1 or l2:
        if l1:
            q.append(l1.val)
            l1 = l1.next
        if l2:
            q.append(l2.val)
            l2 = l2.next
    
    q = sorted(q)
    
    if q:
        head = cur = ListNode(q[0])
    
        for i in q[1:]:
            cur.next = ListNode(i)
            cur = cur.next

        return head