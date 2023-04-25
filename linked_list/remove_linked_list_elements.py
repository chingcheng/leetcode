# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val,
# and return the new head.

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(next=head)
        prev = dummy
        current = head

        while current:
            nxt = current.next
            if current.val == val:
                prev.next = nxt
            else:
                prev = current
            current = current.next

        return dummy.next
