

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if(position==0):
        return head.next
    head.next = deleteNode(head.next, position-1)
    return head
