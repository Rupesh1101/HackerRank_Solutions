

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    if head == None:
        return
    else:
        reversePrint(head.next)
        print(head.data)
