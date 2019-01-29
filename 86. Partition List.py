# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = ListNode(0)
        more_head = ListNode(0)
        less = less_head
        more = more_head

        while head:
            if head.val < x:
                less.next = head
                less = head
            else:
                more.next = head
                more = head
            head = head.next
        less.next = more_head.next
        more.next = None
        return less_head.next
