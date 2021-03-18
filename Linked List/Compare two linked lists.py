
# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    if llist1==None and llist2==None:
        return 1
    elif(llist1==None or llist2==None):
        return 0

    return llist1.data==llist2.data and compare_lists(llist1.next ,llist2.next)

