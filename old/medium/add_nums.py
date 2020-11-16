class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    MEDIUM
    
    Given two linked lists of numbers in reverse order,
    find the sum of the two integers and return it as a linked list
    """
    
    # create an empty string to store the integer
    n1 = n2 = ""
    
    # turn the linked list into a single integer for l1 and l2
    while l1:
        n1 += str(l1.val)
        l1 = l1.next
    while l2:
        n2 += str(l2.val)
        l2 = l2.next
    
    # reverse the number string and turn into integer
    n1 = int(n1[::-1])
    n2 = int(n2[::-1])
    
    # reverse and turn the sum string into a list of integers
    summed_num = [int(n) for n in list(str(n1 + n2)[::-1])]
    
    # helper function to turn the list into a linked list
    def linker(l):
        head = cur = ListNode(l[0])
        
        for n in l[1:]:
            cur.next = ListNode(n)
            cur = cur.next

        return head

    # call helper function and return the answer
    return linker(summed_num)

test1 = [2,4,3]
test2 = [5,6,4]

addTwoNumbers(test1, test2)