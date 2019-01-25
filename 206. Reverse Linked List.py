# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        new_head = None
        while current:
            next_head = current.next
            current.next = new_head
            new_head  = current
            current   = next_head
        return new_head
