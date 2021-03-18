

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    lst = []
    while head:
        lst.append(head.data)
        head = head.next
    return lst[-(positionFromTail+1)]
