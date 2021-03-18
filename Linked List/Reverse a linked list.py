
# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    prev, curr = None, head
    while curr:
        prev, curr.next, curr = curr, prev, curr.next
    return prev
