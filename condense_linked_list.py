# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def condense_linked_list(node):
    d = {}
    
    head = node
    
    # add all node values into dictionary keys  (weed out duplicates)
    while head:
        if head.value not in d:
            d[head.value] = None
        head = head.next
    
    # create a list out of dictionary keys
    nodes = list(d.keys())
    
    # start a linked list using created list `nodes`
    new_head = current = ListNode(nodes[0])
    
    # append all nums in `nodes` to create a linked list
    for n in nodes[1:]:
        current.next = ListNode(n)
        current = current.next
    
    # return the head of the linked list
    return new_head